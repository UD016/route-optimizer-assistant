# Service Department Master File

# Version 1.0.2

# Last Updated: 2026-07-10

# Updated By: Jipeng Li

# Change Log:

v1.0.2
- Added cloning work order 
 
---

# Coordinator Procedures

## Taking a Call

### Objective

Gather all information required to accurately diagnose, quote, schedule, and dispatch a service technician.

### Procedure

1. Greet the customer:

   > "Cummins Service, my name is [your name], how may I help you today?"

2. Have a notebook, paper, or digital document ready to record information.

3. Determine whether an alarm code is present.
   - Record the alarm description.
   - Record the fault code number if available.
   - Examples:
     - Low Coolant
     - FC1223

4. Verify whether the customer already has an account.
   - Existing customer:
     - Retrieve customer number.
     - Confirm name.
     - Confirm billing information.
     - Confirm phone number.
   - New customer:
     - Create a customer account.

5. Obtain site information.
   - Site address
   - On-site contact name
   - On-site contact phone number

6. Obtain generator information.
   - Serial number
   - Data plate information
   - Safety concerns

7. For ATS (Automatic Transfer Switch) issues:
   - Confirm whether a simulated power outage can be performed.
   - Confirm a suitable testing time.

8. For non-Cummins generators:
   - Advise the customer that a technician can still be dispatched.
   - Explain that the technician may not be certified on that specific equipment.
   - Inform the customer that they may be referred to a specialized provider if necessary.

---

## Job Booking (General Procedure)

### Objective

Create and dispatch a work order with complete and accurate information.

### Procedure

#### 1. Complaint Details

Collect:

- Error codes
- Alarm descriptions
- Physical symptoms
- Serial number
- Data plate information
- Site access information
  - Roof access
  - Restricted access
  - Marine applications
  - Other constraints

#### 2. Contact Information

The work order contact should always be the person with whom the coordinator is speaking.

Update contact information if required.

#### 3. On-Site Contact

Record:

- Full name
- Phone number

Include the information in the complaint section.

#### 4. Credit Verification

##### Charge Customers

Verify available credit.

If insufficient:

- Contact Elena DiBernardo
- Request a credit increase

##### Cash Customers

Collect payment details and charge:

- Minimum 4 hours labor
- Appropriate mileage charges

#### 5. Parts Verification

Confirm:

- Required parts are available
- Parts are attached to the work order

If unavailable:

- Contact Parts Department
- Discuss alternatives
- Inform customer of delays

#### 6. Reserve Time Slot

- Select an appropriate FieldAware time slot.
- Create a placeholder or a customer hold on FieldAware.
- Create an Outlook reminder.

#### 7. Technician Consultation

Discuss with the selected technician:

- Generator issue
- Error codes
- Site considerations
- Required expertise

Confirm suitability.

#### 8. Customer Confirmation

After customer approval:

- Send work order to FieldAware.
- Retain:
  - Field Service Basic
  - Request for Quotation

Remove unnecessary reports.

Remove the previously placed placeholder or customer hold.

#### 9. Final Assignment

Assign:

- Technician
- Reports
- FieldAware Job ID

---

## Preparing and Accepting a Quote

### Procedure

1. Retrieve RFQ from FieldAware.

2. Download RFQ or capture required parts information.

3. Create a WOQT in BMS.

4. Send parts request to Parts Department.

Include:

- WOQT number
- RFQ file
- Parts list

#### Important

When "Quote Accept" is specified:

- Parts Department assumes customer approval.
- WOQT may be converted directly into WO.

#### Parts Contacts

Primary Contacts:

- Jean‑François Germain
- Pier‑Jean Morin

Always:
- Send to one
- CC the other

### Customer Approval

A quote is approved when:

- Signed quote is returned

OR

- Customer explicitly approves by email

---

## Invoicing

### Procedure

1. Retrieve FA Job ID.
2. Review Field Service Basic report.
3. Convert technician comments from first-person to third-person.

#### Example

Instead of:

> I performed a visual inspection.

Use:

> The technician performed a visual inspection.

4. Complete:
   - Cause
   - Correction

5. Verify coverage.

6. Verify thank-you message.

7. Update unit hours.

8. Verify SRT values.

#### SRT Rule

Normally:

- Allocated Hours
- Actual Hours
- Billable Hours

Should match.

Exception:

- Do not increase billing when actual hours exceed quoted hours.

9. Verify kilometre charges.

10. Close work order.

### Before Closing

Confirm:

- PO Number entered
- Close checkbox selected
- Security code entered

### Invoice Delivery

#### HighRadius Generated

No additional email required.

#### Manual Delivery

Send by email.

Subject:

```text
[Invoice Number]
```

Email body:

- Brief job summary
- Thank customer

---

# Cash Customers

## Policy Overview

Cash customers create higher financial risk because no approved credit account exists.

### Key Principles

#### No Guaranteed Payment

Service work without payment protection exposes the branch to financial risk.

#### Pre-Authorization Is Not Payment

A pre-authorization:

- Does not guarantee collection
- Must be converted to final payment

#### Cash Flow Protection

Prompt collection protects:

- Cash flow
- Financial stability
- Operational efficiency

### Coordinator Expectations

- Track outstanding balances daily
- Follow up immediately
- Convert pre-authorizations quickly
- Close completed jobs promptly

---

## Cash Customer Procedure - Service Call

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

---

# Priorities

## Daily Priorities

1. Message from On Call items
2. Ensure technicians remain scheduled
3. Emergency service requests
4. Customer quotations
5. Warranty claims
6. Aging WIP invoices

## Highest Priority Events

- Downed generators
- Hydro‑Québec outages

### Candiac Priority Customers

- Vantage
- Cologix
- eStruxture
- Videotron
- Telus
- Bell
- PM Contract Customers

### Ottawa Priority Customers

- PWGSC
- BGIS
- Rogers
- Telus
- PM Contract Customers

---

# Technician Profiles

---

## Alain Duguay

### Home Location
Les Cèdres

### Experience
- 15+ years

### Coverage Territory
- West Island of Montreal
- Vaudreuil
- Hudson
- Areas west of Autoroute 13

### Expertise
- General service
- Preventive maintenance
- Engine work
- Project work

### Security Certifications
- Secret Level II
- Secret Level III
- Dwyer Hill
- Canadian Nuclear Laboratories (CNL)
- RCMP Clearance

### Cummins Qualifications
- Load Bank & PM
- NFPA 70E Electrical Safety
- Fundamentals of Controls
- Fundamentals of ATS
- BETT Qualification
- InPower Qualification
- Alternator Repair
- Generator Frame Repair
- PCC 2100 / 3100 / 3200

### Work Preferences
- Engine Work: Yes
- Projects/Commissioning: Yes
- PM: Yes

### Recommended For
- Government customers
- High-security sites
- Engine diagnostics
- PM contracts

---

## Ali Reza-Sabour

### Home Location
Saint-Clet

### Experience
- 15+ years

### Coverage Territory
- Montreal
- Vaudreuil
- Hudson
- West of Autoroute 13

### Expertise
- General service
- Customer relations

### Security Certifications
- Secret Level II
- Dwyer Hill
- CNL

### Cummins Qualifications
- PCC 2100
- PCC 3100
- PCC 3200
- Controls
- ATS
- Alternators
- Load Bank & PM

### Work Preferences
- Engine Work: Yes
- PM: Yes

### Recommended For
- Customer-facing assignments
- Montreal service calls
- Security-cleared sites

---

## Benoit Laramée

### Home Location
Mercier

### Experience
- 3-5 years

### Coverage Territory
- All regions
- North Shore support
- Ottawa support

### Expertise
- General service
- Flexible scheduling support

### Security Certifications
- Secret Level II

### Cummins Qualifications
- Load Bank & PM
- NFPA 70E
- Controls
- ATS
- PCC 2100
- PCC 3100

### Work Preferences
- Overtime: Yes

### Recommended For
- Coverage gaps
- Technician shortages
- Workload balancing

---

## François Racine

### Home Location
Coteau-du-Lac

### Experience
- 15+ years

### Coverage Territory
- Quebec
- Ottawa
- Kingston

### Expertise
- Projects
- Commissioning
- Start-ups
- Technical leadership

### Security Certifications
- Secret Level II
- Secret Level III
- Dwyer Hill
- CNL
- RCMP

### Cummins Qualifications
- Full generator controls path
- ATS qualifications
- PCC 2100
- PCC 3100
- PCC 3200
- Alternator repair
- Controls
- NSPS

### Work Preferences
- Travel: Yes
- Overtime: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Commissioning
- Complex diagnostics
- Government customers
- Nuclear sites
- Technical consultations

---

## Michael Sulte

### Home Location
Hinchinbrooke

### Experience
- 1-3 years

### Coverage Territory
- Montreal
- South Shore
- Saint-Laurent
- Lasalle
- Huntingdon
- Ormstown
- Hemmingford

### Expertise
- Electrical diagnostics
- Wiring
- Cable installation

### Cummins Qualifications
- Controls
- ATS
- Alternator Repair
- InPower

### Work Preferences
- Overtime: Yes
- PM: Yes

### Recommended For
- Electrical issues
- Wiring projects
- Cable work

---

## Patrick Robitaille

### Home Location
Montreal

### Experience
- Senior Technician

### Coverage Territory
- Montreal
- South Shore
- North Shore
- Ottawa

### Expertise
- General service
- Long-distance travel

### Recommended For
- Regional support
- Ottawa assignments
- Emergency coverage

---

## Alexandre Pelletier-Guay

### Home Location
Sabrevois

### Experience
- 10-15 years

### Coverage Territory
- Montreal
- South Shore

### Expertise
- Large-scale projects
- CN Railway work

### Cummins Qualifications
- Controls
- ATS
- PCC 2100
- PCC 3100

### Work Preferences
- Travel: Yes
- Overtime: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- CN projects
- Railway customers
- Large contracted work

---

## Christian Dubreuil

### Home Location
Delson

### Experience
- 15+ years

### Coverage Territory
- Montreal
- South Shore

### Expertise
- Advanced diagnostics
- Difficult troubleshooting

### Awards
- Cummins Top Tech

### Security Certifications
- Secret Level II

### Cummins Qualifications
- Controls
- ATS
- PCC 2100
- PCC 3100
- NSPS

### Work Preferences
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Escalations
- Difficult failures
- Technical troubleshooting

---

## Donald Lagacé

### Home Location
Saint-Catherine

### Experience
- 15+ years

### Role
- In-Shop Technician

### Expertise
- RV generators
- Portable generators

### Field Service Availability
- No

### Recommended For
- RV repairs
- Portable generator work
- Shop work

---

## Élie Rajotte-Lemay

### Home Location
Beloeil

### Experience
- 1-3 years

### Coverage Territory
- Montreal
- South Shore

### Expertise
- PM work
- General service

### Work Preferences
- Travel: Yes
- PM: Yes

### Recommended For
- Preventive maintenance
- Routine service calls

---

## Kevin Duranceau

### Home Location
Beloeil

### Experience
- 10-15 years

### Coverage Territory
- South Shore
- Montreal

### Expertise
- General service
- Projects

### Security Certifications
- Secret Level II

### Cummins Qualifications
- Controls
- ATS
- PCC 2100
- PCC 3100
- PCC 3200

### Work Preferences
- Travel: Yes
- Overtime: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- South Shore coverage
- Technical service calls
- Projects

---

## Maxime Roy

### Home Location
Saint-Paul-de-l'Île-aux-Noix

### Experience
- 3-5 years

### Coverage Territory
- Downtown Montreal
- Châteauguay

### Expertise
- Start-ups
- Load bank testing
- Projects

### Cummins Qualifications
- Load Bank & PM
- Controls
- ATS
- PCC 2100
- PCC 3100

### Work Preferences
- Projects: Yes

### Recommended For
- Start-ups
- Load bank tests
- Project work

---

## Pier-Luc Côté

### Home Location
Marieville

### Experience
- 10-15 years

### Coverage Territory
- Montreal
- South Shore

### Expertise
- Engine diagnostics
- Engine repair
- Project work

### Cummins Qualifications
- Controls
- ATS
- Alternator Repair
- PCC 2100
- PCC 3100

### Work Preferences
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Engine failures
- Technical investigations
- Projects

---

## Sébastien Pépin-Millette

### Experience
- 1-3 years

### Role
- In-Shop Technician

### Expertise
- Electric buses

### Field Service Availability
- No

### Recommended For
- Electric bus repairs
- Shop operations

---

## Benoit Charette-Gosselin

### Home Location
Saint-Jérôme

### Experience
- 15+ years

### Coverage Territory
- North Shore
- Mont-Tremblant
- Northern Quebec

### Expertise
- Projects
- General service

### Security Certifications
- Secret Level II

### Work Preferences
- Travel: Yes
- Engine Work: Yes

### Recommended For
- Remote locations
- North Shore projects
- Technical service calls

---

## Fredy Diaz

### Home Location
Saint-Eustache

### Experience
- 3-5 years

### Coverage Territory
- Laval
- Montreal

### Expertise
- General service
- Maintenance

### Cummins Qualifications
- Controls
- ATS
- Alternator Repair

### Work Preferences
- Overtime: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Laval service coverage
- Maintenance work

---

## Georges Érick Yamna Nghuedieu

### Home Location
Saint-Eustache

### Experience
- 3-5 years

### Coverage Territory
- Laval
- Montreal

### Expertise
- General service
- Maintenance

### Cummins Qualifications
- Controls
- ATS
- PCC 2100
- PCC 3100

### Work Preferences
- Overtime: Yes
- PM: Yes

### Recommended For
- Laval coverage
- Routine service calls

---

## Martin Bourbonnière

### Home Location
L'Assomption

### Experience
- 15+ years

### Coverage Territory
- North Shore
- Trois-Rivières Corridor

### Expertise
- Projects
- Diagnostics
- General service

### Security Certifications
- Secret Level II

### Cummins Qualifications
- Full controls and ATS path
- PCC 2100
- PCC 3100
- PCC 3200

### Work Preferences
- Travel: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Eastern North Shore
- Projects
- Technical investigations

---

## Patrick Bellefleur

### Home Location
L'Assomption

### Experience
- 15+ years

### Coverage Territory
- North Shore
- Trois-Rivières Corridor

### Expertise
- Projects
- Diagnostics
- General service

### Security Certifications
- Secret Level II

### Cummins Qualifications
- Full controls path
- PCC 2100
- PCC 3100
- PCC 3200

### Work Preferences
- Travel: Yes
- Overtime: Yes
- Engine Work: Yes
- Projects: Yes

### Recommended For
- Projects
- Emergency work
- Eastern North Shore territory coverage

---

# Policies

## General Technician Working Hours

### Field Service

#### Standard

- 56 hours/week
- 12 hours/day maximum
- 6 consecutive days

#### Level 1 Exception

Requires Branch Manager approval:

- 72 hours/week
- 14 hours/day
- 240 hours/month

#### Driving Guidelines

Standard:

- 10 hours driving/day
- 15-minute break every 2 hours
- Combined work and driving not to exceed 12 hours

---

## Night Work Compensation

### Rest Requirement

When finishing work during after-hours, technicians must receive:

- Minimum 8 hours rest

Example:

- Work completed: 3:00 AM
- Earliest return: 11:00 AM

### Administration Responsibilities

Do not schedule work before:

- Completion of required rest period

Use:

```text
4 Hour Night Shift Incentive Pay
```

work order when applicable.

---

# Tribal Knowledge

## Customer Referrals

Refer customers to:

```text
1-800-CUMMINS
```

for:

- Owner manuals
- Installation guides
- Parts lists
- Product documentation

## North Shore Parts Storage

### L'Assomption
- Patrick Bellefleur
- Martin Bourbonnière

### Boisbriand
- Georges Érick Yamna Nghuedieu
- Fredy Diaz

### Mirabel
- Benoit Charette-Gosselin

### Important Rule

Confirm parts arrival before scheduling service.

Parts are sent on Thurdays and arrive and Tuesdays of the following week.

## FieldAware Best Practice

Refresh the scheduler frequently to avoid technician double bookings.

---

# FAQ

(Add future recurring questions and answers here.)