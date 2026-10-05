# AGENTS.md

## 1. Project Mission

This repository implements an AI-powered **Steel Market Intelligence Platform**.

The system collects and analyzes manufacturing-industry news, corporate disclosures, investment activity, strategies, technology developments, steel-industry news, and competitor activity.

The final purpose is not news summarization.

The system must convert external industry signals into actionable steel marketing intelligence.

The core intelligence chain is:

```text
SOURCE
→ EVIDENCE
→ EVENT
→ COMPANY STRATEGY
→ INDUSTRY CHANGE
→ STEEL DEMAND
→ POSCO PRODUCT FIT
→ COMPETITIVE POSITION
→ MARKETING OPPORTUNITY
→ RECOMMENDED ACTION
```

The system should help POSCO marketing, executives, and engineers understand:

- what is changing in customer industries
- which companies are investing
- what customers may need in the future
- how those changes may affect steel demand
- which POSCO products may fit those needs
- what competitors are doing
- what marketing or technical actions should be considered


---

# 2. Core Development Principle

Do not build a generic news aggregation application.

Every major feature should contribute to at least one of the following:

1. detect meaningful industry change
2. understand customer strategy
3. estimate steel-demand implications
4. connect demand with POSCO products
5. identify marketing opportunities
6. compare competitor activity
7. provide evidence-based recommendations


---

# 3. Current Development Strategy

Development is divided into five major phases.

```text
PHASE 1
Project Foundation

PHASE 2
Data Collection Pipeline

PHASE 3
Industry Intelligence Engine

PHASE 4
POSCO Product Brain + Opportunity Engine

PHASE 5
Dashboard + Search + Telegram Delivery
```

Only implement the explicitly requested phase.

Never automatically start the next phase.

Each phase has its own task document under:

```text
/tasks/
```

Examples:

```text
/tasks/phase-01-foundation.md
/tasks/phase-02-collection.md
/tasks/phase-03-intelligence.md
/tasks/phase-04-product-brain.md
/tasks/phase-05-delivery.md
```

The active phase task file defines the implementation scope.


---

# 4. Technology Stack

Use the following technologies unless a phase task explicitly changes them.

## Frontend

```text
Next.js
TypeScript
Tailwind CSS
shadcn/ui
Recharts
```

## Backend

```text
Python
FastAPI
Pydantic
SQLAlchemy
Alembic
```

## Database

```text
PostgreSQL
pgvector
```

pgvector should be introduced only when vector retrieval is required.

## AI

Use OpenAI APIs for:

- structured extraction
- classification
- reasoning
- embeddings
- RAG
- final insight generation

Prefer structured outputs over free-form text parsing.

## Data Collection

Preferred libraries:

```text
httpx
feedparser
BeautifulSoup
```

Use Playwright only when necessary.

Do not use browser automation if API, RSS, or normal HTTP access is available.

## Background Jobs

MVP:

```text
APScheduler
```

Scale stage:

```text
Celery
Redis
```

Do not introduce Celery or Redis before required.

## Deployment

Prefer:

```text
Docker
Docker Compose
```

during MVP development.


---

# 5. Repository Architecture

Maintain clear responsibility boundaries.

Recommended structure:

```text
steel-insight-ai/

AGENTS.md
README.md
.env.example

docs/
tasks/

frontend/

backend/
    api/
    models/
    schemas/
    services/
    repositories/

collectors/
    dart/
    news/
    rss/
    steel_media/
    competitors/

intelligence/
    entity/
    classifier/
    event_engine/
    strategy_engine/
    steel_demand/
    product_matching/
    competitor_engine/
    opportunity_engine/
    persona/

knowledge/
    posco/
    taxonomy/

notifications/
    telegram/

scripts/

tests/
```

Do not mix responsibilities between these layers.


---

# 6. Architecture Boundaries

The following rules are mandatory.

## Collectors

Collectors are responsible only for:

```text
fetch
parse
normalize
```

Collectors must not:

- generate marketing insights
- perform POSCO product matching
- calculate opportunity scores
- contain frontend logic


## Intelligence

The intelligence layer is responsible for:

```text
entity extraction
event extraction
event classification
strategy analysis
steel-demand reasoning
product matching
competitor analysis
opportunity analysis
```

Do not put scraping code inside the intelligence layer.


## API

API routes should:

```text
receive request
validate request
call service
return response
```

Do not place complex business logic directly inside API routes.


## Frontend

Frontend should consume backend APIs.

Do not duplicate intelligence logic in the frontend.


## Knowledge

Product knowledge and taxonomy must be stored outside prompts.

Do not hard-code POSCO product knowledge directly inside Python prompt strings.


---

# 7. Context Loading Rules

Repository context must be loaded progressively.

Minimize unnecessary context usage.

Do not recursively scan large directories unless explicitly required.


## Always Read

At the beginning of each development task read:

```text
/AGENTS.md
```

and the current phase file:

```text
/tasks/phase-XX-*.md
```


## Architecture

Read:

```text
/docs/architecture.md
```

only when:

- making architectural decisions
- modifying module relationships
- adding infrastructure
- changing major application flow


## Data Model

Read:

```text
/docs/data-model.md
```

only when working on:

- SQLAlchemy models
- database schemas
- migrations
- persistence
- relationships
- event storage


## Intelligence

Read:

```text
/docs/intelligence.md
```

only when implementing:

- event extraction
- company strategy analysis
- steel-demand reasoning
- product matching
- opportunity generation
- competitor analysis


---

# 8. POSCO Knowledge Loading Rules

Never recursively read the entire directory:

```text
/knowledge/posco/
```

Always begin with:

```text
/knowledge/posco/index.md
```

The index file determines which product knowledge documents are relevant.

Expected retrieval sequence:

```text
Industry Event
↓
knowledge/posco/index.md
↓
Industry Index
↓
Application
↓
Relevant Product File
```

Example:

```text
EV investment
↓
posco/index.md
↓
automotive/index.md
↓
electric-motor application
↓
relevant electrical-steel product document
```

Load only product files required for the current task.

Do not read unrelated industries.


---

# 9. Taxonomy Loading Rules

Taxonomy files are located under:

```text
/knowledge/taxonomy/
```

Possible files include:

```text
industries.md
events.md
strategies.md
applications.md
materials.md
competitors.md
```

Load only the taxonomy required by the current task.

Examples:

## Event Classification

Read:

```text
industries.md
events.md
```

## Strategy Analysis

Read:

```text
strategies.md
```

## Product Matching

Read:

```text
applications.md
materials.md
```

Do not load all taxonomy documents by default.


---

# 10. Source Code Context Rules

When investigating existing code, inspect the smallest possible scope.

Use:

```text
exact symbol
→ exact file
→ relevant module
→ package
```

Avoid reading entire folders without a reason.

Search for:

- function names
- class names
- routes
- model names
- schema names
- table names

before opening large source files.

Once enough context exists to complete the task, stop loading additional files.


---

# 11. Data Source Principles

Primary sources may include:

```text
OpenDART
NAVER News/API
RSS feeds
steel-industry media
industry associations
corporate IR
corporate newsrooms
government releases
competitor newsrooms
```

Use provider abstraction.

External providers must not be tightly coupled with intelligence logic.

Preferred architecture:

```text
Provider
↓
RawSourceItem
↓
Normalizer
↓
SourceDocument
↓
Database
```


---

# 12. Provider Independence

Implement generic provider interfaces.

Example concept:

```python
class SourceProvider:
    async def fetch(self, ...):
        ...
```

Provider-specific logic should remain inside the provider module.

Examples:

```text
DartProvider
NaverNewsProvider
RSSProvider
```

The intelligence layer should operate on normalized data rather than provider-specific responses.

This is especially important because external APIs may change.


---

# 13. Source Normalization

Collected information should eventually normalize to a common source model.

Recommended fields:

```text
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

Do not store external API response structures directly as application-domain objects.


---

# 14. Source Reliability

Information reliability should be considered when generating intelligence.

Recommended conceptual hierarchy:

```text
Tier 1
official disclosure
government
company IR
company official announcement

Tier 2
industry association
specialized industry publication

Tier 3
major economic or general news

Tier 4
secondary or weak sources
```

Official information should receive higher confidence than secondary reporting.


---

# 15. Fact and Inference Separation

Facts and AI inference must never be mixed.

Example:

FACT:

```text
A company announced construction of a new EV factory.
```

INFERENCE:

```text
The company may be strengthening regional EV production localization.
```

The database and AI output structures should make this distinction explicit.

Never store an AI hypothesis as an observed fact.


---

# 16. Evidence First

Every strategic insight must remain traceable to evidence.

Preferred chain:

```text
Evidence
↓
Observation
↓
Industry Implication
↓
Customer Strategy
↓
Steel Implication
↓
POSCO Opportunity
↓
Recommended Action
```

No evidence means no high-confidence strategic conclusion.

Whenever possible retain:

```text
source_id
source_url
published_at
evidence_text
```

or an equivalent reference.


---

# 17. Event Intelligence

Raw articles should not directly become recommendations.

Preferred pipeline:

```text
SourceDocument
↓
Entity Extraction
↓
Event Extraction
↓
Event Classification
↓
Company Strategy
↓
Steel Demand
```

Typical event categories include:

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

Use the official project taxonomy rather than inventing categories during execution.


---

# 18. Steel Demand Reasoning

Never jump directly from a news article to a POSCO product.

Use this reasoning chain:

```text
Industry Change
↓
Application Change
↓
Component Change
↓
Required Material Properties
↓
Steel Product Category
↓
POSCO Product Candidate
```

Example:

```text
EV production expansion
↓
higher EV motor production
↓
drive motor demand
↓
lower magnetic loss requirement
↓
electrical steel
↓
relevant POSCO product
```

This intermediate reasoning must remain explainable.


---

# 19. POSCO Product Matching

Specific POSCO products can only be recommended when supported by the internal POSCO knowledge base.

Never invent:

- product names
- grades
- dimensions
- mechanical properties
- performance claims
- certifications

If product evidence is insufficient, return an unknown state such as:

```text
PRODUCT_MATCH_UNKNOWN
```

rather than guessing.


---

# 20. Competitor Intelligence

Competitor intelligence should examine dimensions such as:

```text
investment
capacity
geography
technology
product
application
customer partnership
decarbonization
supply chain
commercialization
```

When comparing POSCO with another steel producer, use explicit comparison criteria.

Permitted states include:

```text
ADVANTAGE
PARITY
DISADVANTAGE
UNKNOWN
```

Do not state that POSCO is stronger or weaker without supporting evidence.


---

# 21. Opportunity Score

Opportunity Score represents business attractiveness.

It is not an AI confidence score.

Default weighting:

```text
Industry Impact       20%
Customer Importance   15%
Investment Scale      15%
Steel Demand Impact   20%
POSCO Product Fit     20%
Timing                 10%
```

Total:

```text
100
```

Keep individual component scores available for inspection.

Suggested classifications:

```text
90–100  STRATEGIC
80–89   HIGH
70–79   WATCH
0–69    INFORMATION
```


---

# 22. Confidence Score

Confidence measures reliability of the conclusion.

It must be calculated separately from Opportunity Score.

Possible factors include:

```text
source reliability
independent source count
information consistency
data completeness
recency
inference distance
```

Example:

```text
Opportunity Score: 95
Confidence Score: 62
```

This means:

```text
potentially important opportunity
but incomplete evidence
```

Never combine these two scores into one.


---

# 23. Persona Rules

The system supports multiple information consumers.

Use the same underlying intelligence object.

Do not run independent core analyses for each persona.

Only presentation and emphasis should change.


## EXECUTIVE

Prioritize:

```text
industry structural change
strategic customer movement
market impact
competitive threat
decision required
```

Keep technical details concise.


## MARKETING

Prioritize:

```text
customer
investment
timing
steel demand
POSCO product
competitor
sales opportunity
next action
```


## ENGINEERING

Prioritize:

```text
application
component
material property
steel grade
processing
technical requirement
technical risk
competitor material
development need
```


---

# 24. Telegram Rules

Telegram should deliver intelligence, not raw news.

Primary outputs:

```text
Daily Brief
Strategic Alert
```

Daily Brief may include:

```text
TOP opportunities
major industry changes
important customer movements
competitor movements
watchlist updates
```

Do not send every collected article.

Urgent alerts should require both high importance and sufficient confidence.

Example:

```text
Opportunity Score >= 90
AND
Confidence >= configured threshold
AND
event is materially new
```

Prevent duplicate alerts for the same event.


---

# 25. AI Output Rules

Prefer structured outputs using Pydantic or equivalent schemas.

Avoid:

```text
LLM free-form output
↓
regex parsing
```

Prefer:

```text
schema
↓
structured AI output
↓
validation
↓
database
```

All score values must be validated.

All taxonomy values must be validated.

Unknown values should fail safely or map to defined fallback states.


---

# 26. Prompt Management

Do not embed large prompts directly inside API routes or controllers.

Store prompts in dedicated locations such as:

```text
backend/prompts/
```

or:

```text
intelligence/prompts/
```

Prompts should be:

- versionable
- testable
- reusable
- separated by purpose

Example:

```text
event_extraction.md
strategy_analysis.md
steel_demand.md
product_matching.md
opportunity_generation.md
```


---

# 27. Security Rules

All secrets must come from environment variables.

Never commit:

```text
.env
API keys
tokens
passwords
private credentials
```

Maintain:

```text
.env.example
```

Expected future environment variables may include:

```text
OPENAI_API_KEY
DART_API_KEY
NAVER_CLIENT_ID
NAVER_CLIENT_SECRET
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
DATABASE_URL
REDIS_URL
```

Never log full secrets.


---

# 28. External Content Rules

Prefer data access methods in this order:

```text
1. Official API
2. RSS
3. Official feed
4. Search API
5. permitted HTTP access
6. crawling
```

Do not use scraping when a reliable API or RSS source exists.

Respect:

- robots policies
- terms of service
- copyright restrictions
- rate limits

Do not build a system that republishes full copyrighted articles without appropriate rights.

Prefer storing and analyzing:

```text
metadata
title
URL
permitted excerpts
structured facts
derived intelligence
```

where appropriate.


---

# 29. Duplicate Detection

Avoid using expensive AI calls for simple duplicate detection.

Start with deterministic approaches such as:

```text
normalized URL
content hash
title similarity
```

Semantic duplicate detection may be added later when needed.

Articles describing the same underlying event should eventually be grouped into an event cluster.


---

# 30. Cost Control Principles

Minimize unnecessary LLM calls.

Before calling an LLM consider whether the task can be completed using:

```text
normal code
rules
database query
hashing
metadata filtering
taxonomy lookup
```

Use AI only where reasoning, extraction, classification, or synthesis provides meaningful value.

Do not send entire documents when relevant sections can be retrieved first.

Use retrieval before generation.


---

# 31. Knowledge Retrieval Principle

Use:

```text
metadata filtering
↓
keyword/taxonomy filtering
↓
vector retrieval if necessary
↓
LLM reasoning
```

rather than sending the entire knowledge base to an LLM.

Prefer smaller, relevant context over large context.


---

# 32. Database Principles

Keep raw evidence and derived intelligence separate.

Conceptually:

```text
SOURCE
↓
EVENT
↓
INSIGHT
↓
OPPORTUNITY
```

Do not store all stages inside a single table.

Derived AI results must retain references to their source evidence.


---

# 33. Testing Rules

New functionality must include appropriate tests.

Important test areas include:

```text
collector parsing
normalization
deduplication
event schema validation
taxonomy validation
fact/inference separation
evidence references
score calculation
confidence calculation
product retrieval
unsupported product rejection
persona formatting
API behavior
```

External HTTP calls should be mocked in unit tests.


---

# 34. Validation Before Completion

Before considering a task complete verify:

```text
implementation works
types validate
schemas validate
database migration works if changed
errors are handled
logging exists
tests pass
secrets are not exposed
evidence traceability is maintained
```

Do not report completion while relevant tests are failing.


---

# 35. Scope Control

Do not make unrelated improvements.

Do not perform broad refactoring unless required by the current task.

If the current task concerns:

```text
event extraction
```

do not redesign:

```text
frontend
Telegram
authentication
product knowledge
```

unless the task explicitly requires it.

Prefer narrow, verifiable changes.


---

# 36. File Modification Rules

Before editing code:

1. identify the active phase
2. identify relevant modules
3. inspect the smallest required code scope
4. modify only necessary files
5. run relevant tests

Avoid formatting or rewriting unrelated files.


---

# 37. Documentation Rules

Use:

```text
/docs/progress.md
```

to record completed development work.

After each meaningful phase or task record:

```text
date
phase
completed work
important files changed
tests executed
known problems
next recommended task
```

Update architecture documents only when architecture actually changes.

Do not rewrite documentation simply because wording can be improved.


---

# 38. Decision Log

Important architectural decisions should be recorded in:

```text
/docs/decisions.md
```

Examples:

```text
changing data provider
changing database technology
introducing Redis
changing event taxonomy structure
changing product knowledge architecture
changing AI model strategy
```

Avoid undocumented architectural changes.


---

# 39. Progress Reporting

When finishing a Codex task provide a concise summary containing:

```text
Implemented
Files changed
Tests performed
Known limitations
Next recommended step
```

Do not automatically perform the recommended next step.


---

# 40. Failure Handling

When an implementation cannot be completed:

Do not hide the failure.

Report:

```text
what failed
why it failed
what was successfully completed
what remains
```

Prefer partial working implementation over speculative large rewrites.


---

# 41. MVP Priority

The first important end-to-end workflow is:

```text
OpenDART / News / RSS
↓
Normalized Source
↓
Event
↓
Company Strategy
↓
Steel Demand
↓
POSCO Product
↓
Opportunity
↓
Evidence
↓
Dashboard
```

Prioritize making this chain reliable before expanding the number of features or industries.


---

# 42. Initial Industry Scope

For the MVP, prioritize:

```text
Automotive
Shipbuilding
Energy
```

Do not unnecessarily expand into all manufacturing industries during early development.

The architecture should support expansion later without major redesign.


---

# 43. Design Philosophy

When choosing between:

```text
complex but theoretically scalable
```

and

```text
simple, testable, extensible
```

prefer the second option during MVP development.

Avoid premature optimization.

Avoid premature microservices.

Avoid infrastructure that does not solve a current problem.


---

# 44. Definition of Done

A task is complete only when:

- requirements from the active phase task are implemented
- relevant tests pass
- no obvious security issue exists
- no secrets are committed
- structured schemas validate
- source traceability is preserved
- documentation is updated where required
- unrelated modules were not unnecessarily modified

Then stop.

Do not begin the next development phase unless explicitly instructed.
