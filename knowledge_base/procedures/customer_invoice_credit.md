# Customer Invoice Credit Procedure

# Version 1.0.0

# Last Updated: 2026-07-10

# Updated By: Jipeng Li

# Change Log:

v1.0.0
- Creation of initial document.

## Purpose

This procedure explains how to create a credit against an already invoiced customer work order in BMS.

---

## Prerequisites

- Customer invoice has already been generated.
- User has access to BMS Order Entry.
- Invoice number is available.
- Credit reason has been approved.

---

## Procedure

### Step 1 – Open Order Entry

Navigate to:

Customer Care
→ Maintain Customer Orders
→ Order Entry

---

### Step 2 – Complete Header Information

| Field | Value |
|--------|-------|
| Bill To | Customer account |
| Transaction Type | WOCM |
| Pick Up | Y |
| Contact | Customer contact |
| Ship Via | EM (Email) |
| Unit | Customer unit number |

Press **F10** after entering the unit.

---

### Step 3 – Parts

Open the **Items** tab.

If parts are included in the credit:

- Contact the Parts Department.
- Provide the Order Reference Number.
- Parts must be added by Parts.

---

### Step 4 – Charges

Open the **Charges** tab.

Enter the required credit lines:

- Labor Rebill
- Mileage Credit
- Parts Credit (if applicable)

Important:

- Enter all amounts as **negative values**.
- Enter amounts **before taxes**.
- Taxes will be calculated automatically.

Press **F10**.

---

### Step 5 – Comments

Open the **Comments** tab.

Comment Type:

Standard

Include:

- Reason for credit
- Invoice reference
- Your WWID
- Any additional explanation

Example

IN REFERENCE TO INVOICE XXXXXXX

Credit issued for incorrect labor billing.

WWID: XXXXX

---

### Step 6 – Distributor Comments

Comment Type:

Distributor

Reason:

Other

Enter:

.

(single period)

---

### Step 7 – Complete Invoice

Select **Total Order**.

Verify:

- Original invoice number
- Invoice total
- Purchase Order (PO), if applicable

Enter:

- Invoice Security Code

Select:

Invoice

---

## Important Notes

- WOCM is always used for Service work orders.
- Pick Up should always be set to **Y**.
- Ship Via should always be **EM**.
- Credit amounts must always be entered as negative values before taxes.
- Parts credits must be coordinated with the Parts Department.

---

## Related Procedures

- Invoicing
- Cash Customer Procedure
- Work Order Closing