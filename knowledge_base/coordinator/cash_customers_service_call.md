# Cash Customers - Service Call Procedure

# Version 1.0.2

# Last Updated: 2026-07-10

# Updated By: Jipeng Li

# Change Log:

v1.0.0
- Creation of initial document.


## Service Call Procedure
### Before Dispatch

1. Collect credit card information.
2. Confirm full service pricing.
3. Determine:
   - Personal card
   - Commercial card

### Clover Payment Processing

1. Process payment.
2. Save receipt.
3. Send receipt to customer.
4. Print:
   - Receipt
   - Preview invoice

5. Sign and stamp documents.

6. File in designated payment drawer.

### Deposit Entry in BMS

Create Order Entry:

- Name: DEPOSIT
- Correct tax district
- Correct amount

Comments:

```text
Payment for WO XXXXXX
```

Attach to work order.

### After Work Completion

- Verify technician hours.
- Close invoice.
- Send final invoice.
