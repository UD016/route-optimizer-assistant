# BMS - Searching Records

# Version 1.0.0

# Last Updated: 2026-07-20

# Updated By: Jipeng Li

# Change Log:

v1.0.0
- Creation of initial document.

## Purpose

This document explains the different methods available for searching customers, work orders, work order history, and other records within BMS.

Searching efficiently allows Service Coordinators to quickly retrieve customer information, previous service history, invoices, and work orders.

---

# Search Methods

BMS provides two primary methods for searching information:

1. **Service Lookup**
2. **Work Order Query**

Each method serves a different purpose.

---

# Service Lookup

The **Service Lookup** tool is used to locate:

- Customer Numbers
- Work Orders
- Work Order Quotes (WOQT)
- Invoices
- Customer Work History

---

## Finding a Customer Number

Open:

```text
Service Lookup
```

Under the **Work Orders** section:

1. Select the **binoculars** beside **Customer**.
2. Open **Customer Lookup**.
3. Search using one of the following:

- Customer Name
- Phone Number
- Site Address

### Wildcard Searches

Use the **%** symbol before and after the search value.

Examples:

```text
%CUMMINS%

%6836863%
```

Once the customer has been located:

- Record the Customer Number for future reference.

> **Best Practice**
>
> Whenever possible, search using the customer's phone number to reduce duplicate results.

---

## Viewing Customer Work History

To retrieve a customer's service history:

Open:

```text
Service Lookup
```

Configure the search:

| Field | Value |
|--------|-------|
| Query | All Work Orders |
| Order By | Create Date |

Next:

1. Select the **binoculars** beside **Customer**.
2. Open **Customer Lookup**.
3. Enter the Customer Number in the **Identifier** field.
4. Select the customer.

BMS will display all available work orders associated with every unit owned by that customer.

This information can be used to:

- Review previous repairs.
- Check historical operating hours.
- Review technician notes.
- Verify previous invoices.
- Confirm recurring issues.

---

# Work Order Search

The Work Order window provides another method of searching records.

Open a:

```text
Work Order
```

window.

---

## Enter Query Mode

Press:

```text
F7
```

All searchable fields will become **white**, indicating that BMS has entered Query Mode.

---

## Search Criteria

You may search using any of the following:

- Work Order Number
- Invoice Number
- Customer Number
- Phone Number
- Purchase Order Number
- Supervisor Name
- Market Segment

Enter the appropriate value into the corresponding field.

---

## Execute the Search

Press:

```text
F8
```

to execute the query.

BMS will retrieve all matching records.

---

# Choosing the Right Search Method

| If you need to... | Use |
|-------------------|-----|
| Find a Customer Number | Service Lookup |
| Review customer service history | Service Lookup |
| Find an existing Work Order | Work Order Query |
| Search by Invoice Number | Work Order Query |
| Search by Customer Number | Work Order Query |
| Search by Purchase Order | Work Order Query |
| Search by Supervisor | Work Order Query |

---

# Best Practices

- Use **Service Lookup** whenever customer history is required.
- Use **Work Order Query** when searching for a specific work order or invoice.
- Use wildcard (%) searches whenever the full customer name is unknown.
- Record the Customer Number before beginning other procedures.
- Sort customer history by **Create Date** when reviewing recent service activity.

---

# Common Mistakes

## Forgetting Wildcards

Searching for:

```text
CUMMINS
```

may return no results.

Instead use:

```text
%CUMMINS%
```

---

## Searching the Wrong Window

Use **Service Lookup** for customer history.

Use **Work Order Query** for work order-specific searches.

---

## Not Entering Query Mode

Always press:

```text
F7
```

before entering search criteria in the Work Order window.

---

## Forgetting to Execute the Query

After entering search criteria:

Press:

```text
F8
```

to retrieve matching records.