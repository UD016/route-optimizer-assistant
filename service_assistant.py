"""
Service Coordinator Assistant
Version 0.4.0
Author: UD016

Prototype AI assistant for Cummins Service Operations

Change log:

v0.4.0
- Switched from full knowledge-base injection to lightweight per-question retrieval.
    - Built a helper function that indexes Markdown files inside knowledge_base.
    - Retrieves only the most relevant Markdown chunks for each user question.
    - Injects retrieved excerpts into the agent prompt instead of the full knowledge base.

v0.3.0
- Changed knowledge retrieval method.
    - Defined a helper function to retrieve Markdown files inside knowledge_base instead of retrieving a single master file.
- Specified GPT model in the agent function (5.6 Terra)
- Reduced and refined system prompt.

v0.2.0
- Moved from a built-in prompt mechanism to a helper function integrated within Streamlit.

v0.1.0
- Initial prototype build.
    - Self-contained in the terminal, not usable elsewhere.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from math import log
from pathlib import Path
import re

from agents import Agent, Runner


STOPWORDS = {
    "what", "does", "do", "is", "are", "the", "a", "an", "of", "for",
    "to", "in", "on", "and", "or", "by", "with", "stand", "stands",
    "mean", "meaning", "tell", "me", "about", "please", "can", "you",
    "this", "that", "it"
}


@dataclass(frozen=True)
class Chunk:
    source: str
    text: str
    token_set: frozenset[str]


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s_-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> list[str]:
    normalized = normalize_text(text)
    if not normalized:
        return []
    return normalized.split()


def tokenize_for_retrieval(text: str) -> list[str]:
    return [t for t in tokenize(text) if t not in STOPWORDS]


def extract_acronym(question: str) -> str | None:
    """
    Detect questions like:
    - What does FSPG stand for?
    - What is CSA?
    - Define FSPG
    """
    patterns = [
        r"\bwhat does\s+([A-Z]{2,12})\s+stand for\b",
        r"\bwhat is\s+([A-Z]{2,12})\b",
        r"\bdefine\s+([A-Z]{2,12})\b",
        r"\bmeaning of\s+([A-Z]{2,12})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, question, flags=re.IGNORECASE)
        if match:
            return match.group(1).upper()
    return None


def split_markdown_into_chunks(text: str, max_words: int = 220) -> list[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    chunks: list[str] = []
    current: list[str] = []
    current_word_count = 0

    for para in paragraphs:
        para_words = len(para.split())

        if para_words > max_words:
            if current:
                chunks.append("\n\n".join(current))
                current = []
                current_word_count = 0

            words = para.split()
            for i in range(0, len(words), max_words):
                chunks.append(" ".join(words[i : i + max_words]))
            continue

        if current and current_word_count + para_words > max_words:
            chunks.append("\n\n".join(current))
            current = []
            current_word_count = 0

        current.append(para)
        current_word_count += para_words

    if current:
        chunks.append("\n\n".join(current))

    return chunks


@lru_cache(maxsize=1)
def build_kb_index(path: str = "knowledge_base") -> tuple[Chunk, ...]:
    kb_path = Path(path)
    if not kb_path.exists():
        return tuple()

    chunks: list[Chunk] = []

    for file in sorted(kb_path.rglob("*.md")):
        try:
            text = file.read_text(encoding="utf-8")
        except Exception:
            continue

        relative_source = str(file.relative_to(kb_path))
        file_stem = file.stem

        for chunk_text in split_markdown_into_chunks(text):
            searchable_text = f"{relative_source}\n{file_stem}\n{chunk_text}"
            chunks.append(
                Chunk(
                    source=relative_source,
                    text=chunk_text,
                    token_set=frozenset(tokenize(searchable_text)),
                )
            )

    return tuple(chunks)


def score_chunk(question: str, chunk: Chunk) -> float:
    qtokens = tokenize_for_retrieval(question)
    if not qtokens:
        return 0.0

    normalized_chunk_text = normalize_text(chunk.text)
    normalized_source = normalize_text(chunk.source)

    score = 0.0
    query_counter = Counter(qtokens)

    # Main overlap scoring
    for token, count in query_counter.items():
        if token in chunk.token_set:
            score += 2.0 if len(token) <= 5 else 1.0
            score += 0.25 * log(1 + count)

        if token in normalized_source:
            score += 1.5

    # Exact phrase bonus
    phrase = " ".join(qtokens)
    if phrase and phrase in normalized_chunk_text:
        score += 3.0

    # Acronym boost
    acronym = extract_acronym(question)
    if acronym:
        a = acronym.lower()
        if a in chunk.token_set:
            score += 10.0
        if a in normalized_source:
            score += 5.0
        if a in normalized_chunk_text:
            score += 6.0

    return score


def retrieve_relevant_chunks(
    question: str,
    kb_index: tuple[Chunk, ...],
    top_k: int = 4,
) -> list[Chunk]:
    scored: list[tuple[float, Chunk]] = []

    for chunk in kb_index:
        score = score_chunk(question, chunk)
        if score > 0:
            scored.append((score, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)

    if scored:
        return [chunk for _, chunk in scored[:top_k]]

    # Fallback: try filename/source-token matching before giving up
    qtokens = tokenize_for_retrieval(question)
    fallback = [
        chunk for chunk in kb_index
        if any(token in normalize_text(chunk.source) for token in qtokens)
    ]
    if fallback:
        return fallback[:top_k]

    return list(kb_index[:top_k])


def format_retrieved_context(chunks: list[Chunk], max_chars: int = 12000) -> str:
    if not chunks:
        return "No relevant knowledge base excerpts were found."

    sections: list[str] = []
    total_chars = 0

    for chunk in chunks:
        block = f"### Source: {chunk.source}\n{chunk.text.strip()}"
        if total_chars + len(block) > max_chars:
            break
        sections.append(block)
        total_chars += len(block)

    return "\n\n---\n\n".join(sections)


def build_agent(question: str) -> Agent:
    """
    Build an agent with only the most relevant knowledge excerpts.
    """
    kb_index = build_kb_index("knowledge_base")
    relevant_chunks = retrieve_relevant_chunks(question, kb_index, top_k=4)
    retrieved_context = format_retrieved_context(relevant_chunks)

    instructions = f"""
You are the Service Coordinator Assistant for the Cummins service department.

Your purpose is to help service coordinators perform their work accurately and efficiently by answering questions, explaining procedures, assisting with dispatch decisions, and providing invoicing guidance.

## Knowledge Policy

- The provided knowledge excerpts are the primary source of truth for all Cummins-specific procedures, workflows, terminology, and internal policies.
- If the knowledge excerpts contain the answer, always prioritize them.
- You may use general public knowledge to provide context about external organizations, manufacturers, industry standards, regulations, or technical concepts when the knowledge excerpts do not contain that information.
- If internal knowledge and general knowledge conflict, always follow the knowledge excerpts.
- Never invent procedures, policies, technician qualifications, pricing, customer information, or business rules.
- If the information is unavailable, clearly state what is missing.

## Response Guidelines

- Answer clearly, professionally, and concisely.
- Adapt the amount of detail to the user's question.
- For simple questions (definitions, acronyms, terminology), provide a direct answer.
- For workflow questions (dispatch, invoicing, troubleshooting, scheduling, etc.), guide the user through the appropriate process using the knowledge excerpts.
- When useful, identify missing information before making recommendations.
- Explain your reasoning whenever making recommendations or decisions.
- Suggest practical next steps when appropriate.

## Ambiguity

- If an acronym or term has multiple meanings, present the possible meanings and ask for clarification instead of guessing.
- If a question is ambiguous, ask only the minimum clarification needed.

## Source Transparency

When appropriate, indicate whether your answer is based on:
- the Cummins knowledge base
- general public knowledge
- or a combination of both.

Knowledge excerpts:

{retrieved_context}
""".strip()

    return Agent(
        name="Service Coordinator Assistant",
        model="gpt-5.6-terra",
        instructions=instructions,
    )


# Public function used by the Streamlit application
def ask_service_assistant(question: str) -> str:
    """
    Send a question to the Service Coordinator Assistant
    and return the response.
    """
    agent = build_agent(question)

    result = Runner.run_sync(
        agent,
        question,
    )

    return result.final_output


if __name__ == "__main__":
    print("Service Coordinator Assistant")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("Ask a service question: ").strip()

        if question.lower() in {"quit", "exit", "q"}:
            break

        if not question:
            continue

        print()
        print(ask_service_assistant(question))
        print()