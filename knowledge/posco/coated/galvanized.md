---
product_family: GALVANIZED_STEEL

name_ko: 용융아연도금강판
name_en: POSCO Galvanized Steel

material_category:
  - COATED_STEEL
  - ZINC_COATED_STEEL
  - HOT_DIP_GALVANIZED_STEEL

product_subfamilies:
  - GI
  - GA
  - GI_H

industries:
  - AUTOMOTIVE
  - HOME_APPLIANCE
  - CONSTRUCTION
  - INFRASTRUCTURE
  - ENERGY
  - MACHINERY

applications:
  - AUTOMOTIVE_PANEL
  - AUTOMOTIVE_BODY
  - HOME_APPLIANCE_PANEL
  - PREPAINTED_STEEL_BASE
  - BUILDING_MATERIAL
  - PIPE
  - ELECTRICAL_PANEL
  - SOLAR_SUPPORT
  - METAL_FURNITURE

base_materials:
  - COLD_ROLLED_STEEL
  - HOT_ROLLED_STEEL
  - AUTOMOTIVE_STEEL
  - STRUCTURAL_STEEL
  - HIGH_STRENGTH_STEEL

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY
  - WELDABILITY
  - PAINTABILITY
  - SURFACE_QUALITY
  - LUBRICITY
  - WHITE_RUST_RESISTANCE

post_treatments:
  - NH
  - NP
  - CL
  - CE
  - NY
  - NE
  - NC
  - NW
  - LP
  - LM

source_documents:
  - 2025 Galvanized Steel.pdf

primary_source:
  - 2025 Galvanized Steel.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO Galvanized Steel Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO hot-dip galvanized steel.

This file should be loaded after:

```text
knowledge/posco/coated/index.md
```

selects:

```text
GALVANIZED_STEEL
```

as a relevant product family.

The primary responsibility of this file is to determine:

```text
GI
vs
GA
vs
GI_H
```

and to identify relevant:

```text
BASE MATERIAL
COATING REQUIREMENT
POST-TREATMENT
SURFACE REQUIREMENT
APPLICATION
```

before detailed specification review.

This file does NOT automatically approve:

```text
exact coating weight
exact substrate grade
exact post-treatment
exact dimensions
final welding condition
final forming condition
```

---

# 2. Core Product Positioning

POSCO hot-dip galvanized steel is used across:

```text
AUTOMOTIVE
ELECTRICAL EQUIPMENT
HOME APPLIANCE
CONSTRUCTION
CIVIL ENGINEERING
INDUSTRIAL APPLICATIONS
```

The product family combines:

```text
CORROSION_RESISTANCE
FORMABILITY
WELDABILITY
PAINTABILITY
```

with zinc-based surface protection.

The correct intelligence chain is:

```text
APPLICATION
↓
BASE STEEL
↓
CORROSION REQUIREMENT
↓
FORMING / WELDING / PAINTING REQUIREMENT
↓
GI / GA / GI_H
↓
POST-TREATMENT
↓
COATING WEIGHT
↓
DIMENSION / PROCESS CHECK
↓
ENGINEERING VALIDATION
```

---

# 3. Product Architecture

```text
GALVANIZED_STEEL
│
├── GI
│   └── cold-rolled-base hot-dip galvanized steel
│
├── GA
│   └── galvannealed Zn-Fe alloy coated steel
│
└── GI_H
    └── hot-rolled-base hot-dip galvanized steel
```

Do not treat these as equivalent products.

---

# 4. Core Difference

## GI

```text
COLD_ROLLED_BASE
+
Zn COATING
```

Strong routing characteristics:

```text
CORROSION_RESISTANCE
FORMABILITY
SURFACE_QUALITY
GENERAL_APPLICATION_FLEXIBILITY
```

---

## GA

```text
COLD_ROLLED_BASE
+
Zn COATING
+
Fe-Zn ALLOYING
```

Strong routing characteristics:

```text
WELDABILITY
PAINTABILITY
PAINTED_CORROSION_RESISTANCE
AUTOMOTIVE_APPLICATION
```

---

## GI_H

```text
HOT_ROLLED_BASE
+
Zn COATING
```

Strong routing characteristics:

```text
STRUCTURAL_USE
BUILDING
PIPE
ELECTRICAL_PANEL
SOLAR_SUPPORT
```

---

# 5. Manufacturing Concept

The hot-dip galvanizing process generally includes:

```text
BASE STEEL
↓
PRETREATMENT
↓
ANNEALING
↓
COOLING
↓
ZINC BATH
↓
AIR KNIFE
↓
SKIN PASS
↓
POST-TREATMENT
↓
INSPECTION
↓
OILING
```

For GA an additional alloying step is applied:

```text
Zn COATING
↓
REHEATING
↓
Fe / Zn DIFFUSION
↓
Zn-Fe ALLOY LAYER
```

This alloying step is a major reason why GA must be handled separately from GI.

---

# 6. Zinc Protection Principle

Zinc coating protects the steel substrate through:

```text
BARRIER PROTECTION
+
SACRIFICIAL PROTECTION
```

The galvanized product should therefore be interpreted as a system consisting of:

```text
BASE STEEL
+
ZINC-BASED COATING
+
OPTIONAL POST-TREATMENT
```

Do not evaluate corrosion resistance from the base steel alone.

---

# 7. GI

Canonical code:

```text
GI
```

Full name:

```text
HOT_DIP_GALVANIZED_STEEL
```

Primary base:

```text
COLD_ROLLED_BASE
```

Product structure:

```text
POST-TREATMENT
↓
Zn COATING
↓
COLD-ROLLED STEEL
```

---

# 8. GI Product Character

The source describes GI as being produced from cold-rolled base steel.

During solidification of molten zinc:

```text
Zn crystal growth is controlled
↓
fine surface structure is formed
↓
surface becomes uniform
```

This supports applications requiring:

```text
CORROSION_RESISTANCE
FORMABILITY
SURFACE_APPEARANCE
PAINTING
```

---

# 9. GI Primary Applications

Source-supported GI applications include:

```text
METAL_FURNITURE
HOME_APPLIANCE_INNER_PANEL
HOME_APPLIANCE_OUTER_PANEL
PREPAINTED_STEEL_BASE
AUTOMOTIVE_INNER_PANEL
AUTOMOTIVE_OUTER_PANEL
BUILDING_MATERIAL
PIPE
```

This is a broad-use coated product.

---

# 10. GI Strong Routing Conditions

Use GI as a primary candidate when:

```text
GENERAL_CORROSION_PROTECTION
+
FORMABILITY
+
BROAD_APPLICATION
```

are required.

Strong signals:

```text
home appliance panel
general automotive galvanized panel
painted steel substrate
metal furniture
general building material
```

---

# 11. GI Negative Routing Conditions

Do not automatically use GI when:

```text
EXTREME_CORROSION
HIGH_SALINITY
SEVERE_CUT_EDGE_CORROSION
```

dominates.

Evaluate:

```text
POSMAC_3_0
POSMAC_SUPER
```

through the parent coated router.

---

# 12. GA

Canonical code:

```text
GA
```

Full name:

```text
GALVANNEALED_STEEL
```

Structure:

```text
POST-TREATMENT
↓
Zn-Fe ALLOY COATING
↓
COLD-ROLLED BASE STEEL
```

---

# 13. GA Alloying Concept

After zinc coating:

```text
REHEATING
↓
Fe / Zn DIFFUSION
↓
Zn-Fe ALLOY LAYER
```

is formed.

This differentiates GA from ordinary GI.

---

# 14. GA Product Character

The source describes GA as having stronger:

```text
WELDABILITY
PAINTABILITY
```

than ordinary zinc-coated steel.

The Fe-containing alloy layer also supports:

```text
PAINTED_CORROSION_RESISTANCE
```

Therefore GA is especially relevant for:

```text
PAINTED
+
WELDED
```

components.

---

# 15. GA Primary Applications

Source-supported:

```text
AUTOMOTIVE_INNER_PANEL
AUTOMOTIVE_OUTER_PANEL
HOME_APPLIANCE_INNER_PANEL
HOME_APPLIANCE_OUTER_PANEL
```

The strongest routing domain is:

```text
AUTOMOTIVE_BODY
```

---

# 16. GA Strong Route

```text
AUTOMOTIVE_PANEL
+
PAINTABILITY
+
WELDABILITY
+
CORROSION_RESISTANCE
→ GA
```

Possible components include:

```text
DOOR
BODY_PANEL
INNER_PANEL
OUTER_PANEL
STRUCTURAL_BODY_COMPONENT
```

but exact substrate availability must still be verified.

---

# 17. GA Formability Caution

GA has a harder and less ductile alloy coating layer than ordinary GI.

Therefore severe drawing may produce:

```text
POWDERING
```

from brittle alloy-layer portions.

The source notes that powdering tendency can be influenced by:

```text
COATING_WEIGHT
OILING
PRESS_CONDITION
```

Do not assume:

```text
GA FORMABILITY = GI FORMABILITY
```

---

# 18. GA Powdering Rule

If:

```text
DEEP_DRAWING
+
GA
```

is required:

check:

```text
coating amount
lubrication
press condition
component geometry
substrate grade
```

before final recommendation.

Return:

```text
FORMING_VALIDATION_REQUIRED
```

when necessary.

---

# 19. GI_H

Canonical code:

```text
GI_H
```

Full internal meaning:

```text
HOT_ROLLED_BASE_HOT_DIP_GALVANIZED_STEEL
```

Base steel:

```text
HOT_ROLLED_STEEL
```

---

# 20. GI_H Primary Applications

Source-supported applications:

```text
BUILDING_MATERIAL
PIPE
ELECTRICAL_PANEL
HOME_APPLIANCE_INNER_PANEL
SOLAR_SUPPORT
```

GI(H) is therefore primarily a:

```text
STRUCTURAL / INDUSTRIAL GALVANIZED ROUTE
```

rather than a passenger-car outer-panel route.

---

# 21. GI_H Strong Routing

```text
HOT_ROLLED_BASE
+
CORROSION_PROTECTION
+
STRUCTURAL_APPLICATION
→ GI_H
```

Examples:

```text
PIPE
BUILDING_COMPONENT
SOLAR_SUPPORT
ELECTRICAL_PANEL
```

---

# 22. GI vs GI_H

The key distinction is not only corrosion performance.

It is:

```text
BASE MATERIAL
```

Use:

```text
GI
→ cold-rolled-base route
```

Use:

```text
GI_H
→ hot-rolled-base route
```

Therefore:

```text
APPLICATION
+
BASE_STEEL_REQUIREMENT
```

must be known.

---

# 23. GI vs GA

## GI

Prefer when:

```text
GENERAL_CORROSION
FORMABILITY
SURFACE_UNIFORMITY
BROAD_USE
```

dominate.

## GA

Prefer when:

```text
WELDABILITY
PAINTABILITY
PAINTED_CORROSION
```

are particularly important.

---

# 24. Selection Matrix

| Condition | Primary Route |
|---|---|
| General cold-rolled galvanized application | GI |
| Automotive painted/welded panel | GA |
| Hot-rolled structural galvanized component | GI_H |
| General appliance panel | GI |
| Automotive coated body panel | GI or GA |
| Building/pipe hot-rolled base | GI_H |
| Solar support, ordinary environment | GI_H |
| Severe solar corrosion | consider PosMAC 3.0 |
| Extreme coastal solar | consider PosMAC Super |

---

# 25. Base Steel Is Separate From Coating

A coated product must preserve substrate identity.

Example:

```text
590DP + GI
```

means:

```text
590DP
= substrate strength / forming system

GI
= surface corrosion protection
```

Therefore the correct Product Brain chain is:

```text
AUTOMOTIVE COMPONENT
↓
AUTOMOTIVE STEEL FAMILY
↓
SUBSTRATE GRADE
↓
COATING REQUIREMENT
↓
GI / GA
```

Do not allow `galvanized.md` to replace `automotive-steel.md`.

---

# 26. Automotive Cross-Domain Routing

Example:

```text
DOOR_OUTER
```

may require:

```text
../automotive/automotive-steel.md
+
./galvanized.md
```

First decide:

```text
substrate strength/formability
```

Then:

```text
GI or GA
```

---

# 27. AHSS Coating Availability

POSCO's automotive product knowledge shows that coated availability varies by substrate grade.

Examples include combinations such as:

```text
CR
EG
GI
GA
```

but not every grade supports every coating.

Therefore:

```text
AUTOMOTIVE_GRADE
+
GI / GA
```

must always trigger:

```text
SUBSTRATE_COATING_AVAILABILITY_CHECK
```

---

# 28. Example — DP Steel

Possible combinations in the approved automotive product source vary across:

```text
490DP
590DP
780DP
980DP variants
```

Some support:

```text
GI
GA
```

while others differ.

Do not infer:

```text
ALL_DP → GI + GA
```

---

# 29. Coating Weight

Coating amount is a separate design variable.

Selection considerations include:

```text
TARGET_DURABILITY
CORROSION_ENVIRONMENT
FORMING_REQUIREMENT
WELDING_REQUIREMENT
FINAL_USE
```

General source direction:

```text
HIGHER_CORROSION_DEMAND
→ heavier coating may be considered
```

but:

```text
FORMABILITY
+
WELDABILITY
```

may favor lower coating amounts.

---

# 30. Coating Weight Rule

Forbidden:

```text
MORE_COATING = ALWAYS_BETTER
```

Correct:

```text
CORROSION
vs
FORMING
vs
WELDING
vs
APPLICATION
```

trade-off.

Exact coating weight requires engineering/customer-order confirmation.

---

# 31. White Rust vs Red Rust

The source distinguishes:

```text
WHITE_RUST
```

on zinc coating from:

```text
RED_RUST
```

associated with substrate corrosion.

These must remain separate in data modeling.

---

# 32. White Rust Behavior

The source indicates white-rust occurrence is strongly influenced by:

```text
POST_TREATMENT
```

and does not simply increase/decrease according to zinc coating amount in the same way as substrate red-rust protection.

Therefore:

```text
WHITE_RUST_RESISTANCE
```

should not be modeled only through coating weight.

---

# 33. Red Rust Behavior

The source indicates increased zinc coating amount generally delays substrate red-rust development in the referenced tests.

However:

```text
LAB_TEST
≠
FIELD_SERVICE_LIFE
```

Do not convert coating-weight test behavior into an unsupported lifetime claim.

---

# 34. Post-Treatment Architecture

The catalog includes multiple post-treatment families such as:

```text
NH
NP
CL
CE
NY
NE
NC
NW
LP
LM
```

These post-treatments provide functions including:

```text
CORROSION_RESISTANCE
LUBRICITY
WELDABILITY
ENVIRONMENTAL_COMPLIANCE
```

Post-treatment must be modeled separately from:

```text
GI / GA / GI_H
```

---

# 35. Post-Treatment Examples

The source lists names/functions including concepts such as:

```text
NON_CHROMATE
CHROMATE_LIGHT
CHROMATE_ECO
NON_CHROMATE_HYBRID
NON_CHROMATE_EXCELLENT
NON_CHROMATE_WELDABILITY
LUBRICATION_PHOSPHATE
LUBRICATION_METALLIC
```

Exact availability varies by:

```text
product
plant
application
```

Do not infer universal availability.

---

# 36. Cr-Free Treatment

The manufacturing description indicates Cr-free resin treatment may be applied to:

```text
prevent white rust
+
improve corrosion resistance
```

The ordering guidance also notes:

```text
Cr treatment
or
Cr-free treatment
```

can help suppress white rust.

---

# 37. Lubricity

Lubricity is relevant when:

```text
PRESS_FORMING
DRAWING
```

are important.

Potential post-treatment functions include:

```text
LUBRICATION
```

but exact selection must be based on:

```text
forming process
customer oil
press condition
surface requirement
```

---

# 38. Oiling

Oiling is separate from post-treatment.

The source allows oil amount to be selected according to customer use conditions.

Important caution:

```text
NO_POST_TREATMENT
+
NO_OILING
```

may increase white-rust risk.

Therefore this combination should trigger:

```text
WHITE_RUST_RISK_WARNING
```

---

# 39. Formability

The source describes continuous hot-dip galvanized GI as having:

```text
strong coating adhesion
```

with only a thin brittle Fe-Zn intermediate alloy layer.

Therefore coating peeling during drawing is limited under the described conditions.

The source also describes modern vertical-furnace products as having forming performance approaching cold-rolled material.

---

# 40. Formability Decision

For:

```text
SEVERE_DRAWING
```

prefer careful evaluation of:

```text
GI
```

versus:

```text
GA
```

because GA's harder alloy layer may create powdering risk.

---

# 41. Paintability

Paint performance depends strongly on:

```text
PAINT_PRETREATMENT
```

The source emphasizes proper degreasing before:

```text
PHOSPHATE
CHROMATE
NON_CR
```

pretreatment.

Direct painting without appropriate preparation should not be assumed to provide optimal adhesion.

---

# 42. Painting Guardrail

Forbidden:

```text
GALVANIZED
→ paint directly without pretreatment
```

Recommended route:

```text
GALVANIZED
↓
DEGREASING
↓
CHEMICAL_PRETREATMENT
↓
PAINT
```

depending on customer process.

---

# 43. GA Paintability

The source particularly associates GA's Zn-Fe alloy layer with good:

```text
PAINTABILITY
```

and:

```text
PAINTED_CORROSION_RESISTANCE
```

This is a key reason for GA's automotive routing.

---

# 44. Welding

Hot-dip galvanized material behaves differently from bare cold-rolled steel during resistance welding because zinc:

```text
has high electrical conductivity
+
can adhere to electrodes
```

Therefore welding parameters and electrode management matter.

---

# 45. Resistance Welding Caution

The source states that zinc can adhere to:

```text
ELECTRODES
```

during resistance welding.

Therefore:

```text
PERIODIC_ELECTRODE_CLEANING
```

may be required.

Detailed welding process design remains:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 46. Seam Welding

The source notes the use of:

```text
KNURL-GEAR DRIVE
```

as a way to extend electrode life in seam welding.

This is process guidance, not a mandatory universal requirement.

---

# 47. Brazing Caution

The source specifically cautions against:

```text
HIGH_TEMPERATURE_BRAZING
```

and especially:

```text
GA BRAZING
```

This caution must be preserved in engineering responses.

---

# 48. Welding Fume

Welding galvanized steel can generate:

```text
FUME
```

The source instructs that welding should occur in:

```text
WELL_VENTILATED_ENVIRONMENT
```

This is a process/safety requirement, not a product-performance attribute.

---

# 49. Soldering

The source states ordinary hot-dip galvanized products can be difficult to solder using:

```text
GENERAL_FLUX
```

Therefore solderability must not be assumed.

---

# 50. Storage

Important storage risks include:

```text
MOISTURE
WATER_INGRESS
TEMPERATURE_DIFFERENCE
LONG_STORAGE
```

These can promote:

```text
WHITE_RUST
```

---

# 51. Storage Rules

Preferred storage:

```text
DRY
VENTILATED
INDOOR
```

Avoid:

```text
MOIST_AREA
WATER_EXPOSURE
EXTREME_TEMPERATURE_DIFFERENCE
```

If packaging becomes damaged:

```text
REPAIR_PACKAGING
```

If moisture penetrates:

```text
DRY_IMMEDIATELY
```

---

# 52. Inventory Rule

The source advises minimizing long inventory periods because:

```text
WHITE_RUST
```

may gradually develop even with packaging.

Therefore coated product handling should favor:

```text
SHORT_STORAGE_PERIOD
```

where possible.

---

# 53. Processing Lubricant Caution

Lubricants containing additives that attack zinc may:

```text
CORRODE_ZINC
```

Therefore use:

```text
NON_CORROSIVE_LUBRICANT
```

where possible.

If corrosive processing fluid must be used:

```text
DEGREASE_IMMEDIATELY
+
APPLY_CORROSION_PROTECTION
```

after processing.

---

# 54. Processing Environment

Avoid forming in environments with:

```text
HIGH_HUMIDITY
SO2
HEAVY_SMOKE / POLLUTANTS
```

where possible.

These conditions may negatively affect galvanized surfaces.

---

# 55. Aging

The source notes that steel properties may change with time and may result in:

```text
REDUCED_FORMABILITY
STRETCHER_STRAIN
FLUTING
```

for susceptible grades.

Therefore non-aging steel should be selected where those effects are unacceptable.

This behavior is primarily related to substrate grade, not coating family alone.

---

# 56. Use-Condition Guardrail

The catalog explicitly cautions against using material for an application different from the purpose specified at ordering.

Therefore:

```text
ORDERED_APPLICATION
≠
NEW_APPLICATION
```

should trigger:

```text
APPLICATION_REVALIDATION_REQUIRED
```

---

# 57. Manufacturing Range

The source provides separate production-range maps for:

```text
GI
GA
GI_H
```

and different:

```text
CQ
DQ
DDQ
EDDQ
STRUCTURAL
HIGH_STRENGTH
```

classes.

Do not reduce these diagrams to one global:

```text
MIN_THICKNESS
MAX_THICKNESS
MIN_WIDTH
MAX_WIDTH
```

for the family.

---

# 58. Manufacturing Range Rule

Exact availability depends on:

```text
PRODUCT
GRADE
SPECIFICATION
POST_TREATMENT
EDGE
THICKNESS
WIDTH
PLANT
```

Therefore:

```text
SIZE_AVAILABILITY_CHECK_REQUIRED
```

for exact commercial requests.

---

# 59. High-Strength GI Rule

The source specifically states that:

```text
TS ≥ 490 MPa
```

high-strength GI manufacturing-range inquiries should be coordinated through the appropriate inquiry/quality process.

Therefore the Product Brain should NOT assume standard range availability for all high-strength galvanized grades.

---

# 60. Mill Edge vs Slit Edge

Manufacturing range can differ according to:

```text
MILL_EDGE
vs
SLIT_EDGE
```

The source notes Slit Edge may reduce available width relative to the displayed Mill Edge range for certain products.

Therefore edge requirement must be included in exact size validation.

---

# 61. Ordering Inputs

Before exact product recommendation collect:

```text
application
product family
base steel
grade
required mechanical properties
coating type
coating amount
post-treatment
surface condition
oiling
thickness
width
edge condition
forming process
welding process
painting process
corrosion environment
```

---

# 62. Coating Selection Inputs

Before selecting exact zinc coating amount:

```text
target durability
environment
forming severity
welding requirement
paint requirement
final application
```

must be known.

If missing:

```text
COATING_WEIGHT_UNKNOWN
```

---

# 63. Post-Treatment Selection Inputs

Before selecting exact post-treatment:

```text
white rust requirement
painting process
welding
lubricity
anti-fingerprint requirement
environmental requirement
storage condition
```

must be known.

Return:

```text
POST_TREATMENT_UNKNOWN
```

if insufficient.

---

# 64. GI Routing Example — Home Appliance

Input:

```text
HOME_APPLIANCE
+
INNER_OUTER_PANEL
+
CORROSION_RESISTANCE
+
FORMABILITY
```

Primary:

```text
GI
```

Possible additional evaluation:

```text
EG
POSMAC_1_5
```

depending on:

```text
surface quality
paint
anti-fingerprint
corrosion target
```

---

# 65. GA Routing Example — Automotive Body

Input:

```text
AUTOMOTIVE
+
BODY_PANEL
+
RESISTANCE_WELDING
+
PAINTING
+
CORROSION_RESISTANCE
```

Primary candidate:

```text
GA
```

Next checks:

```text
substrate grade
forming severity
coating availability
coating weight
powdering risk
```

---

# 66. GI Routing Example — Automotive

Input:

```text
AUTOMOTIVE
+
PANEL
+
CORROSION_RESISTANCE
+
FORMABILITY
```

Candidate:

```text
GI
```

But if:

```text
WELDABILITY
+
PAINTABILITY
```

become dominant:

```text
GA
```

may receive higher priority.

---

# 67. GI_H Example — Solar Support

Input:

```text
SOLAR_SUPPORT
+
HOT_ROLLED_STRUCTURAL_BASE
+
GENERAL_OUTDOOR_CORROSION
```

Candidate:

```text
GI_H
```

If:

```text
SEVERE_CORROSION
+
CUT_EDGE
```

route upward to:

```text
POSMAC_3_0
```

If:

```text
COASTAL
+
HIGH_SALINITY
```

evaluate:

```text
POSMAC_SUPER
```

---

# 68. GI_H Example — Pipe

Input:

```text
STRUCTURAL_PIPE
+
HOT_ROLLED_BASE
+
CORROSION_PROTECTION
```

Primary:

```text
GI_H
```

Do not confuse with:

```text
OIL_AND_GAS_PIPELINE
```

which belongs to the API / line-pipe material domain.

---

# 69. GI/GA vs EG

Possible routing:

```text
HOT_DIP_ROUTE
→ GI / GA
```

```text
HIGH_SURFACE_QUALITY
+
LOW_THERMAL_PROCESS_IMPACT
→ EG candidate
```

Do not assume EG is technically interchangeable with GI/GA.

Load:

```text
./electro-galvanized.md
```

for detailed comparison.

---

# 70. GI vs PosMAC 1.5

Possible transition hypothesis:

```text
GI
↓
need higher corrosion resistance
but retain:
surface quality
welding
forming
↓
POSMAC_1_5 candidate
```

This is:

```text
MATERIAL_SUBSTITUTION_CANDIDATE
```

not automatic substitution.

---

# 71. GI vs PosMAC 3.0

If the customer problem is:

```text
SEVERE_OUTDOOR_CORROSION
+
CUT_EDGE_CORROSION
```

GI may become insufficient.

Route comparison:

```text
GI
vs
POSMAC_3_0
```

Exact performance comparison must preserve test conditions.

---

# 72. Negative Routing Rules

## Automotive ≠ GA automatically

Some automotive substrates use:

```text
GI
GA
EG
```

Select according to component/process.

---

## Building ≠ GI_H automatically

If extreme environmental corrosion is present:

```text
POSMAC
```

may be more relevant.

---

## High corrosion ≠ heavy zinc coating automatically

Evaluate:

```text
coating amount
vs
PosMAC alternative
vs
manufacturing requirements
```

---

## More coating ≠ better product

High coating amount can create:

```text
FORMING
WELDING
```

trade-offs.

---

## GA ≠ best forming product

GA's alloy layer can create:

```text
POWDERING
```

under severe drawing conditions.

---

# 73. Product Selection Matrix

```text
GENERAL CORROSION
+
COLD-ROLLED BASE
→ GI

AUTOMOTIVE
+
WELD
+
PAINT
→ GA

HOT-ROLLED STRUCTURAL BASE
+
GENERAL CORROSION
→ GI_H

SEVERE OUTDOOR
+
CUT EDGE
→ leave GALVANIZED family
→ evaluate POSMAC_3_0

EXTREME COASTAL
→ evaluate POSMAC_SUPER
```

---

# 74. Product Candidate Object

Recommended:

```yaml
product_family: GALVANIZED_STEEL

application: AUTOMOTIVE_BODY

component:
  - BODY_PANEL

base_material:
  family: AUTOMOTIVE_STEEL
  grade: UNKNOWN

requirements:
  - CORROSION_RESISTANCE
  - WELDABILITY
  - PAINTABILITY

subfamily_candidates:
  - product: GA
    priority: P1
    reason:
      - automotive body application
      - welding required
      - painting required

  - product: GI
    priority: P2
    reason:
      - general corrosion protection
      - substrate availability must be checked

missing_information:
  - substrate_grade
  - coating_weight
  - forming_severity
  - post_treatment

final_status:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 75. Structural Product Object

```yaml
product_family: GALVANIZED_STEEL

application: SOLAR_SUPPORT

base_material:
  HOT_ROLLED

environment:
  OUTDOOR_GENERAL

requirements:
  - CORROSION_RESISTANCE
  - STRUCTURAL_USE

subfamily_candidates:
  - product: GI_H
    priority: P1

escalation_rule:
  severe_corrosion:
    route_to: POSMAC_3_0

  extreme_coastal:
    route_to: POSMAC_SUPER
```

---

# 76. Daily Intelligence Mode

For normal daily intelligence:

Do NOT retrieve:

```text
exact coating weight
post-treatment code
manufacturing size table
welding parameter
```

Preferred output:

```text
GALVANIZED_STEEL
→ GI / GA / GI_H direction
```

Recommended configuration:

```yaml
daily_galvanized_analysis:
  allow_subfamily_selection: true
  allow_exact_coating_weight: false
  allow_exact_post_treatment: false
  allow_dimension_lookup: false
  allow_pdf_lookup: false
```

---

# 77. Marketing Mode

Marketing analysis may include:

```text
product family
GI / GA / GI_H route
customer application
relative benefit
replacement hypothesis
customer questions
```

Example:

```text
Customer is redesigning a painted and spot-welded
automotive body component.

GA may be relevant because the application combines:
welding, painting and corrosion requirements.

Next checks:
substrate grade, forming severity,
coating amount and customer paint process.
```

---

# 78. Engineering Mode

Engineering analysis may retrieve:

```text
substrate grade
mechanical properties
coating amount
post-treatment
surface finish
oiling
dimensions
edge type
forming requirement
welding condition
painting pretreatment
```

and may inspect:

```text
2025 Galvanized Steel.pdf
```

directly.

---

# 79. Corrosion Test Guardrail

Corrosion tests must retain:

```text
TEST_METHOD
COATING_AMOUNT
POST_TREATMENT
EXPOSURE_TIME
TEST_CONDITION
```

Do not store only:

```text
corrosion resistance = good
```

for engineering-level analysis.

---

# 80. Numerical Data Guardrail

If exact coating weight, dimensions or mechanical properties are requested:

```text
SOURCE_LOOKUP_REQUIRED
```

because many values differ by:

```text
grade
product
plant
post-treatment
size
```

Do not infer them from family name.

---

# 81. Knowledge Hierarchy

For galvanized-steel claims use source priority:

```text
1. 2025 Galvanized Steel.pdf
2. application-specific POSCO product guide
3. parent coated/index.md
```

For substrate properties:

```text
use substrate product MD
```

Example:

```text
590DP mechanical properties
→ automotive/automotive-steel.md

GI coating behavior
→ coated/galvanized.md
```

---

# 82. Product Hallucination Guardrail

Never invent:

```text
coating weight
post-treatment availability
substrate compatibility
width
thickness
mechanical property
corrosion test result
welding parameter
service life
customer approval
```

If unsupported:

```text
UNKNOWN
```

---

# 83. Unknown States

Supported states:

```text
GALVANIZED_SUBFAMILY_UNKNOWN

BASE_STEEL_UNKNOWN

SUBSTRATE_GRADE_UNKNOWN

COATING_WEIGHT_UNKNOWN

POST_TREATMENT_UNKNOWN

SURFACE_FINISH_UNKNOWN

FORMING_SEVERITY_UNKNOWN

WELDING_REQUIREMENT_UNKNOWN

PAINT_PROCESS_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

SUBSTRATE_COATING_AVAILABILITY_CHECK

FORMING_VALIDATION_REQUIRED

WELDING_PROCEDURE_REVIEW_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 84. Retrieval Keywords

```text
GI
GA
GI(H)
hot-dip galvanized
galvannealed
용융아연도금
합금화아연도금
열연용융아연도금
자동차 도금강판
아연도금강판
건축 아연도금
태양광 지지대
도장강판 소재
Zn coating
Zn-Fe
```

Keywords are retrieval aids only.

---

# 85. Routing Algorithm

```pseudo
function route_galvanized(context):

    identify base_material
    identify application

    if base_material == HOT_ROLLED
       and application in [
          BUILDING,
          PIPE,
          SOLAR_SUPPORT,
          STRUCTURAL
       ]:
        candidate = GI_H

    else if application == AUTOMOTIVE
       and WELDABILITY
       and PAINTABILITY:
        candidate = GA

    else if general_corrosion_requirement:
        candidate = GI

    if severe_corrosion
       and cut_edge_exposure:
        escalate_to POSMAC_3_0

    if extreme_coastal
       or high_salinity:
        evaluate POSMAC_SUPER

    verify:
        substrate_grade
        coating_weight
        post_treatment
        forming
        welding
        dimension

    return candidate
```

---

# 86. Example — Automotive DP + GA

Input:

```text
CUSTOMER:
automotive manufacturer

COMPONENT:
structural body member

SUBSTRATE:
590DP

REQUIREMENTS:
spot welding
painting
corrosion resistance
```

Reasoning:

```text
590DP
↓
automotive substrate
↓
paint + welding
↓
GA candidate
```

Required next check:

```text
590DP GA availability
```

Do not assume coating availability solely from this file.

---

# 87. Example — Appliance GI

```yaml
industry: HOME_APPLIANCE

application:
  - OUTER_PANEL

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY
  - PAINTABILITY

product_candidate:
  family: GALVANIZED_STEEL
  subfamily: GI

post_treatment:
  status: UNKNOWN

missing_information:
  - surface_requirement
  - paint_process
  - anti_fingerprint_requirement
```

---

# 88. Example — Severe Solar Environment

Input:

```text
solar support
+
hot-rolled base
+
general outdoor environment
```

route:

```text
GI_H
```

But:

```text
solar support
+
severe cut-edge corrosion
```

route:

```text
POSMAC_3_0 evaluation
```

And:

```text
solar support
+
coastal high salinity
```

route:

```text
POSMAC_SUPER evaluation
```

---

# 89. Final Knowledge Chain

```text
CUSTOMER SIGNAL
↓
APPLICATION
↓
BASE STEEL
↓
CORROSION REQUIREMENT
↓
FORMING
+
WELDING
+
PAINTING
↓
GALVANIZED_STEEL
↓
GI / GA / GI_H
↓
SUBSTRATE COMPATIBILITY
↓
COATING WEIGHT
↓
POST-TREATMENT
↓
SIZE / EDGE
↓
ENGINEERING VALIDATION
↓
MARKETING OPPORTUNITY
```

---

# 90. Final Rule

The correct objective is NOT:

```text
MAXIMUM ZINC COATING
```

or:

```text
GA FOR EVERY AUTOMOTIVE APPLICATION
```

The correct objective is:

```text
RIGHT BASE STEEL
+
RIGHT GALVANIZED SUBFAMILY
+
RIGHT COATING AMOUNT
+
RIGHT POST-TREATMENT
+
RIGHT FABRICATION PROCESS
```

The preferred reasoning order is:

```text
APPLICATION
↓
BASE STEEL
↓
PROCESS REQUIREMENT
↓
GI / GA / GI_H
↓
DETAILED COATING SPEC
```

not:

```text
GI / GA FIRST
↓
JUSTIFY LATER
```

The responsibility of this file ends at:

```text
DEFENSIBLE GALVANIZED PRODUCT CANDIDATE
```

Final customer specification remains an engineering and product-quality decision.
