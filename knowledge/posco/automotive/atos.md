---
product_family: ATOS

name_ko: 자동차구조용 고강도강
name_en: POSCO ATOS / AuTOmobile Structural Steel

industry:
  - AUTOMOTIVE
  - MACHINERY

applications:
  - COMMERCIAL_VEHICLE
  - HEAVY_AUTOMOTIVE_STRUCTURE
  - HEAVY_EQUIPMENT_STRUCTURE

components:
  - TRUCK_FRAME
  - TRAILER_FRAME
  - COMMERCIAL_VEHICLE_FRAME
  - SPECIAL_PURPOSE_VEHICLE_FRAME
  - BOOM_ARM
  - CRANE_BOOM
  - WHEEL_DISC
  - STRUCTURAL_MEMBER

material_category:
  - HOT_ROLLED_STEEL
  - HIGH_STRENGTH_STRUCTURAL_STEEL

requirements:
  - HIGH_STRENGTH
  - HIGH_YIELD_STRENGTH
  - COLD_FORMABILITY
  - BENDABILITY
  - WELDABILITY
  - FATIGUE_RESISTANCE
  - IMPACT_RESISTANCE
  - WEIGHT_REDUCTION
  - STRUCTURAL_STABILITY

product_series:
  - ATOS540
  - ATOS590
  - ATOS780

supply_forms:
  - HR

source_documents:
  - 2026 ATOS.pdf
  - 2026 Hot Rolled Steel.pdf
  - 2025 Automotive Steel.pdf

primary_source:
  - 2026 ATOS.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO ATOS Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO ATOS.

ATOS is a high-strength hot-rolled structural steel family intended primarily for automotive structural applications such as:

```text
TRUCK_FRAME
TRAILER_FRAME
SPECIAL_PURPOSE_VEHICLE_FRAME
BOOM_ARM
WHEEL_DISC
```

This file should be loaded only after upstream routing identifies:

```text
AUTOMOTIVE
or
MACHINERY
```

together with a structural application requiring:

```text
HIGH_STRENGTH
+
COLD_FORMABILITY
+
WELDABILITY
+
WEIGHT_REDUCTION
```

This file answers:

```text
Is ATOS the correct POSCO product family?
```

and:

```text
Should ATOS540, ATOS590, or ATOS780 be evaluated?
```

It does NOT independently approve a final grade for a customer component.

---

# 2. Core Product Positioning

POSCO defines ATOS as:

```text
AuTOmobile Structural Steel
```

and describes the family as automotive structural steels having generally:

```text
TENSILE_STRENGTH > 500 MPa
YIELD_STRENGTH > 300 MPa
```

within the high-strength structural-steel concept.

POSCO's supplied ATOS guide identifies the commercial family:

```text
ATOS540
ATOS590
ATOS780
```

for structural applications.

---

# 3. Core Intelligence Chain

Use:

```text
CUSTOMER SIGNAL
↓
COMMERCIAL / HEAVY VEHICLE
↓
STRUCTURAL COMPONENT
↓
LOAD + STIFFNESS + WEIGHT REQUIREMENT
↓
HIGH-STRENGTH HOT-ROLLED STRUCTURAL STEEL
↓
ATOS
↓
540 / 590 / 780 CLASS
↓
THICKNESS + FORMING + WELDING CHECK
↓
ENGINEERING VALIDATION
```

Do not route:

```text
AUTOMOTIVE
→ ATOS
```

without structural-component evidence.

---

# 4. Material Design Concept

The automotive-steel catalog describes ATOS as a high-strength hot-rolled product with:

```text
nano-scale precipitates
+
fine ferritic grains
```

The material concept includes:

```text
PRECIPITATION_STRENGTHENING
FINE_GRAIN_STRUCTURE
```

which supports:

```text
HIGH_TENSILE_STRENGTH
IMPACT_RESISTANCE
FATIGUE_STABILITY
```

The source also states that ATOS is designed with low carbon to improve:

```text
COLD_FORMABILITY
WELDABILITY
```

while small additions of:

```text
Nb
Ti
Mo
```

are used to secure strength.

---

# 5. Primary Applications

Source-supported major applications include:

```text
COMMERCIAL_VEHICLE_FRAME
TRUCK_FRAME
TRAILER_FRAME
SPECIAL_PURPOSE_VEHICLE_FRAME
CRANE_BOOM
BOOM_ARM
WHEEL_DISC
```

The strongest source-backed ATOS780 applications are:

```text
BOOM_ARM
TRUCK_FRAME
TRAILER_FRAME
```

The dedicated ATOS guide explicitly associates ATOS780 with high strength, strong cold formability, and these applications.

---

# 6. Strong Routing Conditions

ATOS should be considered when all or most of the following are true:

```text
STRUCTURAL_COMPONENT
+
HOT_ROLLED_PRODUCT
+
HIGH_STRENGTH
+
COLD_FORMABILITY
+
WELDABILITY
+
WEIGHT_REDUCTION
```

Strong signal examples:

```text
truck frame lightweighting
trailer frame redesign
commercial vehicle structural upgrade
boom-arm weight reduction
special-purpose vehicle frame strength increase
```

---

# 7. Weak Routing Conditions

ATOS should NOT be selected from:

```text
HIGH_STRENGTH
```

alone.

High strength may instead route to:

```text
AUTOMOTIVE_STEEL
POS_TEN
SHIPBUILDING_PLATE
CONSTRUCTION_PLATE
```

depending on application.

---

# 8. ATOS vs Passenger-Car AHSS

This distinction is mandatory.

## Passenger-car crash/body component

Examples:

```text
SIDE_SILL
BUMPER_BEAM
A_PILLAR
BODY_IN_WHITE
CRASH_MEMBER
```

Primary route:

```text
AUTOMOTIVE_STEEL
```

Possible families:

```text
DP
TRIP
CP
MART
HPF
```

Do NOT default to ATOS.

---

## Commercial/heavy structural frame

Examples:

```text
TRUCK_FRAME
TRAILER_FRAME
COMMERCIAL_VEHICLE_FRAME
```

Primary route:

```text
ATOS
```

---

# 9. ATOS vs PosTen

This distinction is also critical.

## ATOS

Primary form:

```text
HOT_ROLLED COIL / SHEET
```

Strong applications:

```text
COMMERCIAL_VEHICLE_FRAME
TRUCK_FRAME
TRAILER_FRAME
WHEEL_DISC
```

---

## PosTen

Primary concept:

```text
HIGH_TENSILE_PLATE
```

Strong applications:

```text
HEAVY_EQUIPMENT
CRANE
HEAVY_BOOM
THICK_PLATE_STRUCTURE
```

Routing rule:

```text
vehicle / frame hot-rolled structural sheet
→ ATOS

heavy thick-plate structural application
→ POS_TEN
```

Do not select based only on the word:

```text
BOOM
```

Thickness and product form must be known.

---

# 10. ATOS Grade Architecture

Current canonical grades:

```text
ATOS540
ATOS590
ATOS780
```

Treat these as separate strength classes.

Do not automatically assume:

```text
ATOS780 is always better.
```

Higher strength may reduce thickness but can change:

```text
FORMABILITY
BENDING
WELDING
STIFFNESS
BUCKLING
DESIGN REQUIREMENTS
```

---

# 11. ATOS540

Canonical code:

```text
ATOS540
```

Source-supported minimum mechanical requirements include:

```text
TENSILE_STRENGTH ≥ 540 MPa
YIELD_STRENGTH ≥ 340 MPa
```

The dedicated guide also provides thickness-dependent elongation requirements and a 180° bending test with:

```text
inside radius = 1.5t
```

for the specified test direction.

---

# 11.1 ATOS540 Routing

Use ATOS540 as a candidate when:

```text
structural strength increase
```

is required, but the application does not necessarily justify the higher strength level of ATOS590 or ATOS780.

Possible use:

```text
conventional commercial vehicle frame
structural member
moderate lightweighting
```

Exact component suitability still requires customer specification.

---

# 12. ATOS590

Canonical code:

```text
ATOS590
```

Dedicated ATOS guide values:

```text
TENSILE_STRENGTH ≥ 590 MPa
YIELD_STRENGTH ≥ 420 MPa
```

The dedicated ATOS catalog is the primary authority for these values.

Important source note:

The separate 2026 Hot Rolled Steel catalog shows a different ATOS590 minimum yield-strength value in one section.

Therefore:

```text
SOURCE_CONFLICT_PRESENT
```

must be preserved.

Use:

```text
2026 ATOS.pdf
```

as the canonical product guide for ATOS-specific specification data, and do not silently reconcile differing figures across catalogs.

---

# 12.1 ATOS590 Routing

Consider ATOS590 when:

```text
ATOS540 strength insufficient
+
cold forming still important
+
structural lightweighting desired
```

Potential applications:

```text
COMMERCIAL_VEHICLE_FRAME
TRAILER_STRUCTURE
STRUCTURAL_MEMBER
```

Do not select merely because:

```text
590 MPa class
```

appears in a customer specification.

Check actual yield, elongation, bending, thickness and welding requirements.

---

# 13. ATOS780

Canonical code:

```text
ATOS780
```

This is the highest-strength ATOS grade explicitly represented as a core commercial family in the supplied dedicated guide.

Source-supported minimum requirements:

```text
TENSILE_STRENGTH ≥ 780 MPa
YIELD_STRENGTH ≥ 700 MPa
```

and the catalog associates ATOS780 with:

```text
HIGH_STRENGTH
EXCELLENT_COLD_FORMABILITY
TRUCK_FRAME
TRAILER_FRAME
BOOM_ARM
```

 

---

# 13.1 ATOS780 Representative Material Data

The dedicated guide provides an example tensile curve for 6 mm material showing representative values:

```text
YS = 759 MPa
TS = 814 MPa
EL = 21.1%
```

These are representative example data.

Store as:

```text
TYPICAL / REPRESENTATIVE
```

not:

```text
GUARANTEED_SPEC
```

The same page identifies:

```text
Ferritic Microstructure
+
Nano Precipitates
```

as the representative microstructure concept.

---

# 14. Grade Comparison

| Grade | Minimum TS | Minimum YS | Primary Routing Direction |
|---|---:|---:|---|
| ATOS540 | 540 MPa | 340 MPa | baseline high-strength structural |
| ATOS590 | 590 MPa | 420 MPa* | higher structural strength |
| ATOS780 | 780 MPa | 700 MPa | advanced lightweight / high-strength structural |

`*` Use the dedicated 2026 ATOS guide as primary source.

Do not turn this table into:

```text
540 < 590 < 780 = automatic upgrade path
```

because:

```text
FORMABILITY
STIFFNESS
BUCKLING
FATIGUE
WELDING
GEOMETRY
```

must also be considered.

---

# 15. Elongation

The source provides thickness-dependent elongation values.

Examples from the dedicated ATOS guide show different minimum elongation requirements according to:

```text
GRADE
+
THICKNESS RANGE
+
TEST SPECIMEN
```

Therefore:

```text
ELONGATION
```

must NOT be represented as one universal value per ATOS grade.

Store:

```yaml
elongation:
  value_type: THICKNESS_DEPENDENT
  source_lookup_required: true
```

when detailed engineering data are required.

---

# 16. Bendability

The dedicated guide specifies a bending condition for ATOS grades using:

```text
180° bending
inside radius = 1.5t
```

for the referenced test configuration.

Bendability is a major ATOS selection factor.

However:

```text
catalog bend test passed
```

does not guarantee:

```text
all customer forming geometries are acceptable
```

Actual forming evaluation may depend on:

```text
bend radius
edge condition
rolling direction
thickness
component geometry
forming sequence
```

---

# 17. Cold Formability

ATOS is specifically designed to retain useful cold-forming capability despite high strength.

Key reasons described in the source include:

```text
LOW_CARBON_DESIGN
+
MICROALLOY_STRENGTHENING
+
FINE_GRAIN_STRUCTURE
```

The automotive-steel source explicitly states that ATOS uses low-carbon design to improve:

```text
COLD_FORMABILITY
WELDABILITY
```

while Nb/Ti/Mo additions support strength.

---

# 18. Weight Reduction

A major ATOS business proposition is:

```text
HIGH_STRENGTH
→ THICKNESS_REDUCTION POSSIBILITY
→ WEIGHT_REDUCTION
```

But this relation must be handled cautiously.

The Hot Rolled Steel catalog explicitly notes that thickness reduction based on higher yield strength must also consider:

```text
ELASTIC_DEFLECTION
BUCKLING
```

and that reinforcing design may be necessary.

Therefore:

```text
higher strength
≠
automatic proportional thickness reduction
```

---

# 19. Historical Lightweighting Example

The POSCO automotive catalog provides an application example comparing ATOS540 with ATOS780 in commercial-vehicle frames.

Examples shown include:

```text
15-ton dump
24-ton cargo
```

with frame-design changes and reported weight-reduction examples of approximately:

```text
40%
42%
```

for those particular historical designs.

These figures must be stored as:

```text
APPLICATION_EXAMPLE
```

not:

```text
GENERAL_ATOS780_WEIGHT_REDUCTION
```

Never tell a customer:

```text
ATOS780 reduces frame weight by 40%
```

without replicating the relevant design conditions.

---

# 20. Weight-Reduction Intelligence Rule

Allowed:

```text
ATOS780 may support vehicle-frame lightweighting
through higher-strength structural design.
```

Not allowed:

```text
ATOS780 will reduce weight by 40%.
```

unless referring explicitly to the source application example.

---

# 21. Welding

Weldability is a major ATOS engineering consideration.

The source provides:

```text
recommended welding consumables
Ceq information
pre/post-heating guidance
heat-input information
```

for ATOS590 and ATOS780.

Exact welding recommendations should only be surfaced in:

```text
ENGINEERING_MODE
```

---

# 21.1 Welding Consumable Examples

The dedicated guide lists example AWS consumable classifications for ATOS590 and ATOS780, including solid-wire and flux-cored-wire options.

These are technical source examples.

Do not convert them into:

```text
mandatory welding consumable
```

for all customer processes.

---

# 21.2 Preheat / Postheat

The source indicates that preheating and post-heating are:

```text
typically unnecessary
```

for the referenced conditions.

This statement must retain its context.

Do not generalize it to:

```text
preheating is never required.
```

Customer welding procedure, thickness, restraint, ambient condition and heat input still matter.

---

# 22. Heat Input

The catalog includes welding heat-input guidance and an indicated test range/context.

Therefore exact welding proposal requires:

```text
WPS
JOINT_TYPE
THICKNESS
WELD_CONSUMABLE
HEAT_INPUT
RESTRAINT
```

Return:

```text
WELDING_PROCEDURE_REVIEW_REQUIRED
```

for final process recommendations.

---

# 23. Chemistry

The dedicated guide provides maximum chemistry requirements.

Examples include:

```text
C
Si
Mn
P
S
```

and alloy-design information.

However normal marketing intelligence should not load chemistry.

Exact chemistry should be retrieved only for:

```text
welding analysis
customer specification
equivalent-grade review
engineering evaluation
```

---

# 24. Chemistry Routing Rule

Default:

```text
DO NOT LOAD CHEMISTRY
```

Engineering query:

```text
LOAD CHEMISTRY
```

if needed.

---

# 25. Supply Form

The automotive-steel catalog lists ATOS540, ATOS590 and ATOS780 as:

```text
HR
```

with uncoated availability in that table.

Therefore canonical supply form in this knowledge base is:

```text
HOT_ROLLED
```

Do not assume:

```text
EG
GI
GA
```

availability for these ATOS grades from the provided sources.

---

# 26. Coating Guardrail

If the customer's application requires:

```text
GALVANIZED
COATED
CORROSION_RESISTANCE
```

do not automatically attach a galvanized coating to ATOS.

Instead:

```text
ATOS technical structural fit
+
separate corrosion / coating investigation
```

may be required.

Return:

```text
COATING_SOLUTION_REQUIRED
```

when necessary.

---

# 27. Thickness Ranges

The dedicated ATOS guide provides applied thickness ranges approximately:

```text
ATOS540
3.2–12.7 mm

ATOS590
3.2–12.7 mm

ATOS780
2.5–14.0 mm
```

for the product-property tables.

These should NOT automatically be treated as the complete current orderable range.

The source explicitly states:

```text
manufacturable sizes may change
and should be confirmed at ordering.
```

Therefore exact orderability requires:

```text
SIZE_AVAILABILITY_CHECK_REQUIRED
```

---

# 28. Width / Manufacturing Range

The ATOS guide provides manufacturing-range diagrams for:

```text
ATOS590
ATOS780
```

including thickness/width combinations.

Do not convert the diagram into a simplified permanent rule unless the exact table is programmatically extracted and versioned.

Use:

```text
MANUFACTURING_RANGE_SOURCE_LOOKUP_REQUIRED
```

for:

```text
exact thickness
exact width
orderability
```

questions.

---

# 29. Dimension Standard

The dedicated guide states that appearance, shape, dimensions, mass and tolerances follow:

```text
JIS G 3134
```

for the referenced ATOS product definition.

Do not assume this automatically satisfies every customer's dimensional standard.

---

# 30. Structural Design Considerations

ATOS selection should consider more than tensile strength.

Required design dimensions may include:

```text
YIELD_STRENGTH
TENSILE_STRENGTH
BENDING
STIFFNESS
BUCKLING
FATIGUE
IMPACT
WELDING
THICKNESS
COMPONENT_GEOMETRY
```

This is especially important for frame lightweighting.

---

# 31. Stiffness Guardrail

Increasing yield/tensile strength does not increase Young's modulus proportionally.

Therefore reducing thickness may negatively affect:

```text
ELASTIC_DEFLECTION
```

The POSCO hot-rolled catalog explicitly cautions that reinforcement design may be necessary for elastic deflection.

---

# 32. Buckling Guardrail

Buckling may occur within the elastic region and depends heavily on geometry.

Therefore:

```text
HIGHER_STRENGTH
```

alone cannot ensure:

```text
BUCKLING_PERFORMANCE
```

The source explicitly warns that structural reinforcement may also be needed for buckling.

---

# 33. Fatigue

The automotive-steel source associates ATOS's fine ferritic grain structure with:

```text
stable fatigue properties
```

and impact performance.

However:

```text
catalog fatigue positioning
```

does not equal a component fatigue-life guarantee.

For:

```text
frame durability
cyclic loading
boom fatigue
```

return:

```text
FATIGUE_VALIDATION_REQUIRED
```

---

# 34. Impact Resistance

Fine ferritic grains are described as supporting:

```text
IMPACT_RESISTANCE
```

in ATOS.

Final component impact performance still depends on:

```text
temperature
thickness
geometry
weld
notch
loading mode
```

Do not make a universal impact guarantee.

---

# 35. ATOS540 Routing

Recommended use when:

```text
HIGH_STRENGTH_STRUCTURAL
+
moderate strength upgrade
+
good forming required
```

Potential position:

```text
baseline ATOS structural route
```

Do not choose if customer explicitly requires:

```text
YS ≥ 700 MPa
```

or equivalent high-strength target.

---

# 36. ATOS590 Routing

Recommended when:

```text
greater strength than ATOS540
+
structural weight reduction
+
cold forming
+
welding
```

must be balanced.

Potentially useful for:

```text
COMMERCIAL_VEHICLE_FRAME
STRUCTURAL_MEMBER
```

but exact component evidence is required.

---

# 37. ATOS780 Routing

Strong routing conditions:

```text
TRUCK_FRAME
TRAILER_FRAME
BOOM_ARM
+
HIGH_STRENGTH
+
COLD_FORMABILITY
+
WEIGHT_REDUCTION
```

Source support for this route is direct.

---

# 38. Grade Selection Decision

## Moderate structural requirement

Possible:

```text
ATOS540
```

---

## Higher frame strength

Possible:

```text
ATOS590
```

---

## Maximum current ATOS family strength / aggressive lightweighting

Possible:

```text
ATOS780
```

But final selection requires:

```text
required YS
required TS
thickness
bend condition
weld condition
stiffness
buckling
fatigue
```

---

# 39. Grade Selection Inputs

Before selecting exact ATOS grade, collect:

```text
component
vehicle type
gross vehicle weight
load condition
required yield strength
required tensile strength
required elongation
required thickness
width
bend radius
forming direction
press capability
weld method
weld consumable
heat input
fatigue requirement
impact requirement
stiffness requirement
buckling requirement
corrosion requirement
customer specification
```

If these are incomplete:

```text
GRADE_UNKNOWN
```

---

# 40. Product Family Output

Example:

```yaml
product_family: ATOS

application:
  - COMMERCIAL_VEHICLE

component:
  - TRUCK_FRAME

requirements:
  - HIGH_STRENGTH
  - COLD_FORMABILITY
  - WELDABILITY
  - WEIGHT_REDUCTION

grade_candidates:
  - ATOS590
  - ATOS780

grade_selection:
  status: GRADE_UNKNOWN

missing_information:
  - target_yield_strength
  - required_thickness
  - bend_radius
  - frame_stiffness_requirement
  - welding_process
```

---

# 41. Example — Truck Frame Lightweighting

Input:

```text
Truck manufacturer redesigns chassis frame
to reduce vehicle weight.
```

Reasoning:

```text
COMMERCIAL_VEHICLE
↓
TRUCK_FRAME
↓
HIGH_STRENGTH
+
WEIGHT_REDUCTION
+
COLD_FORMABILITY
+
WELDABILITY
↓
ATOS
```

Candidate:

```text
ATOS590 / ATOS780
```

Need:

```text
design load
thickness
yield target
stiffness
buckling
forming
```

before exact grade selection.

---

# 42. Example — 15-Ton Dump Frame

The POSCO source includes an application example using:

```text
ATOS540
→ ATOS780
```

in a redesigned 15-ton dump-frame concept.

This is useful as:

```text
SOURCE_SUPPORTED_LIGHTWEIGHTING_CASE
```

but must not be converted into a general design prescription.

---

# 43. Example — Trailer Frame

Input:

```text
Trailer maker increases payload capacity
while targeting lower vehicle weight.
```

Possible route:

```text
TRAILER_FRAME
↓
HIGH_STRENGTH
+
WEIGHT_REDUCTION
↓
ATOS
```

ATOS780 may be a strong candidate if:

```text
HIGH_YIELD_STRENGTH
```

is also required.

Exact recommendation remains:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 44. Example — Boom Arm

Input:

```text
Special-purpose vehicle maker redesigns crane boom.
```

Routing question:

```text
Is the product form hot-rolled sheet/coil-based structural material
or thick plate?
```

If:

```text
HR structural application
```

then:

```text
ATOS780 candidate
```

If:

```text
heavy thick plate
```

then evaluate:

```text
POS_TEN
```

Do not route solely from the word:

```text
BOOM
```

---

# 45. Example — Passenger-Car Bumper Beam

Input:

```text
Passenger-car bumper-beam strength upgrade
```

Do NOT route by default:

```text
ATOS780
```

Primary route:

```text
AUTOMOTIVE_STEEL
```

with:

```text
MART
HPF
PHT
```

as possible families depending on manufacturing route.

---

# 46. Example — Wheel Disc

ATOS source material associates ATOS with:

```text
WHEEL_DISC
```

applications.

However automotive-steel `FB` may also be relevant to wheel-disc applications.

Therefore route:

```text
WHEEL_DISC
↓
ATOS / FB comparison required
```

and compare:

```text
strength
forming mechanism
hole expansion
product form
component design
```

before selection.

---

# 47. ATOS vs FB for Chassis

## FB

Strong when:

```text
HOLE_EXPANSION
STRETCH_FLANGEABILITY
```

are dominant.

## ATOS

Strong when:

```text
STRUCTURAL_HIGH_STRENGTH
WEIGHT_REDUCTION
FRAME_APPLICATION
```

are dominant.

Do not decide from:

```text
CHASSIS
```

alone.

---

# 48. ATOS vs HSLA

Both may be high-strength structural materials.

Use:

```text
component type
strength target
supply form
forming requirement
```

to differentiate.

ATOS has especially strong source-backed routing to:

```text
COMMERCIAL_VEHICLE_FRAME
TRUCK / TRAILER FRAME
BOOM ARM
```

---

# 49. Negative Routing Rules

## Generic automobile production expansion

Do NOT immediately route:

```text
ATOS
```

---

## Passenger-car body

Do NOT normally route:

```text
ATOS
```

Use:

```text
AUTOMOTIVE_STEEL
```

---

## EV traction motor

Do NOT route:

```text
ATOS
```

Use:

```text
HYPER_NO
```

---

## Excavator bucket

Do NOT route:

```text
ATOS
```

if abrasion resistance is dominant.

Use:

```text
POS_AR
```

---

## Heavy thick-plate crane boom

Do not assume ATOS.

Evaluate:

```text
POS_TEN
```

depending on plate geometry/thickness.

---

# 50. Marketing Opportunity Types

ATOS-related opportunities may include:

```text
LIGHTWEIGHTING
MATERIAL_UPGRADE
PAYLOAD_INCREASE
STRUCTURAL_OPTIMIZATION
FUEL_EFFICIENCY_SUPPORT
EV_COMMERCIAL_VEHICLE_WEIGHT_REDUCTION
TECHNICAL_PROPOSAL
JOINT_DEVELOPMENT
LOCALIZATION
NEW_DEMAND
DEMAND_GROWTH
```

These are business classifications, not material properties.

---

# 51. Event-to-ATOS Routing

## Commercial Vehicle Production Expansion

```text
CAPACITY_EXPANSION
↓
COMMERCIAL_VEHICLE
↓
FRAME_DEMAND
↓
ATOS opportunity
```

Only if frame/material scope is relevant.

---

## New Lightweight Truck Platform

```text
PRODUCT_LAUNCH
or
R_AND_D
↓
LIGHTWEIGHTING
↓
TRUCK_FRAME
↓
HIGH_STRENGTH_STRUCTURAL_STEEL
↓
ATOS
```

---

## Trailer Payload Upgrade

```text
R_AND_D
↓
PAYLOAD_INCREASE
+
WEIGHT_REDUCTION
↓
TRAILER_FRAME
↓
ATOS
```

---

# 52. Daily Intelligence Mode

Automated daily intelligence should normally stop at:

```text
ATOS
```

or:

```text
ATOS590 / ATOS780 CANDIDATE
```

only when strength requirements are clearly stated.

Recommended:

```yaml
daily_atos_analysis:
  allow_product_family: true
  allow_grade_candidate: true
  allow_exact_grade_recommendation: false
  allow_welding_detail: false
  allow_pdf_lookup: false
```

---

# 53. Marketing Mode

Marketing output should emphasize:

```text
customer structural change
weight reduction objective
frame/component
ATOS relevance
possible grade class
technical questions to ask
```

Example:

```text
Customer is redesigning a truck frame for lightweighting.

ATOS is relevant because the requirement combines:
high strength, cold forming, welding and structural weight reduction.

Potential classes:
ATOS590 / ATOS780

Next action:
confirm target yield strength, thickness,
bend requirement and welding process.
```

---

# 54. Engineering Mode

Engineering retrieval may include:

```text
exact chemistry
yield strength
tensile strength
elongation
bend test
Ceq
welding consumable
heat input
thickness range
width range
JIS reference
```

Original source verification is recommended.

---

# 55. Numeric Data Status

Store numeric values using:

```yaml
value:
unit:
value_type:
test_condition:
source_document:
source_section:
```

Possible value types:

```text
GUARANTEED_SPEC
REPRESENTATIVE
APPLICATION_EXAMPLE
```

Do not merge them.

---

# 56. Source Conflict Rule

The knowledge base currently contains overlapping ATOS data from:

```text
2026 ATOS.pdf
2026 Hot Rolled Steel.pdf
2025 Automotive Steel.pdf
```

If values differ:

```text
DO NOT SILENTLY RECONCILE
```

Use canonical source priority:

```text
1. 2026 ATOS.pdf
2. 2026 Hot Rolled Steel.pdf
3. 2025 Automotive Steel.pdf
```

and record:

```text
SOURCE_CONFLICT
```

where materially relevant.

---

# 57. Dedicated Product Guide Authority

For ATOS-specific technical values:

```text
2026 ATOS.pdf
```

is the canonical source.

The other catalogs are supporting sources for:

```text
application context
portfolio context
historical examples
```

---

# 58. Commercial Status

The 2025 Automotive Steel catalog marks ATOS540, ATOS590 and ATOS780 as commercial hot-rolled uncoated products in its availability table.

Current knowledge status:

```yaml
ATOS540:
  catalog_status: COMMERCIAL_PRODUCT

ATOS590:
  catalog_status: COMMERCIAL_PRODUCT

ATOS780:
  catalog_status: COMMERCIAL_PRODUCT
```

This is based on the supplied source set.

Future catalog revisions may change status.

---

# 59. Grade Registry

```text
ATOS540
ATOS590
ATOS780
```

Canonical family only.

Do not invent:

```text
ATOS690
ATOS880
ATOS1000
```

as current supported canonical grades unless an approved source explicitly establishes them.

---

# 60. Important Note on Higher ATOS Strength References

The general Hot Rolled Steel catalog contains references that suggest higher-strength ATOS-related concepts beyond the core ATOS540–780 family.

However the dedicated `2026 ATOS.pdf` supplied for this knowledge base defines the principal production family as:

```text
ATOS540–780
```

Therefore this file should currently treat:

```text
ATOS540
ATOS590
ATOS780
```

as canonical.

Anything beyond this requires:

```text
NEW_APPROVED_SOURCE_REQUIRED
```

---

# 61. Customer Questions

Before proposing ATOS, ask:

```text
What exact component is being redesigned?
Is it a frame, wheel, boom or another structural member?
What is the current material?
What is the current thickness?
What is the target weight reduction?
What yield strength is required?
What tensile strength is required?
What bend radius is required?
What forming process is used?
What welding process is used?
What fatigue life is required?
What stiffness limit applies?
What buckling mode controls the design?
What corrosion protection is required?
```

---

# 62. Grade Selection Example

Input:

```text
TRUCK_FRAME
current steel = ATOS540-type class
goal = significant lightweighting
cold pressing required
welding required
```

Possible output:

```yaml
product_family: ATOS

grade_candidates:
  - ATOS590
  - ATOS780

priority:
  ATOS780: P1
  ATOS590: P2

reason:
  - higher strength requested
  - commercial vehicle frame
  - lightweighting target
  - cold forming required

missing_information:
  - target_yield_strength
  - stiffness_requirement
  - buckling_requirement
  - bend_radius
  - welding_procedure

final_status:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 63. Weak Example

Bad:

```text
Truck production will increase.

→ Recommend ATOS780.
```

Problems:

```text
frame demand not proven
strength target unknown
current grade unknown
component unknown
design objective unknown
```

Correct:

```text
Commercial-vehicle production expansion may increase
structural steel demand.

ATOS may be relevant if frame or high-strength
structural components are within the investment scope.
```

---

# 64. Strong Example

```text
Customer is developing a lighter truck chassis frame
and is evaluating higher-strength hot-rolled steel.

Application:
TRUCK_FRAME

Requirements:
HIGH_STRENGTH
COLD_FORMABILITY
WELDABILITY
WEIGHT_REDUCTION

POSCO Product Family:
ATOS

Candidate classes:
ATOS590 / ATOS780

Next technical checks:
stiffness, buckling, bend radius, thickness and welding.
```

---

# 65. Product Hallucination Guardrail

Never invent:

```text
ATOS grade
strength value
elongation
thickness range
width
welding parameter
weight reduction percentage
commercial status
customer adoption
equivalent standard
```

If unsupported:

```text
UNKNOWN
```

---

# 66. Retrieval Keywords

Useful aliases/signals:

```text
ATOS
AuTOmobile Structural Steel
자동차구조용 고강도강
고강도 열연
truck frame
트럭 프레임
trailer frame
트레일러 프레임
commercial vehicle frame
상용차 프레임
boom arm
붐암
crane boom
특장차
wheel disc
경량 프레임
```

Keywords are retrieval aids.

They do not replace application validation.

---

# 67. Product Routing Algorithm

```pseudo
function route_atos(context):

    if context.component in [
        PASSENGER_BODY,
        CRASH_MEMBER,
        EV_MOTOR,
        BATTERY_CELL
    ]:
        return NOT_ATOS

    if context.component in [
        TRUCK_FRAME,
        TRAILER_FRAME,
        COMMERCIAL_VEHICLE_FRAME
    ]:
        product_family = ATOS

    else if context.component in [
        BOOM_ARM,
        CRANE_BOOM
    ]:
        determine_product_form()

        if HOT_ROLLED_STRUCTURAL:
            product_family = ATOS

        if THICK_PLATE:
            evaluate POS_TEN

    else:
        require structural application evidence

    if grade inputs insufficient:
        return ATOS with GRADE_UNKNOWN

    if moderate_strength:
        candidate += ATOS540

    if higher_strength:
        candidate += ATOS590

    if high_yield_strength
       and aggressive lightweighting:
        candidate += ATOS780

    verify:
        thickness
        bendability
        stiffness
        buckling
        fatigue
        welding

    return grade_candidates with:
        ENGINEERING_REVIEW_REQUIRED
```

---

# 68. ATOS Opportunity Object

Recommended structured output:

```yaml
industry: AUTOMOTIVE

application: COMMERCIAL_VEHICLE

component: TRUCK_FRAME

performance_goals:
  - WEIGHT_REDUCTION
  - PAYLOAD_INCREASE

material_requirements:
  - HIGH_STRENGTH
  - COLD_FORMABILITY
  - WELDABILITY
  - FATIGUE_RESISTANCE

product_family:
  - ATOS

grade_candidates:
  - ATOS590
  - ATOS780

technical_risks:
  - STIFFNESS
  - BUCKLING
  - WELDING
  - FATIGUE

missing_information:
  - target_yield_strength
  - current_thickness
  - target_thickness
  - bend_radius
  - welding_method

confidence: 86

final_selection:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 69. Final ATOS Knowledge Chain

```text
CUSTOMER SIGNAL
↓
COMMERCIAL / STRUCTURAL VEHICLE CHANGE
↓
FRAME / STRUCTURAL COMPONENT
↓
HIGH STRENGTH + COLD FORMING + WELDING
↓
ATOS
↓
ATOS540 / ATOS590 / ATOS780
↓
THICKNESS + BENDING + WELDING
↓
STIFFNESS + BUCKLING + FATIGUE
↓
GRADE CANDIDATE
↓
ENGINEERING VALIDATION
↓
MARKETING OPPORTUNITY
```

---

# 70. Final Rule

The purpose of ATOS is not:

```text
USE THE HIGHEST STRENGTH GRADE
```

The correct objective is:

```text
OPTIMIZE
STRUCTURAL STRENGTH
+
WEIGHT
+
FORMABILITY
+
WELDABILITY
+
STIFFNESS
+
BUCKLING
+
FATIGUE
```

for the actual component.

The preferred reasoning order is:

```text
COMPONENT
↓
STRUCTURAL FUNCTION
↓
DESIGN REQUIREMENT
↓
ATOS FAMILY
↓
GRADE CLASS
↓
ENGINEERING VALIDATION
```

not:

```text
ATOS780
↓
find a reason to use it
```

The responsibility of this file ends at:

```text
DEFENSIBLE ATOS GRADE CANDIDATE
```

Final application approval remains an engineering decision.
