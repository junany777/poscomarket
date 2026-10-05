# Steel Market Intelligence Platform Data Model

## 1. Document Purpose

This document defines the logical data model for the Steel Market Intelligence Platform.

The model is designed to support:

- external source collection
- company and industry tracking
- manufacturing-industry event extraction
- company strategy analysis
- steel-demand reasoning
- POSCO product knowledge
- product matching
- competitor intelligence
- opportunity scoring
- evidence traceability
- persona-based presentation
- watchlists
- Telegram alerts
- natural-language search

This document defines logical entities, relationships, important fields, constraints, indexes, and lifecycle states.

Detailed implementation may evolve through Alembic migrations.

---

# 2. Core Modeling Principle

The most important rule is to keep the following concepts separate:

```text
SOURCE
↓
EVENT
↓
INSIGHT
↓
OPPORTUNITY
```

These must not be collapsed into one table.

Definitions:

```text
SOURCE
Collected evidence such as news, disclosure, IR material, RSS content, or official announcement.

EVENT
A structured real-world occurrence derived from one or more sources.

INSIGHT
An analytical interpretation derived from events and other evidence.

OPPORTUNITY
A business or marketing opportunity derived from validated insights, steel demand, POSCO product fit, and competitive context.
```

---

# 3. High-Level Entity Relationship

```text
industries
    │
    ├────────────── companies
    │                   │
    │                   ├──────── company_aliases
    │                   ├──────── company_industries
    │                   └──────── company_relationships
    │
source_providers
    │
    └──────────── source_documents
                        │
                        ├──────── source_entities
                        │
                        └──────── event_evidence
                                      │
                                      ▼
                                    events
                                      │
                   ┌──────────────────┼──────────────────┐
                   │                  │                  │
                   ▼                  ▼                  ▼
             event_entities     event_strategies    steel_demand_hypotheses
                                                       │
                                                       ▼
                                                 product_matches
                                                       │
                                                       ▼
products ───────── product_applications ───────── opportunities
                                                       │
                                                       ├──── opportunity_evidence
                                                       ├──── opportunity_scores
                                                       ├──── competitor_comparisons
                                                       └──── recommended_actions

users
  │
  ├──── watchlists
  ├──── alerts
  └──── saved_queries
```

---

# 4. Data Domains

The database is logically divided into eight domains.

```text
1. Reference Data
2. Company Intelligence
3. Source Collection
4. Event Intelligence
5. Steel Demand
6. POSCO Product Knowledge
7. Opportunity Intelligence
8. User Delivery
```

---

# 5. Common Field Conventions

Most primary entities should contain:

```text
id
created_at
updated_at
```

Use UUID primary keys for application-domain entities unless a simpler integer key is clearly more appropriate.

Recommended:

```text
UUID
```

for:

- companies
- source_documents
- events
- insights
- products
- opportunities
- users
- alerts

Timestamps should use:

```text
TIMESTAMP WITH TIME ZONE
```

Store timestamps in UTC.

Presentation should convert to the user's local timezone.

---

# 6. Audit Fields

Important analytical entities should support auditability.

Recommended common fields:

```text
created_at
updated_at
created_by
processing_version
model_version
prompt_version
```

Not every table needs all fields.

Use these primarily for AI-generated or derived objects.

---

# 7. Reference Data

## 7.1 industries

Purpose:

Defines supported manufacturing and steel-related industries.

Fields:

```text
id
code
name_ko
name_en
parent_id
description
is_active
created_at
updated_at
```

Example codes:

```text
AUTOMOTIVE
SHIPBUILDING
ENERGY
BATTERY
SEMICONDUCTOR
CONSTRUCTION
MACHINERY
HOME_APPLIANCE
DEFENSE
AEROSPACE
ROBOTICS
HYDROGEN
DATA_CENTER
```

Constraints:

```text
code UNIQUE
```

Index:

```text
idx_industries_parent_id
```

---

# 8. Company Intelligence

## 8.1 companies

Purpose:

Stores customers, potential customers, suppliers, steel competitors, and other relevant companies.

Fields:

```text
id
canonical_name
name_ko
name_en
company_type
company_size
country_code
headquarters_region
website
dart_corp_code
stock_code
lei
is_customer
is_competitor
is_watchlist_default
status
created_at
updated_at
```

company_type examples:

```text
MANUFACTURER
STEELMAKER
SUPPLIER
CUSTOMER
GOVERNMENT
ASSOCIATION
OTHER
```

company_size examples:

```text
LARGE
MID
SME
GLOBAL
STARTUP
UNKNOWN
```

status:

```text
ACTIVE
INACTIVE
MERGED
UNKNOWN
```

Important constraints:

```text
dart_corp_code UNIQUE when present
stock_code UNIQUE only within applicable market scope
```

Indexes:

```text
idx_companies_canonical_name
idx_companies_country_code
idx_companies_company_type
idx_companies_is_competitor
idx_companies_is_customer
```

---

# 9. company_aliases

Purpose:

Supports company name normalization and entity resolution.

Fields:

```text
id
company_id
alias
language
alias_type
normalized_alias
created_at
```

alias_type:

```text
OFFICIAL
SHORT_NAME
ENGLISH
KOREAN
BRAND
FORMER_NAME
OTHER
```

Example:

```text
Hyundai Motor Company
Hyundai Motor
현대자동차
현대차
```

Constraints:

```text
(company_id, normalized_alias) UNIQUE
```

Index:

```text
idx_company_aliases_normalized_alias
```

---

# 10. company_industries

Purpose:

Many-to-many relationship between companies and industries.

Fields:

```text
company_id
industry_id
relationship_type
is_primary
confidence
created_at
```

relationship_type:

```text
PRIMARY
SECONDARY
EMERGING
SUPPLY_CHAIN
```

Constraint:

```text
(company_id, industry_id, relationship_type) UNIQUE
```

---

# 11. company_relationships

Purpose:

Tracks business relationships between companies.

Examples:

```text
customer-supplier
joint venture
strategic alliance
competitor
subsidiary
parent company
technology partner
```

Fields:

```text
id
source_company_id
target_company_id
relationship_type
start_date
end_date
confidence
evidence_summary
created_at
updated_at
```

relationship_type:

```text
CUSTOMER
SUPPLIER
JV
PARTNER
SUBSIDIARY
PARENT
COMPETITOR
TECHNOLOGY_PARTNER
OTHER
```

---

# 12. Source Collection Domain

## 12.1 source_providers

Purpose:

Defines external data providers.

Fields:

```text
id
code
name
provider_type
base_url
reliability_tier
default_reliability_score
collection_method
is_active
created_at
updated_at
```

provider_type:

```text
DISCLOSURE
NEWS
RSS
CORPORATE_IR
GOVERNMENT
INDUSTRY_MEDIA
ASSOCIATION
COMPETITOR
OTHER
```

collection_method:

```text
API
RSS
HTTP
SEARCH_API
MANUAL
```

Example providers:

```text
OPENDART
NAVER_NEWS
FERROTIMES
STEEL_DAILY
KOSA
COMPANY_IR
```

---

# 13. source_documents

Purpose:

Canonical normalized representation of collected information.

One row represents one collected document.

Fields:

```text
id
provider_id
external_id
source_type
title
body
summary
url
canonical_url
author
published_at
collected_at
language
content_hash
title_hash
raw_metadata
processing_status
duplicate_of_id
copyright_storage_mode
created_at
updated_at
```

source_type:

```text
DISCLOSURE
NEWS
PRESS_RELEASE
RSS_ARTICLE
REPORT
IR
GOVERNMENT_NOTICE
ASSOCIATION_POST
OTHER
```

processing_status:

```text
COLLECTED
NORMALIZED
DUPLICATE
READY_FOR_ANALYSIS
ANALYZED
FAILED
```

copyright_storage_mode:

```text
FULL_TEXT_ALLOWED
EXCERPT_ONLY
METADATA_ONLY
UNKNOWN
```

Important constraints:

```text
(provider_id, external_id) UNIQUE when external_id exists
content_hash indexed
canonical_url indexed
```

Indexes:

```text
idx_source_documents_published_at
idx_source_documents_provider_id
idx_source_documents_processing_status
idx_source_documents_content_hash
idx_source_documents_canonical_url
```

Potential future full-text index:

```text
GIN index
```

for title and permitted content.

---

# 14. source_entities

Purpose:

Stores entities identified inside a source document before event generation.

Fields:

```text
id
source_document_id
entity_type
entity_value
normalized_value
company_id
industry_id
confidence
start_offset
end_offset
created_at
```

entity_type:

```text
COMPANY
INDUSTRY
COUNTRY
REGION
TECHNOLOGY
PRODUCT
APPLICATION
FACILITY
AMOUNT
PERSON
OTHER
```

This table allows entity extraction results to be reused without rerunning AI.

---

# 15. Event Intelligence Domain

## 15.1 events

Purpose:

Stores structured real-world events derived from source evidence.

Fields:

```text
id
primary_company_id
industry_id
event_type
event_subtype
title
description
country_code
region
city
investment_amount
investment_currency
investment_amount_krw
capacity_value
capacity_unit
event_date
announced_at
start_date
target_date
status
extraction_confidence
importance_score
processing_version
model_version
prompt_version
created_at
updated_at
```

event_type:

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

status:

```text
ANNOUNCED
PLANNED
IN_PROGRESS
COMPLETED
CANCELLED
UNKNOWN
```

Important rule:

```text
An event cannot be persisted as validated without at least one evidence source.
```

Indexes:

```text
idx_events_primary_company_id
idx_events_industry_id
idx_events_event_type
idx_events_announced_at
idx_events_target_date
idx_events_importance_score
```

---

# 16. event_evidence

Purpose:

Many-to-many relationship between events and source documents.

Fields:

```text
event_id
source_document_id
evidence_role
evidence_strength
is_primary
supporting_excerpt
created_at
```

evidence_role:

```text
PRIMARY_SOURCE
CONFIRMING_SOURCE
SUPPLEMENTARY
CONTRADICTING
```

evidence_strength:

```text
0.0 - 1.0
```

Constraint:

```text
(event_id, source_document_id) UNIQUE
```

This table is critical for explainability.

---

# 17. event_entities

Purpose:

Associates multiple companies, technologies, products, applications, or locations with one event.

Fields:

```text
id
event_id
entity_type
company_id
industry_id
entity_value
relationship_role
confidence
created_at
```

relationship_role examples:

```text
INVESTOR
TARGET_COMPANY
CUSTOMER
SUPPLIER
PARTNER
JV_PARTNER
LOCATION
TECHNOLOGY
APPLICATION
OTHER
```

---

# 18. Event Clustering

## 18.1 event_clusters

Purpose:

Groups related or duplicate events.

Fields:

```text
id
cluster_key
canonical_event_id
cluster_type
similarity_score
created_at
updated_at
```

cluster_type:

```text
DUPLICATE
FOLLOW_UP
RELATED
```

---

# 19. event_cluster_members

Fields:

```text
cluster_id
event_id
similarity_score
created_at
```

This allows multiple articles or follow-up announcements to resolve into one event family.

---

# 20. Strategy Intelligence

## 20.1 event_strategies

Purpose:

Stores inferred company strategies derived from events.

Fields:

```text
id
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
created_at
updated_at
```

strategy_type:

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
OTHER
```

time_horizon:

```text
SHORT
MEDIUM
LONG
UNKNOWN
```

Important:

This table stores **INFERENCE**, not observed fact.

The evidence must remain connected through the parent event.

---

# 21. Insights

## 21.1 insights

Purpose:

Stores reusable analytical conclusions not yet converted into direct business opportunities.

Fields:

```text
id
insight_type
industry_id
company_id
event_id
headline
summary
observation
industry_implication
company_implication
time_horizon
confidence_score
status
processing_version
model_version
prompt_version
created_at
updated_at
```

insight_type:

```text
INDUSTRY
COMPANY
TECHNOLOGY
DEMAND
COMPETITOR
SUPPLY_CHAIN
OTHER
```

status:

```text
DRAFT
VALIDATED
PUBLISHED
ARCHIVED
```

---

# 22. insight_evidence

Purpose:

Links an insight to supporting evidence.

Fields:

```text
insight_id
source_document_id
event_id
evidence_role
created_at
```

An insight may be supported by both direct documents and structured events.

---

# 23. Steel Demand Domain

## 23.1 steel_demand_hypotheses

Purpose:

Represents a hypothesis connecting industry or customer change to steel demand.

Fields:

```text
id
event_id
insight_id
industry_id
application_id
component_id
steel_category
material_requirement_summary
required_properties
demand_direction
demand_magnitude
time_horizon
reasoning_summary
confidence_score
status
processing_version
model_version
prompt_version
created_at
updated_at
```

demand_direction:

```text
INCREASE
DECREASE
SHIFT
NEW_DEMAND
UNCERTAIN
```

demand_magnitude:

```text
LOW
MEDIUM
HIGH
UNKNOWN
```

status:

```text
HYPOTHESIS
VALIDATED
REJECTED
```

Important:

This table does not yet represent a specific POSCO product recommendation.

---

# 24. Applications

## 24.1 applications

Purpose:

Defines industrial applications that consume steel.

Fields:

```text
id
industry_id
code
name_ko
name_en
description
parent_id
created_at
updated_at
```

Examples:

```text
EV_BODY
EV_MOTOR
BATTERY_CASE
SHIP_HULL
LNG_TANK
WIND_TOWER
HYDROGEN_PIPELINE
```

Constraint:

```text
code UNIQUE
```

---

# 25. Components

## 25.1 components

Purpose:

Defines physical components within applications.

Fields:

```text
id
application_id
code
name_ko
name_en
description
created_at
updated_at
```

Examples:

```text
MOTOR_CORE
BODY_IN_WHITE
BATTERY_CASE
HULL_PLATE
PRESSURE_VESSEL
PIPE
```

---

# 26. POSCO Product Knowledge Domain

## 26.1 product_families

Purpose:

Groups related POSCO products.

Fields:

```text
id
code
name
description
created_at
updated_at
```

Examples:

```text
AUTOMOTIVE_STEEL
ELECTRICAL_STEEL
THICK_PLATE
STAINLESS
ENERGY_STEEL
```

---

# 27. products

Purpose:

Stores structured POSCO product knowledge.

Fields:

```text
id
product_family_id
product_code
product_name
product_name_ko
product_name_en
description
steel_grade
product_status
source_document_path
knowledge_version
created_at
updated_at
```

product_status:

```text
ACTIVE
DEPRECATED
EXPERIMENTAL
UNKNOWN
```

Important rule:

Product records must originate from approved POSCO knowledge sources.

Do not create speculative product records.

---

# 28. product_properties

Purpose:

Stores technical and functional properties.

Fields:

```text
id
product_id
property_name
property_category
value_text
value_numeric
unit
min_value
max_value
source_reference
created_at
```

property_category:

```text
MECHANICAL
MAGNETIC
CHEMICAL
CORROSION
FORMABILITY
WELDABILITY
THERMAL
SURFACE
SUSTAINABILITY
OTHER
```

---

# 29. product_applications

Purpose:

Maps POSCO products to industries, applications, and components.

Fields:

```text
id
product_id
industry_id
application_id
component_id
fit_level
fit_reason
source_reference
created_at
updated_at
```

fit_level:

```text
PRIMARY
SUPPORTED
POSSIBLE
UNKNOWN
```

Constraint:

```text
(product_id, application_id, component_id) UNIQUE
```

---

# 30. product_benefits

Purpose:

Stores commercial or customer-facing benefits.

Fields:

```text
id
product_id
benefit_type
benefit_text
source_reference
created_at
```

benefit_type:

```text
WEIGHT_REDUCTION
ENERGY_EFFICIENCY
STRENGTH
CORROSION_RESISTANCE
FORMABILITY
LOW_CARBON
PRODUCTIVITY
COST
SAFETY
OTHER
```

---

# 31. product_embeddings

Purpose:

Optional semantic retrieval support.

Fields:

```text
id
product_id
chunk_key
content
embedding
metadata
created_at
updated_at
```

Use pgvector.

Do not introduce this table until semantic retrieval is required.

Recommended indexes:

```text
vector index
product_id
```

---

# 32. Product Matching

## 32.1 product_matches

Purpose:

Stores evaluated relationships between steel demand hypotheses and POSCO products.

Fields:

```text
id
steel_demand_hypothesis_id
product_id
fit_score
fit_confidence
fit_reason
matching_properties
missing_requirements
status
processing_version
model_version
prompt_version
created_at
updated_at
```

status:

```text
MATCHED
POSSIBLE
REJECTED
UNKNOWN
```

fit_score:

```text
0 - 100
```

Important rule:

If no reliable knowledge supports a match:

```text
status = UNKNOWN
```

rather than fabricating a result.

---

# 33. Competitor Intelligence Domain

## 33.1 competitor_profiles

Purpose:

Stores competitor-specific metadata.

Fields:

```text
id
company_id
market_position
regions
focus_industries
notes
created_at
updated_at
```

The linked company must have:

```text
is_competitor = true
```

---

# 34. competitor_capabilities

Purpose:

Stores structured competitor capability observations.

Fields:

```text
id
competitor_company_id
industry_id
application_id
capability_type
capability_summary
maturity_level
confidence
source_document_id
valid_from
valid_to
created_at
updated_at
```

capability_type:

```text
PRODUCT
TECHNOLOGY
CAPACITY
GEOGRAPHY
CUSTOMER_RELATIONSHIP
LOW_CARBON
SUPPLY_CHAIN
COST
OTHER
```

maturity_level:

```text
ANNOUNCED
DEVELOPMENT
COMMERCIAL
MATURE
UNKNOWN
```

---

# 35. competitor_comparisons

Purpose:

Stores POSCO-versus-competitor comparison for an opportunity.

Fields:

```text
id
opportunity_id
competitor_company_id
comparison_dimension
posco_position
competitor_position
comparison_result
reasoning_summary
confidence_score
created_at
updated_at
```

comparison_result:

```text
ADVANTAGE
PARITY
DISADVANTAGE
UNKNOWN
```

comparison_dimension examples:

```text
TECHNOLOGY
PRODUCT
LOCAL_SUPPLY
CAPACITY
COST
SUSTAINABILITY
CUSTOMER_RELATIONSHIP
COMMERCIALIZATION
```

---

# 36. Opportunity Domain

## 36.1 opportunities

Purpose:

Represents the main business object delivered to users.

Fields:

```text
id
company_id
industry_id
primary_event_id
primary_insight_id
steel_demand_hypothesis_id
primary_product_match_id
headline
summary
opportunity_type
opportunity_level
opportunity_score
confidence_score
time_horizon
market_window_start
market_window_end
status
is_strategic_alert_candidate
processing_version
model_version
prompt_version
created_at
updated_at
```

opportunity_type:

```text
NEW_DEMAND
DEMAND_GROWTH
PRODUCT_SUBSTITUTION
PREMIUMIZATION
LOCALIZATION
TECHNICAL_PROPOSAL
JOINT_DEVELOPMENT
COMPETITOR_DEFENSE
NEW_CUSTOMER
OTHER
```

opportunity_level:

```text
STRATEGIC
HIGH
WATCH
INFORMATION
```

status:

```text
DRAFT
VALIDATED
PUBLISHED
DISMISSED
ARCHIVED
```

Indexes:

```text
idx_opportunities_company_id
idx_opportunities_industry_id
idx_opportunities_opportunity_score
idx_opportunities_confidence_score
idx_opportunities_created_at
idx_opportunities_status
```

---

# 37. Opportunity Scoring

## 37.1 opportunity_score_components

Purpose:

Stores individual scoring components instead of only the final score.

Fields:

```text
id
opportunity_id
score_type
raw_score
weight
weighted_score
reason
created_at
updated_at
```

score_type:

```text
INDUSTRY_IMPACT
CUSTOMER_IMPORTANCE
INVESTMENT_SCALE
STEEL_DEMAND_IMPACT
POSCO_PRODUCT_FIT
TIMING
```

Default weights:

```text
INDUSTRY_IMPACT       0.20
CUSTOMER_IMPORTANCE   0.15
INVESTMENT_SCALE      0.15
STEEL_DEMAND_IMPACT   0.20
POSCO_PRODUCT_FIT     0.20
TIMING                0.10
```

Constraint:

```text
(opportunity_id, score_type) UNIQUE
```

This allows future score recalculation without regenerating the entire opportunity.

---

# 38. Confidence Components

## 38.1 confidence_score_components

Purpose:

Explains why an analysis has a certain confidence level.

Fields:

```text
id
entity_type
entity_id
factor_type
score
weight
reason
created_at
```

factor_type:

```text
SOURCE_RELIABILITY
SOURCE_INDEPENDENCE
SOURCE_AGREEMENT
DATA_COMPLETENESS
RECENCY
INFERENCE_DISTANCE
PRODUCT_KNOWLEDGE_SUPPORT
```

entity_type may refer to:

```text
EVENT
INSIGHT
STEEL_DEMAND
PRODUCT_MATCH
OPPORTUNITY
```

---

# 39. Opportunity Evidence

## 39.1 opportunity_evidence

Purpose:

Links opportunity cards directly to supporting evidence.

Fields:

```text
opportunity_id
source_document_id
event_id
insight_id
evidence_role
importance
created_at
```

evidence_role:

```text
BUSINESS_FACT
STRATEGY_SUPPORT
STEEL_DEMAND_SUPPORT
PRODUCT_SUPPORT
COMPETITOR_SUPPORT
OTHER
```

---

# 40. Recommended Actions

## 40.1 recommended_actions

Purpose:

Stores actionable recommendations separately from the opportunity summary.

Fields:

```text
id
opportunity_id
action_type
persona
title
description
priority
due_horizon
owner_role
status
confidence
created_at
updated_at
```

action_type:

```text
MARKETING
SALES
TECHNICAL
RESEARCH
CUSTOMER_ENGAGEMENT
COMPETITOR_MONITORING
PRODUCT_DEVELOPMENT
EXECUTIVE_REVIEW
OTHER
```

persona:

```text
EXECUTIVE
MARKETING
ENGINEERING
GENERAL
```

priority:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

status:

```text
PROPOSED
ACCEPTED
IN_PROGRESS
COMPLETED
DISMISSED
```

---

# 41. Persona Rendering

## 41.1 persona_views

Purpose:

Optional cache of persona-specific rendered output.

Fields:

```text
id
opportunity_id
persona
headline
summary
key_points
recommended_actions
rendered_at
model_version
prompt_version
created_at
```

Important:

This is presentation data only.

Core intelligence remains stored in the underlying opportunity.

If outputs can be generated cheaply, this table may be omitted during MVP.

---

# 42. User Domain

## 42.1 users

Purpose:

Stores application users.

Fields:

```text
id
email
display_name
role
persona
is_active
timezone
created_at
updated_at
last_login_at
```

role:

```text
ADMIN
USER
ANALYST
VIEWER
```

persona:

```text
EXECUTIVE
MARKETING
ENGINEERING
GENERAL
```

---

# 43. Watchlists

## 43.1 watchlists

Purpose:

Stores user-defined monitoring groups.

Fields:

```text
id
user_id
name
description
is_default
created_at
updated_at
```

---

# 44. watchlist_items

Purpose:

Stores watchlist targets.

Fields:

```text
id
watchlist_id
item_type
company_id
industry_id
value
priority
created_at
```

item_type:

```text
COMPANY
INDUSTRY
COMPETITOR
TECHNOLOGY
APPLICATION
REGION
KEYWORD
```

priority:

```text
HIGH
MEDIUM
LOW
```

---

# 45. Saved Queries

## 45.1 saved_queries

Purpose:

Stores frequently used Ask Steel AI queries.

Fields:

```text
id
user_id
name
query_text
query_type
filters
is_pinned
created_at
updated_at
```

---

# 46. Search History

## 46.1 search_history

Purpose:

Optional analytics for user search behavior.

Fields:

```text
id
user_id
query_text
resolved_intent
filters
result_count
created_at
```

Do not store sensitive prompt content unnecessarily.

---

# 47. Alerts

## 47.1 alerts

Purpose:

Stores generated alerts before or after delivery.

Fields:

```text
id
user_id
opportunity_id
alert_type
channel
title
message
status
priority
deduplication_key
scheduled_at
sent_at
failed_at
failure_reason
created_at
updated_at
```

alert_type:

```text
DAILY_BRIEF
STRATEGIC
WATCHLIST
SYSTEM
```

channel:

```text
TELEGRAM
IN_APP
EMAIL_FUTURE
```

status:

```text
PENDING
SENT
FAILED
CANCELLED
```

Important constraint:

```text
deduplication_key UNIQUE where applicable
```

This prevents repeated Strategic Alerts.

---

# 48. Telegram Configuration

## 48.1 notification_channels

Purpose:

Stores channel-level configuration without exposing secrets.

Fields:

```text
id
user_id
channel_type
external_target_id
is_active
settings
created_at
updated_at
```

Do not store bot tokens here.

Bot tokens remain in environment variables or a secrets manager.

---

# 49. Daily Briefs

## 49.1 daily_briefs

Purpose:

Stores generated daily summaries.

Fields:

```text
id
brief_date
persona
headline
summary
opportunity_ids
industry_summary
competitor_summary
watchlist_summary
status
generated_at
sent_at
created_at
updated_at
```

status:

```text
DRAFT
READY
SENT
FAILED
```

For PostgreSQL, `opportunity_ids` may be normalized later if relationship complexity grows.

---

# 50. Job Processing Domain

## 50.1 processing_jobs

Purpose:

Tracks collection and intelligence pipeline jobs.

Fields:

```text
id
job_type
provider_id
status
started_at
completed_at
items_processed
items_succeeded
items_failed
error_summary
metadata
created_at
updated_at
```

job_type:

```text
COLLECTION
NORMALIZATION
EVENT_EXTRACTION
STRATEGY_ANALYSIS
STEEL_DEMAND
PRODUCT_MATCHING
OPPORTUNITY_GENERATION
DAILY_BRIEF
ALERT_DELIVERY
```

status:

```text
PENDING
RUNNING
SUCCESS
PARTIAL
FAILED
```

---

# 51. AI Execution Log

## 51.1 ai_runs

Purpose:

Tracks AI processing for audit and cost analysis.

Fields:

```text
id
operation_type
entity_type
entity_id
model_name
prompt_version
input_token_count
output_token_count
estimated_cost
latency_ms
status
error_code
started_at
completed_at
created_at
```

operation_type:

```text
ENTITY_EXTRACTION
EVENT_EXTRACTION
STRATEGY_ANALYSIS
STEEL_DEMAND
PRODUCT_MATCHING
OPPORTUNITY_GENERATION
PERSONA_RENDERING
ASK_STEEL_AI
```

Do not store complete sensitive prompts or copyrighted source text unless necessary.

---

# 52. Data Lineage

Every major derived entity should support traceability.

Expected path:

```text
Opportunity
↓
Product Match
↓
Steel Demand Hypothesis
↓
Insight / Strategy
↓
Event
↓
Source Document
↓
Original URL
```

A user should be able to move backward from a recommendation to its evidence.

This lineage is mandatory for high-value insights.

---

# 53. Fact vs Inference Modeling

Facts and inference must be structurally separate.

FACT:

```text
source_documents
events
```

INFERENCE:

```text
event_strategies
insights
steel_demand_hypotheses
product_matches
opportunities
recommended_actions
```

The distinction must remain visible to developers and users.

---

# 54. JSONB Usage

PostgreSQL JSONB may be used for flexible metadata.

Recommended uses:

```text
raw_metadata
required_properties
matching_properties
filters
settings
processing metadata
```

Do not use JSONB as a replacement for core relational fields.

Bad:

```text
events.data = everything
```

Good:

```text
events.event_type
events.company_id
events.investment_amount

plus

events.additional_metadata JSONB
```

---

# 55. Monetary Values

Financial and investment data should store:

```text
original amount
original currency
normalized amount
normalization date/rate if used
```

Recommended fields:

```text
investment_amount
investment_currency
investment_amount_krw
fx_rate_used
fx_rate_date
```

Do not permanently overwrite original values after conversion.

---

# 56. Date Modeling

Distinguish dates carefully.

Examples:

```text
published_at
announced_at
event_date
start_date
target_date
completed_at
```

Do not use one generic `date` field for all concepts.

---

# 57. Soft Deletion

For critical analytical entities, prefer archival status over hard delete.

Examples:

```text
ARCHIVED
DISMISSED
INACTIVE
```

Hard deletion may be allowed for:

```text
temporary processing data
failed imports
test records
```

subject to audit requirements.

---

# 58. Versioning

AI-derived objects may change when prompts or models change.

Maintain where relevant:

```text
processing_version
model_version
prompt_version
```

This allows comparison such as:

```text
Opportunity generated using prompt v1.4
vs
Opportunity generated using prompt v1.5
```

---

# 59. Important Unique Constraints

Recommended uniqueness rules include:

```text
industries.code

company_aliases(company_id, normalized_alias)

source_documents(provider_id, external_id)

event_evidence(event_id, source_document_id)

product_applications(product_id, application_id, component_id)

opportunity_score_components(opportunity_id, score_type)

alerts.deduplication_key
```

Exact implementation may vary based on nullable fields.

---

# 60. Important Database Indexes

At minimum consider indexes for:

```text
companies.canonical_name
companies.stock_code
companies.dart_corp_code

source_documents.published_at
source_documents.processing_status
source_documents.content_hash
source_documents.canonical_url

events.primary_company_id
events.industry_id
events.event_type
events.announced_at

insights.company_id
insights.industry_id

steel_demand_hypotheses.event_id
steel_demand_hypotheses.steel_category

products.product_family_id
product_applications.industry_id
product_applications.application_id

opportunities.company_id
opportunities.industry_id
opportunities.opportunity_score
opportunities.confidence_score
opportunities.status

alerts.status
alerts.scheduled_at
```

Add indexes based on real query plans rather than speculative optimization.

---

# 61. Search Architecture Support

The data model must support three main search modes.

## Structured Search

Examples:

```text
industry = automotive
event_type = CAPEX
country = USA
date >= last 6 months
```

Use relational filters.

## Full-Text Search

Examples:

```text
"전기강판"
"북미 현지 생산"
```

Use PostgreSQL full-text search where appropriate.

## Semantic Search

Examples:

```text
"미국 전기차 생산 확대와 관련된 철강 기회"
```

Use pgvector only for relevant text chunks.

Do not use semantic search when a direct relational query is sufficient.

---

# 62. MVP Table Priority

Not every table should be built in Phase 1.

Recommended implementation order:

## Phase 1

Create:

```text
industries
companies
source_providers
```

## Phase 2

Add:

```text
company_aliases
company_industries
source_documents
source_entities
processing_jobs
```

## Phase 3

Add:

```text
events
event_evidence
event_entities
event_clusters
event_cluster_members
event_strategies
insights
insight_evidence
steel_demand_hypotheses
applications
components
ai_runs
```

## Phase 4

Add:

```text
product_families
products
product_properties
product_applications
product_benefits
product_embeddings
product_matches
competitor_profiles
competitor_capabilities
competitor_comparisons
opportunities
opportunity_score_components
confidence_score_components
opportunity_evidence
recommended_actions
```

## Phase 5

Add:

```text
users
watchlists
watchlist_items
saved_queries
search_history
alerts
notification_channels
daily_briefs
persona_views
```

---

# 63. Tables That May Be Deferred

The following are useful but not mandatory for initial MVP:

```text
company_relationships
persona_views
search_history
product_embeddings
competitor_capabilities
daily_briefs
```

Implement them only when required.

Avoid creating every possible table before the first end-to-end workflow works.

---

# 64. End-to-End Data Example

Example scenario:

```text
현대자동차가 미국 EV 공장 확대 발표
```

Data flow:

```text
source_documents

provider:
NAVER / company IR / DART

↓

events

event_type:
CAPEX

primary_company:
Hyundai Motor

↓

event_strategies

strategy:
LOCALIZATION
ELECTRIFICATION

↓

steel_demand_hypotheses

application:
EV_MOTOR

component:
MOTOR_CORE

steel_category:
ELECTRICAL_STEEL

demand_direction:
INCREASE

↓

product_matches

POSCO product candidate:
relevant electrical steel product

↓

opportunities

opportunity_type:
DEMAND_GROWTH

opportunity_score:
92

confidence_score:
84

↓

recommended_actions

MARKETING:
Review long-term demand forecast

ENGINEERING:
Assess technical requirement alignment
```

---

# 65. Example Evidence Chain

A valid Opportunity should allow this trace:

```text
Opportunity #123
↓
Primary Event #456
↓
Event Evidence
↓
Source Document #789
↓
Original corporate release
```

And separately:

```text
Opportunity #123
↓
Product Match #222
↓
Product #333
↓
knowledge/posco/... source document
```

This allows both external and internal evidence to be verified.

---

# 66. Opportunity Object Concept

The Opportunity object should be treated as the central business object in the application.

It combines references to:

```text
customer
industry
event
strategy
steel demand
product match
competitor context
scores
recommended actions
evidence
```

It should not duplicate all upstream content.

Use foreign keys and related entities instead of copying large blocks of data.

---

# 67. Data Integrity Rules

The following rules should be enforced at service or database level.

### Rule 1

Validated Event requires evidence.

### Rule 2

Product Match requires a valid product record.

### Rule 3

Opportunity must reference a company or industry context.

### Rule 4

Opportunity Score must remain within:

```text
0 - 100
```

### Rule 5

Confidence Score must remain within:

```text
0 - 100
```

### Rule 6

Product recommendation cannot reference an unknown product name.

### Rule 7

AI inference cannot overwrite source facts.

### Rule 8

Source records should not be silently mutated after analysis.

---

# 68. Data Lifecycle

Recommended lifecycle:

```text
COLLECT
↓
NORMALIZE
↓
DEDUPLICATE
↓
ANALYZE
↓
VALIDATE
↓
PUBLISH
↓
ARCHIVE
```

Source lifecycle:

```text
COLLECTED
→ NORMALIZED
→ READY_FOR_ANALYSIS
→ ANALYZED
```

Event lifecycle:

```text
EXTRACTED
→ VALIDATED
→ UPDATED
→ ARCHIVED
```

Opportunity lifecycle:

```text
DRAFT
→ VALIDATED
→ PUBLISHED
→ DISMISSED / ARCHIVED
```

---

# 69. Updating Existing Events

A later source may provide new information about an existing event.

Do not create a completely unrelated event every time.

Preferred flow:

```text
new source
↓
event similarity check
↓
existing event found
↓
attach new evidence
↓
update selected structured fields
↓
recalculate confidence
↓
re-evaluate opportunity if material change
```

Maintain enough audit information to understand what changed.

---

# 70. Event Material Change

An existing event should trigger opportunity recalculation when material fields change.

Examples:

```text
investment amount changed
target date changed
capacity changed
project cancelled
new major partner added
technology scope changed
official confirmation added
```

Minor article wording changes should not trigger full recomputation.

---

# 71. Confidence Recalculation

Confidence should improve when:

```text
official source appears
multiple independent sources confirm
missing data becomes available
product evidence improves
```

Confidence may decrease when:

```text
sources conflict
project is delayed
official denial appears
information becomes stale
```

Store confidence components so recalculation remains explainable.

---

# 72. Scoring Recalculation

Opportunity Score should be recalculable independently.

Example:

```text
customer importance changes
investment size updated
POSCO product fit changes
timing becomes more urgent
```

Do not require complete AI regeneration when only deterministic scoring changes.

---

# 73. Data Retention

Recommended retention principles:

```text
structured facts:
long-term

event history:
long-term

opportunities:
long-term with archival

AI run logs:
configurable retention

raw copyrighted article text:
source-rights dependent

temporary processing payloads:
short retention
```

---

# 74. Privacy and Security

Do not store unnecessary personal data.

The system is primarily company and industry intelligence.

User data should be limited to:

```text
authentication
persona
preferences
watchlists
saved queries
notification settings
```

Secrets must never be stored in business tables.

---

# 75. Data Model Design Principles

When extending this model, follow these rules:

```text
Facts before inference

Evidence before recommendation

Normalized relations before duplicated text

Structured fields before giant JSON blobs

Explicit lifecycle states before implicit behavior

Scores with components before unexplained final numbers

Product knowledge references before product claims

Provider independence before source-specific design

Traceability before convenience
```

---

# 76. MVP Definition of Data Success

The data model is sufficient for MVP when the following chain can be persisted and retrieved:

```text
SourceDocument
↓
Event
↓
Company Strategy
↓
Steel Demand Hypothesis
↓
POSCO Product Match
↓
Opportunity
↓
Opportunity Score
↓
Confidence Score
↓
Recommended Action
↓
Evidence
```

The user must be able to move from an Opportunity back to both:

```text
external evidence
```

and

```text
internal POSCO product evidence
```

without relying on hidden LLM memory.

That traceability is the central data-model requirement of the system.
