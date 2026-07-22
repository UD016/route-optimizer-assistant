# Power BI - WIP Management

# Version 1.0.0

# Last Updated: 2026-07-20

# Updated By: Jipeng Li

# Change Log:

v1.0.0
- Creation of initial document.

## Purpose

This document explains how Service Coordinators use Power BI to retrieve and manage the Work In Progress (WIP) report.

The WIP report is used to monitor open Work Orders, prioritize follow-up actions, and maintain an acceptable Days Sales Outstanding (DSO).

---

# Systems Used

- Power BI
- Microsoft Excel

---

# Opening Power BI

It is recommended to use **Google Chrome** when accessing Power BI.

Open the Power BI dashboard.

On the left navigation panel:

1. Select **Most Used**.
2. Open **WIP**.
3. Select **WIP Detail**.

This report displays all open Work Orders.

---

# Recommended Filters

Apply the following filters before reviewing the report.

| Filter | Recommended Value |
|----------|-------------------|
| GEO / AREA VP | All |
| BRANCH | Candiac or Ottawa |
| SUPERVISOR | Your Name |
| WIP Category | All |

All remaining filters may remain on **All** unless a more specific search is required.

---

# Exporting the WIP Report

To export the report:

1. Select the **three-dot menu** (⋯).
2. Choose:

```text
Export Data
```

3. Select:

```text
Data with current layout
```

4. Select:

```text
Export
```

The report will be downloaded as a Microsoft Excel file.

---

# Opening the Export

Locate the downloaded file.

Depending on your browser settings, it may be found in:

- Browser Downloads
- Windows Downloads folder
- Another user-defined download location

Open the Excel file.

---

# Preparing the Spreadsheet

The exported spreadsheet contains numerous columns.

Hide columns that are not required for daily WIP management.

To hide a column:

1. Right-click the column header.
2. Select:

```text
Hide
```

This allows the report to focus on the information most relevant to the Service Coordinator.

---

# Key Columns

The following columns are typically the most useful.

| Column | Description |
|----------|-------------|
| ORDER # | Work Order Number |
| SUBTYPE | Work Order subtype |
| WO SUP. NAME | Assigned supervisor |
| AGE | Age of the Work Order |
| DNL | Days No Labor |
| TOTAL | Total Work Order value |
| CUST. NAME | Customer name |
| BMS STATUS COMMENT | Current status and coordinator notes |

---

# Using the WIP Report

The WIP report should be reviewed regularly to:

- Monitor open Work Orders.
- Identify aging work orders.
- Follow up on jobs with no recent labor activity.
- Identify invoices requiring attention.
- Prioritize coordinator workload.

Regular review of the report helps reduce delays in billing and work order completion.

---

# Performance Objective

The objective is to maintain the WIP report as accurately as possible.

Particular attention should be given to:

- Aging Work Orders
- Days No Labor (DNL)
- Days Sales Outstanding (DSO)

Target:

```text
DSO < 13 Days
```

Maintaining a low DSO improves branch cash flow and overall operational performance.

---

# Best Practices

- Review the WIP report daily.
- Apply filters before exporting.
- Hide unnecessary columns to simplify analysis.
- Prioritize Work Orders with high AGE or DNL values.
- Keep BMS Status Comments up to date to reflect current progress.

---

# Common Mistakes

## Incorrect Branch Selected

Verify that the correct branch has been selected before exporting the report.

---

## Reviewing All Supervisors

Filter by your own supervisor name unless reviewing branch-wide performance.

---

## Ignoring Aging Work Orders

High AGE and DNL values often indicate Work Orders requiring immediate follow-up.

---

## Outdated Status Comments

Keep BMS Status Comments current to ensure the WIP accurately reflects the latest progress.

---

# Coordinator Tip

The WIP report is one of the most valuable tools for managing daily workload.

Reviewing it at the beginning and end of each day helps identify overdue Work Orders, prioritize invoicing activities, and maintain the branch's DSO target.