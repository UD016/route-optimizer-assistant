# Coordinator - Hydro-Québec Invoicing Requirements

# Version 1.0.0

# Last Updated: 2026-07-15

# Updated By: Jipeng Li

# Change Log:

v1.0.0
- Creation of initial document.

## Purpose

This document outlines the invoicing requirements specific to Hydro-Québec work orders.

Failure to include the required information will result in the invoice being automatically rejected by Hydro-Québec's invoice processing system.

---

# Required Information

Every Hydro-Québec invoice must include the following information:

- Purchase Order (PO) number
- Hydro-Québec Work Order Number
- Hydro-Québec Approver Code (CII)

All three pieces of information are mandatory.

---

# Hydro-Québec Work Order Number

## Format

The Hydro-Québec work order number:

- Contains **8 digits**
- Begins with either:
  - **307**
  - **308**

Example:

```text
30712345
```

---

# Hydro-Québec Approver Code (CII)

## Format

The approver code:

- Contains **2 letters followed by 4 numbers**

Example:

```text
DD2271
```

For the **Montréal** region, the standard approver code is:

```text
DD2271
```

---

# BMS Entry Requirements

## Complaint Section

The following information must be entered in the **COMPLAINT** section of the work order:

- Hydro-Québec Work Order Number
- Hydro-Québec Approver Code (CII)

Example:

```text
***** ORDRE DE TRAVAIL 30712345 *****

***** DD2271 *****
```

> Do not rely on the PO number alone. The Work Order Number and Approver Code must also be entered in the COMPLAINT section.

---

# Before Sending the Invoice

Verify that the invoice contains:

- ✅ Purchase Order (PO)
- ✅ Hydro-Québec Work Order Number
- ✅ Hydro-Québec Approver Code (CII)

If any of these items are missing, the invoice should **not** be sent.

---

# Invoice Submission

Once all required information has been verified, send the invoice to:

```text
COMPTESFOURNISSEURS@HYDRO.QC.CA
```

---

# Important

Hydro-Québec uses an automated invoice validation system.

Invoices missing any of the required information will be **automatically rejected** and will not be processed.

---

# Common Mistakes

## Missing Work Order Number

Every Hydro-Québec invoice must include the Hydro-Québec work order number.

---

## Missing Approver Code

The approver code (CII) must always accompany the work order number.

---

## Incorrect Location

The Work Order Number and Approver Code must be entered in the **COMPLAINT** section of the BMS work order.

---

## Related Documents

- coordinator_invoicing.md
- coordinator_customer_invoice_credit.md