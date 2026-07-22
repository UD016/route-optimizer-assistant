# Coordinator Procedure - Invoicing

# Version 1.0.1

# Last Updated: 2026-07-15

# Updated By: Jipeng Li

# Change Log:

v1.0.1
- Added rules when there is an RFQ report.
- Added minor details.

v1.0.0
- Creation of initial document.

# Purpose

How to properly invoice a customer work order once the job has been completed by technicians.

# Procedure

1. Retrieve FA Job ID.
2. Review Field Service Basic and Request for Quotation (RFQ) reports.

## RFQ Rule

If there is an RFQ report filled by a technician, ensure that the quote has already been prepared and sent to the customer for approval before invoicing.
Otherwise it is easy to lose track of quotes that should have been prepared and sent out.

3. Convert technician comments from first-person to third-person.

## Example

Instead of:

> I performed a visual inspection.

Use:

> The technician performed a visual inspection.

4. Complete:
   - Complaint
   - Cause
   - Correction
   - Coverage
   - Remark

5. Update unit hours.

6. Verify SRT values.

## SRT Rule

Normally:

- Allocated Hours
- Actual Hours
- Billable Hours

Should match.

Exception:

- Do not increase billing when actual hours exceed quoted hours.

7. Verify kilometre charges.

8. Close work order.

## Before Closing

Confirm:

- PO Number entered
- Close checkbox selected
- Security code entered

## Invoice Delivery

### HighRadius Generated

No additional email required.

### Manual Delivery

Send by email.

Subject:

```text
[Invoice Number]
```

Email body:

- Brief job summary
- Thank customer
