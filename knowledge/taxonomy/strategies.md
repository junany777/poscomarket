# Strategy Taxonomy and Inference Rules

## 1. Purpose

This document defines the canonical company strategy taxonomy used by the Steel Market Intelligence Platform.

Strategies are inferred from validated events and evidence.

A strategy is not the same as an event.

Example:

```text
Event:
NEW_FACTORY

Possible Strategy:
GROWTH
LOCALIZATION
ELECTRIFICATION
```

The system must clearly distinguish:

```text
FACT
```

from:

```text
STRATEGY INFERENCE
```

Do not store inferred strategy as factual evidence.

---

# 2. Core Principle

A Strategy represents a likely business direction suggested by one or more events.

The system should answer:

```text
What does this company appear to be trying to achieve?
```

not:

```text
What happened?
```

"What happened?" belongs to Event Intelligence.

---

# 3. Strategy Inference Chain

Use this reasoning sequence:

```text
Evidence
↓
Event
↓
Observed Business Action
↓
Possible Strategic Intent
↓
Strategy Classification
↓
Confidence
```

Never infer strategy directly from an article headline without first identifying the underlying event.

---

# 4. Strategy Output Structure

Recommended structured output:

```json
{
  "strategy_type": "LOCALIZATION",
  "summary": "The company appears to be increasing regional manufacturing and sourcing capability.",
  "inference_basis": [
    "New manufacturing facility in North America",
    "Supplier localization program"
  ],
  "time_horizon": "MEDIUM",
  "confidence": 87
}
```

---

# 5. Number of Strategies Per Event

Default rule:

```text
1 Primary Strategy
+
0 to 2 Secondary Strategies
```

Recommended maximum:

```text
3 strategies per event
```

Do not attach every plausible strategy to every event.

The strategy set should represent only the strongest and most useful interpretations.

---

# 6. Primary Strategy

The Primary Strategy should represent the main strategic intent behind the event.

Example:

```text
Event:
Company builds new EV plant in the U.S.

Possible Strategies:

LOCALIZATION
GROWTH
ELECTRIFICATION
```

If the main purpose is regional production:

```text
Primary:
LOCALIZATION
```

Secondary:

```text
GROWTH
ELECTRIFICATION
```

---

# 7. Canonical Strategy Types

Use the following canonical strategies:

```text
GROWTH
LOCALIZATION
PREMIUMIZATION
COST_REDUCTION
ELECTRIFICATION
AUTOMATION
DECARBONIZATION
VERTICAL_INTEGRATION
SUPPLY_CHAIN_RESILIENCE
NEW_MARKET_ENTRY
TECHNOLOGY_LEADERSHIP
PORTFOLIO_EXPANSION
CAPACITY_OPTIMIZATION
CUSTOMER_LOCK_IN
GLOBAL_EXPANSION
BUSINESS_RESTRUCTURING
RISK_DIVERSIFICATION
DIGITAL_TRANSFORMATION
OTHER
UNKNOWN
```

Do not dynamically create new top-level strategy types during normal analysis.

---

# 8. GROWTH

Canonical code:

```text
GROWTH
```

Korean name:

```text
성장 확대
```

Use when a company appears to be increasing:

```text
sales capacity
production
market share
customers
geographic reach
business scale
```

Typical supporting events:

```text
NEW_FACTORY
CAPACITY_EXPANSION
CAPEX
CONTRACT
```

Signals:

```text
capacity increase
major investment
production increase
market expansion
additional plant
large order backlog
```

Example:

```text
Company expands annual automotive production by 30%.
```

Likely strategy:

```text
GROWTH
```

---

# 9. LOCALIZATION

Canonical code:

```text
LOCALIZATION
```

Korean name:

```text
현지화
```

Use when a company appears to be increasing local:

```text
manufacturing
sourcing
supply
R&D
service capability
```

near a target market.

Typical events:

```text
NEW_FACTORY
SUPPLY_CHAIN
PROCUREMENT
JOINT_VENTURE
```

Signals:

```text
local production
local sourcing
near customer
regional manufacturing
local supply chain
domestic-content requirement
```

Example:

```text
Automaker builds a U.S. EV factory and expands U.S. supplier sourcing.
```

Primary strategy may be:

```text
LOCALIZATION
```

---

# 10. PREMIUMIZATION

Canonical code:

```text
PREMIUMIZATION
```

Korean name:

```text
고부가가치화
```

Use when a company appears to shift toward:

```text
higher-value products
premium products
higher specifications
higher-performance markets
higher margins
```

Typical events:

```text
PRODUCT_LAUNCH
R_AND_D
NEW_BUSINESS
```

Signals:

```text
premium
advanced
high performance
ultra-high strength
high efficiency
high specification
luxury
specialty
```

Steel relevance is often high because premiumization may increase demand for advanced steel grades.

---

# 11. COST_REDUCTION

Canonical code:

```text
COST_REDUCTION
```

Korean name:

```text
원가 절감
```

Use when a company appears focused on reducing:

```text
manufacturing cost
material cost
energy cost
labor cost
logistics cost
```

Typical events:

```text
AUTOMATION
PROCUREMENT
SUPPLY_CHAIN
CAPACITY_OPTIMIZATION
```

Signals:

```text
cost saving
efficiency
productivity
supplier consolidation
process simplification
lower-cost sourcing
```

Do not infer COST_REDUCTION simply because a company reports weak earnings.

There must be a concrete action suggesting cost reduction.

---

# 12. ELECTRIFICATION

Canonical code:

```text
ELECTRIFICATION
```

Korean name:

```text
전동화
```

Use when a company increases business activity related to:

```text
EV
electric motors
battery systems
power electronics
electrified machinery
```

Typical events:

```text
NEW_FACTORY
R_AND_D
PRODUCT_LAUNCH
CAPACITY_EXPANSION
```

Examples:

```text
EV production expansion
electric motor development
battery pack manufacturing
```

Steel relevance may include:

```text
electrical steel
AHSS
battery-case steel
lightweight steel
```

---

# 13. AUTOMATION

Canonical code:

```text
AUTOMATION
```

Korean name:

```text
자동화
```

Use when a company increases:

```text
robotics
smart manufacturing
automated logistics
unmanned production
AI-assisted production
```

Typical events:

```text
CAPEX
R_AND_D
NEW_FACTORY
```

Signals:

```text
robot
smart factory
automation
digital manufacturing
unmanned
AI manufacturing
```

Do not confuse with DIGITAL_TRANSFORMATION if the main action is physical production automation.

---

# 14. DECARBONIZATION

Canonical code:

```text
DECARBONIZATION
```

Korean name:

```text
탈탄소화
```

Use when a company appears to reduce:

```text
CO2 emissions
fossil fuel use
carbon intensity
energy emissions
```

Typical events:

```text
ESG
CAPEX
R_AND_D
PRODUCT_LAUNCH
```

Signals:

```text
carbon neutrality
green steel
renewable energy
hydrogen
EAF conversion
low-carbon production
CCUS
```

Do not infer DECARBONIZATION from generic ESG language without concrete action.

---

# 15. VERTICAL_INTEGRATION

Canonical code:

```text
VERTICAL_INTEGRATION
```

Korean name:

```text
수직계열화
```

Use when a company moves upstream or downstream in its value chain.

Examples:

```text
automaker invests in battery production

battery producer secures raw-material assets

steelmaker acquires processing or distribution capability
```

Typical events:

```text
M_AND_A
JOINT_VENTURE
NEW_BUSINESS
NEW_FACTORY
```

The key test is:

```text
Is the company increasing control over adjacent value-chain stages?
```

---

# 16. SUPPLY_CHAIN_RESILIENCE

Canonical code:

```text
SUPPLY_CHAIN_RESILIENCE
```

Korean name:

```text
공급망 안정화
```

Use when the company reduces exposure to:

```text
single supplier
single country
logistics disruption
geopolitical risk
raw-material shortage
```

Typical events:

```text
SUPPLY_CHAIN
PROCUREMENT
JOINT_VENTURE
NEW_FACTORY
```

Signals:

```text
dual sourcing
supplier diversification
regional sourcing
strategic inventory
China+1
supply-security agreement
```

---

# 17. NEW_MARKET_ENTRY

Canonical code:

```text
NEW_MARKET_ENTRY
```

Korean name:

```text
신시장 진입
```

Use when a company enters:

```text
new country
new customer industry
new market segment
new commercial market
```

Typical events:

```text
NEW_BUSINESS
EXPORT
M_AND_A
JOINT_VENTURE
NEW_FACTORY
```

Example:

```text
Steel company enters EV motor material market for the first time.
```

Likely strategy:

```text
NEW_MARKET_ENTRY
```

---

# 18. TECHNOLOGY_LEADERSHIP

Canonical code:

```text
TECHNOLOGY_LEADERSHIP
```

Korean name:

```text
기술 리더십 강화
```

Use when a company appears to seek competitive advantage through proprietary or advanced technology.

Typical events:

```text
R_AND_D
PRODUCT_LAUNCH
JOINT_DEVELOPMENT
```

Signals:

```text
next generation
world first
advanced technology
new process
high performance
patent
pilot technology
```

Avoid using this merely because a company performs normal R&D.

There should be evidence of strategic technological differentiation.

---

# 19. PORTFOLIO_EXPANSION

Canonical code:

```text
PORTFOLIO_EXPANSION
```

Korean name:

```text
사업 포트폴리오 확대
```

Use when a company adds:

```text
new product categories
new technologies
new services
adjacent businesses
```

without necessarily entering a completely new market.

Difference:

```text
NEW_MARKET_ENTRY
= new market

PORTFOLIO_EXPANSION
= broader offering
```

---

# 20. CAPACITY_OPTIMIZATION

Canonical code:

```text
CAPACITY_OPTIMIZATION
```

Korean name:

```text
생산능력 최적화
```

Use when a company changes production structure to improve:

```text
utilization
efficiency
plant mix
line allocation
regional production balance
```

Examples:

```text
closing low-efficiency facility
shifting production between plants
modernizing production line
reducing excess capacity
```

This differs from GROWTH.

Capacity may remain flat or decline while efficiency improves.

---

# 21. CUSTOMER_LOCK_IN

Canonical code:

```text
CUSTOMER_LOCK_IN
```

Korean name:

```text
고객관계 장기화
```

Use when a company strengthens long-term customer relationships through:

```text
long-term supply contract
joint development
exclusive supply
co-investment
integrated technical support
```

Typical events:

```text
CONTRACT
R_AND_D
JOINT_VENTURE
```

Use carefully.

Do not classify every long-term contract as customer lock-in unless relationship depth is strategically meaningful.

---

# 22. GLOBAL_EXPANSION

Canonical code:

```text
GLOBAL_EXPANSION
```

Korean name:

```text
글로벌 확대
```

Use when a company increases geographic presence across multiple foreign markets.

Difference from LOCALIZATION:

```text
LOCALIZATION
= local production/sourcing in a specific market

GLOBAL_EXPANSION
= broader international expansion
```

Example:

```text
Company simultaneously expands operations in the U.S., Europe, and Southeast Asia.
```

---

# 23. BUSINESS_RESTRUCTURING

Canonical code:

```text
BUSINESS_RESTRUCTURING
```

Korean name:

```text
사업 구조조정
```

Use when a company materially reorganizes:

```text
business portfolio
facilities
subsidiaries
workforce
assets
business units
```

Typical events:

```text
M_AND_A
DIVESTITURE
FINANCIAL_CHANGE
CAPACITY_OPTIMIZATION
```

Examples:

```text
selling non-core business
plant closure
business consolidation
subsidiary restructuring
```

---

# 24. RISK_DIVERSIFICATION

Canonical code:

```text
RISK_DIVERSIFICATION
```

Korean name:

```text
위험 분산
```

Use when a company deliberately reduces concentration risk across:

```text
countries
customers
suppliers
technologies
products
markets
```

Difference from SUPPLY_CHAIN_RESILIENCE:

```text
SUPPLY_CHAIN_RESILIENCE
= supply continuity

RISK_DIVERSIFICATION
= broader business exposure diversification
```

---

# 25. DIGITAL_TRANSFORMATION

Canonical code:

```text
DIGITAL_TRANSFORMATION
```

Korean name:

```text
디지털 전환
```

Use when the company materially changes business or operations through:

```text
AI
digital platforms
data systems
digital twins
software-defined products
cloud systems
```

Typical events:

```text
CAPEX
R_AND_D
NEW_BUSINESS
```

Difference from AUTOMATION:

```text
AUTOMATION
= automated physical operations

DIGITAL_TRANSFORMATION
= data/software-driven operating model
```

---

# 26. OTHER

Canonical code:

```text
OTHER
```

Use only when:

```text
a meaningful strategy is evident
but no current taxonomy fits
```

Store:

```text
strategy_summary
classification_note
```

for later taxonomy review.

---

# 27. UNKNOWN

Canonical code:

```text
UNKNOWN
```

Use when:

```text
available evidence is insufficient to determine strategic intent
```

UNKNOWN is preferable to forcing a plausible-looking strategy.

---

# 28. Event-to-Strategy Mapping

Events may suggest common strategy candidates.

This mapping is only a starting prior.

It must not automatically assign strategy.

| Event | Typical Strategy Candidates |
|---|---|
| CAPEX | GROWTH, AUTOMATION, DECARBONIZATION |
| NEW_FACTORY | GROWTH, LOCALIZATION, GLOBAL_EXPANSION |
| CAPACITY_EXPANSION | GROWTH, CAPACITY_OPTIMIZATION |
| M_AND_A | NEW_MARKET_ENTRY, VERTICAL_INTEGRATION, PORTFOLIO_EXPANSION |
| JOINT_VENTURE | NEW_MARKET_ENTRY, LOCALIZATION, RISK_DIVERSIFICATION |
| PRODUCT_LAUNCH | PREMIUMIZATION, TECHNOLOGY_LEADERSHIP, PORTFOLIO_EXPANSION |
| R_AND_D | TECHNOLOGY_LEADERSHIP, ELECTRIFICATION, DECARBONIZATION |
| SUPPLY_CHAIN | SUPPLY_CHAIN_RESILIENCE, LOCALIZATION |
| PROCUREMENT | COST_REDUCTION, SUPPLY_CHAIN_RESILIENCE |
| CONTRACT | GROWTH, CUSTOMER_LOCK_IN |
| ESG | DECARBONIZATION |
| EXPORT | GLOBAL_EXPANSION, NEW_MARKET_ENTRY |
| FINANCIAL_CHANGE | BUSINESS_RESTRUCTURING, COST_REDUCTION |

This table does not replace evidence-based analysis.

---

# 29. Multi-Strategy Rule

One event may support multiple strategies.

Example:

```text
Company builds EV factory in the U.S.
```

Possible:

```text
Primary:
LOCALIZATION

Secondary:
GROWTH
ELECTRIFICATION
```

Do not add:

```text
AUTOMATION
TECHNOLOGY_LEADERSHIP
DECARBONIZATION
```

unless evidence supports them.

---

# 30. Primary Strategy Selection

Choose the strategy that best explains:

```text
Why is the company taking this action?
```

Use the following factors:

```text
source emphasis
company context
event characteristics
recent related events
stated management objective
downstream business effect
```

---

# 31. Strategy Selection Heuristic

If several candidates remain, use:

```text
Explicit management statement      35%
Event-action alignment              25%
Recent company pattern              20%
Strategic specificity               10%
Downstream explanatory value        10%
```

The highest supported strategy becomes Primary.

---

# 32. Explicit Strategy Statement

If official management says:

```text
"We are building this plant to localize production for North American customers."
```

then:

```text
LOCALIZATION
```

should receive high confidence.

Do not override an explicit management explanation with a weaker model inference.

---

# 33. Inferred Strategy

Example:

Evidence:

```text
Company builds three regional factories near key customers.
```

No explicit strategy statement.

Inference:

```text
LOCALIZATION
```

Allowed wording:

```text
appears to
suggests
is consistent with
may indicate
```

Avoid:

```text
the company definitely intends
```

unless explicitly stated.

---

# 34. Strategy Confidence

Recommended confidence:

```text
90-100
explicitly stated by company or supported by multiple direct actions

80-89
strongly supported by event structure and evidence

70-79
reasonable inference with moderate evidence

60-69
weak but plausible inference

below 60
prefer UNKNOWN or omit strategy
```

---

# 35. Strategy Time Horizon

Use:

```text
IMMEDIATE
SHORT
MEDIUM
LONG
UNKNOWN
```

Recommended interpretation:

```text
IMMEDIATE:
0-3 months

SHORT:
3-12 months

MEDIUM:
1-3 years

LONG:
3+ years
```

---

# 36. Strategy From Multiple Events

A single event can be noisy.

Strategy confidence may increase when several related events support the same direction.

Example:

```text
Event 1:
U.S. factory

Event 2:
U.S. supplier localization

Event 3:
U.S. R&D center
```

Combined strategy:

```text
LOCALIZATION
```

with stronger confidence.

---

# 37. Strategy Pattern Analysis

For company-level intelligence, aggregate strategies over time.

Example:

```text
Last 12 months

LOCALIZATION      5 events
ELECTRIFICATION   4 events
GROWTH            3 events
```

Possible company strategy summary:

```text
North American localization and electrification appear to be dominant current strategic themes.
```

Do not equate raw event count with strategic importance.

Use materiality and confidence.

---

# 38. Strategy Strength

Future implementations may classify strategy strength:

```text
WEAK
MODERATE
STRONG
DOMINANT
```

Suggested inputs:

```text
number of supporting events
event materiality
source quality
investment scale
management statements
time consistency
```

This is separate from confidence.

---

# 39. Strategy vs Opportunity

Strategy is not automatically a POSCO opportunity.

Example:

```text
Strategy:
DIGITAL_TRANSFORMATION
```

may have little direct steel relevance.

Required downstream chain:

```text
Strategy
↓
Industry/Application Change
↓
Steel Demand
↓
Product Fit
↓
Opportunity
```

---

# 40. Strategy vs Steel Demand

Do not jump:

```text
LOCALIZATION
→ more steel demand
```

Instead:

```text
LOCALIZATION
↓
regional production change
↓
application/component demand
↓
steel requirement
```

Steel demand must be analyzed separately.

---

# 41. Automotive Strategy Examples

Example:

```text
Event:
EV plant expansion
```

Possible strategies:

```text
ELECTRIFICATION
GROWTH
LOCALIZATION
```

Example:

```text
Event:
new ultra-light EV platform development
```

Possible:

```text
TECHNOLOGY_LEADERSHIP
PREMIUMIZATION
ELECTRIFICATION
```

---

# 42. Shipbuilding Strategy Examples

Event:

```text
major LNG carrier order
```

Possible:

```text
GROWTH
CUSTOMER_LOCK_IN
```

Event:

```text
ammonia-fueled vessel R&D
```

Possible:

```text
TECHNOLOGY_LEADERSHIP
DECARBONIZATION
```

---

# 43. Energy Strategy Examples

Event:

```text
offshore wind manufacturing plant investment
```

Possible:

```text
GROWTH
NEW_MARKET_ENTRY
LOCALIZATION
```

Event:

```text
hydrogen infrastructure R&D
```

Possible:

```text
DECARBONIZATION
TECHNOLOGY_LEADERSHIP
PORTFOLIO_EXPANSION
```

---

# 44. Steel Competitor Strategy Examples

Event:

```text
competitor builds electric arc furnace
```

Possible:

```text
DECARBONIZATION
CAPACITY_OPTIMIZATION
```

Event:

```text
competitor establishes U.S. automotive processing center
```

Possible:

```text
LOCALIZATION
CUSTOMER_LOCK_IN
GLOBAL_EXPANSION
```

---

# 45. M&A Strategy Examples

Example:

```text
Steelmaker acquires automotive processor.
```

Possible:

```text
VERTICAL_INTEGRATION
CUSTOMER_LOCK_IN
```

Example:

```text
Industrial manufacturer acquires robotics company.
```

Possible:

```text
PORTFOLIO_EXPANSION
NEW_MARKET_ENTRY
AUTOMATION
```

---

# 46. Supply Chain Strategy Examples

Event:

```text
Company adds second supplier in another country.
```

Likely:

```text
SUPPLY_CHAIN_RESILIENCE
RISK_DIVERSIFICATION
```

Event:

```text
Company moves sourcing closer to factory.
```

Likely:

```text
LOCALIZATION
SUPPLY_CHAIN_RESILIENCE
```

---

# 47. Cost vs Resilience Ambiguity

Example:

```text
Company changes steel supplier.
```

Possible reasons:

```text
COST_REDUCTION
SUPPLY_CHAIN_RESILIENCE
LOCALIZATION
```

Do not choose without evidence.

If source does not explain why:

```text
strategy = UNKNOWN
```

or low-confidence inference.

---

# 48. Growth vs Localization

Example:

```text
Company builds new foreign plant.
```

Ask:

```text
Is the main objective more production?
```

Then:

```text
GROWTH
```

Ask:

```text
Is the main objective producing closer to customers/market?
```

Then:

```text
LOCALIZATION
```

Both may coexist.

Choose one Primary based on evidence.

---

# 49. Growth vs Global Expansion

Use:

```text
GROWTH
```

when the main effect is increasing business scale.

Use:

```text
GLOBAL_EXPANSION
```

when expansion across geographic markets is the defining strategy.

---

# 50. New Market Entry vs Portfolio Expansion

Use:

```text
NEW_MARKET_ENTRY
```

when entering a new customer/market domain.

Use:

```text
PORTFOLIO_EXPANSION
```

when adding offerings around an existing market.

Example:

```text
Automaker starts robot business
→ NEW_MARKET_ENTRY
```

Example:

```text
Automaker adds premium EV model
→ PORTFOLIO_EXPANSION or PREMIUMIZATION
```

---

# 51. Technology Leadership vs R&D

R_AND_D is an Event.

TECHNOLOGY_LEADERSHIP is a Strategy.

Not all R&D implies TECHNOLOGY_LEADERSHIP.

Example:

```text
routine product improvement
→ R_AND_D event
→ no TECHNOLOGY_LEADERSHIP necessarily
```

Example:

```text
next-generation proprietary technology program
→ R_AND_D
→ TECHNOLOGY_LEADERSHIP
```

---

# 52. Decarbonization vs ESG

ESG is an Event category.

DECARBONIZATION is a Strategy.

Example:

```text
Event:
ESG - EAF transition program

Strategy:
DECARBONIZATION
```

---

# 53. Strategy Inference From Contract

CONTRACT does not always imply strategy.

Example:

```text
one normal customer order
```

may produce:

```text
no strategy inference
```

Large multi-year contract may imply:

```text
CUSTOMER_LOCK_IN
GROWTH
NEW_MARKET_ENTRY
```

depending on context.

---

# 54. Strategy Inference From CAPEX

CAPEX alone is ambiguous.

Example:

```text
KRW 5T investment plan
```

Possible strategies:

```text
GROWTH
AUTOMATION
DECARBONIZATION
TECHNOLOGY_LEADERSHIP
```

Use destination of investment to infer strategy.

If unspecified:

```text
GROWTH
```

may still be too speculative.

Use UNKNOWN if needed.

---

# 55. Strategy Inference From Factory Closure

Factory closure may suggest:

```text
CAPACITY_OPTIMIZATION
COST_REDUCTION
BUSINESS_RESTRUCTURING
```

Select based on source evidence.

Do not automatically interpret closure as corporate weakness.

---

# 56. Contradictory Strategy Signals

Companies may pursue apparently conflicting strategies.

Example:

```text
factory expansion
+
plant closure
```

Possible explanation:

```text
growth in one region
+
capacity optimization in another
```

Do not force one global strategy when evidence suggests portfolio-level differences.

---

# 57. Business Unit Scope

Strategy should preserve scope.

Example:

```text
company:
Samsung Electronics

business unit:
Semiconductor
```

Strategy:

```text
CAPACITY_EXPANSION / TECHNOLOGY_LEADERSHIP
```

may apply only to the semiconductor business.

Do not automatically apply it to the whole company.

---

# 58. Geography Scope

Strategy may be region-specific.

Example:

```text
LOCALIZATION
region = North America
```

Do not generalize:

```text
company is globally localizing everything
```

without evidence.

---

# 59. Strategy Duration

A strategy may be:

```text
TEMPORARY
TACTICAL
MULTI_YEAR
STRUCTURAL
```

This may be added later as a field if useful.

For MVP, use:

```text
time_horizon
```

---

# 60. Strategy Evidence Requirements

Every strategy must reference at least:

```text
one validated event
```

Recommended high-confidence strategy:

```text
one official event
or
multiple independent supporting events
```

No event/evidence:

```text
no persisted strategy
```

---

# 61. Strategy Inference Guardrail

Never infer strategy solely from:

```text
stock price
analyst opinion
article headline sentiment
generic CEO quote
rumor
single vague keyword
```

without a concrete business action.

---

# 62. Strategy Wording

Good:

```text
The investment appears consistent with a localization strategy.
```

Good:

```text
Recent capacity additions suggest continued growth in North America.
```

Bad:

```text
The company has definitely decided to dominate the North American market.
```

Avoid exaggerated intent.

---

# 63. Strategy Confidence vs Strategy Importance

These are different.

Example:

```text
Strategy:
LOCALIZATION

Confidence:
95

Importance:
MEDIUM
```

Meaning:

```text
we are very sure localization is occurring
but the business impact may be moderate
```

Do not merge confidence and importance.

---

# 64. Strategy Materiality

Future scoring may consider:

```text
investment size
capacity impact
revenue impact
market share impact
customer importance
geographic scope
```

Materiality is not part of the canonical taxonomy.

---

# 65. Strategy Change Detection

The system should eventually detect changes such as:

```text
GROWTH → CAPACITY_OPTIMIZATION

GLOBAL_EXPANSION → LOCALIZATION

COST_REDUCTION → PREMIUMIZATION
```

This can be useful for executive insights.

Strategy change requires multi-event historical evidence.

---

# 66. Strategy Trend Window

Recommended analysis windows:

```text
3 months
6 months
12 months
36 months
```

Do not treat every historical event equally.

Recent material events should receive higher relevance in current strategy summaries.

---

# 67. Strategy Persistence

Recommended data-model relationship:

```text
Event
↓
event_strategies
```

Fields should include:

```text
event_id
company_id
strategy_type
strategy_summary
inference_basis
confidence
time_horizon
is_primary
processing_version
model_version
prompt_version
```

---

# 68. Strategy Recalculation

Recalculate when:

```text
new official evidence appears
event materially changes
multiple related events accumulate
strategy prompt changes
taxonomy changes
```

Do not recalculate merely because frontend display changes.

---

# 69. Company-Level Strategy Profile

A company strategy profile may aggregate:

```text
current dominant strategies
emerging strategies
declining strategies
regional strategies
technology strategies
```

Example:

```text
Dominant:
LOCALIZATION
ELECTRIFICATION

Emerging:
AUTOMATION

Declining:
UNKNOWN
```

This should be derived from events, not manually invented.

---

# 70. Strategy-to-Steel-Demand Transition

After strategy classification, the next stage should ask:

```text
What operational or product change could this strategy create?
```

Example:

```text
ELECTRIFICATION
↓
EV production increases
↓
motor-core demand increases
↓
electrical steel demand
```

Another:

```text
DECARBONIZATION
↓
low-carbon material procurement
↓
green steel requirement
```

---

# 71. Strategy Relevance to POSCO

Some strategies have stronger steel relevance.

Examples:

```text
GROWTH
LOCALIZATION
PREMIUMIZATION
ELECTRIFICATION
DECARBONIZATION
VERTICAL_INTEGRATION
SUPPLY_CHAIN_RESILIENCE
TECHNOLOGY_LEADERSHIP
```

often have direct downstream implications.

Strategies such as:

```text
DIGITAL_TRANSFORMATION
```

may have indirect or low steel relevance.

Do not force a steel opportunity.

---

# 72. Strategy-to-Opportunity Examples

Example:

```text
LOCALIZATION
↓
local sourcing requirement
↓
regional steel supply need
↓
potential supply-chain opportunity
```

Example:

```text
PREMIUMIZATION
↓
higher performance requirement
↓
advanced material demand
↓
premium steel opportunity
```

Example:

```text
DECARBONIZATION
↓
low-carbon material requirement
↓
lower-emission steel demand
↓
green-product opportunity
```

---

# 73. Strategy Classification Output

Recommended AI output:

```json
{
  "primary_strategy": {
    "strategy_type": "LOCALIZATION",
    "summary": "The company appears to be increasing local production capability near the North American market.",
    "inference_basis": [
      "New U.S. manufacturing facility",
      "Regional supplier expansion"
    ],
    "confidence": 91,
    "time_horizon": "MEDIUM"
  },
  "secondary_strategies": [
    {
      "strategy_type": "GROWTH",
      "confidence": 84
    },
    {
      "strategy_type": "ELECTRIFICATION",
      "confidence": 89
    }
  ]
}
```

---

# 74. Overclassification Guardrail

Bad:

```text
NEW_FACTORY
↓
GROWTH
LOCALIZATION
GLOBAL_EXPANSION
AUTOMATION
DIGITAL_TRANSFORMATION
DECARBONIZATION
TECHNOLOGY_LEADERSHIP
RISK_DIVERSIFICATION
```

Correct approach:

```text
Primary:
LOCALIZATION

Secondary:
GROWTH
ELECTRIFICATION
```

if evidence supports those three.

---

# 75. Underclassification Guardrail

Do not ignore an obvious second strategy when materially relevant.

Example:

```text
EV factory in new foreign market
```

Could reasonably support:

```text
LOCALIZATION
+
ELECTRIFICATION
```

The goal is minimal but sufficiently explanatory classification.

---

# 76. Unknown Strategy Example

Evidence:

```text
Company invests KRW 500B.
```

No purpose disclosed.

Do not assume:

```text
GROWTH
```

Correct:

```text
UNKNOWN
```

or no strategy persistence until further evidence appears.

---

# 77. Golden Test Case 1

Input:

```text
Automaker builds a new EV factory near major U.S. customers.
```

Expected:

```text
Primary:
LOCALIZATION

Secondary:
ELECTRIFICATION
GROWTH
```

---

# 78. Golden Test Case 2

Input:

```text
Steelmaker converts blast-furnace capacity toward EAF and low-carbon production.
```

Expected:

```text
Primary:
DECARBONIZATION

Secondary:
CAPACITY_OPTIMIZATION
```

---

# 79. Golden Test Case 3

Input:

```text
Manufacturer acquires a battery-material producer.
```

Expected candidates:

```text
VERTICAL_INTEGRATION
PORTFOLIO_EXPANSION
NEW_MARKET_ENTRY
```

Select Primary based on acquisition rationale.

If purpose is supply control:

```text
VERTICAL_INTEGRATION
```

---

# 80. Golden Test Case 4

Input:

```text
Company introduces next-generation ultra-high-strength product aimed at premium EVs.
```

Expected:

```text
Primary:
PREMIUMIZATION

Secondary:
TECHNOLOGY_LEADERSHIP
```

---

# 81. Golden Test Case 5

Input:

```text
Company adds suppliers in Mexico and India to reduce dependence on one country.
```

Expected:

```text
Primary:
SUPPLY_CHAIN_RESILIENCE

Secondary:
RISK_DIVERSIFICATION
```

---

# 82. Golden Test Case 6

Input:

```text
Company shuts an underutilized factory and shifts production to its most efficient plant.
```

Expected:

```text
Primary:
CAPACITY_OPTIMIZATION

Secondary:
COST_REDUCTION
```

---

# 83. Golden Test Case 7

Input:

```text
Shipbuilder signs ten-year collaboration with a major shipping customer for next-generation vessels.
```

Possible:

```text
Primary:
CUSTOMER_LOCK_IN

Secondary:
TECHNOLOGY_LEADERSHIP
```

only if joint technology development is part of the agreement.

---

# 84. Golden Test Case 8

Input:

```text
Company opens factories in the U.S., Poland, and Vietnam to expand international sales.
```

Expected:

```text
Primary:
GLOBAL_EXPANSION

Secondary:
GROWTH
```

---

# 85. Golden Test Case 9

Input:

```text
Manufacturer introduces AI-based production management software across existing plants.
```

Expected:

```text
Primary:
DIGITAL_TRANSFORMATION
```

If robots physically automate production:

```text
AUTOMATION
```

may also apply.

---

# 86. Golden Test Case 10

Input:

```text
Company invests in hydrogen-related R&D without a clear commercial roadmap.
```

Possible:

```text
TECHNOLOGY_LEADERSHIP
```

only if evidence indicates differentiation intent.

Otherwise:

```text
strategy = UNKNOWN
```

while event remains:

```text
R_AND_D
```

---

# 87. Strategy Prompt Rules

Strategy-analysis prompts must explicitly instruct:

```text
Infer strategy only from supplied evidence and validated events.

Do not treat inference as fact.

Select no more than 3 strategies per event.

Choose one Primary Strategy when sufficient evidence exists.

Use canonical taxonomy only.

Do not create a strategy simply because it is plausible.

Prefer UNKNOWN when evidence is insufficient.

Use cautious language for inferred management intent.

Separate strategy confidence from business importance.
```

---

# 88. Strategy Retrieval for Ask Steel AI

When a user asks:

```text
"현대자동차는 최근 어떤 전략을 강화하고 있어?"
```

Do not analyze every raw article again.

Retrieve:

```text
recent material events
+
stored event_strategies
+
confidence
+
evidence
```

Then synthesize the current strategy view.

---

# 89. Strategy Dashboard

Possible company strategy view:

```text
Hyundai Motor

Dominant Strategies

LOCALIZATION      Strong
ELECTRIFICATION   Strong
GROWTH            Moderate

Supporting Events:
6

Confidence:
High
```

Strategy strength should derive from accumulated evidence, not raw mention count.

---

# 90. Strategy and Competitor Comparison

For competitor intelligence, compare strategy directions rather than only products.

Example:

```text
POSCO:
DECARBONIZATION
PREMIUMIZATION

Competitor:
LOCALIZATION
CUSTOMER_LOCK_IN
```

This may reveal competitive gaps before direct product comparison.

---

# 91. Strategy Change Alert

Future Strategic Alert may be generated when:

```text
important customer strategy materially changes
```

Example:

```text
Customer shifts from global sourcing to local procurement.
```

Possible implication:

```text
LOCALIZATION increases
↓
supply model may need review
```

Strategy alerts should require multiple supporting signals or high-quality evidence.

---

# 92. Taxonomy Change Rule

Before adding a new Strategy code, verify:

```text
existing taxonomy cannot represent it

it appears repeatedly across companies

it has clear analytical value

it helps steel-demand or opportunity reasoning

it is not merely an event, industry, technology, or business outcome
```

Major changes should be recorded in:

```text
docs/decisions.md
```

---

# 93. Final Strategy Rule

The strategy taxonomy exists to explain the likely direction behind observed corporate actions.

The system should prefer:

```text
few
strong
evidence-supported
explainable
strategies
```

over:

```text
many
generic
plausible-looking
strategies
```

The desired chain is:

```text
SOURCE
↓
EVENT
↓
STRATEGY
↓
INDUSTRY / APPLICATION CHANGE
↓
STEEL DEMAND
↓
POSCO PRODUCT
↓
OPPORTUNITY
```

Strategy classification is successful when it improves downstream steel-demand and opportunity analysis without converting speculation into fact.
