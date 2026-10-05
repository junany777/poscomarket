# Steel Market Intelligence Platform Intelligence Design

## 1. Document Purpose

This document defines the intelligence pipeline of the Steel Market Intelligence Platform.

It specifies:

- intelligence processing stages
- inputs and outputs
- fact vs inference rules
- event extraction
- company strategy analysis
- steel-demand reasoning
- POSCO product matching
- competitor analysis
- opportunity generation
- scoring
- confidence calculation
- persona rendering
- search synthesis
- AI guardrails
- cost-control rules
- validation rules

The intelligence system must produce structured, explainable, evidence-based outputs.

It must not behave as a generic summarization engine.

---

# 2. Core Intelligence Mission

The system converts industrial information into actionable steel marketing intelligence.

Primary chain:

```text
SOURCE DOCUMENT
↓
ENTITY
↓
EVENT
↓
COMPANY STRATEGY
↓
INDUSTRY IMPLICATION
↓
STEEL DEMAND
↓
POSCO PRODUCT MATCH
↓
COMPETITOR CONTEXT
↓
OPPORTUNITY
↓
ACTION
```

Every downstream conclusion must preserve lineage to upstream evidence.

---

# 3. Intelligence Principles

The following principles are mandatory.

```text
Evidence before inference

Structure before prose

Facts and inference remain separate

Do not jump directly from article to product

Do not invent product specifications

Do not invent competitor claims

Do not convert uncertainty into certainty

Prefer deterministic logic where possible

Use AI for extraction, reasoning, and synthesis where it adds value

Every high-value recommendation must be explainable
```

---

# 4. Intelligence Pipeline Overview

The recommended pipeline is:

```text
SourceDocument
↓
Pre-Filter
↓
Entity Extraction
↓
Event Extraction
↓
Event Validation
↓
Event Clustering
↓
Strategy Analysis
↓
Industry Implication
↓
Steel Demand Hypothesis
↓
POSCO Product Retrieval
↓
Product Fit Analysis
↓
Competitor Retrieval
↓
Competitor Comparison
↓
Opportunity Scoring
↓
Confidence Scoring
↓
Recommended Actions
↓
Persona Rendering
```

Each stage should produce structured output.

Each stage should be independently testable.

---

# 5. Pre-Filter Stage

The system should not send every collected source to an LLM.

Use deterministic filtering first.

Recommended sequence:

```text
language check
↓
duplicate check
↓
industry relevance
↓
company relevance
↓
event relevance
↓
LLM processing
```

Possible filter conditions:

```text
known company mention
known industry keyword
investment keyword
factory keyword
capacity keyword
technology keyword
M&A keyword
new business keyword
supply-chain keyword
regulation keyword
contract keyword
ESG keyword
```

Low-relevance content may remain searchable without entering the full intelligence pipeline.

---

# 6. Relevance Classification

Before deep analysis, classify source relevance.

Output:

```json
{
  "is_relevant": true,
  "relevance_score": 86,
  "industries": ["AUTOMOTIVE"],
  "companies": ["Hyundai Motor Company"],
  "reason": "New EV manufacturing investment with potential steel demand impact"
}
```

Recommended relevance score:

```text
0 - 100
```

Suggested behavior:

```text
80-100:
full intelligence processing

60-79:
process if company or industry is on watchlist

40-59:
store for search, normally do not process deeply

0-39:
archive as low relevance
```

Thresholds should be configurable.

---

# 7. Entity Extraction

## Goal

Extract structured domain entities from a normalized source.

Possible entity types:

```text
COMPANY
INDUSTRY
COUNTRY
REGION
FACILITY
TECHNOLOGY
PRODUCT
APPLICATION
COMPONENT
INVESTMENT_AMOUNT
CAPACITY
DATE
CUSTOMER
SUPPLIER
PERSON
```

Example input:

```text
현대자동차가 미국 조지아주 전기차 생산시설에 추가 투자할 계획이다.
```

Expected output:

```json
{
  "companies": [
    {
      "raw_name": "현대자동차",
      "canonical_name": "Hyundai Motor Company",
      "company_id": "..."
    }
  ],
  "industries": ["AUTOMOTIVE"],
  "countries": ["US"],
  "regions": ["Georgia"],
  "technologies": ["EV"],
  "facilities": ["EV manufacturing facility"]
}
```

Entity resolution should reuse existing company records and aliases where possible.

---

# 8. Entity Resolution

LLM extraction and company identity resolution are separate concerns.

Recommended process:

```text
raw mention
↓
normalized string
↓
alias lookup
↓
company match
↓
confidence
```

Example aliases:

```text
현대차
현대자동차
Hyundai Motor
Hyundai Motor Company
```

should resolve to one company record.

If resolution is uncertain:

```text
company_id = null
resolution_status = AMBIGUOUS
```

Do not silently create duplicate companies.

---

# 9. Event Extraction

## Goal

Convert source facts into a structured real-world event.

An event represents a meaningful business or industrial occurrence.

Supported event types should use the project taxonomy.

Typical values:

```text
CAPEX
NEW_FACTORY
CAPACITY_EXPANSION
NEW_BUSINESS
M_AND_A
JOINT_VENTURE
PRODUCT_LAUNCH
R_AND_D
SUPPLY_CHAIN
PROCUREMENT
CONTRACT
ESG
EXPORT
REGULATION
FINANCIAL_CHANGE
OTHER
```

---

# 10. Event Extraction Output

Recommended structured output:

```json
{
  "event_type": "CAPEX",
  "event_subtype": "EV_FACTORY",
  "primary_company": "Hyundai Motor Company",
  "industry": "AUTOMOTIVE",
  "title": "Hyundai Motor expands U.S. EV manufacturing investment",
  "description": "Additional investment in EV manufacturing capacity in Georgia.",
  "country_code": "US",
  "region": "Georgia",
  "investment_amount": 5000000000,
  "investment_currency": "USD",
  "announced_at": "2026-09-10",
  "start_date": null,
  "target_date": "2028-12-31",
  "status": "ANNOUNCED",
  "extraction_confidence": 91
}
```

Do not include strategic interpretation in the factual event object unless the source explicitly states it.

---

# 11. Event Validation

Before persisting a validated event:

```text
event type must be valid
primary company must be resolvable or clearly represented
at least one evidence source must exist
dates must be logically valid
currency must be standardized
numeric values must pass validation
confidence must be within range
```

Invalid or incomplete events may remain:

```text
DRAFT
```

or

```text
NEEDS_REVIEW
```

depending on implementation.

---

# 12. Event Evidence

Every event should preserve direct supporting evidence.

Recommended evidence object:

```json
{
  "source_document_id": "...",
  "evidence_role": "PRIMARY_SOURCE",
  "supporting_excerpt": "The company announced an additional investment...",
  "evidence_strength": 0.95
}
```

Evidence excerpts should remain short and legally appropriate.

---

# 13. Event Clustering

Multiple sources may describe one real-world event.

Recommended clustering signals:

```text
same company
same event type
similar title
similar dates
same facility
same investment amount
same location
semantic similarity
```

Use deterministic signals first.

Semantic similarity may be added only when needed.

Possible cluster behavior:

```text
Source A
Source B
Source C
↓
One Event
```

or:

```text
Event 1
Event 2
↓
Related Event Cluster
```

---

# 14. Strategy Analysis

## Goal

Infer what an event may imply about company strategy.

Strategy is inference, not fact.

Supported strategic dimensions may include:

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
```

---

# 15. Strategy Analysis Input

Use:

```text
validated event
+
supporting evidence
+
recent company events if relevant
```

Do not load unrelated historical data.

---

# 16. Strategy Analysis Output

Recommended format:

```json
{
  "strategies": [
    {
      "strategy_type": "LOCALIZATION",
      "summary": "The company appears to be strengthening local EV production in North America.",
      "inference_basis": [
        "New U.S. manufacturing investment",
        "Expansion of local EV capacity"
      ],
      "confidence": 84,
      "time_horizon": "MEDIUM"
    },
    {
      "strategy_type": "ELECTRIFICATION",
      "summary": "The investment supports continued expansion of the company's EV production portfolio.",
      "confidence": 90,
      "time_horizon": "MEDIUM"
    }
  ]
}
```

Use language such as:

```text
suggests
indicates
appears to
is consistent with
may imply
```

when expressing inference.

Avoid presenting inference as confirmed management intent.

---

# 17. Industry Implication Analysis

## Goal

Determine how a company event may affect its broader industry.

Example:

```text
Company EV investment
↓
regional EV production capacity increases
↓
supplier localization pressure rises
↓
demand for locally supplied automotive materials may increase
```

Output should be concise and structured.

Recommended fields:

```json
{
  "industry_effect": "REGIONAL_CAPACITY_EXPANSION",
  "direction": "POSITIVE",
  "magnitude": "MEDIUM",
  "summary": "North American EV manufacturing capacity is likely to expand.",
  "time_horizon": "MEDIUM",
  "confidence": 78
}
```

---

# 18. Steel Demand Reasoning

This is one of the most important stages.

The system must not reason:

```text
EV factory
↓
POSCO electrical steel
```

directly.

Required reasoning chain:

```text
Industry Change
↓
Application Change
↓
Component Change
↓
Material Requirement
↓
Steel Category
```

---

# 19. Steel Demand Example

Input:

```text
EV manufacturing capacity expansion
```

Reasoning:

```text
EV production increases
↓
drive motor production increases
↓
motor-core demand increases
↓
low magnetic loss becomes important
↓
electrical steel demand may increase
```

Another path:

```text
EV production increases
↓
vehicle body production increases
↓
body-in-white demand increases
↓
high strength + weight reduction required
↓
advanced automotive sheet demand may increase
```

One event may produce multiple steel-demand hypotheses.

---

# 20. Steel Demand Output

Recommended structured format:

```json
{
  "hypotheses": [
    {
      "application": "EV_MOTOR",
      "component": "MOTOR_CORE",
      "steel_category": "ELECTRICAL_STEEL",
      "required_properties": [
        "LOW_MAGNETIC_LOSS",
        "HIGH_EFFICIENCY"
      ],
      "demand_direction": "INCREASE",
      "demand_magnitude": "MEDIUM",
      "time_horizon": "MEDIUM",
      "reasoning_summary": "Higher EV production may increase drive-motor demand and therefore electrical-steel requirements.",
      "confidence": 82
    }
  ]
}
```

---

# 21. Steel Demand Guardrails

Do not generate highly specific demand-volume forecasts unless supporting data exists.

Avoid unsupported output such as:

```text
demand will increase by 27.4%
```

unless the number is calculated from real production and material-intensity data.

Allowed qualitative outputs:

```text
LOW
MEDIUM
HIGH
UNKNOWN
```

and:

```text
INCREASE
DECREASE
SHIFT
NEW_DEMAND
UNCERTAIN
```

---

# 22. POSCO Product Retrieval

Specific product matching begins only after a steel-demand hypothesis exists.

Retrieval input:

```text
industry
application
component
steel category
required properties
```

Retrieval sequence:

```text
knowledge/posco/index.md
↓
relevant industry index
↓
application metadata
↓
candidate products
↓
specific product documents
```

Never recursively read the full POSCO knowledge base.

---

# 23. Product Candidate Retrieval

Candidate filtering should prefer structured metadata.

Example:

```text
industry = AUTOMOTIVE
application = EV_MOTOR
component = MOTOR_CORE
steel_category = ELECTRICAL_STEEL
```

Candidate products should be selected before LLM judgment.

Use semantic retrieval only if metadata filtering is insufficient.

---

# 24. Product Matching Analysis

Input:

```text
steel demand hypothesis
+
candidate product knowledge
```

Output:

```json
{
  "matches": [
    {
      "product_id": "...",
      "product_name": "...",
      "fit_score": 91,
      "fit_confidence": 88,
      "fit_reason": "The product is intended for high-efficiency motor applications and aligns with the identified low-magnetic-loss requirement.",
      "matching_properties": [
        "low magnetic loss",
        "motor application"
      ],
      "missing_requirements": [],
      "status": "MATCHED"
    }
  ]
}
```

---

# 25. Product Matching Guardrails

Never:

```text
invent product
invent grade
invent strength
invent magnetic property
invent certification
invent customer adoption
```

If a required technical fact is absent:

```text
UNKNOWN
```

must be used.

If no reliable product match exists:

```text
PRODUCT_MATCH_UNKNOWN
```

should be returned.

---

# 26. Competitor Intelligence

Competitor analysis should reuse the same event pipeline where possible.

Competitor event examples:

```text
new capacity
technology development
new product
major customer partnership
regional expansion
decarbonization project
new mill
M&A
```

Primary dimensions:

```text
PRODUCT
TECHNOLOGY
CAPACITY
GEOGRAPHY
CUSTOMER_RELATIONSHIP
LOCAL_SUPPLY
LOW_CARBON
COMMERCIALIZATION
```

---

# 27. Competitor Comparison

Input:

```text
customer requirement
POSCO capability
competitor capability
evidence
```

Output:

```json
{
  "competitor": "Example Steel Co.",
  "dimensions": [
    {
      "dimension": "LOCAL_SUPPLY",
      "comparison_result": "DISADVANTAGE",
      "summary": "The competitor has established local production while POSCO relies more heavily on external supply.",
      "confidence": 76
    }
  ]
}
```

Allowed comparison states:

```text
ADVANTAGE
PARITY
DISADVANTAGE
UNKNOWN
```

Do not use unsupported adjectives such as:

```text
best
superior
dominant
weak
```

without evidence.

---

# 28. Opportunity Generation

An Opportunity is the primary business-facing analytical object.

Input:

```text
Event
+
Strategy
+
Industry Implication
+
Steel Demand
+
POSCO Product Match
+
Competitor Context
```

Output should answer:

```text
What happened?

Why does it matter?

What steel demand may change?

Which POSCO capability is relevant?

What competitive risk exists?

What should marketing or engineering consider doing?
```

---

# 29. Opportunity Output Structure

Recommended output:

```json
{
  "headline": "Potential electrical-steel opportunity from North American EV expansion",
  "summary": "Expansion of EV production may increase future motor-core material demand.",
  "facts": [
    "Company announced additional EV manufacturing investment."
  ],
  "company_strategy": [
    "LOCALIZATION",
    "ELECTRIFICATION"
  ],
  "industry_implication": "Regional EV production capacity may increase.",
  "steel_demand_implication": "Electrical steel demand for motor cores may increase.",
  "product_candidates": [
    "..."
  ],
  "competitor_context": "Local competitor supply capability should be monitored.",
  "recommended_marketing_action": "Estimate medium-term customer demand and evaluate local supply strategy.",
  "recommended_technical_action": "Review application-specific efficiency requirements with the customer.",
  "time_horizon": "MEDIUM",
  "opportunity_score": 91,
  "confidence_score": 84
}
```

---

# 30. Opportunity Score

Opportunity Score measures commercial attractiveness.

Default formula:

```text
Industry Impact       20%
Customer Importance   15%
Investment Scale      15%
Steel Demand Impact   20%
POSCO Product Fit     20%
Timing                 10%
```

Each component:

```text
0 - 100
```

Final score:

```text
sum(component × weight)
```

---

# 31. Opportunity Score Classification

Recommended classification:

```text
90-100:
STRATEGIC

80-89:
HIGH

70-79:
WATCH

0-69:
INFORMATION
```

The UI should show both:

```text
final score
component breakdown
```

---

# 32. Customer Importance Score

Customer Importance may consider:

```text
existing customer status
company size
strategic industry role
steel consumption potential
watchlist priority
regional importance
```

This score should increasingly use deterministic business metadata rather than pure LLM judgment.

If no business metadata exists, use a conservative default.

---

# 33. Investment Scale Score

Where numeric investment exists, use deterministic rules.

Example conceptual buckets:

```text
very small
small
medium
large
strategic
```

Thresholds may differ by industry.

Do not ask the LLM to freely invent the score if normalized financial values are available.

---

# 34. Product Fit Score

Product Fit should primarily derive from product-match analysis.

Possible factors:

```text
application match
component match
required-property match
steel-category match
evidence completeness
```

Do not equate a semantic keyword match with strong technical fit.

---

# 35. Timing Score

Timing reflects commercial actionability.

Possible factors:

```text
investment already announced
facility construction stage
procurement window
target production date
development stage
commercialization date
```

Near-term actionable opportunities may score higher than speculative long-term themes.

---

# 36. Confidence Score

Confidence measures analytical reliability.

It is separate from Opportunity Score.

Recommended factors:

```text
Source Reliability
Source Independence
Source Agreement
Data Completeness
Recency
Inference Distance
Product Knowledge Support
```

Possible weighted concept:

```text
Source Reliability        25%
Source Independence       15%
Source Agreement          15%
Data Completeness         15%
Recency                   10%
Inference Distance        10%
Product Knowledge Support 10%
```

Weights may be tuned later.

---

# 37. Inference Distance

Inference Distance represents how many reasoning steps separate the conclusion from direct evidence.

Example:

```text
Official source:
Company will construct EV plant.
```

Direct conclusion:

```text
EV production capacity will increase.
```

Low inference distance.

More distant conclusion:

```text
A specific steel grade will be required in a specific annual volume.
```

High inference distance unless additional evidence exists.

Confidence should generally decrease as inference distance increases.

---

# 38. Source Reliability

Recommended conceptual reliability:

```text
Tier 1:
official disclosure
government
corporate IR
official press release

Tier 2:
industry association
specialized industry publication

Tier 3:
major news

Tier 4:
secondary source
unverified source
```

Reliability should ultimately be stored in provider metadata and used deterministically.

---

# 39. Independent Source Rule

Ten copies of the same syndicated article do not equal ten independent confirmations.

The system should distinguish:

```text
duplicate reporting
```

from:

```text
independent evidence
```

Confidence should increase only with genuinely independent evidence.

---

# 40. Contradicting Evidence

The system must preserve contradicting sources.

Example:

```text
Source A:
project proceeds

Source B:
project delayed
```

Do not discard one automatically.

Recommended behavior:

```text
mark contradiction
lower confidence
show conflicting evidence
delay high-confidence recommendation if necessary
```

---

# 41. Recommended Actions

Actions should be practical and role-specific.

Possible action types:

```text
MARKETING
SALES
TECHNICAL
RESEARCH
CUSTOMER_ENGAGEMENT
COMPETITOR_MONITORING
PRODUCT_DEVELOPMENT
EXECUTIVE_REVIEW
```

Good action:

```text
Review the customer's 2027-2029 EV capacity ramp and estimate potential electrical-steel volume.
```

Weak action:

```text
Monitor the market closely.
```

Prefer concrete next steps.

---

# 42. Action Guardrails

Do not recommend:

```text
unsupported price changes
unsupported technical commitments
unverified product guarantees
customer claims not backed by evidence
illegal or unethical competitive behavior
```

Recommendations are decision support, not autonomous commercial decisions.

---

# 43. Persona Rendering

The system should analyze once and render differently by persona.

Core object:

```text
Opportunity
```

Rendered as:

```text
EXECUTIVE
MARKETING
ENGINEERING
```

Do not repeat the full intelligence pipeline for each persona.

---

# 44. Executive Renderer

Executive output should prioritize:

```text
what changed
why it matters
market impact
strategic customer relevance
competitive threat
decision needed
```

Suggested structure:

```text
Headline

Why it matters

Strategic implication

Opportunity / risk

Decision required

Evidence confidence
```

Avoid unnecessary technical detail.

---

# 45. Marketing Renderer

Marketing output should prioritize:

```text
customer
investment
timeline
steel demand
product fit
competitor
sales opportunity
next action
```

Suggested structure:

```text
Customer

Signal

Commercial implication

Relevant POSCO products

Competitive context

Recommended approach

Timing

Evidence
```

---

# 46. Engineering Renderer

Engineering output should prioritize:

```text
application
component
required material properties
technical requirements
product fit
technical gap
competitor material
development need
```

Avoid unsupported technical specifications.

---

# 47. Daily Brief Intelligence

Daily Brief should not simply summarize all articles.

Recommended selection sequence:

```text
new events
↓
high relevance
↓
high opportunity
↓
watchlist relevance
↓
diversity by industry/company
↓
brief generation
```

Daily Brief may include:

```text
TOP Opportunities
Major Industry Changes
Customer Movements
Competitor Activity
Watchlist Changes
```

---

# 48. Strategic Alert Intelligence

Strategic Alerts should be rare.

Default trigger concept:

```text
Opportunity Score >= 90
AND
Confidence Score >= configurable threshold
AND
event is materially new
AND
alert not previously sent
```

Material change may include:

```text
official confirmation
major investment increase
major capacity change
project delay
cancellation
new customer
new competitor entry
technology commercialization
```

---

# 49. Ask Steel AI

Ask Steel AI should prefer existing structured intelligence.

Query flow:

```text
User Query
↓
Intent Classification
↓
Entity Resolution
↓
Structured Retrieval
↓
Evidence Retrieval
↓
Product Retrieval if necessary
↓
Competitor Retrieval if necessary
↓
LLM Synthesis
```

Do not start with general model knowledge.

---

# 50. Ask Steel AI Intent Types

Possible intents:

```text
COMPANY_OVERVIEW
COMPANY_STRATEGY
INDUSTRY_TREND
INVESTMENT_SEARCH
OPPORTUNITY_SEARCH
PRODUCT_MATCH
COMPETITOR_COMPARE
STEEL_DEMAND
EVENT_SEARCH
EXECUTIVE_BRIEF
```

Example:

```text
"현대자동차 최근 투자 중 철강 영업기회를 찾아줘"
```

Intent:

```text
OPPORTUNITY_SEARCH
```

Entities:

```text
company = Hyundai Motor
time = recent
```

---

# 51. Ask Steel AI Retrieval Priority

Recommended order:

```text
structured database filters
↓
stored events
↓
stored opportunities
↓
source evidence
↓
POSCO knowledge
↓
semantic retrieval
↓
LLM synthesis
```

This minimizes cost and improves reliability.

---

# 52. Search Answer Structure

For analytical questions, preferred answer format:

```text
Answer

Key Evidence

Interpretation

POSCO Implication

Confidence

Sources
```

Clearly label inference where applicable.

---

# 53. Prompt Architecture

Prompts should be separated by purpose.

Recommended files:

```text
intelligence/prompts/

relevance_classifier.md
entity_extraction.md
event_extraction.md
strategy_analysis.md
industry_implication.md
steel_demand.md
product_matching.md
competitor_analysis.md
opportunity_generation.md
persona_executive.md
persona_marketing.md
persona_engineering.md
ask_steel_ai.md
```

Each prompt should be versioned.

---

# 54. Prompt Design Rules

Every analytical prompt should define:

```text
role
task
allowed evidence
output schema
uncertainty behavior
forbidden behavior
taxonomy
examples if necessary
```

Prompts should explicitly state:

```text
Do not invent missing facts.

If evidence is insufficient, return UNKNOWN.

Separate facts from inference.

Use only supplied product knowledge for product claims.
```

---

# 55. Structured Output

Use validated schema output whenever possible.

Example Pydantic-style concept:

```python
class EventExtractionResult:
    event_type: EventType
    primary_company: str
    industry: IndustryCode
    investment_amount: float | None
    confidence: int
```

Validation must occur before persistence.

Invalid structured output should:

```text
retry with limited repair
or
fail safely
```

Do not persist malformed analysis.

---

# 56. Model Selection Strategy

Do not automatically use the most expensive model for every stage.

Use lighter models for:

```text
simple classification
entity extraction
relevance filtering
formatting
```

Use stronger reasoning models for:

```text
strategy inference
steel-demand reasoning
product-fit reasoning
competitor comparison
complex opportunity synthesis
```

Model selection should remain configurable.

---

# 57. Cost Control

Major cost-saving rules:

```text
deduplicate before AI
filter before AI
reuse stored extraction
reuse stored events
do not rerun unchanged analysis
retrieve small context
avoid loading entire knowledge bases
cache stable product knowledge
```

Do not regenerate opportunity output simply because the user changes persona.

---

# 58. Reprocessing Rules

Re-run intelligence only when necessary.

Triggers may include:

```text
new evidence
event material change
product knowledge update
prompt version change
model migration
manual review request
```

No reprocessing needed for:

```text
UI formatting change
persona display change
minor source wording change
```

---

# 59. Processing Version

Derived entities should preserve:

```text
processing_version
model_version
prompt_version
```

This supports:

```text
audit
comparison
rollback
quality evaluation
```

---

# 60. Human Feedback Loop

The UI should eventually support feedback such as:

```text
Useful
Not useful
Product match correct
Product match incorrect
Opportunity relevant
Opportunity irrelevant
```

Feedback should later support:

```text
threshold tuning
prompt improvement
retrieval tuning
scoring improvement
```

Do not automatically retrain or change logic based on one feedback event.

---

# 61. Quality Evaluation

Important evaluation metrics:

```text
Event Extraction Accuracy

Company Resolution Accuracy

Event Deduplication Accuracy

Strategy Inference Quality

Steel Demand Precision

Product Match Precision

Opportunity Relevance

Evidence Coverage

Alert Precision
```

Quality should be evaluated on curated test cases.

---

# 62. Golden Test Set

Create a small curated intelligence test set.

Recommended initial cases:

```text
automotive EV investment
shipbuilding LNG vessel order
energy wind-tower project
competitor steel capacity investment
customer factory cancellation
conflicting news sources
no valid POSCO product match
```

Each case should define expected:

```text
event type
company
industry
strategy
steel category
product-match behavior
opportunity behavior
```

---

# 63. Failure Modes

Important failure modes include:

```text
hallucinated product

duplicate event explosion

incorrect company matching

fact interpreted as inference

inference stored as fact

unsupported numeric forecast

false competitor comparison

irrelevant news generating opportunity

high score with weak evidence
```

Tests and guardrails should explicitly cover these.

---

# 64. Unknown Handling

Unknown is a valid result.

Supported unknown states may include:

```text
UNKNOWN
AMBIGUOUS
INSUFFICIENT_EVIDENCE
PRODUCT_MATCH_UNKNOWN
COMPETITOR_POSITION_UNKNOWN
```

Do not force every input into a confident answer.

---

# 65. Intelligence Status

Recommended processing statuses:

```text
PENDING
PROCESSING
SUCCESS
PARTIAL
FAILED
NEEDS_REVIEW
```

`PARTIAL` may be used when:

```text
event extracted successfully
but product match unavailable
```

A partial result is preferable to fabricated completion.

---

# 66. Explainability

Every opportunity should provide a "Why" chain.

Recommended format:

```text
Evidence

→ Company announced new EV production capacity

Observation

→ EV manufacturing capacity is increasing

Strategy

→ Localization and electrification appear to be priorities

Steel Implication

→ Motor-core and automotive-sheet demand may rise

POSCO Match

→ Relevant product candidates found

Opportunity

→ Customer engagement opportunity exists
```

This chain should come from stored intermediate results, not from newly invented UI prose.

---

# 67. Evidence Strength

Evidence strength may consider:

```text
source tier
directness
specificity
recency
independence
```

Example:

```text
official company announcement:
HIGH

specialized media quoting company:
MEDIUM-HIGH

anonymous market rumor:
LOW
```

High-value opportunities should not rely solely on low-strength evidence.

---

# 68. Time Horizon

Use standardized horizons:

```text
IMMEDIATE
SHORT
MEDIUM
LONG
UNKNOWN
```

Suggested interpretation:

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

Exact definitions may be adjusted by business users.

---

# 69. Industry-Specific Reasoning

Industry reasoning should be modular.

Initial MVP:

```text
AUTOMOTIVE
SHIPBUILDING
ENERGY
```

Each industry may later have specialized mappings.

Example:

```text
AUTOMOTIVE
EV
→ motor
→ motor core
→ electrical steel
```

```text
SHIPBUILDING
LNG carrier
→ cryogenic tank
→ low-temperature performance
→ relevant plate / stainless category
```

```text
ENERGY
offshore wind
→ tower / structure
→ strength + corrosion resistance
→ plate / structural steel
```

Industry mappings should live in taxonomy/reference files rather than hard-coded prompts where possible.

---

# 70. Rule + AI Hybrid Design

Prefer hybrid reasoning.

Example:

```text
LLM:
extracts event and identifies application

Rules/taxonomy:
maps application to known component categories

Retrieval:
finds relevant POSCO products

LLM:
evaluates fit and explains reasoning
```

Avoid asking one LLM prompt to perform the entire chain from raw article to final recommendation.

---

# 71. Deterministic Logic Candidates

Prefer standard code for:

```text
score calculation
currency normalization
date normalization
duplicate URL detection
content hashing
taxonomy validation
threshold checks
alert deduplication
watchlist matching
```

Use AI where semantic interpretation is required.

---

# 72. Intelligence Orchestrator

The intelligence system should have a central orchestration service.

Conceptual flow:

```python
process_source(source_id)

1. load source
2. relevance check
3. extract entities
4. extract event
5. validate event
6. cluster event
7. analyze strategy
8. analyze steel demand
9. optionally retrieve products
10. optionally analyze competitors
11. generate opportunity
12. calculate scores
13. persist results
```

Each step should be callable independently for testing and reprocessing.

---

# 73. Partial Pipeline Execution

The system should support stopping at different stages.

Examples:

Phase 3:

```text
Source
→ Event
→ Strategy
→ Steel Demand
```

Phase 4:

```text
Steel Demand
→ Product Match
→ Opportunity
```

This is important for staged development and cost control.

---

# 74. Idempotency

Processing the same unchanged source multiple times should not create duplicate events or opportunities.

Use:

```text
source hash
processing version
event matching
deduplication keys
```

where appropriate.

---

# 75. Intelligence Reuse

Stored structured intelligence should be reused.

Example:

```text
User asks company overview
```

Do not rerun all event extraction.

Use existing:

```text
events
strategies
opportunities
evidence
```

and synthesize from them.

---

# 76. Freshness

Not all intelligence ages at the same speed.

Examples:

```text
company announcement:
stable fact

investment status:
may change

competitor capacity:
may change

product specification:
relatively stable

market opportunity:
time-sensitive
```

The system may later assign freshness windows by entity type.

---

# 77. Staleness Handling

If important information is old:

```text
show source date
reduce confidence where appropriate
flag as possibly stale
```

Do not present old competitive context as current without qualification.

---

# 78. Contradiction Handling

When new information invalidates previous inference:

```text
preserve old record
mark superseded or outdated
create updated analysis
```

Do not silently erase analytical history.

---

# 79. Competitor Uncertainty

If competitor information is incomplete:

```text
comparison_result = UNKNOWN
```

This is preferable to inventing a position.

---

# 80. Product Knowledge Priority

When product knowledge conflicts with general model knowledge:

```text
internal POSCO knowledge wins
```

For product claims, the LLM should use only approved internal knowledge.

General model knowledge may help interpret industry concepts but not override product facts.

---

# 81. Search Evidence Rules

Ask Steel AI answers should distinguish:

```text
Verified Fact
AI Interpretation
Recommendation
```

A strong response may conceptually contain:

```text
FACT:
Customer announced new investment.

INTERPRETATION:
This may increase regional demand.

POSCO IMPLICATION:
Relevant product family may benefit.

ACTION:
Review procurement timing with the customer.
```

---

# 82. Output Language

The system should support Korean as the primary business language.

Source documents may be:

```text
Korean
English
other languages
```

Store normalized entity codes independent of display language.

Example:

```text
industry code:
AUTOMOTIVE

display:
자동차
```

---

# 83. Translation

Translation should not alter facts.

When translating:

```text
company name
amount
date
technical term
product name
```

must remain accurate.

Where important, retain original terminology.

---

# 84. Technical Terminology

Prefer standardized taxonomy over free-form synonyms.

Example:

Use:

```text
ELECTRICAL_STEEL
```

internally.

Display may show:

```text
전기강판
```

This improves search, scoring, and product matching consistency.

---

# 85. Opportunity Rejection

Not every event should generate an opportunity.

Reject or downgrade if:

```text
no meaningful steel impact

no relevant customer relationship

no product fit

too speculative

low evidence

event already fully reflected

duplicate opportunity
```

The system should be comfortable producing:

```text
NO_ACTIONABLE_OPPORTUNITY
```

---

# 86. Opportunity Deduplication

Prevent multiple cards for the same underlying commercial opportunity.

Signals may include:

```text
same company
same event cluster
same steel-demand hypothesis
same product family
same time horizon
```

Follow-up information should update an existing opportunity where appropriate.

---

# 87. Opportunity Update

An existing opportunity may be recalculated when:

```text
new evidence
new product knowledge
new competitor action
investment amount changes
project schedule changes
official confirmation arrives
```

Preserve history where practical.

---

# 88. Alert Quality

Strategic Alert precision is more important than alert volume.

Target behavior:

```text
few
important
high-confidence
actionable
```

Avoid notification fatigue.

---

# 89. Executive-Level Insight

A strong executive insight should answer:

```text
What changed?
Why now?
How large could the impact be?
What does it mean for POSCO?
What decision may be required?
```

It should not be a reformatted article summary.

---

# 90. Marketing-Level Insight

A strong marketing insight should answer:

```text
Which customer?
What investment or strategy?
Which demand may change?
Which product may fit?
Who competes?
When should we act?
What should we do next?
```

---

# 91. Engineering-Level Insight

A strong engineering insight should answer:

```text
Which application?
Which component?
Which material requirement?
Which existing product fits?
What technical information is missing?
Is development required?
```

---

# 92. MVP Intelligence Scope

Initial intelligence scope should prioritize:

```text
Automotive
Shipbuilding
Energy
```

Initial event focus:

```text
CAPEX
NEW_FACTORY
CAPACITY_EXPANSION
NEW_BUSINESS
R_AND_D
SUPPLY_CHAIN
CONTRACT
ESG
```

Do not attempt perfect coverage of all industries at first.

---

# 93. MVP Success Criteria

The intelligence system is successful when it can reliably process:

```text
SourceDocument
↓
Event
↓
Strategy
↓
Steel Demand
↓
POSCO Product Match
↓
Opportunity
↓
Evidence
```

and provide a result that a marketing user can understand and act on.

---

# 94. Golden End-to-End Example

Input:

```text
A major automotive company announces expansion of a North American EV plant.
```

Expected intelligence flow:

```text
EVENT

CAPEX
+
CAPACITY_EXPANSION

↓

STRATEGY

LOCALIZATION
+
ELECTRIFICATION

↓

INDUSTRY IMPLICATION

regional EV manufacturing capacity increases

↓

STEEL DEMAND

EV motor
→ motor core
→ electrical steel

and

vehicle body
→ high-strength automotive sheet

↓

POSCO PRODUCT RETRIEVAL

retrieve only relevant automotive product knowledge

↓

PRODUCT MATCH

candidate products with fit evidence

↓

COMPETITOR CONTEXT

local competitor supply position

↓

OPPORTUNITY

customer engagement and supply-strategy opportunity

↓

ACTION

marketing:
review future demand and procurement timing

engineering:
review application requirements and technical fit
```

---

# 95. Final Intelligence Rule

The system should never optimize for producing the most impressive answer.

It should optimize for producing the most useful answer that can be defended by evidence.

The preferred behavior is:

```text
accurate
structured
traceable
useful
cautious when uncertain
```

rather than:

```text
verbose
confident
speculative
```

The final goal is to create a **steel marketing intelligence engine**, not a generic AI summarizer.
