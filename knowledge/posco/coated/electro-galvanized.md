---
product_family: ELECTRO_GALVANIZED_STEEL

name_ko: 전기아연도금강판
name_en: POSCO Electro Galvanized Steel

material_category:
  - COATED_STEEL
  - ELECTRO_GALVANIZED_STEEL
  - ZINC_COATED_STEEL

product_subfamilies:
  - EG_PURE_ZN
  - EG_ZN_NI
  - AUTOMOTIVE_FUEL_TANK_EG

industries:
  - AUTOMOTIVE
  - HOME_APPLIANCE
  - CONSTRUCTION
  - ELECTRONICS
  - METAL_FURNITURE

applications:
  - AUTOMOTIVE_PANEL
  - AUTOMOTIVE_BODY
  - AUTOMOTIVE_FUEL_TANK
  - HOME_APPLIANCE_PANEL
  - PREPAINTED_STEEL_BASE
  - BUILDING_INTERIOR
  - METAL_FURNITURE
  - ELECTRONIC_EQUIPMENT

components:
  - DOOR_OUTER
  - HOOD
  - FENDER
  - REAR_FLOOR
  - RADIATOR_SUPPORT
  - FUEL_TANK
  - APPLIANCE_INNER_PANEL
  - APPLIANCE_OUTER_PANEL
  - OA_EQUIPMENT
  - LCD_COMPONENT

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY
  - WELDABILITY
  - PAINTABILITY
  - SURFACE_QUALITY
  - ANTI_FINGERPRINT
  - LUBRICITY
  - ELECTRICAL_CONDUCTIVITY
  - PROCESS_BLACKENING_RESISTANCE

coating_systems:
  - PURE_ZN
  - ZN_NI

post_treatments:
  - XX
  - AW
  - AF
  - PL
  - PM
  - AL
  - AG
  - AC
  - OILING
  - FUNCTIONAL_RESIN
  - FUEL_TANK_CR_FREE_RESIN

source_documents:
  - 2025 Electro Galvanized Steel.pdf

primary_source:
  - 2025 Electro Galvanized Steel.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO Electro Galvanized Steel Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO electro-galvanized steel.

This file should be loaded after:

```text
knowledge/posco/coated/index.md
```

selects:

```text
ELECTRO_GALVANIZED_STEEL
```

as a relevant product family.

The primary responsibility of this file is to determine:

```text
PURE_ZN
vs
ZN_NI
vs
AUTOMOTIVE_FUEL_TANK_EG
```

and identify the proper:

```text
POST_TREATMENT
APPLICATION
BASE_MATERIAL
SURFACE REQUIREMENT
FORMING REQUIREMENT
WELDING REQUIREMENT
```

before detailed specification review.

This file does NOT automatically approve:

```text
exact coating amount
exact substrate grade
exact post-treatment
exact dimensions
exact welding current
final customer specification
```

---

# 2. Core Product Positioning

POSCO electro-galvanized steel is produced using electroplating and is available in two main coating systems:

```text
PURE_ZN
ZN_NI_ALLOY
```

The approved source also lists multiple post-treatment systems including:

```text
PHOSPHATE
CR_FREE_RESIN
ANTI_CORROSION_OILING
ANTI_FINGERPRINT
FUNCTIONAL_RESIN
```

The product family is used primarily in:

```text
AUTOMOTIVE
HOME_APPLIANCE
BUILDING_INTERIOR
METAL_FURNITURE
ELECTRONICS
```

The source explicitly describes Pure-Zn and Zn-Ni alloy as the two principal coating types and notes that phosphate-based coatings, Cr-free resin, and anti-corrosion oiling are available as post-treatments.

---

# 3. Core Intelligence Chain

Use:

```text
APPLICATION
↓
BASE MATERIAL
↓
SURFACE REQUIREMENT
↓
CORROSION REQUIREMENT
↓
FORMABILITY
↓
WELDABILITY
↓
PAINTABILITY
↓
PURE_ZN / ZN_NI
↓
POST_TREATMENT
↓
DIMENSION / SPECIFICATION
↓
ENGINEERING VALIDATION
```

Do not use:

```text
AUTOMOTIVE
→ ZN_NI
```

or:

```text
HOME_APPLIANCE
→ PURE_ZN
```

without checking actual requirements.

---

# 4. Product Architecture

```text
ELECTRO_GALVANIZED_STEEL
│
├── EG_PURE_ZN
│   ├── untreated
│   ├── oiled
│   ├── phosphate
│   ├── anti-fingerprint
│   └── functional surface treatments
│
├── EG_ZN_NI
│   ├── automotive panel
│   ├── untreated / oiled
│   ├── phosphate
│   └── functional resin
│
└── AUTOMOTIVE_FUEL_TANK_EG
    └── Zn-Ni + Cr-free functional resin
```

These routes must remain separate.

---

# 5. Electrogalvanizing vs Hot-Dip Galvanizing

The source highlights two important electrogalvanizing characteristics:

```text
LOWER_COATING_AMOUNT
+
NO_THERMAL_INFLUENCE_FROM_HOT_DIP_PROCESS
```

Because of this, the base material's mechanical properties and formability can remain close to those of the original:

```text
CR
or
HR
```

substrate.

The catalog explicitly states that electrogalvanized steel has relatively low coating mass compared with GI/GA and no thermal effect from the coating process, allowing material properties and formability comparable to the CR or HR substrate.

---

# 6. Core Selection Difference

## EG_PURE_ZN

Prioritize when:

```text
SURFACE_QUALITY
FORMABILITY
PAINTABILITY
ANTI_FINGERPRINT
HOME_APPLIANCE
BUILDING_INTERIOR
METAL_FURNITURE
```

are dominant.

---

## EG_ZN_NI

Prioritize when:

```text
AUTOMOTIVE
+
CORROSION_RESISTANCE
+
WELDABILITY
+
PAINTABILITY
```

are dominant.

---

## AUTOMOTIVE_FUEL_TANK_EG

Prioritize when:

```text
AUTOMOTIVE_FUEL_TANK
+
GASOLINE_RESISTANCE
+
WELDABILITY
+
CORROSION_RESISTANCE
+
CR_FREE_REQUIREMENT
```

are present.

---

# 7. EG_PURE_ZN

Canonical code:

```text
EG_PURE_ZN
```

Coating concept:

```text
PURE_ZN
+
STEEL_SUBSTRATE
```

Typical optional layers:

```text
PHOSPHATE
ANTI_FINGERPRINT_RESIN
OIL
SPECIAL_FILM
```

---

# 8. Pure-Zn Primary Applications

Source-supported applications include:

```text
HOME_APPLIANCE_INNER_PANEL
HOME_APPLIANCE_OUTER_PANEL
PREPAINTED_STEEL_BASE
BUILDING_INTERIOR
BUILDING_EXTERIOR
METAL_FURNITURE
```

The catalog specifically associates Pure-Zn electrogalvanized steel with appliance panels, painted steel substrate, building interior/exterior materials, and metal furniture.

---

# 9. Pure-Zn Strong Routing

Use:

```text
EG_PURE_ZN
```

when the application requires:

```text
GOOD_SURFACE
+
GOOD_FORMABILITY
+
PAINTABILITY
+
CORROSION_PROTECTION
```

and extreme automotive corrosion performance is not the primary requirement.

---

# 10. Pure-Zn Surface Advantage

The electrogalvanized product has a flat surface that supports:

```text
PAINT_SURFACE_QUALITY
```

The source states that phosphate treatment can be applied to improve:

```text
PAINT_ADHESION
+
PAINTED_CORROSION_RESISTANCE
```

This is a major reason Pure-Zn is relevant for painted applications.

---

# 11. Pure-Zn Formability

Because electroplating does not subject the substrate to hot-dip thermal processing:

```text
BASE_STEEL_FORMABILITY
```

is largely preserved.

Strong route:

```text
DEEP_FORMING
+
SURFACE_QUALITY
+
COATING
→ EG_PURE_ZN candidate
```

provided the substrate grade itself is suitable.

---

# 12. EG_ZN_NI

Canonical code:

```text
EG_ZN_NI
```

Coating concept:

```text
Zn-Ni ALLOY
+
STEEL_SUBSTRATE
```

The catalog identifies:

```text
Zn-10~15% Ni
```

in the Zn-Ni product structure illustration for automotive use.

Do not generalize this composition to every Zn-Ni product unless the source supports the specific product.

---

# 13. Zn-Ni Development Purpose

The source states that Zn-Ni alloy coating was developed to improve automotive body corrosion durability, particularly against deicing salts such as:

```text
NaCl
CaCl2
```

and to improve resistance to perforation corrosion.

Therefore strong environmental signals include:

```text
ROAD_SALT
DEICING_SALT
AUTOMOTIVE_BODY_CORROSION
```

---

# 14. Zn-Ni Primary Advantages

Source-supported directional advantages include:

```text
CORROSION_RESISTANCE
WELDABILITY
PAINTABILITY
```

compared with Pure-Zn in the stated automotive context.

The source explains that Ni addition creates a harder/higher-melting coating and allows lower-current welding than Pure-Zn while suppressing steel corrosion over long exposure.

---

# 15. Zn-Ni Automotive Applications

Source-supported examples:

```text
DOOR_OUTER
HOOD
FENDER
REAR_FLOOR
PASSENGER_CAR_INNER_PANEL
PASSENGER_CAR_OUTER_PANEL
```

These are direct application examples in the catalog.

---

# 16. Zn-Ni Strong Routing

```text
AUTOMOTIVE_PANEL
+
CORROSION_RESISTANCE
+
WELDABILITY
+
PAINTABILITY
→ EG_ZN_NI
```

This is one of the strongest source-supported routes.

---

# 17. Zn-Ni Negative Routing

Do not use:

```text
ZN_NI
```

automatically for:

```text
HOME_APPLIANCE
METAL_FURNITURE
BUILDING_INTERIOR
```

unless the product requirements justify it.

Pure-Zn is the stronger default route for those source-supported applications.

---

# 18. Pure-Zn vs Zn-Ni

| Requirement | Pure-Zn | Zn-Ni |
|---|---|---|
| General surface quality | strong | relevant |
| Appliance use | strong | weak/default no |
| Painted steel substrate | strong | relevant |
| Automotive body | possible | strong |
| Road-salt corrosion | limited routing evidence | strong |
| Welding priority | possible | strong |
| Paintability | strong with phosphate | strong |
| Fuel tank | no default | specialized Zn-Ni route |

This is a routing table, not a universal performance ranking.

---

# 19. Corrosion Protection Principle

The source describes zinc's:

```text
GALVANIC_ACTION
```

as protecting the substrate through sacrificial protection.

When exposed to the atmosphere:

```text
THIN_PROTECTIVE_FILM
```

forms on the zinc surface and contributes to corrosion protection.

---

# 20. Corrosion Guardrail

Do not translate laboratory corrosion behavior into:

```text
FIELD_LIFETIME
```

unless the source provides an approved correlation.

Forbidden:

```text
better SST result
→ same percentage longer field life
```

---

# 21. Automotive Coating Mass Note

The catalog states that automotive electrogalvanized products may use:

```text
HEAVIER_COATING
```

to enhance corrosion resistance.

Do not convert this into:

```text
MORE_COATING = ALWAYS_BETTER
```

because:

```text
FORMING
WELDING
SURFACE
COST
```

must also be considered.

---

# 22. Weldability

Electrogalvanized zinc coating can reduce spot-welding performance compared with bare CR because of:

```text
contact condition
electrical characteristics
coating behavior
```

However the source states that appropriate:

```text
WELDING_CONDITION
+
POST_TREATMENT
```

can enable satisfactory:

```text
SPOT_WELDING
SEAM_WELDING
```

performance.

---

# 23. Zn-Ni Weldability

The catalog specifically associates Zn-Ni with:

```text
LOWER_CURRENT_WELDING
```

relative to Pure-Zn in the compared automotive use case.

Therefore:

```text
AUTOMOTIVE
+
RESISTANCE_WELDING
```

is a strong Zn-Ni routing signal.

---

# 24. Welding Guardrail

Do not use a catalog welding-current example as:

```text
UNIVERSAL_WELDING_PARAMETER
```

because final welding conditions depend on:

```text
sheet thickness
substrate grade
electrode
coating amount
joint geometry
equipment
```

Return:

```text
WELDING_PROCEDURE_REVIEW_REQUIRED
```

for final process recommendation.

---

# 25. Paintability

The source states that phosphate treatment is applied to improve:

```text
PAINT_ADHESION
PAINTED_CORROSION_RESISTANCE
```

because the electrogalvanized surface is flat and suitable for painted finishes.

---

# 26. Paintability Route

```text
PAINTED_COMPONENT
+
HIGH_SURFACE_QUALITY
→ PURE_ZN + PHOSPHATE candidate
```

or:

```text
AUTOMOTIVE_BODY
+
PAINTING
+
WELDING
→ ZN_NI candidate
```

depending on application.

---

# 27. Post-Treatment Architecture

The source provides multiple post-treatment codes.

Canonical internal codes:

```text
XX
AW
AF
PL
PM
AL
AG
AC
```

These must remain independent from coating alloy selection.

---

# 28. XX — Untreated

Canonical code:

```text
XX
```

Meaning:

```text
UNTREATED
```

Use only where no additional surface functional treatment is required.

Do not assume:

```text
UNTREATED
→ sufficient white-rust resistance
```

without environment/storage validation.

---

# 29. AW — Antifinger Weldability

Canonical:

```text
AW
```

Full name:

```text
ANTIFINGER_WELDABILITY
```

Primary properties:

```text
ANTI_FINGERPRINT
CONDUCTIVITY
WELDABILITY
```

Use when:

```text
fingerprint resistance
+
electrical/welding function
```

are important.

---

# 30. AF — Antifinger Formability

Canonical:

```text
AF
```

Full name:

```text
ANTIFINGER_FORMABILITY
```

Primary properties:

```text
ANTI_FINGERPRINT
CORROSION_RESISTANCE
FORMABILITY
NON_CONDUCTIVITY
```

The source associates this treatment with deep-forming electronic/appliance applications.

---

# 31. PL — Phosphate Light

Canonical:

```text
PL
```

Full name:

```text
PHOSPHATE_LIGHT
```

Primary routing:

```text
PAINTABILITY
```

Use for:

```text
PAINTED_STEEL
COLOR_STEEL
```

applications where phosphate pretreatment supports paint adhesion.

---

# 32. PM — Phosphate Metallic

Canonical:

```text
PM
```

Full name:

```text
PHOSPHATE_METALLIC
```

Primary characteristics:

```text
PAINTABILITY
CORROSION_RESISTANCE
FORMABILITY
```

Potential use:

```text
POWDER_COATING
```

according to the source's application table.

---

# 33. AL — Antifinger Lubricant

Canonical:

```text
AL
```

Full name:

```text
ANTIFINGER_LUBRICANT
```

Primary properties:

```text
ANTI_FINGERPRINT
CORROSION_RESISTANCE
PROCESS_BLACKENING_RESISTANCE
LUBRICITY
FORMABILITY
```

Use when processing requires:

```text
FORMING
+
SURFACE_APPEARANCE
+
LUBRICITY
```

---

# 34. AG — Antifinger General

Canonical:

```text
AG
```

Full name:

```text
ANTIFINGER_GENERAL
```

Primary characteristics:

```text
ANTI_FINGERPRINT
CORROSION_RESISTANCE
CONDUCTIVITY
```

Use as a general anti-fingerprint functional treatment where these properties are relevant.

---

# 35. AC — Antifinger Conductivity

Canonical:

```text
AC
```

Full name:

```text
ANTIFINGER_CONDUCTIVITY
```

Primary characteristics:

```text
ANTI_FINGERPRINT
CORROSION_RESISTANCE
CONDUCTIVITY
```

Strong application signals include:

```text
LCD
COPY_MACHINE
COMPUTER_COMPONENT
OA_EQUIPMENT
```

depending on the source application table.

---

# 36. Post-Treatment Routing Matrix

| Requirement | Candidate |
|---|---|
| no functional surface treatment | XX |
| fingerprint + welding | AW |
| fingerprint + formability | AF |
| paint adhesion | PL |
| paint + corrosion + forming | PM |
| fingerprint + lubrication/forming | AL |
| general antifingerprint | AG |
| antifingerprint + conductivity | AC |

This is a first-stage routing matrix only.

---

# 37. Post-Treatment Selection Rule

Required sequence:

```text
COATING SYSTEM
↓
APPLICATION
↓
SURFACE FUNCTION
↓
POST-TREATMENT
```

Not:

```text
POST-TREATMENT CODE
↓
find an application
```

---

# 38. Pure-Zn Post-Treatment Use

The source indicates Pure-Zn products may use:

```text
UNTREATED
OILED
PHOSPHATE
ANTI_FINGERPRINT
BLACK_RESIN
```

depending on line/product.

Do not assume all treatments are available on every line.

---

# 39. Zn-Ni Post-Treatment Use

Zn-Ni products may use:

```text
OILING
PHOSPHATE
FUNCTIONAL_RESIN
```

with automotive applications strongly represented.

The source specifically associates functional resin with:

```text
FUEL_TANK
```

use.

---

# 40. Automotive Fuel Tank Steel

Canonical internal code:

```text
AUTOMOTIVE_FUEL_TANK_EG
```

This is a specialized electrogalvanized route.

Application:

```text
AUTOMOTIVE_FUEL_TANK
```

---

# 41. Fuel Tank Product Concept

The source describes an environmentally oriented fuel-tank steel that removes:

```text
Pb
Cr
```

from the previous Pb-Sn-type concept.

The coating system is:

```text
Zn-Ni
+
Cr-free resin
```

The source identifies it specifically as an environmentally friendly automotive fuel-tank sheet.

---

# 42. Fuel Tank Coating Structure

Source-supported structure:

```text
Cr-free resin
↓
Zn-Ni coating
↓
Steel substrate
```

The catalog gives representative coating data:

```text
Zn-Ni = 20–30 g/m²
Cr-free resin = 800–1200 mg/m²
```

for the described fuel-tank product.

These figures must remain specific to the fuel-tank product.

Do NOT generalize them to all Zn-Ni electrogalvanized products.

---

# 43. Fuel Tank Performance Areas

The source compares the Cr-free fuel-tank product on:

```text
WELDABILITY
CORROSION_RESISTANCE
GASOLINE_CORROSION_RESISTANCE
PAINTABILITY
FORMABILITY
```

against the previous Pb-Sn product concept.

These are source-supported evaluation dimensions.

---

# 44. Fuel Tank Strong Routing

```text
AUTOMOTIVE
+
FUEL_TANK
+
GASOLINE_RESISTANCE
+
SEAM_WELDING
+
ENVIRONMENTAL_RESTRICTION
→ AUTOMOTIVE_FUEL_TANK_EG
```

This is a strong, direct route.

---

# 45. Fuel Tank Negative Routing

Do not use the fuel-tank Zn-Ni/Cr-free structure for:

```text
DOOR_OUTER
HOOD
FENDER
```

by default.

Those belong to the general:

```text
EG_ZN_NI
```

automotive-panel route.

---

# 46. Radiator Support

The source also associates the automotive functional electrogalvanized category with:

```text
RADIATOR_SUPPORT
```

in the application table.

Do not infer that the same fuel-tank coating system necessarily applies.

---

# 47. Substrate Grades

The source contains multiple electrogalvanized substrate grades for:

```text
GENERAL_FORMING
DRAWING
DEEP_DRAWING
NON_AGING_DEEP_DRAWING
STRUCTURAL
HIGH_STRENGTH
```

Examples include POSCO grade families such as:

```text
ENSC
ENSD
ENSP
ENSE
ENSN
EN37
ENCHSP60TR
ENCHSP35R
ENCHSP40R
ENCHSP35E
ENCHSP38E
```

These are grade-level product knowledge.

Do not load the full grade table during normal marketing intelligence.

---

# 48. Representative Grade Categories

Conceptual routing:

```text
GENERAL_USE
→ ENSC

FORMING
→ ENSD

DEEP_DRAWING
→ ENSP

NON_AGING_EXTRA_DEEP_DRAWING
→ ENSE

NON_AGING_DEEP_DRAWING
→ ENSN

STRUCTURAL
→ EN37

HIGH_STRENGTH
→ ENCHSP series
```

This is a retrieval aid.

Exact mechanical properties must be verified from the source.

---

# 49. Grade-Level Mechanical Data

The source provides mechanical properties such as:

```text
YP
TS
ELONGATION
BENDING
```

for multiple POSCO grades and corresponding standards.

Do not copy all values into daily intelligence.

Use:

```text
GRADE_PROPERTY_LOOKUP_REQUIRED
```

when detailed selection is requested.

---

# 50. High-Strength Grade Caution

The source notes that some high-strength corresponding specifications require:

```text
ADVANCE_CONSULTATION
```

or separate inquiry.

Therefore:

```text
HIGH_STRENGTH_EG
```

must not be assumed to have standard availability.

Return:

```text
HIGH_STRENGTH_GRADE_CONFIRMATION_REQUIRED
```

where applicable.

---

# 51. Production Lines

The source provides separate EGL production capabilities with differing:

```text
WIDTH
THICKNESS
COATING_TYPE
POST_TREATMENT
```

availability.

Examples in the supplied guide include lines capable of:

```text
PURE_ZN
ZN_NI
```

and different post-treatment combinations.

Do not assume every product/treatment can be made on every line.

---

# 52. Manufacturing Range

The source lists representative line ranges such as:

```text
WIDTH 800–1650 mm
WIDTH 800–1860 mm

THICKNESS approximately
0.25 / 0.35 / 0.40
to
2.3 mm
```

depending on production line.

These values are line-specific.

Do NOT create one universal:

```text
EG_MIN_WIDTH
EG_MAX_WIDTH
EG_MIN_THICKNESS
EG_MAX_THICKNESS
```

without preserving line/product context.

---

# 53. Size Availability Rule

Exact manufacturability depends on:

```text
coating system
grade
post-treatment
production line
thickness
width
```

Therefore exact orderability requires:

```text
SIZE_AVAILABILITY_CHECK_REQUIRED
```

---

# 54. Dimension Tolerances

The source states dimension tolerances follow:

```text
KS
JIS
```

for the defined standard conditions.

Other requested dimensions require separate consultation.

Do not infer tolerance for non-standard product without source confirmation.

---

# 55. Thickness Tolerance Note

The source states that thickness tolerance is applied using:

```text
ORDERED_STEEL_THICKNESS
+
CORRESPONDING_ZINC_THICKNESS
```

and specifies a measurement position inside the edge.

These details belong to engineering/order review.

---

# 56. Exact Dimension Rule

For:

```text
exact thickness
exact width
flatness
length tolerance
straightness
```

use:

```text
SOURCE_LOOKUP_REQUIRED
```

rather than simplified family-level assumptions.

---

# 57. EG vs GI/GA

This distinction is important.

## EG

Strengths:

```text
SURFACE_QUALITY
FORMABILITY
BASE_MATERIAL_PROPERTY_RETENTION
POST_TREATMENT_FLEXIBILITY
```

## GI / GA

Strengths may include:

```text
HOT_DIP_PROCESS
BROADER_HOT_DIP_COATING_ROUTE
AUTOMOTIVE_COATED_AHSS
GENERAL_BUILDING_APPLICATIONS
```

Use application/process context.

---

# 58. EG vs GI Routing

Consider EG when:

```text
HIGH_SURFACE_QUALITY
+
FORMABILITY
+
PAINTABILITY
```

are strong.

Consider GI when:

```text
GENERAL_CORROSION
+
BROAD_APPLICATION
+
HOT_DIP_ROUTE
```

is preferred.

---

# 59. EG Zn-Ni vs GA

Both may be relevant to automotive body panels.

Use:

```text
substrate availability
corrosion requirement
welding process
paint process
coating architecture
customer standard
```

to distinguish.

Do not use:

```text
AUTOMOTIVE → GA
```

or:

```text
AUTOMOTIVE → Zn-Ni
```

as automatic rules.

---

# 60. Cross-Domain Automotive Rule

Example:

```text
DOOR_OUTER
```

may require:

```text
../automotive/automotive-steel.md
+
./electro-galvanized.md
```

The first file determines:

```text
SUBSTRATE FAMILY / GRADE
```

This file determines:

```text
ELECTROGALVANIZED COATING
+
POST_TREATMENT
```

---

# 61. Substrate + Coating Separation

Example:

```text
HIGH_STRENGTH_AUTOMOTIVE_STEEL
+
ZN_NI
```

must be modeled as two layers.

Do not create one combined invented grade unless an approved catalog defines it.

---

# 62. Surface Quality Router

If:

```text
SURFACE_QUALITY
```

is dominant:

Primary candidates:

```text
EG_PURE_ZN
```

with possible:

```text
ANTI_FINGERPRINT
PHOSPHATE
```

post-treatment depending on use.

---

# 63. Anti-Fingerprint Router

If:

```text
ANTI_FINGERPRINT
```

is required:

Possible routes include:

```text
AW
AF
AL
AG
AC
```

Do not select one until secondary function is known.

---

# 64. Anti-Fingerprint Decision

```text
ANTI_FINGERPRINT + WELDABILITY
→ AW

ANTI_FINGERPRINT + FORMABILITY
→ AF

ANTI_FINGERPRINT + LUBRICITY
→ AL

ANTI_FINGERPRINT + GENERAL_USE
→ AG

ANTI_FINGERPRINT + CONDUCTIVITY
→ AC
```

---

# 65. Paint Router

```text
PAINTABILITY
+
GENERAL PAINTED MATERIAL
→ PL / PM candidate
```

Selection depends on:

```text
paint process
corrosion target
forming requirement
```

---

# 66. Electronics Router

For:

```text
LCD
COPY_MACHINE
COMPUTER_COMPONENT
OA_EQUIPMENT
```

with:

```text
ANTI_FINGERPRINT
+
CONDUCTIVITY
```

evaluate:

```text
AC
or
AW
```

depending on welding/conductivity needs.

---

# 67. Appliance Router

Input:

```text
HOME_APPLIANCE
+
SURFACE_QUALITY
+
FORMABILITY
+
ANTI_FINGERPRINT
```

Primary:

```text
EG_PURE_ZN
```

Potential treatments:

```text
AF
AL
AG
AC
```

depending on function.

---

# 68. Automotive Panel Router

Input:

```text
AUTOMOTIVE
+
BODY_PANEL
+
CORROSION
+
WELDING
+
PAINT
```

Primary candidate:

```text
EG_ZN_NI
```

Application examples:

```text
DOOR_OUTER
HOOD
FENDER
REAR_FLOOR
```

---

# 69. Fuel Tank Router

Input:

```text
AUTOMOTIVE
+
FUEL_TANK
+
GASOLINE_CORROSION
+
SEAM_WELDING
+
CR_FREE
```

Primary:

```text
AUTOMOTIVE_FUEL_TANK_EG
```

Structure:

```text
Cr-free resin
+
Zn-Ni
+
steel substrate
```

---

# 70. Negative Routing Rules

## Appliance ≠ Zn-Ni automatically

Pure-Zn is the primary catalog route.

---

## Automotive ≠ Zn-Ni always

Substrate, component, coating requirement, welding and paint process must be known.

---

## Surface quality ≠ EG always

GI, PosMAC 1.5 or other materials may also be candidates.

---

## High corrosion ≠ Zn-Ni automatically

Severe outdoor or coastal structural corrosion may instead route to:

```text
POSMAC_3_0
POSMAC_SUPER
```

---

## Fuel tank ≠ general Zn-Ni panel

Use specialized fuel-tank route.

---

# 71. Product Routing Score

Suggested:

```text
Application Match         20%
Surface Requirement       20%
Corrosion Requirement     20%
Formability               15%
Welding                   10%
Paintability              10%
Evidence Completeness      5%
```

Interpretation:

```text
90–100
DIRECT_ROUTE

80–89
STRONG_ROUTE

70–79
POSSIBLE_ROUTE

60–69
WEAK_ROUTE

<60
DO_NOT_LOAD
```

---

# 72. Product Candidate Object

```yaml
product_family: ELECTRO_GALVANIZED_STEEL

application: AUTOMOTIVE_BODY

component:
  - DOOR_OUTER

requirements:
  - CORROSION_RESISTANCE
  - WELDABILITY
  - PAINTABILITY

subfamily_candidates:
  - product: EG_ZN_NI
    priority: P1
    reason:
      - direct automotive panel application
      - corrosion requirement
      - welding requirement
      - painting requirement

post_treatment:
  status: UNKNOWN

missing_information:
  - substrate_grade
  - coating_amount
  - paint_process
  - welding_process
```

---

# 73. Appliance Candidate Object

```yaml
product_family: ELECTRO_GALVANIZED_STEEL

application: HOME_APPLIANCE

component:
  - OUTER_PANEL

requirements:
  - SURFACE_QUALITY
  - FORMABILITY
  - ANTI_FINGERPRINT

subfamily:
  EG_PURE_ZN

post_treatment_candidates:
  - AF
  - AL
  - AG

missing_information:
  - conductivity_requirement
  - lubrication_requirement
  - forming_severity
```

---

# 74. Fuel Tank Candidate Object

```yaml
product_family: ELECTRO_GALVANIZED_STEEL

application: AUTOMOTIVE_FUEL_TANK

subfamily:
  AUTOMOTIVE_FUEL_TANK_EG

coating_system:
  Zn_Ni: true

functional_layer:
  CR_FREE_RESIN

requirements:
  - GASOLINE_CORROSION_RESISTANCE
  - CORROSION_RESISTANCE
  - WELDABILITY
  - FORMABILITY

final_status:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 75. Daily Intelligence Mode

For normal daily intelligence:

Do NOT retrieve:

```text
exact coating mass
exact resin mass
exact post-treatment code
exact dimensions
welding current
mechanical property table
```

Preferred output:

```text
ELECTRO_GALVANIZED_STEEL
→ PURE_ZN / ZN_NI direction
```

Recommended:

```yaml
daily_eg_analysis:
  allow_subfamily_selection: true
  allow_post_treatment_candidate: true
  allow_exact_specification: false
  allow_pdf_lookup: false
```

---

# 76. Marketing Mode

Marketing analysis may include:

```text
application
Pure-Zn / Zn-Ni route
surface benefit
corrosion benefit
post-treatment direction
customer questions
```

Example:

```text
Customer is reviewing a painted automotive outer panel
with stronger corrosion protection and spot-welding requirements.

Zn-Ni electrogalvanized steel is a relevant candidate.

Next checks:
substrate grade,
coating amount,
paint pretreatment,
spot-welding process.
```

---

# 77. Engineering Mode

Engineering analysis may retrieve:

```text
coating mass
Zn-Ni composition
post-treatment code
functional resin mass
substrate grade
mechanical properties
bendability
width
thickness
dimension tolerance
welding data
SST data
```

Original source PDF should be consulted.

---

# 78. Corrosion-Test Guardrail

Corrosion data must retain:

```text
TEST_METHOD
EXPOSURE_TIME
COATING
POST_TREATMENT
TEST_CONDITION
```

Do not transform:

```text
SST performance
```

into:

```text
field service life
```

without validated correlation.

---

# 79. Welding-Test Guardrail

Spot/seam current data in the fuel-tank section are source-specific test examples.

Do not convert them into:

```text
STANDARD_WELDING_CURRENT
```

for every fuel tank design.

---

# 80. Numeric Data Classification

Every numeric value should be stored with:

```yaml
value:
unit:
value_type:
test_condition:
application:
source:
```

Allowed value types:

```text
SPECIFICATION
REPRESENTATIVE
TEST_RESULT
APPLICATION_EXAMPLE
```

---

# 81. Source Authority

For this product family:

```text
2025 Electro Galvanized Steel.pdf
```

is the canonical source.

Do not override its terminology using general model knowledge.

---

# 82. Source Scope Rule

If this source does not establish:

```text
current customer qualification
current commercial status for a specific grade
current exact production range
specific grade + treatment combination
```

return:

```text
UNKNOWN
```

or:

```text
CONFIRMATION_REQUIRED
```

---

# 83. Unknown States

Supported:

```text
EG_SUBFAMILY_UNKNOWN

BASE_STEEL_UNKNOWN

SUBSTRATE_GRADE_UNKNOWN

COATING_AMOUNT_UNKNOWN

POST_TREATMENT_UNKNOWN

FORMING_SEVERITY_UNKNOWN

WELDING_REQUIREMENT_UNKNOWN

PAINT_PROCESS_UNKNOWN

COMMERCIAL_STATUS_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

HIGH_STRENGTH_GRADE_CONFIRMATION_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 84. Retrieval Keywords

```text
Electro Galvanized Steel
EG
Pure Zn
Zn-Ni
전기아연도금
전기아연도금강판
Zn-Ni 합금도금
Pure-Zn
자동차 외판
Door Outer
Hood
Fender
Rear Floor
연료탱크 강판
Fuel Tank
내지문
Anti-fingerprint
Phosphate
Cr-free
```

These keywords are navigation aids only.

---

# 85. Routing Algorithm

```pseudo
function route_electro_galvanized(context):

    identify application
    identify substrate
    identify surface_requirements
    identify corrosion_requirements
    identify welding
    identify painting
    identify forming

    if application == AUTOMOTIVE_FUEL_TANK:
        route AUTOMOTIVE_FUEL_TANK_EG
        require Cr_free / fuel compatibility validation

    else if application == AUTOMOTIVE_BODY
        and corrosion
        and welding
        and paint:
        candidate = EG_ZN_NI

    else if application in [
        HOME_APPLIANCE,
        BUILDING_INTERIOR,
        METAL_FURNITURE,
        ELECTRONICS
    ]:
        candidate = EG_PURE_ZN

    else:
        candidate = EG_SUBFAMILY_UNKNOWN

    if antifingerprint:
        select post-treatment based on:
            weldability
            formability
            lubricity
            conductivity

    if paintability:
        evaluate phosphate treatment

    verify:
        substrate_grade
        coating_amount
        post_treatment
        dimensions
        manufacturing_line

    return candidate
```

---

# 86. Example — Door Outer

```yaml
industry: AUTOMOTIVE

application: VEHICLE_BODY

component:
  - DOOR_OUTER

requirements:
  - CORROSION_RESISTANCE
  - WELDABILITY
  - PAINTABILITY

product_family:
  ELECTRO_GALVANIZED_STEEL

subfamily:
  EG_ZN_NI

reason:
  - source-supported automotive application
  - corrosion-resistant route
  - weldability requirement
  - paintability requirement

missing_information:
  - substrate_grade
  - coating_amount
  - post_treatment
```

---

# 87. Example — Refrigerator Panel

```yaml
industry: HOME_APPLIANCE

application:
  - REFRIGERATOR

component:
  - OUTER_PANEL

requirements:
  - SURFACE_QUALITY
  - FORMABILITY
  - ANTI_FINGERPRINT

subfamily:
  EG_PURE_ZN

post_treatment_candidates:
  - AF
  - AL
  - AG
  - AC

selection_status:
  POST_TREATMENT_UNKNOWN
```

---

# 88. Example — Automotive Fuel Tank

```yaml
industry: AUTOMOTIVE

application:
  AUTOMOTIVE_FUEL_TANK

requirements:
  - GASOLINE_CORROSION_RESISTANCE
  - WELDABILITY
  - FORMABILITY
  - CORROSION_RESISTANCE
  - CR_FREE

product_family:
  ELECTRO_GALVANIZED_STEEL

subfamily:
  AUTOMOTIVE_FUEL_TANK_EG

coating:
  ZN_NI

functional_treatment:
  CR_FREE_RESIN

final_status:
  ENGINEERING_REVIEW_REQUIRED
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
SURFACE REQUIREMENT
↓
FORMING
+
CORROSION
+
WELDING
+
PAINTING
↓
ELECTRO_GALVANIZED_STEEL
↓
PURE_ZN
or
ZN_NI
or
FUEL_TANK_EG
↓
POST-TREATMENT
↓
COATING AMOUNT
↓
DIMENSION / GRADE
↓
ENGINEERING VALIDATION
↓
MARKETING OPPORTUNITY
```

---

# 90. Final Rule

The purpose of electrogalvanized steel routing is NOT:

```text
AUTOMOTIVE = Zn-Ni
```

or:

```text
APPLIANCE = Pure-Zn
```

The correct objective is:

```text
RIGHT BASE MATERIAL
+
RIGHT COATING SYSTEM
+
RIGHT SURFACE FUNCTION
+
RIGHT FORMABILITY
+
RIGHT WELDABILITY
+
RIGHT PAINTABILITY
```

The preferred reasoning order is:

```text
APPLICATION
↓
SUBSTRATE
↓
FUNCTIONAL REQUIREMENT
↓
PURE_ZN / ZN_NI
↓
POST-TREATMENT
↓
DETAILED SPECIFICATION
```

not:

```text
COATING TYPE FIRST
↓
JUSTIFY LATER
```

The responsibility of this file ends at:

```text
DEFENSIBLE ELECTROGALVANIZED PRODUCT CANDIDATE
```

Final customer specification remains an engineering and product-quality decision.
