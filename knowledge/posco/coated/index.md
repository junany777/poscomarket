---

knowledge_domain: POSCO_COATED_STEEL
document_type: PRODUCT_ROUTER

parent_router:

- ../index.md

taxonomy_dependencies:

- ../../taxonomy/industries.md
- ../../taxonomy/applications.md
- ../../taxonomy/materials.md

local_product_files:

- galvanized.md
- electro-galvanized.md
- posmac-1.5.md
- posmac-3.0.md
- posmac-super.md

product_families:

- GALVANIZED_STEEL
- ELECTRO_GALVANIZED_STEEL
- POSMAC_1_5
- POSMAC_3_0
- POSMAC_SUPER

industries:

- AUTOMOTIVE
- HOME_APPLIANCE
- CONSTRUCTION
- ENERGY
- MACHINERY
- INFRASTRUCTURE

## knowledge_status: VERIFIED

# POSCO Coated Steel Product Knowledge Router

## 1. Purpose

This file is the product-routing layer for POSCO coated steel products.

It determines which coated-steel product knowledge file should be loaded after the intelligence system identifies a need related to:

```text
CORROSION_RESISTANCE
SURFACE_QUALITY
PAINTABILITY
WELDABILITY
FORMABILITY
CUT_EDGE_CORROSION_RESISTANCE
SEVERE_ENVIRONMENT_CORROSION_RESISTANCE
```

The main routing chain is:

```text
APPLICATION
↓
COMPONENT
↓
BASE MATERIAL REQUIREMENT
↓
OPERATING ENVIRONMENT
↓
CORROSION SEVERITY
↓
SURFACE / FORMING / WELDING REQUIREMENT
↓
COATED PRODUCT FAMILY
↓
PRODUCT KNOWLEDGE FILE
```

This file does NOT select an exact coating amount, substrate grade, post-treatment, or final customer specification.

---

# 2. Core Routing Principle

Coated steel selection must not begin with a product name.

Do not use:

```text
CORROSION
→ PosMAC
```

or:

```text
AUTOMOTIVE
→ GI
```

Instead use:

```text
APPLICATION
+
ENVIRONMENT
+
CORROSION SEVERITY
+
FABRICATION PROCESS
+
SURFACE REQUIREMENT
+
WELDING REQUIREMENT
+
PAINTING REQUIREMENT
↓
PRODUCT FAMILY
```

---

# 3. Product Architecture

The coated-steel knowledge domain is divided into:

```text
COATED_STEEL
│
├── GALVANIZED_STEEL
│   ├── GI
│   ├── GA
│   └── GI_H
│
├── ELECTRO_GALVANIZED_STEEL
│   ├── PURE_ZN
│   └── ZN_NI
│
└── ZN_MG_AL_ALLOY_COATED_STEEL
    ├── POSMAC_1_5
    ├── POSMAC_3_0
    └── POSMAC_SUPER
```

These product families must remain separate.

---

# 4. Default Product Files

## GALVANIZED_STEEL

File:

```text
./galvanized.md
```

Internal routes:

```text
GI
GA
GI_H
```

Primary use conditions:

```text
GENERAL_CORROSION_PROTECTION
AUTOMOTIVE_PANEL
HOME_APPLIANCE
BUILDING_MATERIAL
PIPE
SOLAR_SUPPORT
```

---

## ELECTRO_GALVANIZED_STEEL

File:

```text
./electro-galvanized.md
```

Internal routes:

```text
PURE_ZN
ZN_NI
```

Primary use conditions:

```text
SURFACE_QUALITY
PAINTABILITY
FORMABILITY
AUTOMOTIVE_PANEL
HOME_APPLIANCE
INTERIOR_MATERIAL
```

---

## POSMAC_1_5

File:

```text
./posmac-1.5.md
```

Primary use conditions:

```text
CORROSION_RESISTANCE
+
SURFACE_QUALITY
+
WELDABILITY
+
FORMABILITY
```

Strong industries:

```text
AUTOMOTIVE
HOME_APPLIANCE
PRECOATED_STEEL
```

---

## POSMAC_3_0

File:

```text
./posmac-3.0.md
```

Primary use conditions:

```text
HIGH_CORROSION_RESISTANCE
CUT_EDGE_CORROSION_RESISTANCE
FORMED_SECTION_CORROSION_RESISTANCE
```

Strong applications:

```text
SOLAR_STRUCTURE
OUTDOOR_STRUCTURE
C_CHANNEL
CORROSION_EXPOSED_STRUCTURE
```

---

## POSMAC_SUPER

File:

```text
./posmac-super.md
```

Primary use conditions:

```text
EXTREME_CORROSION_RESISTANCE
HIGH_SALINITY
HIGH_HUMIDITY
COASTAL
MARINE_ATMOSPHERE
```

---

# 5. Routing Priority

The router should normally return:

```text
1 Primary Product Family
+
0 to 1 Secondary Product Family
```

Default maximum:

```yaml
max_product_files: 2
```

Use three files only when:

```text
explicit comparative analysis
```

is requested.

---

# 6. Corrosion Severity Model

Use the following internal routing levels.

```text
LEVEL_1
GENERAL_CORROSION

LEVEL_2
ENHANCED_CORROSION

LEVEL_3
SEVERE_CORROSION

LEVEL_4
EXTREME_CORROSION
```

Directional mapping:

```text
LEVEL_1
→ GI / GA / EG

LEVEL_2
→ POSMAC_1_5 / GI / GA

LEVEL_3
→ POSMAC_3_0

LEVEL_4
→ POSMAC_SUPER
```

This is a routing prior only.

Application and manufacturing requirements may override it.

---

# 7. GENERAL_CORROSION

Use when:

```text
ordinary atmospheric exposure
indoor appliance use
standard automotive corrosion requirement
general building material
```

Primary candidates:

```text
GI
GA
EG
```

Do not load PosMAC automatically.

---

# 8. ENHANCED_CORROSION

Use when corrosion resistance must exceed ordinary galvanized material but:

```text
surface quality
welding
forming
```

remain important.

Strong candidate:

```text
POSMAC_1_5
```

Possible alternative:

```text
GI / GA
```

depending on application.

---

# 9. SEVERE_CORROSION

Typical conditions:

```text
OUTDOOR
HIGH_HUMIDITY
REPEATED_WET_DRY
EXPOSED_CUT_EDGES
STRUCTURAL_COMPONENT
```

Primary:

```text
POSMAC_3_0
```

---

# 10. EXTREME_CORROSION

Typical environment:

```text
HIGH_SALINITY
COASTAL
MARINE_ATMOSPHERE
HIGH_HUMIDITY
SEVERE_CHEMICAL_EXPOSURE
```

Primary:

```text
POSMAC_SUPER
```

Do not automatically treat immersion seawater service as equivalent to atmospheric coastal exposure.

---

# 11. GALVANIZED_STEEL Router

Parent family:

```text
GALVANIZED_STEEL
```

Subfamilies:

```text
GI
GA
GI_H
```

Product file:

```text
./galvanized.md
```

---

# 12. GI

Canonical code:

```text
GI
```

Meaning:

```text
HOT_DIP_GALVANIZED_STEEL
```

Typical substrate:

```text
COLD_ROLLED_BASE
```

Primary benefits:

```text
CORROSION_RESISTANCE
SURFACE_UNIFORMITY
PAINTABILITY
FORMABILITY
```

Typical applications:

```text
AUTOMOTIVE_INNER_OUTER_PANEL
HOME_APPLIANCE
METAL_FURNITURE
BUILDING_MATERIAL
PIPE
PREPAINTED_STEEL_BASE
```

---

# 13. GA

Canonical code:

```text
GA
```

Meaning:

```text
GALVANNEALED_STEEL
```

Product concept:

```text
Zn coating
+
Fe-Zn alloying
```

Primary routing advantages:

```text
WELDABILITY
PAINTABILITY
PAINTED_CORROSION_RESISTANCE
```

Strong application:

```text
AUTOMOTIVE_BODY_PANEL
```

Use GA when:

```text
AUTOMOTIVE
+
PAINTING
+
RESISTANCE_SPOT_WELDING
```

is a major requirement.

Do not treat GA and GI as interchangeable.

---

# 14. GI_H

Canonical code:

```text
GI_H
```

Meaning:

```text
HOT_ROLLED_BASE_HOT_DIP_GALVANIZED_STEEL
```

Typical applications:

```text
BUILDING_MATERIAL
PIPE
ELECTRICAL_PANEL
HOME_APPLIANCE_INNER_PANEL
SOLAR_SUPPORT
```

Use when:

```text
HOT_ROLLED_BASE
+
CORROSION_PROTECTION
```

is appropriate.

---

# 15. GI vs GA

Use:

```text
GI
```

when general galvanizing and broad forming/application flexibility dominate.

Use:

```text
GA
```

when:

```text
WELDABILITY
+
PAINTABILITY
+
PAINTED_CORROSION_RESISTANCE
```

are especially important.

Do not select GA solely because the application is automotive.

---

# 16. Coating Weight Guardrail

Increasing coating amount can improve corrosion durability.

However higher coating amount may affect:

```text
FORMABILITY
WELDABILITY
SURFACE_BEHAVIOR
```

Therefore:

```text
MORE_ZINC = ALWAYS_BETTER
```

is forbidden logic.

Exact coating-weight selection belongs in:

```text
galvanized.md
```

---

# 17. ELECTRO_GALVANIZED_STEEL Router

Canonical family:

```text
ELECTRO_GALVANIZED_STEEL
```

File:

```text
./electro-galvanized.md
```

Subfamilies:

```text
PURE_ZN
ZN_NI
```

---

# 18. Electro-Galvanized Core Positioning

Primary characteristics:

```text
CORROSION_RESISTANCE
FORMABILITY
WELDABILITY
PAINTABILITY
SURFACE_QUALITY
```

Strong application domains:

```text
AUTOMOTIVE
HOME_APPLIANCE
BUILDING_INTERIOR
METAL_FURNITURE
```

---

# 19. EG Formability Routing

The source notes that electrogalvanizing uses less deposited coating and avoids the thermal influence associated with hot-dip galvanizing.

Therefore base-material properties and formability can remain close to:

```text
CR
or
HR
```

substrate characteristics.

Use EG when:

```text
BASE_STEEL_FORMABILITY
+
SURFACE_FUNCTION
+
CORROSION_PROTECTION
```

must coexist.

---

# 20. PURE_ZN Electrogalvanized

Canonical code:

```text
EG_PURE_ZN
```

Strong use contexts:

```text
HOME_APPLIANCE_PANEL
PAINTED_STEEL_BASE
BUILDING_INTERIOR
METAL_FURNITURE
```

Possible requirements:

```text
SURFACE_QUALITY
PAINTABILITY
CORROSION_RESISTANCE
ANTI_FINGERPRINT
```

---

# 21. ZN_NI Electrogalvanized

Canonical code:

```text
EG_ZN_NI
```

Strong source-backed automotive context:

```text
PASSENGER_CAR_PANEL
DOOR_OUTER
HOOD
FENDER
REAR_FLOOR
```

Primary routing properties:

```text
CORROSION_RESISTANCE
WELDABILITY
PAINTABILITY
```

The source specifically links Zn-Ni to enhanced vehicle corrosion protection and lower-current welding capability compared with Pure Zn.

---

# 22. EG Post-Treatment

Possible post-treatments include:

```text
UNTREATED
OILING
PHOSPHATE
ANTI_FINGERPRINT
CR_FREE_RESIN
FUNCTIONAL_RESIN
```

Post-treatment selection is separate from:

```text
PURE_ZN
vs
ZN_NI
```

Do not collapse them.

---

# 23. EG vs GI/GA

Use EG when:

```text
SURFACE_QUALITY
FORMABILITY
PAINTABILITY
LOW_THERMAL_PROCESS_IMPACT
```

are important.

Use GI/GA when:

```text
HOT_DIP_GALVANIZED_ROUTE
broader coating range
automotive coated AHSS
building / pipe
```

are more relevant.

Exact substrate availability must be verified independently.

---

# 24. POSMAC Family

Parent family:

```text
POSMAC
```

Full concept:

```text
POSCO MAGNESIUM ALUMINIUM ALLOY COATING
```

Subfamilies:

```text
POSMAC_1_5
POSMAC_3_0
POSMAC_SUPER
```

Do not treat:

```text
PosMAC
```

as one product.

---

# 25. POSMAC_1_5

Canonical code:

```text
POSMAC_1_5
```

Coating concept:

```text
Zn - 1.5% Mg - 1.5% Al
```

Primary product positioning:

```text
CORROSION_RESISTANCE
+
SURFACE_QUALITY
+
WELDABILITY
+
FORMABILITY
```

Source-backed applications emphasize:

```text
HOME_APPLIANCE
AUTOMOTIVE
PRECOATED_STEEL
```

---

# 26. PosMAC 1.5 vs GI

Directional source positioning:

```text
higher corrosion resistance than ordinary GI
+
better cut-edge corrosion resistance
```

while maintaining:

```text
GI-compatible processing
assembly
painting
```

in the source-described product concept.

Do not assume all GI applications can automatically be converted to PosMAC 1.5.

---

# 27. PosMAC 1.5 vs PosMAC 3.0

This distinction is important.

## POSMAC_1_5

Prioritize:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
AUTOMOTIVE / APPLIANCE
```

## POSMAC_3_0

Prioritize:

```text
HIGHER_CORROSION_RESISTANCE
SEVERE_CORROSION_ENVIRONMENT
CUT_EDGE_CORROSION_RESISTANCE
```

The product source explicitly positions PosMAC 1.5 with lower Mg/Al content to improve surface quality and weldability relative to PosMAC 3.0.

---

# 28. POSMAC_3_0

Canonical code:

```text
POSMAC_3_0
```

Primary requirements:

```text
HIGH_CORROSION_RESISTANCE
CUT_EDGE_CORROSION_RESISTANCE
BENDING_SECTION_CORROSION_RESISTANCE
FORMED_SECTION_CORROSION_RESISTANCE
```

Strong applications:

```text
SOLAR_STRUCTURE
C_CHANNEL
OUTDOOR_STRUCTURE
CORROSION_EXPOSED_COMPONENT
```

---

# 29. PosMAC 3.0 Corrosion Routing

The product guide reports substantially higher corrosion resistance than ordinary hot-dip galvanized material under specified SST/CCT test conditions.

Use:

```text
POSMAC_3_0
```

as a strong candidate when:

```text
GI corrosion performance is insufficient
+
environment is severe
+
extreme marine exposure is not necessarily required
```

---

# 30. PosMAC 3.0 Cut-Edge Routing

Strong route:

```text
CUT_COMPONENT
PUNCHED_COMPONENT
C_CHANNEL
FORMED_STRUCTURE
+
CUT_EDGE_CORROSION
→ POSMAC_3_0
```

The source describes corrosion-product film formation around exposed cut sections.

Do not interpret this as:

```text
CUT_EDGE_NEVER_RUSTS
```

Initial red rust may still occur on exposed substrate before protective corrosion products develop.

---

# 31. PosMAC 3.0 Fabrication Rule

Source routing supports:

```text
processing
assembly
painting
```

using processes comparable to ordinary GI.

This is useful for replacement hypotheses.

However customer process compatibility still requires validation.

---

# 32. POSMAC_SUPER

Canonical code:

```text
POSMAC_SUPER
```

Primary positioning:

```text
EXTREME_CORROSION_RESISTANCE
```

Primary environments:

```text
HIGH_SALINITY
HIGH_HUMIDITY
COASTAL
ISLAND_COASTAL
WATER_SIDE
SEVERE_OUTDOOR
```

---

# 33. PosMAC Super Relative Positioning

Source-derived directional hierarchy:

```text
GI
↓
POSMAC_1_5
↓
POSMAC_3_0
↓
POSMAC_SUPER
```

may be useful strictly for:

```text
CORROSION_RESISTANCE ROUTING
```

but this is NOT a universal quality ranking.

For example:

```text
SURFACE_QUALITY
WELDABILITY
AUTOMOTIVE_FORMING
```

may favor PosMAC 1.5 over PosMAC Super.

---

# 34. PosMAC Super vs PosMAC 3.0

Use PosMAC Super when:

```text
corrosion severity is extreme
```

and particularly when:

```text
HIGH_SALINITY
HIGH_HUMIDITY
COASTAL
```

are material design drivers.

The supplied product guide reports PosMAC Super as having higher flat-section and formed-section corrosion resistance than PosMAC 3.0 in the documented CCT comparisons.

---

# 35. PosMAC Super Chemical Environment

The supplied product guide contains comparative test results in:

```text
ALKALINE_ENVIRONMENT
ACIDIC_DROPLET_ENVIRONMENT
```

and reports strong chemical-resistance performance relative to several other coated products under the documented test conditions.

Do NOT generalize these laboratory tests to:

```text
ALL_CHEMICAL_SERVICE
```

For chemical process equipment, stainless, titanium, or other materials may still be required.

---

# 36. PosMAC Super Cut Edge

The source describes:

```text
SELF_HEALING_EFFECT
```

via corrosion-product formation around cut sections.

However:

```text
SELF_HEALING
```

must not be interpreted as restoration of original metallic coating.

Use the term only in the source-defined corrosion context.

---

# 37. PosMAC Super Thick Cut Edge Caution

The source recommends repair painting in certain cut-edge conditions.

Important routing trigger:

```text
BASE_METAL_THICKNESS > 1.6 mm
+
EXPOSED_CUT_EDGE
```

may require:

```text
REPAIR_PAINT_RECOMMENDATION_CHECK
```

The source also recommends considering repair painting when visible initial red rust is unacceptable.

This caution must be preserved in:

```text
posmac-super.md
```

---

# 38. PosMAC Super Storage Caution

Long-term storage or exposure to trapped moisture may create:

```text
WHITE_RUST
```

risk.

The source recommends:

```text
early use
first-in-first-out
avoid moisture-trapping storage
```

Detailed handling requirements belong in:

```text
posmac-super.md
```

---

# 39. PosMAC Super Galling / Scratch Routing

The source reports higher coating hardness and favorable friction behavior compared with GI and other PosMAC families under the documented test.

Potential routing benefit:

```text
PRESS_FORMING
+
TOOL_CONTAMINATION_REDUCTION
+
SCRATCH_RESISTANCE
```

may support PosMAC Super evaluation.

Do not treat this as a universal forming superiority claim.

---

# 40. Product Family Comparison

| Product Family | Main Strength                           | Strong Routing Context                |
| -------------- | --------------------------------------- | ------------------------------------- |
| GI             | general corrosion protection            | automotive, appliance, building, pipe |
| GA             | weldability + paintability              | automotive painted/welded panels      |
| GI_H           | hot-rolled-base coating                 | building, pipe, solar support         |
| EG Pure Zn     | surface + processing                    | appliance, interior, painted material |
| EG Zn-Ni       | corrosion + welding + painting          | automotive panel                      |
| PosMAC 1.5     | corrosion + surface + welding + forming | automotive, appliance                 |
| PosMAC 3.0     | severe corrosion + cut-edge resistance  | solar, outdoor structures             |
| PosMAC Super   | extreme corrosion                       | coastal/high-salinity/high-humidity   |

This table is a routing summary.

---

# 41. Surface Quality Router

If:

```text
SURFACE_QUALITY
```

is a dominant requirement:

Primary candidates:

```text
EG
GI
POSMAC_1_5
```

Use application context.

Example:

```text
HOME_APPLIANCE
+
HIGH_SURFACE_QUALITY
+
FORMABILITY
→ EG / POSMAC_1_5
```

Do not prioritize PosMAC 3.0/Super simply because they offer more corrosion resistance.

---

# 42. Paintability Router

If:

```text
PAINTABILITY
```

is dominant:

Candidates:

```text
GA
EG
GI
POSMAC_1_5
```

Strong automotive route:

```text
GA
```

when welding + painted corrosion performance are also important.

---

# 43. Weldability Router

Potential candidates:

```text
GA
EG_ZN_NI
POSMAC_1_5
```

Do not select coating based on weldability alone.

Required additional information:

```text
welding_process
electrode
current
coating_weight
substrate_grade
```

---

# 44. Formability Router

Strong candidates:

```text
EG
GI
POSMAC_1_5
```

Use:

```text
component geometry
draw depth
bend radius
surface damage tolerance
```

to narrow.

---

# 45. Cut-Edge Corrosion Router

If:

```text
CUT_EDGE_CORROSION_RESISTANCE
```

is a major requirement:

Primary:

```text
POSMAC_3_0
```

Possible:

```text
POSMAC_SUPER
POSMAC_1_5
```

depending on severity and fabrication needs.

---

# 46. Severe Coastal Router

Input:

```text
COASTAL
+
HIGH_SALINITY
+
HIGH_HUMIDITY
```

Primary:

```text
POSMAC_SUPER
```

Secondary:

```text
POSMAC_3_0
```

if comparison is necessary.

---

# 47. Solar Structure Router

Application:

```text
SOLAR_STRUCTURE
```

Normal outdoor:

```text
GI_H
```

Enhanced corrosion:

```text
POSMAC_3_0
```

Coastal / severe salinity:

```text
POSMAC_SUPER
```

Do not select based solely on:

```text
SOLAR
```

because project environment matters.

---

# 48. Automotive Router

## Outer / inner body panel

Possible:

```text
GI
GA
EG
```

Use substrate/product availability.

## High surface + weldability + corrosion

Possible:

```text
POSMAC_1_5
```

where the product/application supports it.

## Severe structural outdoor corrosion

PosMAC 3.0/Super only if the component environment genuinely warrants them.

---

# 49. Home Appliance Router

Possible:

```text
GI
EG
POSMAC_1_5
```

Strong selection factors:

```text
SURFACE_QUALITY
FORMABILITY
PAINTABILITY
CORROSION_RESISTANCE
FINGERPRINT_RESISTANCE
```

---

# 50. Building Material Router

Possible:

```text
GI
GI_H
POSMAC_3_0
POSMAC_SUPER
```

Decision hierarchy:

```text
environment
↓
corrosion severity
↓
cut edges
↓
forming
↓
coating life requirement
```

---

# 51. Pipe Router

General coated structural pipe:

```text
GI_H
```

Potential severe-corrosion fabricated pipe:

```text
POSMAC_3_0
```

Do not confuse this with:

```text
OIL_GAS_PIPELINE
```

which belongs to API / line-pipe steel rather than coated-product routing.

---

# 52. Automotive Substrate + Coating Rule

Coated product is often only one layer of the solution.

Example:

```text
590DP
+
GI
```

means:

```text
AUTOMOTIVE_STEEL SUBSTRATE
+
GALVANIZED COATING
```

The coated router must not replace substrate routing.

Required sequence:

```text
SUBSTRATE FAMILY
↓
COATING REQUIREMENT
↓
COATING FAMILY
```

---

# 53. Cross-Domain Retrieval

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

or:

```text
../automotive/automotive-steel.md
+
./electro-galvanized.md
```

Default maximum:

```text
2 product files
```

---

# 54. Base Material Awareness

Coating selection must preserve the base material.

Possible base routes include:

```text
COLD_ROLLED
HOT_ROLLED
AUTOMOTIVE_AHSS
```

Do not assume every substrate grade is compatible with every coating process.

---

# 55. Product Substitution Guardrail

Do not automatically infer:

```text
GI
→ PosMAC 3.0 replacement
```

or:

```text
GI
→ PosMAC Super replacement
```

because product substitution may affect:

```text
cost
surface
forming
welding
coating weight
customer approval
processing
design
```

Use:

```text
MATERIAL_SUBSTITUTION_CANDIDATE
```

rather than:

```text
DIRECT_REPLACEMENT
```

until validated.

---

# 56. Corrosion Test Guardrail

The POSCO catalogs use tests including:

```text
SST
CCT
OUTDOOR_EXPOSURE
CHEMICAL_IMMERSION
```

Results from one test must not be directly generalized into:

```text
field service life
```

without an approved correlation.

Do not convert:

```text
5x / 10x corrosion resistance
```

from a particular test into:

```text
5x / 10x longer service life
```

---

# 57. Relative Performance Rule

Allowed:

```text
PosMAC 3.0 showed 5–10x higher corrosion resistance
than the compared galvanized material
under the documented test conditions.
```

Not allowed:

```text
PosMAC 3.0 lasts 10 times longer in all environments.
```

---

# 58. Durability Warranty Guardrail

PosMAC Super source includes durability-warranty information for specific:

```text
customer
application
project
environment
```

conditions.

Do not convert that into:

```text
ALL_POSMAC_SUPER_PRODUCTS_HAVE_25_YEAR_WARRANTY
```

Warranty eligibility requires project/customer-specific confirmation.

---

# 59. Post-Treatment Layer

Coated products may include post-treatments.

Possible functions:

```text
CORROSION_RESISTANCE
LUBRICITY
ANTI_FINGERPRINT
PAINT_PREPARATION
TEMPORARY_PROTECTION
```

Post-treatment must be modeled separately from:

```text
COATING_ALLOY
```

---

# 60. Product Routing Score

Suggested score:

```text
Application Match          20%
Environment Match          25%
Corrosion Requirement      20%
Surface Requirement        10%
Forming Requirement        10%
Welding Requirement        10%
Evidence Completeness       5%
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

# 61. Primary Routing Matrix

```text
GENERAL_CORROSION
→ GI

AUTOMOTIVE_WELD + PAINT
→ GA

HIGH_SURFACE / PAINT
→ EG

CORROSION + SURFACE + WELD + FORM
→ POSMAC_1_5

SEVERE_CORROSION + CUT_EDGE
→ POSMAC_3_0

EXTREME_COASTAL / HIGH_SALINITY
→ POSMAC_SUPER
```

This is the central coated-steel routing rule.

---

# 62. Example — Automotive Door Outer

Input:

```text
AUTOMOTIVE
DOOR_OUTER
FORMABILITY
SURFACE_QUALITY
PAINTABILITY
CORROSION_RESISTANCE
```

Candidates:

```text
GI
GA
EG
```

Files:

```text
./galvanized.md
```

and optionally:

```text
./electro-galvanized.md
```

Do not load PosMAC unless additional requirements justify it.

---

# 63. Example — Automotive Panel with Welding Priority

Input:

```text
AUTOMOTIVE_PANEL
+
PAINTABILITY
+
WELDABILITY
+
CORROSION_RESISTANCE
```

Strong candidate:

```text
GA
```

File:

```text
./galvanized.md
```

---

# 64. Example — Home Appliance Panel

Input:

```text
HOME_APPLIANCE
+
SURFACE_QUALITY
+
FORMABILITY
+
CORROSION_RESISTANCE
```

Candidates:

```text
EG
POSMAC_1_5
GI
```

Rank based on:

```text
surface requirement
post-treatment
paint process
welding
corrosion target
```

---

# 65. Example — Solar C-Channel

Input:

```text
ENERGY
SOLAR_STRUCTURE
C_CHANNEL
OUTDOOR
CUT_EDGE_CORROSION
```

Primary:

```text
POSMAC_3_0
```

File:

```text
./posmac-3.0.md
```

---

# 66. Example — Coastal Solar Project

Input:

```text
SOLAR_STRUCTURE
+
COASTAL
+
HIGH_SALINITY
+
HIGH_HUMIDITY
```

Primary:

```text
POSMAC_SUPER
```

Secondary:

```text
POSMAC_3_0
```

for comparison.

Files:

```text
./posmac-super.md
./posmac-3.0.md
```

---

# 67. Example — Interior Metal Furniture

Input:

```text
METAL_FURNITURE
+
SURFACE
+
PAINTABILITY
```

Strong candidates:

```text
EG
GI
```

Do not route to PosMAC Super.

---

# 68. Negative Routing Rules

## Corrosion ≠ PosMAC

Ordinary corrosion may be adequately routed to:

```text
GI
GA
EG
```

---

## Automotive ≠ GA automatically

Some automotive grades/applications use:

```text
GI
GA
EG
```

depending on substrate and application.

---

## Coastal ≠ Stainless automatically

Structural coated steel may be relevant.

Likewise:

```text
POSMAC_SUPER
```

does not replace stainless in every coastal application.

---

## Chemical exposure ≠ PosMAC Super automatically

Chemical equipment may require:

```text
STAINLESS
TITANIUM
ANCOR
```

depending on chemical species and service condition.

---

## High corrosion ≠ PosMAC Super always

If:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
```

dominate, another PosMAC family may be more appropriate.

---

# 69. Missing Information

Before routing final product family, check:

```text
application
component
indoor / outdoor
humidity
salinity
coastal distance
chemical exposure
coating life target
surface requirement
paint requirement
welding requirement
forming requirement
cut-edge exposure
base steel
sheet thickness
post-treatment
customer specification
```

If important variables are missing:

```text
COATED_PRODUCT_FAMILY_UNKNOWN
```

or:

```text
ENVIRONMENT_DATA_REQUIRED
```

---

# 70. Router Output Schema

Recommended:

```yaml
material_domain: COATED_STEEL

application: SOLAR_STRUCTURE

component:
  - C_CHANNEL

environment:
  - OUTDOOR
  - COASTAL

requirements:
  - HIGH_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE

product_candidates:
  - product_family: POSMAC_SUPER
    knowledge_file: ./posmac-super.md
    priority: P1
    reason:
      - coastal environment
      - severe salinity
      - cut-edge exposure

  - product_family: POSMAC_3_0
    knowledge_file: ./posmac-3.0.md
    priority: P2
    reason:
      - strong structural corrosion resistance

files_to_load:
  - ./posmac-super.md
  - ./posmac-3.0.md

missing_information:
  - exact_salinity
  - sheet_thickness
  - durability_target
```

---

# 71. Automotive Dual-File Example

```yaml
industry: AUTOMOTIVE

application: VEHICLE_BODY

component:
  - DOOR_OUTER

substrate_product:
  family: AUTOMOTIVE_STEEL
  knowledge_file: ../automotive/automotive-steel.md

coating_candidates:
  - family: GALVANIZED_STEEL
    route: GI_OR_GA
    knowledge_file: ./galvanized.md

files_to_load:
  - ../automotive/automotive-steel.md
  - ./galvanized.md
```

---

# 72. Daily Intelligence Mode

Daily intelligence should normally stop at:

```text
PRODUCT FAMILY
```

not:

```text
coating mass
post-treatment code
exact surface code
```

Recommended:

```yaml
daily_coated_analysis:
  max_product_files: 1
  allow_secondary_candidate: true
  allow_exact_coating_spec: false
  allow_pdf_lookup: false
```

---

# 73. Marketing Mode

Marketing analysis may retrieve:

```text
product family
relative product positioning
customer benefit
application example
replacement hypothesis
missing qualification information
```

Do not automatically recommend exact coating specification.

---

# 74. Engineering Mode

Engineering analysis may retrieve:

```text
coating composition
coating weight
base steel
thickness
width
surface treatment
post-treatment
corrosion-test data
forming data
welding data
repair-paint requirements
```

Source PDF may be loaded.

---

# 75. Competitive Comparison

When comparing coated products:

Use dimensions relevant to the actual application.

Possible dimensions:

```text
CORROSION_RESISTANCE
CUT_EDGE_RESISTANCE
FORMED_SECTION_RESISTANCE
SURFACE_QUALITY
FORMABILITY
WELDABILITY
PAINTABILITY
COATING_HARDNESS
PROCESS_COMPATIBILITY
```

Do not rank products by corrosion performance alone when customer requirements are broader.

---

# 76. Product Family Registry

| Canonical Code           | Main Role                     | Knowledge File          |
| ------------------------ | ----------------------------- | ----------------------- |
| GALVANIZED_STEEL         | general hot-dip coating       | `galvanized.md`         |
| ELECTRO_GALVANIZED_STEEL | surface/forming/painting      | `electro-galvanized.md` |
| POSMAC_1_5               | corrosion + surface + welding | `posmac-1.5.md`         |
| POSMAC_3_0               | severe corrosion + cut edge   | `posmac-3.0.md`         |
| POSMAC_SUPER             | extreme corrosion             | `posmac-super.md`       |

---

# 77. Subfamily Registry

```text
GALVANIZED_STEEL
├── GI
├── GA
└── GI_H

ELECTRO_GALVANIZED_STEEL
├── EG_PURE_ZN
└── EG_ZN_NI

POSMAC
├── POSMAC_1_5
├── POSMAC_3_0
└── POSMAC_SUPER
```

---

# 78. File Loading Rules

## Automotive painted/welded panel

Load:

```text
galvanized.md
```

---

## Appliance high-surface panel

Load:

```text
electro-galvanized.md
```

or:

```text
posmac-1.5.md
```

depending on corrosion requirement.

---

## Outdoor structural corrosion

Load:

```text
posmac-3.0.md
```

---

## Extreme coastal corrosion

Load:

```text
posmac-super.md
```

---

# 79. Retrieval Search Order

Use:

```text
1. Application
2. Component
3. Environment
4. Corrosion severity
5. Surface / forming / welding requirements
6. coated/index.md
7. product MD frontmatter
8. product MD body
9. source PDF if necessary
```

Do not begin by reading all coated-product PDFs.

---

# 80. Product File Frontmatter Contract

Every coated product MD should contain:

```yaml
---
product_family:

material_category:
  - COATED_STEEL

industries: []

applications: []

components: []

environments: []

requirements: []

coating_system:

post_treatments: []

aliases: []

source_documents: []

knowledge_status: VERIFIED
---
```

---

# 81. Suggested galvanized.md Frontmatter

```yaml
---
product_family: GALVANIZED_STEEL

product_subfamilies:
  - GI
  - GA
  - GI_H

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY
  - WELDABILITY
  - PAINTABILITY

industries:
  - AUTOMOTIVE
  - HOME_APPLIANCE
  - CONSTRUCTION
  - ENERGY

source_documents:
  - 2025 Galvanized Steel.pdf

knowledge_status: VERIFIED
---
```

---

# 82. Suggested electro-galvanized.md Frontmatter

```yaml
---
product_family: ELECTRO_GALVANIZED_STEEL

product_subfamilies:
  - EG_PURE_ZN
  - EG_ZN_NI

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY
  - WELDABILITY
  - PAINTABILITY
  - SURFACE_QUALITY

source_documents:
  - 2025 Electro Galvanized Steel.pdf

knowledge_status: VERIFIED
---
```

---

# 83. Suggested posmac-1.5.md Frontmatter

```yaml
---
product_family: POSMAC_1_5

coating_system:
  Zn: BASE
  Mg_percent: 1.5
  Al_percent: 1.5

requirements:
  - CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - SURFACE_QUALITY
  - WELDABILITY
  - FORMABILITY

industries:
  - AUTOMOTIVE
  - HOME_APPLIANCE

source_documents:
  - 2025 POSMAC1.5.pdf

knowledge_status: VERIFIED
---
```

---

# 84. Suggested posmac-3.0.md Frontmatter

```yaml
---
product_family: POSMAC_3_0

requirements:
  - HIGH_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

industries:
  - ENERGY
  - CONSTRUCTION
  - INFRASTRUCTURE

applications:
  - SOLAR_STRUCTURE
  - OUTDOOR_STRUCTURE

source_documents:
  - 2025 POSMAC3.0.pdf

knowledge_status: VERIFIED
---
```

---

# 85. Suggested posmac-super.md Frontmatter

```yaml
---
product_family: POSMAC_SUPER

requirements:
  - EXTREME_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - CHEMICAL_RESISTANCE
  - SCRATCH_RESISTANCE

environments:
  - COASTAL
  - HIGH_SALINITY
  - HIGH_HUMIDITY
  - SEVERE_OUTDOOR

source_documents:
  - 2025 PosMAC super.pdf

knowledge_status: VERIFIED
---
```

---

# 86. Unknown States

Supported:

```text
COATED_PRODUCT_FAMILY_UNKNOWN

CORROSION_SEVERITY_UNKNOWN

BASE_MATERIAL_UNKNOWN

COATING_WEIGHT_UNKNOWN

POST_TREATMENT_UNKNOWN

SURFACE_REQUIREMENT_UNKNOWN

WELDING_REQUIREMENT_UNKNOWN

ENVIRONMENT_DATA_REQUIRED

SIZE_AVAILABILITY_CHECK_REQUIRED

CUSTOMER_PROCESS_VALIDATION_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 87. Product Hallucination Guardrail

Never invent:

```text
coating composition
coating amount
corrosion test result
surface treatment
warranty
service life
chemical resistance
welding parameter
available substrate grade
production dimension
customer approval
```

If unsupported:

```text
UNKNOWN
```

---

# 88. Source Authority

Canonical source ownership:

```text
GALVANIZED_STEEL
→ 2025 Galvanized Steel.pdf

ELECTRO_GALVANIZED_STEEL
→ 2025 Electro Galvanized Steel.pdf

POSMAC_1_5
→ 2025 POSMAC1.5.pdf

POSMAC_3_0
→ 2025 POSMAC3.0.pdf

POSMAC_SUPER
→ 2025 PosMAC super.pdf
```

Dedicated product catalog outranks cross-references from another product catalog.

---

# 89. Source Conflict Rule

If multiple catalogs provide different:

```text
coating amount
dimension
surface treatment
test condition
product availability
```

do not reconcile silently.

Use:

```text
SOURCE_CONFLICT
```

and prefer:

```text
DEDICATED_PRODUCT_GUIDE
```

as canonical.

---

# 90. Final Coated-Steel Routing Chain

```text
CUSTOMER / INDUSTRY SIGNAL
↓
APPLICATION
↓
COMPONENT
↓
BASE STEEL
↓
ENVIRONMENT
↓
CORROSION SEVERITY
↓
SURFACE / PAINT / WELD / FORM REQUIREMENT
↓
COATED PRODUCT FAMILY
↓
GI / GA / GI_H
or
EG PURE Zn / Zn-Ni
or
POSMAC 1.5 / 3.0 / Super
↓
PRODUCT MD
↓
COATING / POST-TREATMENT / SPECIFICATION
↓
ENGINEERING VALIDATION
↓
MARKETING OPPORTUNITY
```

---

# 91. Final Rule

The goal of this router is NOT:

```text
MAXIMUM CORROSION RESISTANCE
```

The goal is:

```text
RIGHT CORROSION PERFORMANCE
+
RIGHT SURFACE QUALITY
+
RIGHT FORMABILITY
+
RIGHT WELDABILITY
+
RIGHT PAINTABILITY
+
RIGHT APPLICATION
```

The preferred selection order is:

```text
APPLICATION
↓
ENVIRONMENT
↓
CORROSION
↓
FABRICATION
↓
SURFACE
↓
PRODUCT FAMILY
```

not:

```text
MOST ADVANCED COATING
↓
JUSTIFY LATER
```

The responsibility of this file ends at:

```text
SELECT THE CORRECT COATED PRODUCT KNOWLEDGE FILE.
```

Final product specification remains a product/engineering decision.
