# POSCO Product Knowledge Router

## 1. Purpose

This file is the master routing index for POSCO product knowledge.

It connects:

```text
applications.md
↓
materials.md
↓
knowledge/posco/index.md
↓
product-specific knowledge file
```

The purpose of this file is NOT to contain detailed product specifications.

The purpose is to determine:

```text
Which POSCO product knowledge file should be retrieved?
```

The router must minimize unnecessary document loading.

Default behavior:

```text
1 application
→ 1~3 material candidates
→ 1~3 product knowledge files
```

Never retrieve the entire `knowledge/posco/` directory for a single question.

---

# 2. Core Routing Principle

The system must follow this sequence:

```text
INDUSTRY
↓
EVENT
↓
STRATEGY
↓
APPLICATION
↓
COMPONENT
↓
OPERATING ENVIRONMENT
↓
REQUIRED PERFORMANCE
↓
MATERIAL REQUIREMENT
↓
MATERIAL CATEGORY
↓
POSCO PRODUCT FAMILY
↓
PRODUCT KNOWLEDGE FILE
```

Never route directly:

```text
NEWS
→ PRODUCT FILE
```

Never route only by keyword:

```text
"EV"
→ all automotive products
```

Instead:

```text
EV
+
motor investment
+
motor core
+
low core loss
→ Hyper NO
```

---

# 3. Retrieval Levels

The router uses three retrieval levels.

## LEVEL 1 — Category Routing

Determine broad material category.

Example:

```text
EV MOTOR
→ ELECTRICAL_STEEL
```

---

## LEVEL 2 — Product Family Routing

Determine relevant POSCO product family.

Example:

```text
ELECTRICAL_STEEL
+
TRACTION MOTOR
+
LOW CORE LOSS
→ HYPER_NO
```

---

## LEVEL 3 — Product Detail Retrieval

Load the product knowledge file.

Example:

```text
knowledge/posco/automotive/hyper-no.md
```

Specific grade selection happens only after this step.

---

# 4. Maximum Retrieval Rule

Default maximum:

```yaml
max_product_files: 3
```

Preferred:

```yaml
preferred_product_files: 1
```

Allowed expansion:

```text
1 file
→ clear technical match

2 files
→ alternative technologies / competing material concepts

3 files
→ complex application with multiple valid material routes
```

More than 3 product files requires:

```text
COMPLEX_APPLICATION
or
MULTI_COMPONENT_ANALYSIS
```

---

# 5. Folder Structure

```text
knowledge/
└── posco/
    ├── index.md
    │
    ├── automotive/
    │   ├── index.md
    │   ├── automotive-steel.md
    │   ├── atos.md
    │   └── hyper-no.md
    │
    ├── coated/
    │   ├── index.md
    │   ├── galvanized.md
    │   ├── electro-galvanized.md
    │   ├── posmac-1.5.md
    │   ├── posmac-3.0.md
    │   └── posmac-super.md
    │
    ├── plate/
    │   ├── index.md
    │   ├── shipbuilding.md
    │   ├── offshore.md
    │   ├── line-pipe.md
    │   ├── pressure-vessel.md
    │   ├── cryogenic.md
    │   ├── construction.md
    │   ├── posten.md
    │   └── posar.md
    │
    ├── carbon/
    │   ├── index.md
    │   ├── hot-rolled.md
    │   ├── cold-rolled.md
    │   ├── high-carbon.md
    │   └── wire-rod.md
    │
    ├── stainless/
    │   ├── index.md
    │   └── stainless.md
    │
    ├── titanium/
    │   ├── index.md
    │   ├── titanium.md
    │   └── titanium-applications.md
    │
    ├── energy/
    │   ├── index.md
    │   ├── api-steel.md
    │   └── ancor.md
    │
    └── future/
        ├── index.md
        ├── posloop355.md
        └── low-carbon-steel.md
```

---

# 6. Master Product Registry

| Product Family Code | Product | Primary Folder | Knowledge File |
|---|---|---|---|
| AUTOMOTIVE_STEEL | Automotive Steel | automotive | `automotive/automotive-steel.md` |
| ATOS | ATOS | automotive | `automotive/atos.md` |
| HYPER_NO | Hyper NO | automotive | `automotive/hyper-no.md` |
| GALVANIZED_STEEL | GI / GA / GI(H) | coated | `coated/galvanized.md` |
| ELECTRO_GALVANIZED_STEEL | EG | coated | `coated/electro-galvanized.md` |
| POSMAC_1_5 | PosMAC 1.5 | coated | `coated/posmac-1.5.md` |
| POSMAC_3_0 | PosMAC 3.0 | coated | `coated/posmac-3.0.md` |
| POSMAC_SUPER | PosMAC Super | coated | `coated/posmac-super.md` |
| HOT_ROLLED_STEEL | Hot Rolled Steel | carbon | `carbon/hot-rolled.md` |
| COLD_ROLLED_STEEL | Cold Rolled Steel | carbon | `carbon/cold-rolled.md` |
| HIGH_CARBON_STEEL | High Carbon Steel | carbon | `carbon/high-carbon.md` |
| WIRE_ROD | Wire Rod | carbon | `carbon/wire-rod.md` |
| SHIPBUILDING_PLATE | Shipbuilding Plate | plate | `plate/shipbuilding.md` |
| OFFSHORE_PLATE | Offshore Plate | plate | `plate/offshore.md` |
| LINE_PIPE_PLATE | Line Pipe Plate | plate | `plate/line-pipe.md` |
| PRESSURE_VESSEL_PLATE | Pressure Vessel Plate | plate | `plate/pressure-vessel.md` |
| CRYOGENIC_PLATE | Cryogenic Plate | plate | `plate/cryogenic.md` |
| CONSTRUCTION_PLATE | Construction Plate | plate | `plate/construction.md` |
| POS_TEN | PosTen | plate | `plate/posten.md` |
| POS_AR | PosAR | plate | `plate/posar.md` |
| API_STEEL | API Steel | energy | `energy/api-steel.md` |
| ANCOR | ANCOR | energy | `energy/ancor.md` |
| STAINLESS_STEEL | Stainless Steel | stainless | `stainless/stainless.md` |
| TITANIUM | Titanium | titanium | `titanium/titanium.md` |
| POSLOOP355 | PosLoop355 | future | `future/posloop355.md` |
| LOW_CARBON_STEEL | Low Carbon Attribute | future | `future/low-carbon-steel.md` |

---

# 7. Industry Router

## AUTOMOTIVE

Route candidates:

```text
AUTOMOTIVE_STEEL
ATOS
HYPER_NO
GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
POSMAC_1_5
HIGH_CARBON_STEEL
WIRE_ROD
STAINLESS_STEEL
```

Do NOT load all.

Use component routing.

---

## SHIPBUILDING

Route candidates:

```text
SHIPBUILDING_PLATE
OFFSHORE_PLATE
CRYOGENIC_PLATE
STAINLESS_STEEL
TITANIUM
```

---

## ENERGY

Route candidates:

```text
API_STEEL
LINE_PIPE_PLATE
OFFSHORE_PLATE
PRESSURE_VESSEL_PLATE
CRYOGENIC_PLATE
ANCOR
```

---

## CONSTRUCTION

Route candidates:

```text
CONSTRUCTION_PLATE
GALVANIZED_STEEL
POSMAC_3_0
POSMAC_SUPER
HOT_ROLLED_STEEL
```

---

## MACHINERY

Route candidates:

```text
POS_TEN
POS_AR
HIGH_CARBON_STEEL
WIRE_ROD
HOT_ROLLED_STEEL
```

---

## HOME_APPLIANCE

Route candidates:

```text
COLD_ROLLED_STEEL
GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
POSMAC_1_5
STAINLESS_STEEL
```

---

## MINING

Route candidates:

```text
POS_AR
HIGH_MN_WEAR_RESISTANT_STEEL
POS_TEN
```

If no dedicated high-Mn product file exists:

```text
retrieve plate/index.md
```

and then route to the relevant high-Mn section.

---

# 8. Application Router

## EV_MOTOR

Required signals:

```text
electric motor
traction motor
motor core
stator
rotor
high speed motor
```

Primary route:

```text
HYPER_NO
```

Retrieve:

```text
automotive/hyper-no.md
```

Do not retrieve general automotive steel unless structural components are also discussed.

---

## BODY_IN_WHITE

Primary route:

```text
AUTOMOTIVE_STEEL
```

Retrieve:

```text
automotive/automotive-steel.md
```

Relevant internal families:

```text
IF_HSS
DP
TRIP
CP
MART
```

---

## CHASSIS

Candidate route:

```text
AUTOMOTIVE_STEEL
ATOS
```

If:

```text
wheel
lower arm
suspension
```

prefer:

```text
AUTOMOTIVE_STEEL
```

with FB routing.

If:

```text
truck frame
trailer frame
heavy structural frame
```

prefer:

```text
ATOS
```

---

## TRUCK_FRAME

Primary route:

```text
ATOS
```

Retrieve:

```text
automotive/atos.md
```

---

## BUMPER_BEAM

Candidate:

```text
AUTOMOTIVE_STEEL
```

Likely internal family:

```text
MART
```

Retrieve only:

```text
automotive/automotive-steel.md
```

---

## BATTERY_PACK_STRUCTURE

Candidate:

```text
AUTOMOTIVE_STEEL
```

Possible families:

```text
MART
CP
DP
```

Do not recommend a grade before component requirements are known.

---

## AUTOMOTIVE_EXHAUST

Primary route:

```text
STAINLESS_STEEL
```

Retrieve:

```text
stainless/stainless.md
```

---

## AUTOMOTIVE_CLUTCH

Primary route:

```text
HIGH_CARBON_STEEL
```

Retrieve:

```text
carbon/high-carbon.md
```

---

## TIRE_REINFORCEMENT

Primary route:

```text
WIRE_ROD
```

Subfamily:

```text
TIRE_CORD_WIRE_ROD
```

Retrieve:

```text
carbon/wire-rod.md
```

---

# 9. Shipbuilding Application Router

## SHIP_HULL

Primary route:

```text
SHIPBUILDING_PLATE
```

Retrieve:

```text
plate/shipbuilding.md
```

---

## LARGE_CONTAINER_SHIP

Primary:

```text
SHIPBUILDING_PLATE
```

Priority requirements:

```text
HIGH_STRENGTH
BRITTLE_CRACK_RESISTANCE
HIGH_HEAT_INPUT_WELDABILITY
WEIGHT_REDUCTION
```

---

## OFFSHORE_PLATFORM

Primary:

```text
OFFSHORE_PLATE
```

Retrieve:

```text
plate/offshore.md
```

---

## OFFSHORE_WIND

Primary candidates:

```text
OFFSHORE_PLATE
CONSTRUCTION_PLATE
```

Routing logic:

```text
thick primary structural member
→ OFFSHORE_PLATE

general structural member
→ CONSTRUCTION_PLATE
```

---

## LNG_CARRIER

Possible candidates:

```text
SHIPBUILDING_PLATE
CRYOGENIC_PLATE
STAINLESS_STEEL
```

Do not retrieve all by default.

Use component.

---

## LNG_TANK

Primary route:

```text
CRYOGENIC_PLATE
```

Retrieve:

```text
plate/cryogenic.md
```

Possible subfamilies:

```text
9_PERCENT_NI_STEEL
HIGH_MN_CRYOGENIC_STEEL
```

---

# 10. Energy Application Router

## OIL_PIPELINE

Candidates:

```text
API_STEEL
LINE_PIPE_PLATE
```

Default route:

```text
LINE_PIPE_PLATE
```

if the requirement is about:

```text
plate for pipe manufacturing
```

Default route:

```text
API_STEEL
```

if the question is specification / API family focused.

---

## GAS_PIPELINE

Same routing logic as oil pipeline.

Additional requirement:

```text
LOW_TEMPERATURE_TOUGHNESS
```

may affect detailed selection.

---

## SOUR_SERVICE_PIPELINE

Primary:

```text
LINE_PIPE_PLATE
```

Mandatory requirements:

```text
HIC_RESISTANCE
SOUR_SERVICE
SSCC_RESISTANCE
```

Retrieve:

```text
plate/line-pipe.md
```

---

## OILWELL_CASING

Primary:

```text
API_STEEL
```

Relevant API family:

```text
API_5CT
```

Retrieve:

```text
energy/api-steel.md
```

---

## PETROCHEMICAL_PRESSURE_VESSEL

Primary:

```text
PRESSURE_VESSEL_PLATE
```

Retrieve:

```text
plate/pressure-vessel.md
```

---

## POWER_PLANT_EXHAUST

Primary:

```text
ANCOR
```

If environment contains:

```text
SOx
sulfuric acid
dew point corrosion
boiler exhaust
FGD
SCR
GGH
```

retrieve:

```text
energy/ancor.md
```

---

# 11. Construction Application Router

## BUILDING_STRUCTURE

Primary:

```text
CONSTRUCTION_PLATE
```

Retrieve:

```text
plate/construction.md
```

---

## SEISMIC_BUILDING

Primary:

```text
CONSTRUCTION_PLATE
```

Relevant family:

```text
PILAC
HSA
```

---

## BRIDGE

Primary:

```text
CONSTRUCTION_PLATE
```

Relevant family:

```text
HSB
```

---

## WEATHERING_STRUCTURE

Candidates:

```text
CONSTRUCTION_PLATE
HOT_ROLLED_STEEL
```

Select according to:

```text
plate structure
vs
coil / sheet structure
```

---

## SOLAR_STRUCTURE

Candidates:

```text
GALVANIZED_STEEL
POSMAC_3_0
POSMAC_SUPER
```

Routing:

```text
NORMAL_OUTDOOR
→ GALVANIZED_STEEL

SEVERE_CORROSION
→ POSMAC_3_0

COASTAL / HIGH_SALINITY
→ POSMAC_SUPER
```

Maximum product files:

```text
2
```

unless explicit comparison is requested.

---

# 12. Machinery Application Router

## CRANE_BOOM

Primary:

```text
POS_TEN
```

Retrieve:

```text
plate/posten.md
```

---

## HEAVY_EQUIPMENT_FRAME

Candidates:

```text
POS_TEN
ATOS
```

Routing:

```text
thick plate heavy equipment
→ POS_TEN

vehicle / truck structural frame
→ ATOS
```

---

## EXCAVATOR_BUCKET

Primary:

```text
POS_AR
```

Retrieve:

```text
plate/posar.md
```

---

## CHUTE

Candidates:

```text
POS_AR
HIGH_MN_WEAR_RESISTANT_STEEL
```

If severe erosion / slurry:

```text
HIGH_MN_WEAR_RESISTANT_STEEL
```

If general abrasive wear:

```text
POS_AR
```

---

## BEARING

Primary:

```text
WIRE_ROD
```

Subfamily:

```text
BEARING_STEEL_WIRE_ROD
```

---

## SPRING

Primary:

```text
WIRE_ROD
```

Subfamily:

```text
SPRING_STEEL_WIRE_ROD
```

---

## SAW_BLADE

Primary:

```text
HIGH_CARBON_STEEL
```

---

# 13. Coating Router

Use coating requirements independently from industry.

## NORMAL_CORROSION

Candidate:

```text
GALVANIZED_STEEL
```

---

## GOOD_SURFACE + PAINTABILITY

Candidate:

```text
GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
POSMAC_1_5
```

Use application to narrow.

---

## AUTOMOTIVE_COATED_PANEL

Candidates:

```text
GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
AUTOMOTIVE_STEEL
```

Do not recommend coating without checking substrate grade requirements.

---

## SEVERE_OUTDOOR_CORROSION

Candidate:

```text
POSMAC_3_0
```

---

## HIGH_SALINITY / MARINE ATMOSPHERE

Candidate:

```text
POSMAC_SUPER
```

---

# 14. Corrosion Router

```text
ATMOSPHERIC_CORROSION
→ WEATHERING_STEEL / GALVANIZED

COASTAL_CORROSION
→ POSMAC / CORROSION_RESISTANT_PLATE

SEAWATER_STRUCTURE
→ OFFSHORE_PLATE / TITANIUM / STAINLESS
depending component

SULFURIC_ACID
→ ANCOR

COMPOSITE_ACID
→ ANCOR

SOUR_GAS
→ LINE_PIPE_PLATE / PRESSURE_VESSEL_PLATE
```

Do not treat all forms of corrosion as equivalent.

---

# 15. Environment-First Overrides

Environment may override industry routing.

Example:

```text
POWER_PLANT
+
SULFURIC_ACID_DEW_POINT
```

must route to:

```text
ANCOR
```

not generic:

```text
HOT_ROLLED_STEEL
```

Another example:

```text
CONSTRUCTION
+
HIGH_SALINITY_COAST
```

may route:

```text
POSMAC_SUPER
```

instead of ordinary galvanized steel.

---

# 16. Property Router

## HIGH_STRENGTH

Possible candidates:

```text
AUTOMOTIVE_STEEL
ATOS
POS_TEN
CONSTRUCTION_PLATE
SHIPBUILDING_PLATE
```

High strength alone is insufficient for routing.

Require application/component.

---

## WEAR_RESISTANCE

Primary:

```text
POS_AR
```

Possible:

```text
HIGH_MN_WEAR_RESISTANT_STEEL
```

---

## LOW_CORE_LOSS

Primary:

```text
HYPER_NO
```

---

## CRYOGENIC_TOUGHNESS

Candidates:

```text
CRYOGENIC_PLATE
STAINLESS_STEEL
```

Use component and temperature to narrow.

---

## DEW_POINT_CORROSION

Primary:

```text
ANCOR
```

---

## CUT_EDGE_CORROSION_RESISTANCE

Primary candidates:

```text
POSMAC_3_0
POSMAC_SUPER
```

---

## HIGH_SURFACE_QUALITY

Candidates:

```text
COLD_ROLLED_STEEL
ELECTRO_GALVANIZED_STEEL
GALVANIZED_STEEL
```

---

# 17. Competitive Comparison Routing

When the user asks:

```text
compare POSCO against competitor steel products
```

first identify:

```text
application
material category
POSCO product family
```

Only then retrieve competitive information.

Do not compare entire steel-company portfolios.

Comparison unit should normally be:

```text
APPLICATION
+
PRODUCT FAMILY
```

Example:

```text
EV traction motor
+
Hyper NO
+
competitor NO electrical steel
```

---

# 18. Product Candidate Object

The router should return structured candidate data.

```yaml
application: EV_MOTOR

component:
  - MOTOR_CORE

environment:
  - ELECTROMAGNETIC
  - HIGH_SPEED_ROTATION

requirements:
  - LOW_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_STRENGTH

material_candidates:
  - NON_ORIENTED_ELECTRICAL_STEEL

product_candidates:
  - code: HYPER_NO
    file: automotive/hyper-no.md
    priority: 1
    reason: EV traction motor core material
    confidence: 0.95

files_to_load:
  - automotive/hyper-no.md
```

---

# 19. Retrieval Priority

Priority values:

```text
P1
Direct technical fit

P2
Strong alternative

P3
Possible adjacent solution

P4
Background only
```

Default retrieval:

```text
P1 only
```

If P1 confidence is low:

```text
P1 + P2
```

Do not retrieve P3/P4 unless requested.

---

# 20. Confidence Rule

Suggested routing confidence:

```text
0.90 - 1.00
DIRECT_MATCH

0.80 - 0.89
STRONG_MATCH

0.70 - 0.79
POSSIBLE_MATCH

0.60 - 0.69
WEAK_MATCH

< 0.60
DO_NOT_LOAD
```

---

# 21. Evidence Requirements

Product file selection must be explainable.

Every route should preserve:

```text
APPLICATION_EVIDENCE
COMPONENT_EVIDENCE
REQUIREMENT_EVIDENCE
PRODUCT_MATCH_REASON
```

Example:

```yaml
product: HYPER_NO

route_reason:
  application: EV_MOTOR
  component: MOTOR_CORE
  requirement:
    - LOW_CORE_LOSS
    - HIGH_MAGNETIC_FLUX_DENSITY

evidence_strength: STRONG
```

---

# 22. Missing Information Rule

If routing depends on missing data, return:

```text
APPLICATION_CONDITION_REQUIRED
```

Examples of important missing information:

```text
exact component
operating environment
temperature
required strength
thickness
corrosion condition
pressure
forming process
welding process
```

Do not compensate by loading many product files.

---

# 23. Unknown Product Handling

If no suitable POSCO product is found:

```text
PRODUCT_FAMILY_UNKNOWN
```

Do not force a recommendation.

If broad material exists but product information is insufficient:

```text
DETAIL_SOURCE_PENDING
```

---

# 24. Grade Selection Boundary

This index must NOT select exact grade.

The maximum normal output of this router is:

```text
PRODUCT FAMILY
```

Example:

```text
HYPER_NO
```

not:

```text
20PNX1250FY
```

Specific grade selection belongs inside:

```text
product-specific knowledge file
```

and may require:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 25. Low Carbon Routing

Low-carbon steel is a secondary layer.

Do:

```text
PRODUCT TECHNICAL FIT
↓
LOW CARBON AVAILABILITY CHECK
```

Example:

```text
SHIPBUILDING_PLATE
↓
technical fit confirmed
↓
check low-carbon production availability
```

Do not route:

```text
LOW_CARBON
→ arbitrary steel product
```

---

# 26. Low Carbon File

Use:

```text
future/low-carbon-steel.md
```

only when the source event includes:

```text
carbon neutrality
CBAM
green procurement
Scope 3 reduction
low-carbon material
embodied carbon
green steel
carbon footprint
```

The low-carbon file should be loaded together with the technical product file.

Example:

```text
plate/shipbuilding.md
+
future/low-carbon-steel.md
```

Maximum product files remains 3.

---

# 27. Product File Loading Algorithm

```pseudo
function route_product(application_context):

    application = detect_application()
    component = detect_component()
    environment = detect_environment()
    requirements = derive_material_requirements()

    material_candidates =
        materials.lookup(
            application,
            component,
            environment,
            requirements
        )

    product_candidates = []

    for material in material_candidates:

        candidates =
            posco_index.lookup(material)

        for candidate in candidates:

            score =
                application_match * 0.25 +
                component_match * 0.20 +
                property_match * 0.25 +
                environment_match * 0.15 +
                manufacturing_match * 0.10 +
                evidence_score * 0.05

            if score >= 0.70:
                product_candidates.append(candidate)

    sort candidates by score descending

    return top 1~3 product files
```

---

# 28. Retrieval Guardrail

Never do:

```text
grep -R
recursive full folder scan
load all markdown files
read all PDF catalogs
```

for normal analysis.

Preferred:

```text
applications.md
↓
materials.md
↓
posco/index.md
↓
single product md
```

---

# 29. Search Cost Optimization

The system should prioritize structured metadata over semantic full-text search.

Order:

```text
1. Exact taxonomy code
2. Application mapping
3. Product registry
4. Product frontmatter
5. Product document content
6. PDF source
```

PDF retrieval should normally be the last stage.

---

# 30. PDF Retrieval Rule

PDF source should be opened only when:

```text
specific numerical property is required
exact grade specification is required
dimension range is required
chemical composition is required
certification is required
source verification is required
```

Do not repeatedly parse PDFs during daily intelligence generation.

---

# 31. Frontmatter Contract

Every product knowledge file should use this minimum frontmatter:

```yaml
---
product_family:

material_categories: []

industries: []

applications: []

components: []

environments: []

requirements: []

aliases: []

source_documents: []

knowledge_status: VERIFIED

last_reviewed:
---
```

The router should inspect frontmatter before reading the body whenever possible.

---

# 32. Alias Handling

Common aliases should resolve to the canonical code.

Example:

```yaml
HYPER_NO:
  aliases:
    - Hyper NO
    - NO electrical steel
    - non-oriented electrical steel
    - 무방향성 전기강판
    - 모터용 전기강판
```

Example:

```yaml
POS_AR:
  aliases:
    - PosAR
    - wear resistant plate
    - abrasion resistant steel
    - 내마모강
```

Example:

```yaml
POS_TEN:
  aliases:
    - PosTen
    - high tensile plate
    - 고장력 후판
```

Aliases are navigation aids only.

They must not override application logic.

---

# 33. Negative Routing Rules

These rules are important.

## EV does NOT automatically mean Hyper NO

If the article is about:

```text
battery plant
battery cell
charging network
```

do not automatically retrieve:

```text
HYPER_NO
```

---

## Offshore does NOT automatically mean Offshore Plate

If the article is about:

```text
offshore solar support
small corrosion-resistant frame
```

a coated product may be more relevant.

---

## High Strength does NOT automatically mean PosTen

If the application is:

```text
car body crash member
```

route to:

```text
AUTOMOTIVE_STEEL
```

---

## Corrosion does NOT automatically mean PosMAC

If the environment is:

```text
sulfuric acid
```

route to:

```text
ANCOR
```

---

## Wear does NOT automatically mean High Strength Plate

If the requirement is:

```text
abrasion
```

prioritize:

```text
POS_AR
```

---

# 34. Multi-Component Project Rule

Large investment news may contain multiple material opportunities.

Example:

```text
NEW EV FACTORY
```

Possible components:

```text
factory building
vehicle body
battery pack
EV motor
logistics system
```

Do not return one material for the entire event.

Create separate opportunity chains.

Example:

```text
EV motor
→ HYPER_NO

vehicle body
→ AUTOMOTIVE_STEEL

factory structure
→ CONSTRUCTION_PLATE / coated steel
```

---

# 35. Opportunity Decomposition

For large CAPEX events:

```text
EVENT
↓
PROJECT
↓
SYSTEM
↓
COMPONENT
↓
MATERIAL OPPORTUNITY
```

Example:

```text
EV FACTORY CAPEX

PROJECT
EV manufacturing plant

SYSTEM 1
vehicle production

COMPONENT
body structure

→ AUTOMOTIVE_STEEL


SYSTEM 2
motor production

COMPONENT
motor core

→ HYPER_NO
```

---

# 36. Router Output Schema

Recommended output:

```json
{
  "industry": "",
  "application": "",
  "component": "",
  "environment": [],
  "requirements": [],
  "material_candidates": [],
  "product_candidates": [
    {
      "product_family": "",
      "knowledge_file": "",
      "priority": "P1",
      "route_score": 0,
      "reason": ""
    }
  ],
  "files_to_load": [],
  "missing_information": [],
  "confidence": 0
}
```

---

# 37. Executive Insight Mode

For executive users:

Do not load deep product specifications unless essential.

Preferred retrieval:

```text
product family
business relevance
customer opportunity
strategic implication
```

Example:

```text
Hyundai EV motor capacity expansion
→ Hyper NO opportunity
→ potential electrical steel demand increase
```

---

# 38. Marketing User Mode

For marketing users:

Retrieve:

```text
product family
application fit
customer pain point
competitive positioning
sales hypothesis
next action
```

Product file body may be loaded.

---

# 39. Engineer Mode

For engineering users:

Retrieve:

```text
product family
grade family
mechanical properties
dimensions
chemical composition
standards
welding/forming conditions
limitations
```

Product source PDF may be loaded when necessary.

---

# 40. Role-Based Retrieval Depth

```yaml
EXECUTIVE:
  retrieval_depth: 1

MARKETING:
  retrieval_depth: 2

ENGINEER:
  retrieval_depth: 3
```

Definition:

```text
Depth 1
Product Family

Depth 2
Product Family + Product Characteristics

Depth 3
Grade / Specification / Engineering Data
```

---

# 41. Daily Intelligence Routing

For automated daily intelligence:

Default mode:

```text
MARKETING
```

Maximum product files:

```text
2
```

Maximum detailed product retrieval:

```text
1
```

Output should prioritize:

```text
Why this matters
What customer is changing
What material demand may change
Which POSCO product family is relevant
What marketing action should follow
```

---

# 42. Telegram Routing

Telegram daily output should not include large product tables.

Recommended:

```text
[Customer Signal]

Company:
Industry:
Event:

Why Important:
...

Material Opportunity:
...

POSCO Candidate:
...

Marketing Action:
...

Confidence:
...
```

Detailed analysis should remain in the app.

---

# 43. Product Comparison Rule

When two POSCO product families are valid:

Return comparison only on relevant dimensions.

Example:

```text
POSMAC_3_0
vs
POSMAC_SUPER
```

Compare:

```text
corrosion severity
environment
processing requirement
likely application
```

Do not dump full specification tables.

---

# 44. Evidence Traceability

Every selected product should be traceable back to:

```text
source event
↓
application inference
↓
material requirement
↓
product family
↓
POSCO source
```

Recommended trace object:

```yaml
trace:
  event_id:
  application_code:
  material_code:
  product_family:
  source_document:
```

---

# 45. Knowledge Status

Supported status:

```text
VERIFIED
PARTIAL
DETAIL_SOURCE_PENDING
SUPERSEDED
DEPRECATED
UNKNOWN
```

Do not load:

```text
SUPERSEDED
DEPRECATED
```

unless historical comparison is requested.

---

# 46. Duplicate Knowledge Rule

If the same product appears in multiple catalogs:

Do not create duplicate product files.

Example:

```text
ATOS
```

may appear in:

```text
Hot Rolled Steel
ATOS dedicated catalog
```

Use:

```text
automotive/atos.md
```

as the canonical product file.

The dedicated product guide should normally be the primary source.

General catalog references become secondary sources.

---

# 47. Canonical Product Ownership

Use this ownership rule:

```text
Dedicated Product Guide
>
Specialized Product Catalog
>
General Product Catalog
>
Corporate Report
```

Example:

```text
PosAR dedicated guide
→ canonical

Steel Plates PosAR section
→ supporting source
```

---

# 48. Fallback Routing

If application is known but no product family confidently matches:

```text
applications.md
↓
materials.md
↓
MATERIAL CATEGORY
```

Stop there.

Return:

```text
PRODUCT_FAMILY_UNKNOWN
```

Do not search all product files.

---

# 49. Router Decision Example — EV Motor Plant

Input:

```text
A customer announces expansion of EV motor production capacity.
```

Result:

```yaml
industry: AUTOMOTIVE

application: EV_MOTOR

component:
  - MOTOR_CORE

requirements:
  - LOW_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_STRENGTH

material_candidates:
  - NON_ORIENTED_ELECTRICAL_STEEL

product_candidates:
  - product_family: HYPER_NO
    knowledge_file: automotive/hyper-no.md
    priority: P1
    route_score: 0.96

files_to_load:
  - automotive/hyper-no.md
```

---

# 50. Router Decision Example — Offshore Wind

Input:

```text
Company announces large offshore wind foundation investment.
```

Result:

```yaml
industry: ENERGY

application: OFFSHORE_WIND

component:
  - FOUNDATION_STRUCTURE

environment:
  - MARINE

requirements:
  - HIGH_STRENGTH
  - FATIGUE_RESISTANCE
  - WELDABILITY
  - LOW_TEMPERATURE_TOUGHNESS

product_candidates:
  - product_family: OFFSHORE_PLATE
    knowledge_file: plate/offshore.md
    priority: P1

  - product_family: CONSTRUCTION_PLATE
    knowledge_file: plate/construction.md
    priority: P2
```

---

# 51. Router Decision Example — Coastal Solar

```yaml
application: SOLAR_STRUCTURE

component:
  - SUPPORT_FRAME

environment:
  - COASTAL
  - HIGH_SALINITY

requirements:
  - CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE

product_candidates:
  - product_family: POSMAC_SUPER
    knowledge_file: coated/posmac-super.md
    priority: P1

  - product_family: POSMAC_3_0
    knowledge_file: coated/posmac-3.0.md
    priority: P2
```

---

# 52. Router Decision Example — Excavator

```yaml
application: HEAVY_EQUIPMENT

component:
  - BUCKET

environment:
  - ABRASIVE

requirements:
  - WEAR_RESISTANCE
  - ABRASION_RESISTANCE

product_candidates:
  - product_family: POS_AR
    knowledge_file: plate/posar.md
    priority: P1
```

Do not retrieve:

```text
plate/posten.md
```

unless structural strength is separately relevant.

---

# 53. Router Decision Example — Thermal Power

```yaml
application: THERMAL_POWER_EXHAUST

environment:
  - SULFURIC_ACID
  - DEW_POINT_CORROSION

requirements:
  - SULFURIC_ACID_CORROSION_RESISTANCE

product_candidates:
  - product_family: ANCOR
    knowledge_file: energy/ancor.md
    priority: P1
```

---

# 54. Router Decision Example — LNG Storage

```yaml
application: LNG_STORAGE

component:
  - INNER_SHELL

environment:
  - CRYOGENIC

requirements:
  - CRYOGENIC_TOUGHNESS
  - HIGH_STRENGTH
  - FRACTURE_TOUGHNESS

product_candidates:
  - product_family: CRYOGENIC_PLATE
    knowledge_file: plate/cryogenic.md
    priority: P1
```

---

# 55. Router Decision Example — Green Steel Request

Input:

```text
Customer announces low-carbon steel procurement target.
```

Do NOT route directly to one steel product.

First find technical application.

Then load:

```text
technical product file
+
future/low-carbon-steel.md
```

Example:

```text
automotive/automotive-steel.md
+
future/low-carbon-steel.md
```

---

# 56. Daily Processing Rule

During daily news processing:

```text
DO NOT:
load product PDFs
load every product MD
run broad semantic search across the entire product folder
```

Instead:

```text
1. classify application
2. derive requirements
3. route using this index
4. load only selected MD
5. create insight
```

---

# 57. Final Routing Rule

The correct behavior is:

```text
FEW FILES
+
HIGH RELEVANCE
+
CLEAR ROUTING LOGIC
+
TRACEABLE EVIDENCE
```

The incorrect behavior is:

```text
MANY FILES
+
KEYWORD MATCH
+
UNNECESSARY CONTEXT
+
HIGH TOKEN COST
```

---

# 58. Final System Chain

```text
industries.md
↓
events.md
↓
strategies.md
↓
applications.md
↓
materials.md
↓
knowledge/posco/index.md
↓
product-specific MD
↓
marketing intelligence
```

This file is the gateway between:

```text
INDUSTRY INTELLIGENCE
```

and:

```text
POSCO PRODUCT KNOWLEDGE
```

Its primary responsibility is:

```text
LOAD THE RIGHT PRODUCT KNOWLEDGE,
NOT ALL PRODUCT KNOWLEDGE.
```
