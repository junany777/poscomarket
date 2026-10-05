# Industry Taxonomy

## 1. Purpose

This document defines the standard industry taxonomy used by the Steel Market Intelligence Platform.

The taxonomy is used for:

- source classification
- company classification
- event classification
- industry trend analysis
- steel-demand reasoning
- POSCO product retrieval
- opportunity scoring
- dashboard filtering
- Ask Steel AI search

All internal industry classification should use the canonical industry codes defined in this document.

Do not create new industry codes dynamically during normal analysis.

If no valid category exists, use:

```text
OTHER
```

or:

```text
UNKNOWN
```

and flag the item for taxonomy review.

---

# 2. Taxonomy Principles

Industry classification should follow these principles:

```text
Canonical code before free-form label

Primary industry before secondary activity

Customer industry before steel product category

Business activity before company ownership group

Stable taxonomy before ad-hoc LLM labels
```

Example:

```text
Hyundai Motor Company
→ AUTOMOTIVE

HD Hyundai Heavy Industries
→ SHIPBUILDING

Samsung Electronics semiconductor fab investment
→ SEMICONDUCTOR

POSCO electrical-steel development
→ STEEL
```

---

# 3. Industry Hierarchy

The platform should support:

```text
LEVEL 1
Major Industry

LEVEL 2
Subindustry

LEVEL 3
Application / Market Segment
```

This file primarily defines Level 1 and Level 2.

Detailed applications should be maintained separately in:

```text
knowledge/taxonomy/applications.md
```

---

# 4. MVP Priority Industries

Initial MVP priority:

```text
AUTOMOTIVE
SHIPBUILDING
ENERGY
```

These industries should receive the deepest intelligence processing during early development.

Other industries should remain supported structurally but may have lower initial coverage.

---

# 5. Canonical Level 1 Industries

## 5.1 AUTOMOTIVE

Canonical code:

```text
AUTOMOTIVE
```

Korean name:

```text
자동차
```

English name:

```text
Automotive
```

Description:

Companies and value chains related to passenger vehicles, commercial vehicles, electric vehicles, vehicle components, and mobility manufacturing.

Typical subindustries:

```text
PASSENGER_VEHICLE
COMMERCIAL_VEHICLE
EV
HYBRID
AUTOMOTIVE_PARTS
MOBILITY
SPECIAL_PURPOSE_VEHICLE
```

Representative companies:

```text
Hyundai Motor
Kia
Toyota
Volkswagen
GM
Ford
Tesla
BYD
```

Important steel demand areas:

```text
automotive sheet
advanced high-strength steel
electrical steel
galvanized steel
stainless steel
battery-case material
motor-core material
chassis material
```

High-value event keywords:

```text
EV factory
vehicle production
capacity expansion
localization
motor
battery case
body-in-white
lightweight
autonomous driving
mobility
```

---

# 5.2 SHIPBUILDING

Canonical code:

```text
SHIPBUILDING
```

Korean name:

```text
조선
```

English name:

```text
Shipbuilding
```

Description:

Construction and maintenance of commercial vessels, naval vessels, offshore structures, LNG carriers, and related marine systems.

Typical subindustries:

```text
COMMERCIAL_SHIP
LNG_CARRIER
CONTAINER_SHIP
TANKER
NAVAL_SHIP
OFFSHORE
MARINE_EQUIPMENT
```

Representative companies:

```text
HD Hyundai Heavy Industries
Hanwha Ocean
Samsung Heavy Industries
Mitsubishi Heavy Industries
CSSC
```

Important steel demand areas:

```text
thick plate
shipbuilding plate
cryogenic steel
stainless steel
high-strength plate
offshore structural steel
```

High-value event keywords:

```text
vessel order
LNG carrier
shipyard
dock expansion
offshore
FPSO
naval vessel
green ship
methanol
ammonia
hydrogen ship
```

---

# 5.3 ENERGY

Canonical code:

```text
ENERGY
```

Korean name:

```text
에너지
```

English name:

```text
Energy
```

Description:

Power generation, energy infrastructure, renewable energy, oil and gas, nuclear energy, and emerging energy systems.

Typical subindustries:

```text
POWER_GENERATION
RENEWABLE_ENERGY
OIL_GAS
NUCLEAR
HYDROGEN
WIND
SOLAR
ENERGY_INFRASTRUCTURE
```

Important steel demand areas:

```text
thick plate
pipeline steel
pressure-vessel steel
wind-tower steel
electrical steel
stainless steel
corrosion-resistant steel
```

High-value event keywords:

```text
power plant
wind farm
offshore wind
hydrogen
nuclear
pipeline
LNG
gas infrastructure
renewable
energy transition
```

---

# 5.4 BATTERY

Canonical code:

```text
BATTERY
```

Korean name:

```text
배터리
```

English name:

```text
Battery
```

Description:

Secondary battery manufacturing, battery materials, battery modules, packs, recycling, and battery manufacturing equipment.

Typical subindustries:

```text
EV_BATTERY
ESS_BATTERY
BATTERY_CELL
BATTERY_MODULE
BATTERY_PACK
BATTERY_MATERIAL
BATTERY_RECYCLING
```

Representative companies:

```text
LG Energy Solution
Samsung SDI
SK On
CATL
Panasonic Energy
```

Potential steel demand:

```text
battery case material
stainless steel
high-strength sheet
nickel-related stainless applications
facility structural steel
```

Keywords:

```text
gigafactory
battery plant
cell production
battery pack
ESS
recycling
solid-state battery
```

---

# 5.5 SEMICONDUCTOR

Canonical code:

```text
SEMICONDUCTOR
```

Korean name:

```text
반도체
```

English name:

```text
Semiconductor
```

Description:

Semiconductor manufacturing, foundry, memory, semiconductor equipment, fabs, and related infrastructure.

Typical subindustries:

```text
MEMORY
FOUNDRY
LOGIC
SEMICONDUCTOR_EQUIPMENT
SEMICONDUCTOR_MATERIAL
FAB_INFRASTRUCTURE
```

Representative companies:

```text
Samsung Electronics
SK hynix
TSMC
Intel
Micron
```

Potential steel demand:

```text
stainless steel
clean piping
high-purity process equipment
facility structural steel
electrical infrastructure steel
```

Keywords:

```text
fab
cleanroom
semiconductor plant
EUV
HBM
foundry
memory expansion
```

---

# 5.6 CONSTRUCTION

Canonical code:

```text
CONSTRUCTION
```

Korean name:

```text
건설
```

English name:

```text
Construction
```

Description:

Residential, commercial, industrial, infrastructure, civil engineering, and large-scale development projects.

Typical subindustries:

```text
RESIDENTIAL
COMMERCIAL
INFRASTRUCTURE
CIVIL
INDUSTRIAL_FACILITY
MODULAR_CONSTRUCTION
```

Steel demand areas:

```text
rebar
structural steel
H-beam
steel plate
coated steel
stainless
```

Keywords:

```text
construction order
infrastructure
bridge
building
data center
industrial complex
modular
```

---

# 5.7 MACHINERY

Canonical code:

```text
MACHINERY
```

Korean name:

```text
기계
```

English name:

```text
Machinery
```

Description:

Industrial machinery, manufacturing equipment, machine tools, heavy equipment, and production systems.

Typical subindustries:

```text
INDUSTRIAL_MACHINERY
HEAVY_EQUIPMENT
MACHINE_TOOL
MANUFACTURING_EQUIPMENT
AGRICULTURAL_MACHINERY
```

Steel demand areas:

```text
high-strength steel
wear-resistant steel
specialty steel
plate
bar
stainless
```

---

# 5.8 HOME_APPLIANCE

Canonical code:

```text
HOME_APPLIANCE
```

Korean name:

```text
가전
```

English name:

```text
Home Appliance
```

Description:

Consumer and commercial appliances such as refrigerators, washing machines, air conditioners, and kitchen appliances.

Typical subindustries:

```text
REFRIGERATION
WASHING
HVAC
KITCHEN_APPLIANCE
COMMERCIAL_APPLIANCE
```

Steel demand areas:

```text
coated steel
stainless steel
electrical steel
pre-painted steel
sheet steel
```

---

# 5.9 DEFENSE

Canonical code:

```text
DEFENSE
```

Korean name:

```text
방산
```

English name:

```text
Defense
```

Description:

Military vehicles, naval systems, weapon systems, armored systems, defense electronics, and ammunition-related manufacturing.

Typical subindustries:

```text
ARMORED_VEHICLE
MILITARY_SHIP
MISSILE_SYSTEM
DEFENSE_ELECTRONICS
ARTILLERY
```

Steel demand areas:

```text
armor plate
high-strength steel
special plate
specialty alloy steel
naval steel
```

Keywords:

```text
defense contract
tank
armored vehicle
naval ship
artillery
missile
military production
```

---

# 5.10 AEROSPACE

Canonical code:

```text
AEROSPACE
```

Korean name:

```text
항공우주
```

English name:

```text
Aerospace
```

Description:

Aircraft, spacecraft, launch vehicles, satellites, aerospace components, and related manufacturing.

Typical subindustries:

```text
AIRCRAFT
SPACE
SATELLITE
LAUNCH_VEHICLE
AEROSPACE_COMPONENT
```

Steel demand relevance:

```text
specialty stainless
high-strength specialty steel
heat-resistant alloys
ground infrastructure
```

---

# 5.11 ROBOTICS

Canonical code:

```text
ROBOTICS
```

Korean name:

```text
로봇
```

English name:

```text
Robotics
```

Description:

Industrial robots, service robots, humanoid robots, logistics robots, and robotic components.

Typical subindustries:

```text
INDUSTRIAL_ROBOT
HUMANOID
LOGISTICS_ROBOT
SERVICE_ROBOT
ROBOT_COMPONENT
```

Potential steel demand:

```text
electrical steel
high-strength sheet
precision stainless
motor materials
```

Keywords:

```text
humanoid
industrial robot
automation
servo motor
robot factory
```

---

# 5.12 DATA_CENTER

Canonical code:

```text
DATA_CENTER
```

Korean name:

```text
데이터센터
```

English name:

```text
Data Center
```

Description:

Hyperscale data centers, AI data centers, cloud infrastructure, server facilities, and supporting electrical and cooling infrastructure.

Typical subindustries:

```text
HYPERSCALE
AI_DATA_CENTER
CLOUD_DATA_CENTER
EDGE_DATA_CENTER
```

Potential steel demand:

```text
structural steel
electrical steel
transformer material
stainless piping
cooling infrastructure
```

Keywords:

```text
AI data center
hyperscale
GPU cluster
cloud infrastructure
server facility
power demand
transformer
```

---

# 5.13 HYDROGEN

Canonical code:

```text
HYDROGEN
```

Korean name:

```text
수소
```

English name:

```text
Hydrogen
```

Description:

Hydrogen production, transport, storage, utilization, fuel cells, and hydrogen infrastructure.

Typical subindustries:

```text
GREEN_HYDROGEN
BLUE_HYDROGEN
HYDROGEN_STORAGE
HYDROGEN_PIPELINE
FUEL_CELL
HYDROGEN_TRANSPORT
```

Potential steel demand:

```text
hydrogen-resistant steel
pipeline steel
pressure-vessel steel
stainless steel
cryogenic steel
```

Note:

HYDROGEN may be used as:

```text
Level 1 industry
```

when the user explicitly analyzes the hydrogen ecosystem.

For broader energy analysis, it may also be represented as:

```text
ENERGY / HYDROGEN
```

The application should avoid double counting.

---

# 5.14 RENEWABLE_ENERGY

Canonical code:

```text
RENEWABLE_ENERGY
```

Korean name:

```text
재생에너지
```

English name:

```text
Renewable Energy
```

Description:

Wind, solar, tidal, geothermal, and other renewable-power industries.

Typical subindustries:

```text
WIND
OFFSHORE_WIND
SOLAR
TIDAL
GEOTHERMAL
```

Potential steel demand:

```text
wind tower plate
offshore structural steel
corrosion-resistant steel
electrical infrastructure steel
```

Note:

For broad analysis this may be classified under:

```text
ENERGY
```

For renewable-specific dashboards, this canonical code may be used.

Implementation should support parent-child industry relationships.

---

# 5.15 STEEL

Canonical code:

```text
STEEL
```

Korean name:

```text
철강
```

English name:

```text
Steel
```

Description:

Integrated steelmakers, electric-arc-furnace producers, specialty steel companies, rolling operations, and major steel processors.

Typical subindustries:

```text
INTEGRATED_STEEL
EAF
SPECIALTY_STEEL
STAINLESS
STEEL_PROCESSING
STEEL_SERVICE_CENTER
```

Representative companies:

```text
POSCO
Hyundai Steel
Nippon Steel
JFE Steel
ArcelorMittal
Baowu
Nucor
SSAB
Tata Steel
```

This category is especially important for competitor intelligence.

Typical event topics:

```text
capacity
blast furnace
EAF
low-carbon steel
new product
price
joint venture
customer partnership
raw material
green steel
```

---

# 5.16 CHEMICAL

Canonical code:

```text
CHEMICAL
```

Korean name:

```text
화학
```

English name:

```text
Chemical
```

Description:

Petrochemical, specialty chemicals, industrial gases, and chemical-process manufacturing.

Typical subindustries:

```text
PETROCHEMICAL
SPECIALTY_CHEMICAL
INDUSTRIAL_GAS
CHEMICAL_PROCESSING
```

Potential steel demand:

```text
stainless steel
corrosion-resistant steel
pressure-vessel steel
pipeline
plant structural steel
```

---

# 5.17 PETROCHEMICAL

Canonical code:

```text
PETROCHEMICAL
```

Korean name:

```text
석유화학
```

English name:

```text
Petrochemical
```

This may be modeled as a child of:

```text
CHEMICAL
```

or as an explicit industry when detailed analysis is needed.

High-value events:

```text
cracker investment
plant shutdown
capacity reduction
new complex
feedstock change
```

---

# 5.18 LOGISTICS

Canonical code:

```text
LOGISTICS
```

Korean name:

```text
물류
```

English name:

```text
Logistics
```

Description:

Ports, warehouses, logistics automation, shipping logistics, and distribution infrastructure.

Potential steel demand:

```text
structural steel
warehouse structures
automation equipment
container-related steel
```

---

# 5.19 RAILWAY

Canonical code:

```text
RAILWAY
```

Korean name:

```text
철도
```

English name:

```text
Railway
```

Description:

Rail vehicles, rail infrastructure, high-speed rail, metro, and railway equipment.

Steel demand areas:

```text
rail steel
stainless
structural steel
high-strength sheet
electrical steel
```

---

# 5.20 OTHER

Canonical code:

```text
OTHER
```

Use when:

```text
the industry is known
but no current canonical taxonomy applies
```

Do not automatically create a new code.

Log taxonomy-review candidates.

---

# 5.21 UNKNOWN

Canonical code:

```text
UNKNOWN
```

Use when:

```text
industry cannot be reliably determined
```

This is preferable to an unsupported classification.

---

# 6. Industry Parent-Child Relationships

Recommended hierarchy examples:

```text
ENERGY
├── RENEWABLE_ENERGY
│   ├── WIND
│   └── SOLAR
├── HYDROGEN
├── NUCLEAR
└── OIL_GAS
```

```text
AUTOMOTIVE
├── EV
├── HYBRID
├── COMMERCIAL_VEHICLE
└── AUTOMOTIVE_PARTS
```

```text
STEEL
├── INTEGRATED_STEEL
├── EAF
├── STAINLESS
└── SPECIALTY_STEEL
```

The database may represent these through:

```text
industries.parent_id
```

---

# 7. Primary vs Secondary Industry

A company may belong to multiple industries.

Example:

```text
Company:
battery manufacturer

PRIMARY:
BATTERY

SECONDARY:
AUTOMOTIVE
ENERGY
```

Use:

```text
company_industries.relationship_type
```

to distinguish them.

Do not assign several primary industries without strong reason.

---

# 8. Event Industry Classification

The industry of an event may differ from the primary industry of the company.

Example:

```text
Samsung Electronics
primary company industry:
SEMICONDUCTOR
```

Event:

```text
Samsung Electronics invests in an AI data center.
```

Possible event industry:

```text
DATA_CENTER
```

while preserving company industry:

```text
SEMICONDUCTOR
```

This distinction is important.

---

# 9. Cross-Industry Events

Some events span several industries.

Example:

```text
Automaker + battery company joint venture
```

Possible classification:

```text
primary_industry:
AUTOMOTIVE

secondary_industries:
BATTERY
```

The system should choose one primary event industry and preserve additional industry relationships separately.

---

# 10. Industry Classification Rules

Use the following order:

```text
1. Explicit business context in source

2. Event subject

3. Company primary industry

4. Known taxonomy mapping

5. AI inference

6. UNKNOWN
```

Explicit source context should take priority over assumptions.

---

# 11. Industry Confidence

Industry classification should include confidence where generated by AI.

Recommended:

```text
90-100
explicit and unambiguous

75-89
strong contextual evidence

60-74
reasonable inference

below 60
prefer UNKNOWN or manual review
```

---

# 12. Keyword Usage

Keywords may support classification but must not be treated as absolute rules.

Example:

```text
"motor"
```

could relate to:

```text
AUTOMOTIVE
ROBOTICS
HOME_APPLIANCE
MACHINERY
```

Use surrounding context and company information.

---

# 13. Steel Demand Relevance

Industries may be assigned a default steel-demand relevance for filtering purposes.

Suggested conceptual levels:

```text
VERY_HIGH
HIGH
MEDIUM
LOW
UNKNOWN
```

Initial examples:

| Industry | Steel Demand Relevance |
|---|---|
| AUTOMOTIVE | VERY_HIGH |
| SHIPBUILDING | VERY_HIGH |
| ENERGY | VERY_HIGH |
| CONSTRUCTION | VERY_HIGH |
| MACHINERY | HIGH |
| DEFENSE | HIGH |
| RAILWAY | HIGH |
| BATTERY | MEDIUM |
| DATA_CENTER | MEDIUM |
| SEMICONDUCTOR | MEDIUM |
| ROBOTICS | MEDIUM |
| HOME_APPLIANCE | MEDIUM |
| AEROSPACE | MEDIUM |

This value should be used as a filter or prior, not as a final Opportunity Score.

---

# 14. Strategic Priority

The platform may support internal strategic-priority levels independent of steel-demand relevance.

Example:

```text
PRIORITY_1
PRIORITY_2
PRIORITY_3
NORMAL
```

Initial MVP:

```text
AUTOMOTIVE → PRIORITY_1
SHIPBUILDING → PRIORITY_1
ENERGY → PRIORITY_1
```

Priority should be configurable and should not be hard-coded into final business logic.

---

# 15. Industry Trend Directions

For dashboards and intelligence summaries, standardized directions may be used:

```text
EXPANDING
STABLE
CONTRACTING
TRANSFORMING
UNCERTAIN
```

Example:

```text
Industry:
AUTOMOTIVE

Trend:
TRANSFORMING

Drivers:
EV transition
localization
software-defined vehicles
```

These directions are analytical results, not taxonomy codes.

---

# 16. Industry Drivers

Common industry-driver categories:

```text
CAPACITY
TECHNOLOGY
REGULATION
DECARBONIZATION
LOCALIZATION
COST
SUPPLY_CHAIN
DEMAND
DEMOGRAPHICS
DIGITALIZATION
AUTOMATION
GEOPOLITICS
```

Industry drivers should be stored in insight or event structures rather than adding new industries.

---

# 17. Industry-to-Application Relationship

Industry taxonomy should connect to application taxonomy.

Example:

```text
AUTOMOTIVE
↓
EV_MOTOR
↓
MOTOR_CORE
```

```text
SHIPBUILDING
↓
LNG_CARRIER
↓
LNG_TANK
```

```text
ENERGY
↓
OFFSHORE_WIND
↓
WIND_TOWER
```

Detailed definitions belong in:

```text
applications.md
```

---

# 18. Industry-to-Product Retrieval

POSCO product retrieval should begin with industry filtering.

Recommended flow:

```text
event industry
↓
industry taxonomy
↓
application
↓
component
↓
steel requirement
↓
product retrieval
```

Industry match alone is not enough to recommend a product.

---

# 19. Competitor Industry Classification

Steel competitors should generally use:

```text
STEEL
```

as their company primary industry.

Their events may additionally reference customer industries.

Example:

```text
Nippon Steel develops EV motor steel.
```

Company industry:

```text
STEEL
```

Event target industry:

```text
AUTOMOTIVE
```

Both should be preserved.

---

# 20. Company Classification Examples

## Hyundai Motor

```text
PRIMARY:
AUTOMOTIVE

SECONDARY:
MOBILITY
```

## Samsung Electronics

Possible classification:

```text
PRIMARY:
SEMICONDUCTOR or ELECTRONICS
```

depending on business entity scope.

Specific events should be classified using their own context.

## HD Hyundai Heavy Industries

```text
PRIMARY:
SHIPBUILDING

SECONDARY:
ENERGY
```

where relevant.

## POSCO

```text
PRIMARY:
STEEL
```

---

# 21. Do Not Use Company Groups as Industries

Do not classify industries as:

```text
Samsung
Hyundai
LG
SK
```

These are company groups, not industries.

Likewise avoid:

```text
large company
SME
foreign company
```

as industries.

Company size and origin belong in separate fields.

---

# 22. Geography Is Not Industry

Do not create industry codes such as:

```text
US_AUTOMOTIVE
CHINA_STEEL
EU_ENERGY
```

Instead represent:

```text
industry = AUTOMOTIVE
country = US
```

This keeps taxonomy reusable.

---

# 23. Technology Is Not Always Industry

Do not automatically create industries for every technology.

Examples:

```text
AI
AUTONOMOUS_DRIVING
3D_PRINTING
CCUS
```

These should often be stored as:

```text
technology tags
```

unless there is a clear reason to model them as standalone industries.

---

# 24. Future Industry Candidates

Possible future taxonomy additions include:

```text
ELECTRONICS
DISPLAY
MINING
RAW_MATERIAL
AGRICULTURE
MEDICAL_DEVICE
MARINE_EQUIPMENT
TRANSFORMER
ELECTRIC_GRID
```

Do not add these until required by real data or business use cases.

---

# 25. Taxonomy Change Rule

Before adding a new industry code, verify:

```text
1. existing industry cannot represent it

2. it occurs frequently enough to justify a category

3. it has distinct analytical value

4. it affects search, product retrieval, or opportunity analysis

5. it is not merely a technology, company type, geography, or application
```

Important taxonomy changes should be recorded in:

```text
docs/decisions.md
```

---

# 26. Internal Representation

Internally prefer canonical codes.

Example:

```json
{
  "industry_code": "AUTOMOTIVE"
}
```

Frontend may display:

```text
자동차
```

or:

```text
Automotive
```

depending on user language.

---

# 27. AI Output Rule

LLM output must select an industry from the permitted taxonomy.

Example schema concept:

```text
industry:
enum[
  AUTOMOTIVE,
  SHIPBUILDING,
  ENERGY,
  BATTERY,
  SEMICONDUCTOR,
  CONSTRUCTION,
  MACHINERY,
  HOME_APPLIANCE,
  DEFENSE,
  AEROSPACE,
  ROBOTICS,
  DATA_CENTER,
  HYDROGEN,
  RENEWABLE_ENERGY,
  STEEL,
  CHEMICAL,
  PETROCHEMICAL,
  LOGISTICS,
  RAILWAY,
  OTHER,
  UNKNOWN
]
```

Do not accept arbitrary values from LLM responses.

---

# 28. MVP Processing Priority

For initial development:

```text
FULL INTELLIGENCE:

AUTOMOTIVE
SHIPBUILDING
ENERGY
```

Secondary support:

```text
BATTERY
SEMICONDUCTOR
CONSTRUCTION
MACHINERY
DEFENSE
DATA_CENTER
HYDROGEN
ROBOTICS
```

Other industries may initially receive basic classification and search support.

---

# 29. Example Classification 1

Source:

```text
현대자동차가 미국 조지아 EV 공장 생산능력을 확대한다.
```

Classification:

```text
company:
Hyundai Motor

company_industry:
AUTOMOTIVE

event_industry:
AUTOMOTIVE

subindustry:
EV

confidence:
98
```

---

# 30. Example Classification 2

Source:

```text
HD현대중공업이 LNG 운반선 8척을 수주했다.
```

Classification:

```text
company_industry:
SHIPBUILDING

event_industry:
SHIPBUILDING

subindustry:
LNG_CARRIER

confidence:
99
```

---

# 31. Example Classification 3

Source:

```text
두산에너빌리티가 해상풍력 설비 생산시설에 투자한다.
```

Classification:

```text
primary_industry:
ENERGY

subindustry:
OFFSHORE_WIND

related_industry:
RENEWABLE_ENERGY

confidence:
95
```

---

# 32. Example Classification 4

Source:

```text
Nippon Steel develops advanced electrical steel for EV motors.
```

Classification:

```text
company_industry:
STEEL

event_target_industry:
AUTOMOTIVE

application:
EV_MOTOR

technology/product context:
ELECTRICAL_STEEL
```

Do not classify the company itself as AUTOMOTIVE.

---

# 33. Example Classification 5

Source:

```text
Samsung Electronics announces new AI data-center investment.
```

Possible result:

```text
company_industry:
SEMICONDUCTOR

event_industry:
DATA_CENTER

secondary_context:
AI infrastructure
```

Event classification should reflect the actual investment target.

---

# 34. Final Rule

Industry taxonomy exists to make intelligence consistent.

The system should prefer:

```text
one stable canonical industry
+
optional secondary industries
+
subindustry
+
application
+
technology tags
```

over creating new free-form categories.

The primary objective is to support reliable:

```text
source classification
→ event classification
→ industry trend analysis
→ steel demand reasoning
→ POSCO product retrieval
→ opportunity analysis
```

with a stable and expandable industrial taxonomy.
