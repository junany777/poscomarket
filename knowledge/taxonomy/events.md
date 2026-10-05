# Event Taxonomy and Classification Rules

## 1. Purpose

This document defines the canonical event taxonomy and event-classification rules used by the Steel Market Intelligence Platform.

The taxonomy is used for:

- source classification
- event extraction
- event clustering
- company strategy analysis
- steel-demand reasoning
- opportunity generation
- dashboard filtering
- alerts
- Ask Steel AI retrieval

All event extraction must use the canonical event types defined in this document.

Do not dynamically create new event types during normal processing.

If no existing type applies, use:

```text
OTHER
```

If the event itself is unclear, use:

```text
UNKNOWN
```

---

# 2. Core Principle

An Event represents a real-world business or industrial occurrence.

It is not:

```text
an opinion
a broad trend
a journalist interpretation
a generic industry theme
a product feature
```

It should answer:

```text
Who did what, where, when, and with what business significance?
```

---

# 3. Event Extraction Structure

Every extracted event should include:

```text
event_type
event_subtype
primary_company
industry
title
description
country
region
investment_amount
currency
capacity_value
capacity_unit
announced_at
start_date
target_date
status
evidence_ids
extraction_confidence
```

Not every field must be populated.

Missing information should remain null or UNKNOWN.

Do not invent missing data.

---

# 4. Primary Event vs Secondary Event

A source may contain several meaningful business actions.

The system should distinguish:

```text
PRIMARY EVENT
```

and:

```text
SECONDARY EVENTS
```

The Primary Event is the event that best represents the source's central business action.

Secondary Events capture materially distinct actions that are useful for downstream intelligence.

Do not classify every sentence as a separate event.

---

# 5. Maximum Events Per Source

Default rule:

```text
1 Primary Event
+
0 to 2 Secondary Events
```

Recommended maximum:

```text
3 events per source document
```

Exception:

A source may contain more than 3 truly independent events, such as:

```text
annual strategy briefing
multi-business investment announcement
government policy package
large earnings/IR presentation
```

In these cases, the source should first be segmented into logical sections or sub-documents.

Do not generate 8-10 events from one general article.

---

# 6. When to Create Multiple Events

Create separate events only when the actions are independently meaningful.

Example:

```text
Company announces:

1. $3B new battery plant
2. acquisition of battery recycling company
3. joint venture with automaker
```

Valid:

```text
NEW_FACTORY
M_AND_A
JOINT_VENTURE
```

These are distinct business actions.

Do not merge them into one vague event.

---

# 7. When NOT to Create Multiple Events

Do not split when one action naturally implies another.

Example:

```text
Company invests $2B to build a new EV factory.
```

Possible labels:

```text
CAPEX
NEW_FACTORY
```

These describe the same underlying transaction.

Store as one event with:

```text
event_type = NEW_FACTORY
event_subtype = EV_FACTORY

investment_amount = 2B
```

Do not automatically create a separate CAPEX event unless the investment itself has distinct analytical meaning.

---

# 8. Primary Event Selection Rule

Use the following precedence logic.

Ask:

```text
What is the main real-world action?
```

Then choose the most specific event type.

Preferred rule:

```text
Specific physical/business action
>
generic financial action
```

Examples:

```text
NEW_FACTORY
>
CAPEX
```

```text
CAPACITY_EXPANSION
>
CAPEX
```

```text
M_AND_A
>
CAPEX
```

```text
JOINT_VENTURE
>
CAPEX
```

```text
R_AND_D
>
CAPEX
```

when the investment is specifically for an R&D program.

CAPEX should be Primary when the source announces an investment plan without a more specific dominant action.

---

# 9. Primary Event Decision Hierarchy

Use this conceptual priority:

```text
1. M_AND_A
2. JOINT_VENTURE
3. NEW_FACTORY
4. CAPACITY_EXPANSION
5. CONTRACT
6. PRODUCT_LAUNCH
7. R_AND_D
8. SUPPLY_CHAIN
9. PROCUREMENT
10. NEW_BUSINESS
11. ESG
12. EXPORT
13. REGULATION
14. FINANCIAL_CHANGE
15. CAPEX
16. OTHER
```

This is not an absolute business-importance ranking.

It is a rule for selecting the most specific structural action over generic investment labeling.

---

# 10. CAPEX

Canonical code:

```text
CAPEX
```

Korean name:

```text
설비투자 / 자본적지출
```

Use when:

```text
a company announces or commits material investment
and the investment is not better represented by a more specific event type
```

Typical signals:

```text
invest
investment plan
capital expenditure
spend
allocate capital
facility investment
equipment investment
```

Use as Primary when:

```text
investment is broad
multiple facilities are included
specific physical outcome is unclear
```

Example:

```text
Company announces KRW 5 trillion investment across manufacturing operations.
```

Primary:

```text
CAPEX
```

Do not use CAPEX as a separate event if:

```text
Company invests KRW 1 trillion to build a new plant.
```

In this case:

```text
Primary = NEW_FACTORY
investment_amount stored on same event
```

---

# 11. NEW_FACTORY

Canonical code:

```text
NEW_FACTORY
```

Use when:

```text
a company creates a new manufacturing site, plant, mill, fab, shipyard facility, production center, or major greenfield facility
```

Signals:

```text
build new plant
new factory
greenfield
new manufacturing facility
new production site
new mill
new fab
```

Examples:

```text
new EV plant
new steel mill
new battery factory
new semiconductor fab
```

Do not use if:

```text
existing plant capacity is merely increased
```

That should normally be:

```text
CAPACITY_EXPANSION
```

---

# 12. CAPACITY_EXPANSION

Canonical code:

```text
CAPACITY_EXPANSION
```

Use when:

```text
existing production capability is increased materially
```

Examples:

```text
add production line
increase annual capacity
expand plant
increase output
debottleneck existing facility
```

Typical fields:

```text
old_capacity
new_capacity
capacity_increase
capacity_unit
```

If a new factory is built as part of the expansion:

Primary selection depends on source emphasis.

Rule:

```text
New independent site
→ NEW_FACTORY

Expansion inside existing site
→ CAPACITY_EXPANSION
```

---

# 13. CAPEX vs CAPACITY_EXPANSION

Example:

```text
Company invests $800M to expand annual production from 1M to 1.5M tons.
```

Primary:

```text
CAPACITY_EXPANSION
```

Store:

```text
investment_amount = 800M
```

Do not create a second CAPEX event unless the investment program includes additional unrelated investments.

Reason:

```text
capacity increase is the economically meaningful business action
CAPEX is the financing magnitude of that action
```

---

# 14. CAPEX vs NEW_FACTORY

Example:

```text
Company invests KRW 3 trillion to construct a new factory in the U.S.
```

Primary:

```text
NEW_FACTORY
```

Store investment value in the same event.

Secondary CAPEX:

```text
normally not needed
```

---

# 15. M_AND_A

Canonical code:

```text
M_AND_A
```

Use when:

```text
company acquires
merges with
sells
divests
or takes control of another business or major asset
```

Signals:

```text
acquire
acquisition
merge
merger
takeover
divest
sell subsidiary
stake acquisition
```

Subtypes:

```text
ACQUISITION
MERGER
DIVESTITURE
STAKE_ACQUISITION
ASSET_ACQUISITION
```

Primary if ownership/control change is the main action.

---

# 16. JOINT_VENTURE

Canonical code:

```text
JOINT_VENTURE
```

Use when:

```text
two or more companies create or agree to create a jointly owned business entity or production operation
```

Signals:

```text
joint venture
JV
joint company
jointly establish
jointly operate
```

Do not classify simple cooperation agreements as JV.

Use:

```text
PARTNERSHIP
```

only if later introduced as a distinct taxonomy, otherwise use:

```text
OTHER
```

or represent as relationship metadata.

---

# 17. NEW_BUSINESS

Canonical code:

```text
NEW_BUSINESS
```

Use when:

```text
a company enters a materially new business area or market
```

Examples:

```text
automaker enters robotics
shipbuilder enters hydrogen production
steelmaker launches battery-material business
```

Do not use for:

```text
a new product inside an existing business
```

Use:

```text
PRODUCT_LAUNCH
```

instead.

---

# 18. PRODUCT_LAUNCH

Canonical code:

```text
PRODUCT_LAUNCH
```

Use when:

```text
a company commercially launches or begins selling a new product, grade, platform, equipment, or service
```

Signals:

```text
launch
release
commercialize
begin sales
mass production begins
new grade
new model
```

Do not use if:

```text
product is still under development
```

Use:

```text
R_AND_D
```

instead.

---

# 19. R_AND_D

Canonical code:

```text
R_AND_D
```

Korean name:

```text
연구개발
```

Use when:

```text
a company starts, expands, completes, or publicly announces meaningful research and development activity
```

Examples:

```text
new steel grade development
battery technology project
new motor-core material
pilot technology
prototype development
research consortium
```

Signals:

```text
develop
R&D
research
prototype
pilot
demonstration
test technology
joint development
```

Do not use R_AND_D when:

```text
the product is already commercially launched
```

Use:

```text
PRODUCT_LAUNCH
```

Do not use R_AND_D simply because a company mentions innovation.

There must be an identifiable development activity.

---

# 20. R_AND_D vs PRODUCT_LAUNCH

Example:

```text
Company develops a new electrical steel grade and starts pilot testing.
```

Primary:

```text
R_AND_D
```

Example:

```text
Company begins commercial sales of newly developed electrical steel.
```

Primary:

```text
PRODUCT_LAUNCH
```

If one source clearly covers both:

```text
development completed
+
commercial sales begin
```

Primary should usually be:

```text
PRODUCT_LAUNCH
```

Secondary:

```text
R_AND_D
```

only if development completion itself carries meaningful analytical value.

---

# 21. CONTRACT

Canonical code:

```text
CONTRACT
```

Use when:

```text
a company wins, signs, awards, or secures a material commercial contract
```

Examples:

```text
ship order
long-term steel supply contract
construction EPC award
defense contract
equipment supply agreement
offtake agreement
```

Signals:

```text
order
contract
awarded
supply agreement
purchase agreement
offtake
won contract
signed deal
```

Subtypes may include:

```text
SUPPLY_CONTRACT
SHIP_ORDER
EPC_CONTRACT
LONG_TERM_AGREEMENT
DEFENSE_CONTRACT
OFFTAKE
```

---

# 22. CONTRACT Threshold

Do not create CONTRACT events for routine low-value transactions.

Create when one or more applies:

```text
material revenue impact
strategic customer
long-term contract
new market
new technology adoption
large quantity
significant capacity utilization
high steel-demand relevance
```

---

# 23. PROCUREMENT

Canonical code:

```text
PROCUREMENT
```

Use when:

```text
a company materially changes how or from whom it procures products, materials, or strategic inputs
```

Examples:

```text
new steel supplier selection
local sourcing policy
dual-sourcing strategy
strategic procurement agreement
```

Do not use for every purchase order.

PROCUREMENT represents a sourcing strategy or material procurement change.

---

# 24. SUPPLY_CHAIN

Canonical code:

```text
SUPPLY_CHAIN
```

Use when:

```text
a company materially restructures sourcing, production, logistics, localization, or supplier network
```

Examples:

```text
local supplier expansion
China-plus-one strategy
regional supply-chain shift
supplier consolidation
localization program
```

Difference from PROCUREMENT:

```text
PROCUREMENT
= buying decision

SUPPLY_CHAIN
= broader network/structure change
```

---

# 25. ESG

Canonical code:

```text
ESG
```

Use when:

```text
a company announces material decarbonization, environmental, circularity, or sustainability action
```

Examples:

```text
green steel adoption
carbon reduction plan
renewable power conversion
recycling program
low-carbon production investment
```

Avoid using ESG for generic sustainability statements without a concrete action.

---

# 26. EXPORT

Canonical code:

```text
EXPORT
```

Use when:

```text
a company materially expands, enters, or changes export markets
```

Examples:

```text
first shipment to new country
major export contract
new regional export strategy
export volume expansion
```

Do not use when location is merely mentioned.

---

# 27. REGULATION

Canonical code:

```text
REGULATION
```

Use when:

```text
government or regulatory changes materially affect industrial activity, trade, investment, technology, or steel demand
```

Examples:

```text
tariff
emission regulation
local-content requirement
subsidy rule
trade restriction
industrial policy
```

Primary company may be null for regulation events.

Primary entity may be:

```text
government
regulator
jurisdiction
```

---

# 28. FINANCIAL_CHANGE

Canonical code:

```text
FINANCIAL_CHANGE
```

Use when:

```text
a material financial change affects company behavior or strategic capacity
```

Examples:

```text
large earnings deterioration
major profit improvement
debt restructuring
liquidity crisis
credit downgrade
```

Do not use for routine quarterly financial reporting unless the change has strategic relevance.

---

# 29. OTHER

Canonical code:

```text
OTHER
```

Use only when:

```text
the event is clear and meaningful
but no canonical event type applies
```

Every OTHER event should retain:

```text
event_subtype
classification_note
```

for future taxonomy review.

---

# 30. UNKNOWN

Canonical code:

```text
UNKNOWN
```

Use when:

```text
the source suggests an event
but the event type cannot be determined reliably
```

UNKNOWN is preferable to forcing an incorrect taxonomy label.

---

# 31. Compound Event Rule

One source may contain one action with several characteristics.

Example:

```text
Company invests $1B to build a new hydrogen plant that will raise production capacity.
```

Possible concepts:

```text
CAPEX
NEW_FACTORY
CAPACITY_EXPANSION
```

Do not automatically create three events.

Primary decision:

```text
If completely new site:
NEW_FACTORY

If expansion of existing site:
CAPACITY_EXPANSION
```

Store:

```text
investment_amount
capacity_change
```

as event attributes.

---

# 32. Independent Compound Event Rule

Create separate events if each action could occur independently.

Example:

```text
Company announces:
- new EV factory
- acquisition of battery company
```

Create:

```text
Event 1 = NEW_FACTORY
Event 2 = M_AND_A
```

---

# 33. Primary Event Selection Algorithm

Use the following sequence:

```text
STEP 1
Identify all factual business actions.

STEP 2
Group actions describing the same underlying transaction.

STEP 3
Select the most specific event type in each group.

STEP 4
Determine which group is the central focus of the source.

STEP 5
Mark that group as Primary Event.

STEP 6
Create up to two additional Secondary Events only when materially independent.
```

---

# 34. Primary Event Scoring Heuristic

If ambiguity remains, score candidate events using:

```text
Source Headline Match          30%
Source Lead Paragraph Match    25%
Business Materiality           20%
Specificity                    15%
Downstream Intelligence Value  10%
```

The highest score becomes Primary.

This heuristic may be implemented deterministically or with structured AI support.

---

# 35. Headline Dominance Rule

The event explicitly stated in the headline should generally be Primary unless:

```text
headline is misleading
headline is generic
another event clearly represents the substantive action
```

Example headline:

```text
Company to build $2B EV factory in Georgia
```

Primary:

```text
NEW_FACTORY
```

not:

```text
CAPEX
```

---

# 36. Specificity Rule

Prefer:

```text
NEW_FACTORY
```

over:

```text
CAPEX
```

Prefer:

```text
CAPACITY_EXPANSION
```

over:

```text
CAPEX
```

Prefer:

```text
PRODUCT_LAUNCH
```

over:

```text
R_AND_D
```

if commercialization is already occurring.

Prefer:

```text
M_AND_A
```

over:

```text
NEW_BUSINESS
```

when market entry happens through acquisition.

---

# 37. Event Status

Use standardized status values:

```text
ANNOUNCED
PLANNED
APPROVED
IN_PROGRESS
PILOT
COMMERCIAL
COMPLETED
DELAYED
CANCELLED
UNKNOWN
```

Not every status applies to every event.

Examples:

```text
NEW_FACTORY
ANNOUNCED → IN_PROGRESS → COMPLETED
```

```text
R_AND_D
ANNOUNCED → PILOT → COMPLETED
```

```text
PRODUCT_LAUNCH
ANNOUNCED → COMMERCIAL
```

---

# 38. Event Date Rules

Use different fields for different concepts.

```text
announced_at
= when event was publicly announced

event_date
= when event actually happened if known

start_date
= planned or actual start

target_date
= expected completion or commercialization
```

Do not collapse these into one date.

---

# 39. Investment Amount Rule

If a source states an investment amount:

```text
store original value
store original currency
store normalized value separately if calculated
```

Do not infer missing investment amounts.

---

# 40. Capacity Rule

Store capacity only when directly supported or calculable from explicit source data.

Examples:

```text
5 million tons/year
200,000 vehicles/year
30 GWh/year
```

Do not invent production capacity.

---

# 41. Event Confidence

Recommended extraction confidence:

```text
90-100
explicit event, clear company, clear action

75-89
strong but some fields uncertain

60-74
meaningful event inferred from context

below 60
use NEEDS_REVIEW or UNKNOWN where appropriate
```

Confidence is not business importance.

---

# 42. Event Importance

Event importance is separate from extraction confidence.

Importance may consider:

```text
company importance
investment scale
capacity change
strategic technology
market impact
steel-demand relevance
```

This should not alter event classification.

---

# 43. Source-to-Event Examples

## Example 1

Source:

```text
Hyundai Motor will invest $4B to build a new EV factory in the U.S.
```

Event:

```text
Primary:
NEW_FACTORY

event_subtype:
EV_FACTORY

investment_amount:
4B USD

Secondary:
none
```

---

# 44. Example 2

Source:

```text
Existing EV plant will increase capacity from 300,000 to 500,000 vehicles after a $700M investment.
```

Event:

```text
Primary:
CAPACITY_EXPANSION

investment_amount:
700M USD

capacity_change:
300k → 500k
```

Do not create separate CAPEX event.

---

# 45. Example 3

Source:

```text
Steelmaker announces KRW 2 trillion investment across several production facilities without detailed projects.
```

Event:

```text
Primary:
CAPEX
```

---

# 46. Example 4

Source:

```text
Shipbuilder wins order for 12 LNG carriers worth $3B.
```

Event:

```text
Primary:
CONTRACT

event_subtype:
SHIP_ORDER
```

---

# 47. Example 5

Source:

```text
Steelmaker and automaker begin joint development of next-generation EV motor steel.
```

Event:

```text
Primary:
R_AND_D

event_subtype:
JOINT_DEVELOPMENT
```

Do not use JOINT_VENTURE unless a jointly owned entity is actually created.

---

# 48. Example 6

Source:

```text
Company completes development and starts mass production of new automotive steel.
```

Primary:

```text
PRODUCT_LAUNCH
```

Secondary R_AND_D:

```text
normally unnecessary
```

unless development completion is separately significant.

---

# 49. Example 7

Source:

```text
Company acquires a battery-material producer to enter the battery business.
```

Primary:

```text
M_AND_A
```

Secondary:

```text
NEW_BUSINESS
```

may be created if downstream strategy analysis benefits from explicitly tracking market entry.

Default recommendation:

```text
Primary = M_AND_A
NEW_BUSINESS represented in strategy inference
```

This avoids duplicate event inflation.

---

# 50. Example 8

Source:

```text
Steelmaker signs 10-year supply agreement with automaker and will build a local service center.
```

Possible events:

```text
Primary:
CONTRACT

Secondary:
NEW_FACTORY
```

only if the service center is materially important and clearly committed.

If the service center is minor operational detail, keep only CONTRACT.

---

# 51. Example 9

Source:

```text
Government introduces a local-content requirement for EV batteries.
```

Event:

```text
Primary:
REGULATION
```

Downstream inference may identify:

```text
SUPPLY_CHAIN
LOCALIZATION
```

but these should not automatically become separate events unless companies later take concrete actions.

---

# 52. Example 10

Source:

```text
Company announces carbon-neutrality target by 2050.
```

If only aspirational:

```text
ESG
low importance
```

If accompanied by concrete plant conversion investment:

```text
Primary:
CAPACITY_EXPANSION or CAPEX depending on action

Secondary:
ESG
```

Specific physical action should remain Primary.

---

# 53. News Article vs Official Disclosure

The same event may appear in multiple sources.

Do not create one event per source.

Use:

```text
event clustering
+
event_evidence
```

Expected:

```text
DART disclosure
Corporate release
News article
↓
One Event
```

---

# 54. Follow-Up News

A follow-up source should update an existing event when:

```text
same company
same project
same facility
same event type
same approximate timeline
```

Examples of updates:

```text
investment amount revised
target date changed
project delayed
capacity increased
official approval received
```

Do not create a new event unless the underlying business action is materially distinct.

---

# 55. Material Change Rule

Create a new event only if the new development itself is independently meaningful.

Example:

```text
Original:
NEW_FACTORY announced

Later:
construction starts
```

Usually:

```text
update status of existing event
```

Example:

```text
Later:
company cancels project
```

Normally:

```text
update existing event status to CANCELLED
```

and record new evidence.

---

# 56. Event Subtypes

Use event_subtype to preserve specificity without exploding the top-level taxonomy.

Examples:

```text
NEW_FACTORY
→ EV_FACTORY
→ BATTERY_FACTORY
→ STEEL_MILL
→ SEMICONDUCTOR_FAB
```

```text
CONTRACT
→ SHIP_ORDER
→ SUPPLY_CONTRACT
→ EPC_CONTRACT
```

```text
R_AND_D
→ MATERIAL_DEVELOPMENT
→ PILOT_PROJECT
→ JOINT_DEVELOPMENT
```

Subtypes may evolve more frequently than top-level event types.

---

# 57. Event Type vs Strategy

Do not confuse actions with inferred strategy.

Example:

```text
Event:
NEW_FACTORY
```

Possible strategies:

```text
GROWTH
LOCALIZATION
```

Do not create:

```text
LOCALIZATION
```

as an event type.

---

# 58. Event Type vs Industry Trend

Do not classify broad trends as events.

Bad:

```text
EV market growing
```

This is an industry trend.

Good:

```text
Automaker opens EV plant
```

This is an event.

---

# 59. Event Type vs Technology Tag

Do not create event types such as:

```text
AI
HYDROGEN
ROBOTICS
```

These are technology or industry tags.

Example:

```text
R_AND_D
technology_tag = HYDROGEN
```

---

# 60. Event Type vs Application

Do not create event types like:

```text
EV_MOTOR
LNG_CARRIER
WIND_TOWER
```

These belong to application taxonomy.

---

# 61. Company Financial Results

Quarterly earnings alone should not automatically create FINANCIAL_CHANGE.

Use FINANCIAL_CHANGE when:

```text
financial performance materially changes investment capacity
production strategy
business continuity
or market behavior
```

Example:

```text
Company reports severe losses and cancels expansion.
```

Primary may be:

```text
CAPACITY_EXPANSION status update / cancellation
```

FINANCIAL_CHANGE may be secondary context.

---

# 62. Contract Renewal

Routine renewals should not always create new CONTRACT events.

Create when:

```text
value is material
duration changes materially
new supplier/customer relationship
new geography
new technology
strategic importance
```

---

# 63. Rumors

Do not create validated high-confidence events from rumors alone.

Possible handling:

```text
event status = UNKNOWN
confidence low
needs review
```

or store only as source material.

Do not generate high-priority opportunities from unverified rumors.

---

# 64. Announcements vs Intentions

Distinguish:

```text
"will build"
```

from:

```text
"considering building"
```

The latter may remain:

```text
PLANNED
low-to-medium confidence
```

or not become a validated event if too speculative.

---

# 65. Multi-Company Events

One event may involve several companies.

Example:

```text
Automaker and battery company form JV.
```

Primary event:

```text
JOINT_VENTURE
```

Store:

```text
primary_company
partner_company
relationship_role
```

Do not create two duplicate JV events.

---

# 66. Government-Led Events

REGULATION may have no corporate primary company.

Example:

```text
EU introduces new carbon-border rule.
```

Primary entity:

```text
EU
```

Affected industries:

```text
STEEL
AUTOMOTIVE
ENERGY
etc.
```

---

# 67. Event Prioritization for Steel Intelligence

Events with particularly high downstream steel relevance often include:

```text
NEW_FACTORY
CAPACITY_EXPANSION
CONTRACT
R_AND_D
PRODUCT_LAUNCH
SUPPLY_CHAIN
PROCUREMENT
REGULATION
ESG
```

This does not mean other event types are ignored.

---

# 68. Event Processing Priority

Initial MVP priority:

```text
HIGH PRIORITY

CAPEX
NEW_FACTORY
CAPACITY_EXPANSION
CONTRACT
R_AND_D
SUPPLY_CHAIN
ESG
```

Secondary:

```text
PRODUCT_LAUNCH
NEW_BUSINESS
JOINT_VENTURE
M_AND_A
PROCUREMENT
EXPORT
REGULATION
FINANCIAL_CHANGE
```

The system must still classify all supported types.

---

# 69. Event Classification Output

Recommended AI output:

```json
{
  "primary_event": {
    "event_type": "CAPACITY_EXPANSION",
    "event_subtype": "EV_PRODUCTION",
    "confidence": 94,
    "reason": "The article centers on increasing production capacity at an existing facility."
  },
  "secondary_events": [],
  "attributes": {
    "investment_amount": 700000000,
    "investment_currency": "USD",
    "capacity_before": 300000,
    "capacity_after": 500000,
    "capacity_unit": "vehicles/year"
  }
}
```

The `reason` is for validation/debugging and need not always be persisted.

---

# 70. Multiple Event Output

Example:

```json
{
  "primary_event": {
    "event_type": "M_AND_A",
    "event_subtype": "ACQUISITION",
    "confidence": 96
  },
  "secondary_events": [
    {
      "event_type": "NEW_BUSINESS",
      "event_subtype": "BATTERY_RECYCLING",
      "confidence": 82
    }
  ]
}
```

Secondary event should only exist if downstream analysis genuinely benefits from it.

---

# 71. Overclassification Guardrail

Avoid this behavior:

```text
Article:
Company builds new EV plant.

Events:
CAPEX
NEW_FACTORY
CAPACITY_EXPANSION
NEW_BUSINESS
ESG
SUPPLY_CHAIN
```

This is overclassification.

Correct behavior may be:

```text
Primary:
NEW_FACTORY

Attributes:
investment amount
capacity

Strategies:
LOCALIZATION
ELECTRIFICATION

Tags:
EV
```

---

# 72. Underclassification Guardrail

Avoid collapsing truly separate actions.

Example:

```text
Company acquires supplier and separately announces a new plant.
```

Correct:

```text
M_AND_A
+
NEW_FACTORY
```

---

# 73. Event Deduplication Key

A conceptual event deduplication key may use:

```text
company
event_type
facility/project
country/region
time window
major amount/capacity
```

Example:

```text
Hyundai
NEW_FACTORY
Georgia EV Plant
US-GA
2026
```

Do not rely on headline text alone.

---

# 74. Event Update vs New Event Decision

Update existing event when:

```text
same project identity
same core action
new status or details
```

Create new event when:

```text
different project
different facility
different business action
different ownership transaction
different contract
```

---

# 75. Event Confidence vs Source Confidence

Event confidence should consider:

```text
source reliability
clarity of action
consistency across sources
field completeness
```

A clear event from a weaker source may have moderate confidence.

A clear event confirmed by official disclosure may have high confidence.

---

# 76. Event Classification Quality Tests

Tests should include:

```text
CAPEX vs NEW_FACTORY
CAPEX vs CAPACITY_EXPANSION
R_AND_D vs PRODUCT_LAUNCH
JOINT_VENTURE vs PARTNERSHIP
CONTRACT vs PROCUREMENT
SUPPLY_CHAIN vs PROCUREMENT
REGULATION vs company action
financial reporting vs FINANCIAL_CHANGE
```

---

# 77. Golden Test Case 1

Input:

```text
Company will invest $3B to construct a new EV plant.
```

Expected:

```text
Primary = NEW_FACTORY
Secondary = none
```

---

# 78. Golden Test Case 2

Input:

```text
Company will invest $500M to raise existing capacity by 30%.
```

Expected:

```text
Primary = CAPACITY_EXPANSION
Secondary = none
```

---

# 79. Golden Test Case 3

Input:

```text
Company announces a five-year $10B investment program covering automation, R&D, and facility upgrades.
```

Expected:

```text
Primary = CAPEX
```

Secondary events only if individual projects are separately defined and material.

---

# 80. Golden Test Case 4

Input:

```text
Company and customer jointly develop next-generation steel for EV motors.
```

Expected:

```text
Primary = R_AND_D
```

Do not use JOINT_VENTURE unless a JV entity exists.

---

# 81. Golden Test Case 5

Input:

```text
Company receives order for 20 LNG carriers.
```

Expected:

```text
Primary = CONTRACT
subtype = SHIP_ORDER
```

---

# 82. Golden Test Case 6

Input:

```text
Company opens a new mill and separately acquires a local processor.
```

Expected:

```text
Primary = NEW_FACTORY or M_AND_A depending on article central focus
Secondary = the other event
```

Headline and lead paragraph should guide Primary selection.

---

# 83. Golden Test Case 7

Input:

```text
Company launches commercially a product previously under development.
```

Expected:

```text
Primary = PRODUCT_LAUNCH
```

R_AND_D should not normally be a second event.

---

# 84. Golden Test Case 8

Input:

```text
Government increases local-content requirements for EV manufacturing.
```

Expected:

```text
Primary = REGULATION
```

Possible downstream strategy:

```text
LOCALIZATION
SUPPLY_CHAIN_RESILIENCE
```

but not additional events yet.

---

# 85. Event Extraction Prompt Rule

Event-extraction prompts should explicitly include:

```text
Choose the most specific canonical event type.

Do not create CAPEX as a separate event when investment amount belongs to NEW_FACTORY, CAPACITY_EXPANSION, M_AND_A, R_AND_D, or another more specific event.

Create secondary events only when they represent materially independent business actions.

Return no more than 3 events per source.

Do not classify inferred strategy as an event.

Do not invent missing details.

Use UNKNOWN when classification is insufficiently supported.
```

---

# 86. Final Event Rule

The goal of event classification is not to maximize the number of labels.

The goal is to produce the smallest set of structured events that accurately represents the real-world business actions in the source.

Preferred behavior:

```text
specific
minimal
non-duplicative
evidence-based
useful for downstream intelligence
```

Avoid:

```text
generic
overlapping
inflated
speculative
```

The event taxonomy should make the downstream chain reliable:

```text
SOURCE
→ EVENT
→ STRATEGY
→ STEEL DEMAND
→ PRODUCT MATCH
→ OPPORTUNITY
```
