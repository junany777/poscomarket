# Steel Market Intelligence Platform Architecture

## 1. Document Purpose

This document defines the application architecture for the Steel Market Intelligence Platform.

It describes:

- system boundaries
- major application layers
- module responsibilities
- data flow
- external integrations
- AI processing flow
- knowledge architecture
- frontend/backend interaction
- background processing
- security boundaries
- scalability principles

This document does **not** define detailed database schemas, prompt text, product specifications, or event taxonomies.

Those details belong in:

```text
docs/data-model.md
docs/intelligence.md
knowledge/taxonomy/
knowledge/posco/
```

---

# 2. System Objective

The platform is an AI-powered industrial and steel marketing intelligence system.

Its purpose is to detect important changes in manufacturing industries and translate them into actionable marketing intelligence for a steel company.

The system should answer questions such as:

```text
Which customers are investing?

What future businesses are manufacturing companies preparing for?

Which technologies or production capabilities are expanding?

How could those developments affect steel demand?

Which POSCO products may fit those future requirements?

What are competing steel companies doing?

What marketing or technical action should POSCO consider?
```

The system is not intended to operate as a simple news summarizer.

---

# 3. Core Intelligence Flow

The primary value chain of the application is:

```text
EXTERNAL DATA
      ↓
SOURCE COLLECTION
      ↓
NORMALIZATION
      ↓
EVENT DETECTION
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
OPPORTUNITY ANALYSIS
      ↓
PERSONA PRESENTATION
      ↓
DASHBOARD / SEARCH / TELEGRAM
```

A recommendation must never skip directly from:

```text
NEWS
→ POSCO PRODUCT
```

The intermediate reasoning stages are a core architectural requirement.

---

# 4. High-Level Architecture

The recommended MVP architecture is a modular monolith.

```text
                    ┌─────────────────────────┐
                    │     External Sources    │
                    │                         │
                    │ OpenDART                │
                    │ NAVER News              │
                    │ RSS                     │
                    │ Steel Media             │
                    │ Corporate IR            │
                    │ Government Sources      │
                    │ Competitor Sources      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Collection Layer     │
                    │                         │
                    │ Provider Adapters       │
                    │ Fetch                   │
                    │ Parse                   │
                    │ Normalize               │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Source Storage      │
                    │                         │
                    │ SourceDocument          │
                    │ Raw Metadata            │
                    │ Deduplication           │
                    │ Evidence                │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Intelligence Pipeline   │
                    │                         │
                    │ Entity Extraction       │
                    │ Event Extraction        │
                    │ Strategy Analysis       │
                    │ Steel Demand Analysis   │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴────────────────┐
                 │                                │
                 ▼                                ▼
       ┌─────────────────────┐          ┌──────────────────────┐
       │ POSCO Product Brain │          │ Competitor Knowledge │
       │                     │          │                      │
       │ Product MD          │          │ Investment           │
       │ Application Map     │          │ Products             │
       │ Material Properties │          │ Capacity             │
       │ Retrieval           │          │ Partnerships         │
       └──────────┬──────────┘          └──────────┬───────────┘
                  │                                │
                  └──────────────┬─────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │   Opportunity Engine    │
                    │                         │
                    │ Product Fit             │
                    │ Opportunity Score       │
                    │ Confidence Score        │
                    │ Marketing Action        │
                    │ Technical Action        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Application API     │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
        ┌────────────┐     ┌──────────────┐    ┌────────────┐
        │ Dashboard  │     │ Ask Steel AI │    │ Telegram   │
        └────────────┘     └──────────────┘    └────────────┘
```

---

# 5. Architectural Style

The MVP should use a **modular monolith** architecture.

Do not start with microservices.

Reasons:

- easier Codex development
- simpler deployment
- lower infrastructure cost
- simpler debugging
- easier database consistency
- easier refactoring while domain knowledge evolves

Modules must still maintain clear boundaries so they can be extracted later if necessary.

Preferred pattern:

```text
single application
+
clear module boundaries
+
shared PostgreSQL
+
background jobs
```

rather than:

```text
many independent services
+
message brokers
+
distributed transactions
```

during MVP development.

---

# 6. Repository Architecture

Recommended repository structure:

```text
steel-insight-ai/
│
├── AGENTS.md
├── README.md
├── .env.example
├── docker-compose.yml
│
├── docs/
│   ├── architecture.md
│   ├── data-model.md
│   ├── intelligence.md
│   ├── decisions.md
│   └── progress.md
│
├── tasks/
│   ├── phase-01-foundation.md
│   ├── phase-02-collection.md
│   ├── phase-03-intelligence.md
│   ├── phase-04-product-brain.md
│   └── phase-05-delivery.md
│
├── frontend/
│
├── backend/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   └── prompts/
│
├── collectors/
│   ├── base/
│   ├── dart/
│   ├── naver/
│   ├── rss/
│   ├── steel_media/
│   └── competitors/
│
├── intelligence/
│   ├── entity/
│   ├── event_engine/
│   ├── strategy_engine/
│   ├── steel_demand/
│   ├── product_matching/
│   ├── competitor_engine/
│   ├── opportunity_engine/
│   └── persona/
│
├── knowledge/
│   ├── posco/
│   └── taxonomy/
│
├── notifications/
│   └── telegram/
│
├── scripts/
│
└── tests/
```

---

# 7. Layer Responsibilities

## 7.1 Collection Layer

Location:

```text
collectors/
```

Responsibilities:

- communicate with external sources
- retrieve data
- parse provider-specific formats
- normalize provider responses
- handle rate limits
- handle temporary source failure
- produce normalized source objects

The collection layer must not perform business intelligence.

It must not:

- recommend POSCO products
- infer marketing opportunities
- calculate Opportunity Scores
- generate executive summaries

---

# 8. Provider Adapter Architecture

Every external source should be implemented through a provider abstraction.

Conceptual structure:

```python
class SourceProvider:
    async def fetch(self, request):
        ...
```

Provider-specific implementations may include:

```text
DartProvider
NaverNewsProvider
RSSProvider
SteelMediaProvider
CompetitorNewsProvider
```

The application should not depend directly on provider response structures.

Preferred flow:

```text
External API
↓
Provider Adapter
↓
RawSourceItem
↓
Normalizer
↓
SourceDocument
```

This allows providers to be changed without modifying downstream intelligence logic.

---

# 9. Source Collection Priority

Use external data access in the following priority:

```text
1. Official API
2. Official RSS
3. Official feed
4. Search API
5. Normal HTTP access
6. Browser automation
```

Browser automation must be treated as a last resort.

The architecture should support provider replacement.

For example:

```text
NewsProvider
```

should not be tightly coupled to a single vendor.

---

# 10. Source Normalization Layer

All external information must be converted into a common internal representation before AI analysis.

Conceptual normalized object:

```text
SourceDocument

id
provider
source_type
title
body
summary
url
published_at
collected_at
language
company_mentions
industry_mentions
content_hash
raw_metadata
```

Downstream intelligence modules should operate primarily on this normalized structure.

---

# 11. Deduplication Architecture

News collection will frequently produce multiple articles describing the same event.

Two types of duplication should be distinguished.

## Document Duplication

Examples:

```text
same URL
same syndicated article
same article retrieved multiple times
```

Initial detection:

```text
normalized URL
content hash
title similarity
```

## Event Duplication

Different articles may describe one underlying event.

Example:

```text
Article A
"Company announces EV factory investment"

Article B
"Company invests 5 trillion won in EV manufacturing"

Article C
"New EV plant expected to begin production in 2028"
```

These may belong to one event cluster.

Event clustering should occur after normalization.

Do not use expensive AI processing when deterministic duplicate detection is sufficient.

---

# 12. Persistence Architecture

PostgreSQL is the primary system of record.

Conceptually, information should be stored in stages:

```text
SOURCE
↓
EVENT
↓
INSIGHT
↓
OPPORTUNITY
```

Raw evidence and AI-derived intelligence must remain separated.

A SourceDocument represents collected evidence.

An Event represents a structured real-world occurrence.

An Insight represents analytical interpretation.

An Opportunity represents a possible steel marketing action.

Do not collapse these concepts into a single table.

Detailed schema definitions belong in:

```text
docs/data-model.md
```

---

# 13. Intelligence Architecture

The intelligence pipeline transforms source evidence into structured domain intelligence.

Recommended architecture:

```text
SourceDocument
      ↓
Entity Extraction
      ↓
Event Extraction
      ↓
Event Classification
      ↓
Company Strategy Analysis
      ↓
Industry Implication
      ↓
Steel Demand Analysis
```

Each stage should produce structured output.

Each stage should be testable independently.

---

# 14. Entity Extraction

The entity layer detects meaningful domain entities such as:

```text
company
industry
country
region
technology
product
facility
investment
customer
supplier
application
```

Entity extraction should support company resolution.

Example:

```text
현대자동차
현대차
Hyundai Motor
Hyundai Motor Company
```

should eventually resolve to the same company entity.

Entity resolution should be separated from LLM extraction where practical.

---

# 15. Event Engine

The Event Engine converts source documents into structured events.

Examples:

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
```

The Event Engine must store references to its source evidence.

Conceptual relationship:

```text
SourceDocument
   │
   ├── SourceDocument
   │
   └── SourceDocument
          ↓
        Event
```

One event may therefore reference multiple sources.

---

# 16. Strategy Engine

The Strategy Engine interprets what a structured event may imply about a company's business direction.

Possible strategy dimensions include:

```text
growth
localization
premiumization
cost reduction
electrification
automation
decarbonization
vertical integration
supply-chain resilience
new-market entry
technology leadership
```

The system must explicitly distinguish:

```text
FACT
```

from:

```text
INFERENCE
```

Example:

```text
FACT:
Company announced a new U.S. EV facility.

INFERENCE:
The company appears to be strengthening local EV production.
```

This distinction must be preserved throughout the architecture.

---

# 17. Steel Demand Engine

The Steel Demand Engine translates customer or industry developments into possible steel demand implications.

Required conceptual reasoning chain:

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

Example:

```text
EV production expansion
↓
electric motor production expansion
↓
motor core demand increase
↓
low magnetic loss requirement
↓
electrical steel demand
```

At this stage, the system should reason about steel requirements without yet forcing a specific POSCO product match.

---

# 18. POSCO Product Brain

The POSCO Product Brain is the internal product-knowledge subsystem.

Primary knowledge sources may originate from POSCO product PDFs.

The recommended conversion flow is:

```text
POSCO PDF
↓
Markdown normalization
↓
Product metadata
↓
Industry / Application mapping
↓
Retrieval index
```

The product brain should support retrieval by:

```text
industry
application
component
material requirement
product family
steel grade
technical property
customer benefit
```

---

# 19. POSCO Knowledge Structure

Knowledge should be organized hierarchically.

Example:

```text
knowledge/posco/

index.md

automotive/
    index.md
    products/
    applications/

shipbuilding/
    index.md
    products/
    applications/

energy/
    index.md
    products/
    applications/
```

The top-level index should contain routing metadata rather than full product information.

Example retrieval:

```text
EV event
↓
posco/index.md
↓
automotive/index.md
↓
motor application
↓
electrical steel product
```

The application should not load all POSCO product documents for every request.

---

# 20. Product Retrieval Architecture

Product matching should use progressive retrieval.

Recommended sequence:

```text
industry filter
↓
application filter
↓
component filter
↓
product metadata
↓
vector or semantic retrieval if necessary
↓
LLM evaluation
```

Avoid:

```text
all POSCO documents
↓
LLM
```

This reduces latency, cost, and hallucination risk.

---

# 21. Product Matching Engine

The Product Matching Engine receives:

```text
Steel Demand Hypothesis
+
POSCO Product Knowledge
```

and produces candidate products.

Conceptual input:

```text
industry
application
component
required_properties
steel_category
```

Conceptual output:

```text
product_candidate
product_family
fit_reason
knowledge_source
fit_confidence
```

A product must never be recommended without supporting internal product knowledge.

If a valid match cannot be established:

```text
PRODUCT_MATCH_UNKNOWN
```

should be returned.

---

# 22. Competitor Intelligence Architecture

Competitor information should use the same source/event pipeline where possible.

Competitor-specific analysis may examine:

```text
investment
capacity
new plant
product development
technology
customer partnership
geographic expansion
low-carbon strategy
supply-chain strategy
```

Competitor intelligence should produce structured comparison dimensions rather than vague prose.

Conceptual comparison:

```text
Customer Requirement
        ↓
POSCO Capability
        ↕
Competitor Capability
        ↓
Competitive Position
```

Possible comparison states:

```text
ADVANTAGE
PARITY
DISADVANTAGE
UNKNOWN
```

---

# 23. Opportunity Engine

The Opportunity Engine combines:

```text
Event
+
Company Strategy
+
Steel Demand
+
POSCO Product Match
+
Competitor Context
```

to produce an actionable business opportunity.

Conceptual structure:

```text
Industry Signal
      ↓
Customer Strategy
      ↓
Steel Demand
      ↓
Product Fit
      ↓
Competitive Context
      ↓
Business Opportunity
```

---

# 24. Opportunity Score Architecture

Opportunity Score evaluates business attractiveness.

Default factors:

| Factor | Weight |
|---|---:|
| Industry Impact | 20% |
| Customer Importance | 15% |
| Investment Scale | 15% |
| Steel Demand Impact | 20% |
| POSCO Product Fit | 20% |
| Timing | 10% |

Total:

```text
100%
```

Recommended categories:

```text
90–100  STRATEGIC
80–89   HIGH
70–79   WATCH
0–69    INFORMATION
```

Each component score should remain inspectable.

---

# 25. Confidence Architecture

Confidence must be calculated separately.

Confidence represents the reliability of the analysis.

Possible inputs include:

```text
source reliability
number of independent sources
source agreement
information completeness
recency
inference distance
product knowledge support
```

Example:

```text
Opportunity Score = 94
Confidence Score = 63
```

This means:

```text
high potential impact
but incomplete supporting evidence
```

The two scores must never be merged.

---

# 26. Evidence Architecture

Every major insight should be explainable.

Preferred explanation chain:

```text
Evidence
↓
Observation
↓
Company Strategy
↓
Industry Implication
↓
Steel Demand
↓
Product Match
↓
Opportunity
↓
Action
```

The user interface should eventually allow a user to inspect:

```text
Why was this insight generated?
```

without requiring regeneration from the LLM.

Therefore evidence references and intermediate reasoning should be persisted where practical.

---

# 27. Persona Architecture

The platform supports different user personas.

Initial personas:

```text
EXECUTIVE
MARKETING
ENGINEERING
```

The system must not perform three completely separate analyses.

Preferred architecture:

```text
Core Intelligence Object
        ↓
Persona Renderer
   ┌────┼─────┐
   ↓    ↓     ↓
Exec Marketing Engineer
```

The underlying facts, evidence, scores, and opportunity object remain the same.

Only the presentation emphasis changes.

---

# 28. Executive Presentation

Executive output should prioritize:

```text
major industry change
strategic customer movement
competitive threat
potential business impact
decision required
```

Avoid excessive material-property detail.

---

# 29. Marketing Presentation

Marketing output should prioritize:

```text
customer
investment
timing
market opportunity
steel demand
POSCO product fit
competitor
sales approach
next action
```

---

# 30. Engineering Presentation

Engineering output should prioritize:

```text
application
component
required properties
grade
technical specification
processing
technical gap
competitor material
development requirement
```

---

# 31. Backend Architecture

Recommended backend stack:

```text
FastAPI
Pydantic
SQLAlchemy
Alembic
PostgreSQL
```

Backend responsibilities:

```text
API
business services
repositories
authentication
validation
database access
intelligence orchestration
```

API routes should remain thin.

Preferred flow:

```text
API Route
↓
Service
↓
Repository / Intelligence Module
↓
Database
```

Avoid:

```text
API Route
↓
complex SQL
↓
LLM prompt
↓
external API
```

inside a single route function.

---

# 32. Backend API Structure

Recommended API prefix:

```text
/api/v1
```

Possible future endpoint groups:

```text
/api/v1/health

/api/v1/industries
/api/v1/companies
/api/v1/events
/api/v1/opportunities
/api/v1/competitors
/api/v1/search
/api/v1/insights
/api/v1/watchlists
/api/v1/alerts
```

Detailed endpoint design should be added as implementation progresses.

---

# 33. Frontend Architecture

Recommended frontend stack:

```text
Next.js
TypeScript
Tailwind CSS
shadcn/ui
Recharts
```

The frontend should primarily consume backend APIs.

Do not duplicate intelligence logic in TypeScript.

Primary application areas:

```text
Dashboard
Industry Radar
Companies
Opportunities
Steel Market
Competitor Radar
Ask Steel AI
Reports
Watchlist
Alerts
Settings
```

---

# 34. Dashboard Architecture

The dashboard should prioritize intelligence over raw article volume.

Primary dashboard blocks may include:

```text
TOP Opportunities

Industry Movement

Customer Activity

Competitor Movement

Strategic Alerts

Watchlist Updates
```

Do not make:

```text
number of articles collected
```

the primary dashboard KPI.

---

# 35. Opportunity Card

Opportunity is the main application object shown to users.

Recommended Opportunity Card structure:

```text
Company

Event

Industry

Opportunity Score

Confidence Score

Company Strategy

Steel Demand Implication

POSCO Product Candidate

Competitor Context

Recommended Marketing Action

Recommended Technical Action

Evidence
```

The user should be able to expand the evidence and reasoning chain.

---

# 36. Ask Steel AI Architecture

Ask Steel AI is the conversational query interface.

It should operate on existing structured intelligence whenever possible.

Recommended flow:

```text
User Question
↓
Query Classification
↓
Company / Industry Resolution
↓
Structured Event Retrieval
↓
Opportunity Retrieval
↓
Evidence Retrieval
↓
POSCO Product Retrieval if required
↓
LLM Synthesis
↓
Evidence-Based Response
```

Avoid using general LLM knowledge when verified internal or collected information exists.

---

# 37. Search Types

The conversational interface should eventually support questions such as:

```text
현대자동차의 최근 투자 중 자동차강판 영업기회를 찾아줘.

최근 6개월 조선 3사의 투자전략을 비교해줘.

미국 데이터센터 확대가 철강 수요에 어떤 영향을 줄까?

최근 일본 철강사의 자동차용 강재 전략을 알려줘.

POSCO 제품 중 수소산업 확대와 연결되는 제품을 찾아줘.
```

Search should combine structured filtering and semantic retrieval.

---

# 38. Background Processing Architecture

Data collection and intelligence analysis should run asynchronously from normal user requests.

MVP architecture:

```text
APScheduler
```

Example schedules:

```text
OpenDART collection
News collection
RSS collection
Event processing
Daily brief generation
```

As workload grows, background processing may migrate to:

```text
Celery
+
Redis
```

This transition should not require redesigning core domain logic.

---

# 39. Data Processing States

Long-running intelligence processing should use explicit states.

Conceptual examples:

```text
COLLECTED
NORMALIZED
DUPLICATE
READY_FOR_ANALYSIS
ANALYZED
FAILED
```

Opportunity processing may use:

```text
PENDING
GENERATED
VALIDATED
PUBLISHED
```

Explicit states improve retry logic and observability.

---

# 40. Failure Isolation

Failure of one provider must not stop the entire collection process.

Example:

```text
DART success
NAVER failure
RSS success
```

must still allow successfully collected data to proceed.

Each external provider should have isolated:

```text
timeout
retry
logging
error handling
```

---

# 41. Retry Architecture

Retries should be used for temporary failures such as:

```text
network timeout
rate limiting
temporary server errors
```

Do not retry permanently invalid requests indefinitely.

Retry strategy should use:

```text
limited attempts
backoff
structured logging
```

---

# 42. AI Integration Architecture

LLM calls should be isolated behind dedicated intelligence services.

Do not call LLM APIs directly from:

```text
frontend
API routes
collectors
database models
```

Preferred architecture:

```text
Application Service
↓
Intelligence Service
↓
OpenAI Client
```

This allows:

```text
model changes
prompt changes
mock testing
cost monitoring
fallback logic
```

without rewriting business modules.

---

# 43. Structured AI Output

AI extraction should prefer validated structured outputs.

Preferred flow:

```text
Input Evidence
↓
Prompt
↓
Structured Model Output
↓
Pydantic Validation
↓
Business Rules
↓
Persistence
```

Avoid relying on regular expressions to parse free-form AI answers.

---

# 44. Prompt Architecture

Prompts should be version-controlled separately.

Recommended location:

```text
backend/prompts/
```

or:

```text
intelligence/prompts/
```

Example:

```text
event_extraction.md
company_strategy.md
steel_demand.md
product_matching.md
competitor_analysis.md
opportunity_generation.md
persona_executive.md
persona_marketing.md
persona_engineering.md
```

Prompt text should not become mixed into route handlers.

---

# 45. Cost Optimization Architecture

LLM calls should occur after deterministic filtering.

Preferred processing:

```text
raw collection
↓
URL/hash deduplication
↓
industry filter
↓
company relevance filter
↓
event relevance filter
↓
LLM analysis
```

Avoid:

```text
every collected article
↓
multiple LLM calls
```

without relevance filtering.

---

# 46. AI Call Separation

Different AI responsibilities should remain logically separate.

Examples:

```text
Event Extraction
Strategy Analysis
Steel Demand Analysis
Product Matching
Opportunity Generation
Persona Rendering
```

However, the system should avoid unnecessary calls.

Where appropriate, closely related lightweight operations may share one structured call.

The architectural goal is:

```text
high reliability
+
reasonable token cost
+
testable outputs
```

rather than maximizing the number of agents or calls.

---

# 47. Knowledge Retrieval Architecture

Knowledge retrieval should follow:

```text
Metadata Filter
↓
Taxonomy Filter
↓
Semantic Retrieval
↓
LLM Reasoning
```

Vector retrieval should support retrieval, not replace structured filtering.

Examples of metadata:

```text
industry
application
component
product_family
grade
technology
competitor
```

---

# 48. Vector Database Strategy

Use PostgreSQL with pgvector when semantic retrieval becomes necessary.

Avoid introducing a separate vector database during the MVP unless scale requires it.

Benefits:

```text
one database
simpler operations
relational metadata filtering
vector search together
```

Vector embeddings may be used for:

```text
POSCO product retrieval
article similarity
semantic search
related-event retrieval
```

---

# 49. Telegram Architecture

Telegram is a delivery channel, not part of core intelligence generation.

Recommended architecture:

```text
Opportunity Database
↓
Briefing Service
↓
Persona / Format Renderer
↓
Telegram Adapter
↓
Telegram API
```

The notification module should not independently recalculate opportunities.

---

# 50. Daily Brief

One scheduled Daily Brief should summarize the most relevant intelligence.

Conceptual structure:

```text
TOP Strategic Opportunities

Major Industry Movements

Important Customer Events

Competitor Activity

Watchlist Changes
```

Raw article lists should not dominate the briefing.

---

# 51. Strategic Alerts

Strategic alerts should be rare.

Recommended conceptual condition:

```text
Opportunity Score >= threshold
AND
Confidence Score >= threshold
AND
event is materially new
```

Duplicate alerts must be prevented.

---

# 52. Watchlist Architecture

Users should eventually be able to track:

```text
companies
industries
competitors
technologies
applications
regions
```

Watchlists should affect:

```text
dashboard ranking
search priority
Telegram briefing
alert priority
```

Watchlists should not modify underlying facts or core scoring.

---

# 53. Security Architecture

All external credentials must remain server-side.

Examples:

```text
OPENAI_API_KEY
DART_API_KEY
NAVER_CLIENT_ID
NAVER_CLIENT_SECRET
TELEGRAM_BOT_TOKEN
DATABASE_URL
```

Never expose these credentials through frontend bundles.

Secrets must be provided through environment variables or a future secrets manager.

---

# 54. Environment Architecture

Maintain separate environments:

```text
development
test
production
```

Configuration should be centralized.

Recommended conceptual configuration service:

```text
backend/core/config.py
```

Application code should not directly call:

```text
os.getenv(...)
```

throughout multiple modules.

---

# 55. Logging Architecture

Structured logging should capture:

```text
timestamp
module
provider
operation
status
duration
error
```

For intelligence jobs also record where useful:

```text
model
token usage
processing stage
source count
result ID
```

Never log full secrets.

Avoid logging unnecessary copyrighted full-text content.

---

# 56. Observability

The MVP should at minimum track:

```text
collector success/failure
provider response errors
number of normalized documents
duplicate count
event extraction failures
LLM failures
opportunities generated
Telegram delivery failures
```

Advanced observability may be added later.

---

# 57. Copyright and Content Storage

Where source rights are limited, avoid unnecessary permanent storage of full copyrighted articles.

Prefer storing:

```text
title
source
URL
publication date
permitted excerpt
structured facts
derived intelligence
```

Full-text storage must depend on source rights and collection method.

---

# 58. Scalability Strategy

Scale should occur incrementally.

## MVP

```text
Next.js
FastAPI
PostgreSQL
APScheduler
Docker Compose
```

## Medium Scale

Possible additions:

```text
Redis
Celery
worker processes
pgvector indexing
object storage
```

## Higher Scale

Only when justified:

```text
dedicated ingestion workers
message queues
separate search infrastructure
service extraction
```

Do not introduce these before real workload requires them.

---

# 59. Initial MVP Scope

Initial supported industries:

```text
Automotive
Shipbuilding
Energy
```

Initial company watchlist should remain intentionally limited.

Example scope:

```text
major Korean manufacturers
major global customers
major steel competitors
```

The architecture must allow additional industries without redesigning the entire application.

---

# 60. Phase Mapping

The architecture maps to development phases as follows.

## Phase 1 — Foundation

Build:

```text
frontend
backend
PostgreSQL
Docker
configuration
logging
basic API
```

No AI intelligence yet.

---

## Phase 2 — Collection

Build:

```text
provider interfaces
OpenDART
NAVER
RSS
normalization
deduplication
source storage
scheduler
```

---

## Phase 3 — Intelligence

Build:

```text
entity extraction
event extraction
event classification
strategy analysis
steel demand analysis
```

Do not force POSCO product recommendations yet.

---

## Phase 4 — Product and Opportunity

Build:

```text
POSCO product knowledge
product retrieval
product matching
competitor intelligence
opportunity scoring
confidence scoring
recommended actions
```

---

## Phase 5 — Delivery

Build:

```text
dashboard
company search
industry radar
opportunity UI
Ask Steel AI
watchlist
persona views
Telegram Daily Brief
Strategic Alerts
```

---

# 61. End-to-End MVP Scenario

The architecture must support the following scenario.

```text
1. OpenDART or news source reports a manufacturing-company investment.

2. Collector retrieves the source.

3. Source is normalized into SourceDocument.

4. Duplicate detection confirms whether it is new.

5. Event Engine extracts a structured CAPEX or NEW_FACTORY event.

6. Strategy Engine identifies possible strategic direction.

7. Steel Demand Engine identifies possible steel demand implications.

8. POSCO Product Brain retrieves relevant products.

9. Product Matching evaluates product relevance.

10. Competitor Engine provides related competitive context if available.

11. Opportunity Engine calculates:
    - Opportunity Score
    - Confidence Score
    - recommended actions

12. Opportunity is stored.

13. Dashboard displays the Opportunity Card.

14. User opens evidence to understand why the recommendation exists.

15. High-priority opportunities may appear in the Telegram Daily Brief.
```

This end-to-end path is the primary definition of architectural success.

---

# 62. Architectural Principles

When making future architecture decisions, prioritize:

```text
Evidence before inference

Structure before prose

Retrieval before generation

Deterministic logic before AI where possible

Modular boundaries before microservices

Traceability before impressive wording

Simple infrastructure before premature scale

Product knowledge before product recommendation

Business relevance before article volume
```

---

# 63. Non-Goals for MVP

The following are not required for the initial MVP:

```text
full enterprise CRM integration

real-time millisecond streaming

microservice architecture

Kubernetes

complex multi-agent orchestration

automatic customer email sending

automatic quotation generation

full enterprise ERP integration

fully autonomous sales decision-making
```

The MVP should prove that meaningful steel marketing opportunities can be derived reliably from external industry signals.

---

# 64. Architectural Success Criteria

The architecture is successful when the system can reliably perform:

```text
External Signal
↓
Structured Event
↓
Customer Strategy
↓
Steel Demand
↓
POSCO Product Fit
↓
Marketing Opportunity
↓
Evidence-Based Action
```

while preserving:

- traceability
- modularity
- reasonable AI cost
- explainability
- testability
- security
- future extensibility

The system should evolve from a market-information application into a **steel marketing decision-support platform**, while keeping every major recommendation connected to verifiable evidence.
