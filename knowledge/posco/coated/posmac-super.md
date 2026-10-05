---
product_family: POSMAC_SUPER

name_ko: PosMAC Super
name_en: POSCO Magnesium Aluminium Alloy Coating Product Super

material_category:
  - COATED_STEEL
  - CORROSION_RESISTANT_ALLOY_COATED_STEEL
  - ZN_MG_AL_ALLOY_COATED_STEEL

coating_system:
  base: Zn
  Mg_percent: 5.0
  Al_percent: 12.0

base_materials:
  - HOT_ROLLED_STEEL

industries:
  - ENERGY
  - CONSTRUCTION
  - INFRASTRUCTURE
  - INDUSTRIAL_PLANT
  - AQUACULTURE
  - AGRICULTURE

applications:
  - FLOATING_SOLAR_STRUCTURE
  - FLOATING_SOLAR_WALKWAY
  - ONSHORE_SOLAR_STRUCTURE
  - INDUSTRIAL_PLANT_STRUCTURE
  - INDUSTRIAL_CABLE_TRAY
  - AQUACULTURE_STRUCTURE
  - BRIDGE_SAFETY_BARRIER
  - GUARDRAIL
  - COASTAL_STREET_LIGHT_STRUCTURE
  - ROAD_SIGN
  - ROAD_NOISE_BARRIER
  - INDUSTRIAL_NOISE_BARRIER
  - FENCE
  - GREENHOUSE_EQUIPMENT

environments:
  - EXTREME_CORROSION
  - HIGH_SALINITY
  - HIGH_HUMIDITY
  - COASTAL
  - ISLAND_COASTAL
  - MARINE_ATMOSPHERE
  - WATER_SIDE
  - INDUSTRIAL_POLLUTION

requirements:
  - EXTREME_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE
  - BENDING_SECTION_CORROSION_RESISTANCE
  - CUP_FORMED_SECTION_CORROSION_RESISTANCE
  - CHEMICAL_RESISTANCE
  - AMMONIA_RESISTANCE
  - ACIDIC_ENVIRONMENT_RESISTANCE
  - ALKALINE_ENVIRONMENT_RESISTANCE
  - WHITE_RUST_RESISTANCE
  - GALLING_RESISTANCE
  - SCRATCH_RESISTANCE
  - WELDABILITY
  - STRUCTURAL_DURABILITY

post_treatments:
  - CE

standards:
  - KS_D_3030

source_documents:
  - 2025 PosMAC super.pdf

primary_source:
  - 2025 PosMAC super.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO PosMAC Super Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO PosMAC Super.

It should be loaded after:

```text
knowledge/posco/coated/index.md
```

selects:

```text
POSMAC_SUPER
```

as a relevant product family.

Its responsibility is to determine whether PosMAC Super is a defensible candidate based on:

```text
APPLICATION
↓
OPERATING ENVIRONMENT
↓
SALINITY / HUMIDITY / POLLUTION
↓
CORROSION SEVERITY
↓
CUT EDGE / FORMING / WELDING
↓
POSMAC_SUPER
↓
GRADE
↓
COATING MASS
↓
POST-TREATMENT
↓
SIZE
↓
ENGINEERING VALIDATION
```

This file does NOT automatically approve:

```text
exact service life
exact grade
exact coating mass
exact welding parameter
exact project warranty
exact orderable size
```

---

# 2. Product Definition

PosMAC Super is POSCO's ultra-high-corrosion-resistant Zn-Mg-Al coated steel.

Canonical coating composition:

```text
Zn
+
5% Mg
+
12% Al
```

Canonical product code:

```text
POSMAC_SUPER
```

The source positions the product specifically for:

```text
EXTREME_CORROSION_ENVIRONMENT
```

rather than ordinary atmospheric corrosion.

---

# 3. Core Product Positioning

Primary product concept:

```text
EXTREME_CORROSION_RESISTANCE
+
HIGH_SALINITY
+
HIGH_HUMIDITY
+
CUT_EDGE_RESISTANCE
+
STRUCTURAL_APPLICATION
```

Strongest routing contexts:

```text
WATER_SIDE_STRUCTURE
COASTAL_STRUCTURE
ISLAND_STRUCTURE
MARINE_ATMOSPHERE
INDUSTRIAL_POLLUTION
```

---

# 4. Relative Corrosion Position

The source positions PosMAC Super as having:

```text
> 10x corrosion resistance
vs ordinary GI / GI(H)
```

at the same coating mass in the documented comparison.

It also reports approximately:

```text
2x corrosion resistance
vs existing commercial high-corrosion-resistant alloy-coated products
```

in the source-defined comparison.

These values are:

```text
COMPARATIVE_TEST_RESULTS
```

not field-life guarantees.

---

# 5. Corrosion Claim Guardrail

Allowed:

```text
The catalog reports more than 10x corrosion resistance
versus ordinary GI/GI(H)
under the documented comparison conditions.
```

Allowed:

```text
The catalog reports about 2x higher corrosion performance
than the referenced commercial high-corrosion-resistant
alloy-coated products.
```

Forbidden:

```text
PosMAC Super lasts 10x longer in the field.
```

Forbidden:

```text
PosMAC Super always lasts twice as long as PosMAC 3.0.
```

---

# 6. PosMAC Super vs PosMAC 3.0

Source-supported directional comparison:

```text
POSMAC_3_0
→ HIGH_CORROSION

POSMAC_SUPER
→ EXTREME_CORROSION
```

The source reports PosMAC Super as approximately:

```text
2x stronger flat-surface corrosion performance
than PosMAC 3.0
```

under the documented CCT comparison.

It also reports:

```text
2x better bending-area corrosion performance
```

and:

```text
2x better cup-formed-area corrosion performance
```

than PosMAC 3.0 under the referenced tests.

---

# 7. PosMAC Super Selection Rule

Prefer PosMAC Super when:

```text
HIGH_SALINITY
+
HIGH_HUMIDITY
+
COASTAL / ISLAND
+
STRUCTURAL_APPLICATION
```

or:

```text
INDUSTRIAL_POLLUTION
+
STRONG_CHEMICAL_CORROSION_EXPOSURE
```

dominates.

Prefer PosMAC 3.0 first when:

```text
HIGH_CORROSION
```

is important but the environment is not yet clearly extreme.

---

# 8. PosMAC Super vs PosMAC 1.5

## PosMAC 1.5

Prioritize:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
AUTOMOTIVE
HOME_APPLIANCE
PRECOATED_STEEL
```

## PosMAC Super

Prioritize:

```text
EXTREME_CORROSION
COASTAL
MARINE_ATMOSPHERE
INDUSTRIAL_POLLUTION
STRUCTURAL_DURABILITY
```

Do not rank them as simple quality tiers.

---

# 9. Corrosion Mechanism

The source describes PosMAC Super as forming a dense:

```text
LDH
Layered Double Hydroxide
```

corrosion product.

Representative source compound:

```text
(Zn,Mg)6Al2(OH)16(CO3) · 4H2O
```

The elevated Mg and Al ratio promotes:

```text
DENSE
FAST
ROBUST
```

protective-film formation.

---

# 10. Corrosion-Mechanism Comparison

Directional source model:

```text
GI
→ porous Zn-based corrosion film

PosMAC 1.5 / 3.0
→ dense Zn-Mg corrosion-product film

PosMAC Super
→ fast and robust LDH film
```

This mechanism helps explain the product's extreme-corrosion positioning.

---

# 11. Cut-Edge Corrosion

PosMAC Super has strong source-supported:

```text
CUT_EDGE_CORROSION_RESISTANCE
```

When an edge is cut:

```text
adjacent coating dissolves
↓
corrosion products form
↓
exposed steel becomes covered
↓
corrosion progression is reduced
```

The source refers to this as:

```text
SELF_HEALING
```

---

# 12. Self-Healing Guardrail

`SELF_HEALING` does NOT mean:

```text
metal coating grows back
```

and does NOT mean:

```text
the cut edge never rusts
```

It refers to protective corrosion-product formation.

---

# 13. Initial Red Rust

The source explicitly states that:

```text
EXPOSED_CUT_EDGE
```

may initially develop:

```text
RED_RUST
```

because the base steel is exposed.

As characteristic corrosion products develop:

```text
initial red-rust area
may decrease over time
```

This distinction is mandatory.

---

# 14. Cut-Edge Thickness Rule

If base-steel thickness is:

```text
> 1.6 mm
```

the source recommends:

```text
REPAIR_PAINT
```

because the corrosion-product layer may not fully cover the cut edge.

---

# 15. Visual-Appearance Rule

Even if:

```text
thickness <= 1.6 mm
```

when:

```text
INITIAL_RED_RUST_NOT_ACCEPTABLE
```

the source recommends repair painting according to customer requirements.

Therefore:

```text
corrosion durability
```

and:

```text
initial appearance
```

must remain separate decision axes.

---

# 16. Flat-Surface Corrosion

The source CCT comparison reports:

```text
POSMAC_SUPER
vs
POSMAC_3_0
≈ 2x stronger
```

in flat-area corrosion performance.

It also reports:

```text
POSMAC_SUPER
vs
GI(H) / Batch GI
≈ 10x stronger
```

under the documented test comparison.

These are test-specific claims.

---

# 17. CCT Condition

The source uses:

```text
ISO 14993
```

with a representative cycle:

```text
Salt Spray
2 hr
5% NaCl
35°C

→ Dry
4 hr
25% RH
60°C

→ Humid
2 hr
95% RH
50°C
```

Any numerical comparison must retain the test method.

---

# 18. Bending-Area Corrosion

The source reports PosMAC Super as having approximately:

```text
2x better bending-area corrosion resistance
than PosMAC 3.0
```

and approximately:

```text
5x better
than GI(H) / Batch GI
```

under the referenced comparison.

This is a:

```text
COMPARATIVE_TEST_RESULT
```

not a universal factor.

---

# 19. Cup-Formed Corrosion

The source also reports approximately:

```text
2x better cup-formed-area corrosion performance
than PosMAC 3.0
```

in the documented test.

Strong use signal:

```text
FORMED_STRUCTURE
+
SEVERE_CORROSION
```

---

# 20. Customer-Fabricated Product Evaluation

The catalog evaluates fabricated components such as:

```text
CABLE_TRAY
```

against:

```text
BATCH_GI FABRICATED PRODUCTS
```

under CCT.

This supports PosMAC Super for:

```text
FABRICATED_STRUCTURAL_COMPONENT
```

applications where:

```text
HOLES
CUT_EDGES
BENDS
```

create corrosion risk.

---

# 21. Extreme Environment Routing

Strong route:

```text
HIGH_SALINITY
+
HIGH_HUMIDITY
+
MARINE_ATMOSPHERE
+
STRUCTURAL_STEEL
→ POSMAC_SUPER
```

This is one of the strongest routing rules in the coated Product Brain.

---

# 22. Main Source-Supported Applications

The source lists applications including:

```text
FLOATING_SOLAR_SUPPORT_STRUCTURE
FLOATING_SOLAR_WALKWAY
ONSHORE_SOLAR_STRUCTURE_NEAR_COAST
INDUSTRIAL_PLANT_STRUCTURE
INDUSTRIAL_CABLE_TRAY
AQUACULTURE_STRUCTURE
BRIDGE_SAFETY_BARRIER
GUARDRAIL
COASTAL_STREET_LIGHT_STRUCTURE
ROAD_SIGN
ROAD_NOISE_BARRIER
INDUSTRIAL_NOISE_BARRIER
FENCE
GREENHOUSE_OPENING_EQUIPMENT
```

These are source-supported application examples.

---

# 23. Floating Solar Routing

Strong route:

```text
FLOATING_SOLAR
+
MARINE / HIGH_SALINITY ENVIRONMENT
+
STRUCTURAL_COMPONENT
→ POSMAC_SUPER
```

This is stronger evidence than:

```text
SOLAR
→ POSMAC_SUPER
```

because ordinary inland solar may not require the extreme-corrosion route.

---

# 24. Coastal Onshore Solar

Input:

```text
ONSHORE_SOLAR
+
CLOSE_TO_COAST
+
HIGH_CORROSION_ENVIRONMENT
```

Strong candidate:

```text
POSMAC_SUPER
```

Possible comparison:

```text
POSMAC_3_0
```

if actual salinity/exposure is uncertain.

---

# 25. Aquaculture Routing

The source directly includes:

```text
AQUACULTURE_STRUCTURE
```

in marine-environment applications.

This supports PosMAC Super where:

```text
HIGH_HUMIDITY
+
SALINITY
+
STRUCTURAL_CORROSION
```

are major drivers.

Do not automatically extrapolate this to:

```text
PERMANENT_FULL_SEAWATER_IMMERSION
```

without additional evidence.

---

# 26. Plant Environment Routing

Strong route:

```text
INDUSTRIAL_PLANT
+
POLLUTED_ATMOSPHERE
+
HIGH_CORROSION
→ POSMAC_SUPER
```

Examples:

```text
PLANT_STRUCTURE
PLANT_CABLE_TRAY
```

---

# 27. Chemical Resistance

The source evaluates PosMAC Super across acidic and alkaline environments.

It reports lower coating weight loss than referenced:

```text
GI(H)
POSMAC_3_0
```

under the tested pH range.

This supports:

```text
CHEMICAL_RESISTANCE
```

as a routing property.

---

# 28. pH Test Scope

The source includes pH testing approximately over:

```text
pH 3.0–13.5
```

using:

```text
H2SO4
NaOH
```

based solutions.

Do not generalize this into:

```text
UNIVERSAL_CHEMICAL_RESISTANCE
```

---

# 29. Chemical-Service Guardrail

Chemical suitability depends on:

```text
chemical species
concentration
temperature
exposure duration
immersion
atmospheric exposure
mechanical condition
```

Therefore:

```text
CHEMICAL_SERVICE
```

may require comparison with:

```text
STAINLESS
TITANIUM
ANCOR
```

depending on service conditions.

---

# 30. Ammonia Resistance

The source includes:

```text
5% AMMONIA SOLUTION
```

immersion testing.

It reports PosMAC Super as having stronger chemical resistance than compared:

```text
GALVALUME
GI(H)
POSMAC_3_0
```

under that test.

This is relevant to:

```text
AGRICULTURE
LIVESTOCK
INDUSTRIAL_ENVIRONMENT
```

where ammonia exposure is plausible.

---

# 31. Ammonia Guardrail

Do not infer:

```text
5% ammonia test
→ all ammonia environments
```

Exact concentration and exposure mode matter.

---

# 32. Acidic Droplet Environment

The source also reports strong performance in an:

```text
ACIDIC_DROPLET
```

evaluation compared with:

```text
POSMAC_3_0
BATCH_GI
GI(H)
```

This can support industrial-atmosphere routing.

---

# 33. White Rust

PosMAC Super may still develop:

```text
WHITE_RUST
```

as with other zinc-based coated steels.

High red-rust resistance does NOT imply:

```text
NO_WHITE_RUST
```

---

# 34. White-Rust Mechanism

The dense LDH corrosion product contributes to:

```text
RED_RUST_DELAY
```

but white surface corrosion products may still appear.

Therefore:

```text
WHITE_RUST
```

and:

```text
SUBSTRATE_FAILURE
```

must remain distinct.

---

# 35. Storage Rule

Before installation, store:

```text
COIL
SHEET
FABRICATED_PART
```

in:

```text
DRY
+
WELL_VENTILATED
```

conditions.

Avoid placing material directly on the floor where moisture vapor may accumulate.

---

# 36. Coil Storage

The source recommends:

```text
moisture barrier on floor
+
wooden supports
+
air circulation
```

for coil storage.

Long-term storage should be avoided.

---

# 37. Wet Packaging Caution

Avoid:

```text
WET_MATERIAL
+
SEALED_PLASTIC_COVER
```

because trapped moisture can accelerate surface reaction.

If temporary rain protection is used:

```text
remove cover after rain
↓
allow moisture to evaporate
```

---

# 38. FIFO Rule

For long-term stock:

```text
FIRST_IN_FIRST_OUT
```

is recommended because white-rust risk increases with storage duration.

Opened bare coils should be consumed quickly.

---

# 39. Bare Packaging

The source states that if:

```text
BARE_PACKAGING
```

is selected:

```text
WHITE_RUST_QUALITY_WARRANTY
```

is not provided.

This should trigger:

```text
WHITE_RUST_WARRANTY_WARNING
```

---

# 40. Galling Resistance

The source states PosMAC Super has higher coating hardness than GI and therefore demonstrates strong:

```text
GALLING_RESISTANCE
```

during press processing.

Potential benefit:

```text
REDUCED_DIE_CONTAMINATION
```

---

# 41. Scratch Resistance

The catalog also identifies improved:

```text
SCRATCH_RESISTANCE
```

relative to GI in the referenced comparison.

This is a process benefit, not proof of scratch immunity.

---

# 42. Continuous Water Contact

The source warns that where moisture:

```text
CONTINUOUSLY CONTACTS
```

the coating surface, early corrosion may occur.

Therefore structures should be designed to avoid:

```text
WATER_TRAP
PERSISTENT_DIRECT_WATER_CONTACT
```

where possible.

---

# 43. Continuous Water Contact Rule

If:

```text
CONTINUOUS_WATER_CONTACT
```

is present:

return:

```text
DESIGN_DETAIL_REVIEW_REQUIRED
```

Possible actions:

```text
improve drainage
avoid water pockets
use additional protective material
```

as supported by project design.

---

# 44. Soil Contact

For solar or field structures:

```text
DIRECT_SOIL_CONTACT
```

should be avoided.

Use:

```text
PALLET
SUPPORT
```

during storage and site handling.

Contamination should be removed promptly.

---

# 45. Surface Blackening

The source notes that:

```text
BLACKENING
```

may occur as surface gloss decreases with time.

It is accelerated by:

```text
HIGH_TEMPERATURE
+
HIGH_HUMIDITY
```

The source treats it as a zinc-coating oxidation phenomenon rather than automatic functional failure.

---

# 46. Welding

PosMAC Super can be used in:

```text
ARC_WELDING
HIGH_FREQUENCY_INDUCTION_WELDING
```

for welded structures.

The source states its weldability and weld quality are similar to currently commercialized ternary high-corrosion-resistant coated steel under appropriate conditions.

---

# 47. Welding Guardrail

Every welding application requires:

```text
WELD_PARAMETER_OPTIMIZATION
```

Final conditions must verify:

```text
JOINT_STRENGTH
WELD_QUALITY
```

---

# 48. Liquid-Metal Embrittlement Caution

The source warns that depending on welded structural geometry and stress state:

```text
LIQUID_METAL_EMBRITTLEMENT_CRACKING
```

may occur.

Potential contributing stresses include:

```text
COMPRESSIVE_STRESS
TENSILE_STRESS
```

during welding.

Therefore:

```text
WELDED_STRUCTURAL_APPLICATION
→ WELDING_ENGINEERING_REVIEW_REQUIRED
```

---

# 49. Post-Treatment

Current manufacturing specification lists:

```text
CE
```

as the primary source-supported post-treatment.

Canonical:

```text
CE
= Cr3+ ECO Chromate
```

---

# 50. CE Characteristics

The source describes CE as providing:

```text
WHITE_RUST_RESISTANCE
```

using:

```text
Cr3+
```

chemistry.

It does not contain:

```text
Cr6+
```

but:

```text
CE ≠ CHROMIUM_FREE
```

---

# 51. Manufacturing Form

Current source-supported manufacturing route is:

```text
HOT_ROLLED_BASE
```

with general and structural grades.

Do not assume a CR-base PosMAC Super route from this source.

---

# 52. General Manufacturing Range

The source gives a general manufacturing range approximately:

```text
thickness:
1.15–6.0 mm

width:
880–1400 mm
```

for the product specification section.

The equipment capability section separately shows broader line capability up to:

```text
800–1650 mm
```

but exact product orderability must follow the product-specification tables and inquiry process.

---

# 53. Width Guardrail

For:

```text
width > 1400 mm
```

the source requires:

```text
SEPARATE_CONSULTATION
```

Do not assume standard availability.

---

# 54. Coating Mass

Source-supported total coating mass:

```text
120–430 g/m²
```

for PosMAC Super.

---

# 55. Heavy Coating Rule

For coating mass:

```text
> 350 g/m²
```

the source requires:

```text
SIZE_CONSULTATION_REQUIRED
```

because size availability may differ.

---

# 56. Coating Mass Selection

The ordering guide states:

```text
CORROSIVE_ENVIRONMENT
→ heavier coating may be favorable
```

while:

```text
FORMABILITY
+
WELDABILITY
→ lighter coating may be favorable
```

Therefore:

```text
MAXIMUM_COATING_MASS
```

is not automatically optimal.

---

# 57. Pre-Order Review

All exact orders should check:

```text
GRADE
COATING_MASS
THICKNESS
WIDTH
POST_TREATMENT
EDGE
END_USE
```

Return:

```text
QUALITY_INQUIRY_SPEC_REVIEW_REQUIRED
```

for exact orderability.

---

# 58. Grade Architecture

The source includes:

```text
CQ
STRUCTURAL
```

classes.

Representative POSCO grade keys include:

```text
PM5HT270CQ
PM5HT340R
PM5HT400R
PM5HT440C
PM5HT490C
PM5HT540C
PM5HY550B
```

These should remain grade-level retrieval keys.

---

# 59. Representative Grade Data

Source-supported minimum mechanical values include:

```text
PM5HT270CQ
YP 170–400 MPa
TS 270–450 MPa
EL ≥30%

PM5HT340R
YP ≥245 MPa
TS ≥340 MPa
EL ≥20%

PM5HT400R
YP ≥295 MPa
TS ≥400 MPa
EL ≥18%

PM5HT440C
YP ≥335 MPa
TS ≥440 MPa
EL ≥18%

PM5HT490C
YP ≥365 MPa
TS ≥490 MPa
EL ≥16%

PM5HT540C
YP ≥400 MPa
TS ≥540 MPa
EL ≥16%

PM5HY550B
YP ≥550 MPa
TS ≥560 MPa
EL ≥5%
```

These values belong to exact grade analysis, not daily intelligence.

---

# 60. Coating Metal Bending

The source also provides:

```text
CMB
Coating Metal Bending
```

requirements by grade.

Do not use one CMB value for the entire PosMAC Super family.

---

# 61. KS Standard

The source states POSCO obtained:

```text
KS D 3030
```

certification for PosMAC products.

Standard scope:

```text
HOT-DIP ZINC-ALUMINIUM-MAGNESIUM
ALLOY COATED STEEL SHEETS AND COILS
```

Exact certified grade mapping should be checked at grade level.

---

# 62. Exact Grade Selection Inputs

Before choosing a grade, collect:

```text
component
required YP
required TS
required elongation
structural load
forming requirement
bending requirement
thickness
width
coating mass
welding process
environment
customer specification
```

If missing:

```text
POSMAC_SUPER_GRADE_UNKNOWN
```

---

# 63. Extreme Coastal Routing

Input:

```text
ISLAND_COASTAL_STRUCTURE
+
HIGH_SALINITY
+
HIGH_HUMIDITY
```

Strong candidate:

```text
POSMAC_SUPER
```

This is one of the highest-confidence product routes.

---

# 64. Floating Solar Example

```yaml
industry: ENERGY

application:
  - FLOATING_SOLAR_STRUCTURE

environment:
  - HIGH_SALINITY
  - HIGH_HUMIDITY
  - WATER_SIDE

requirements:
  - EXTREME_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

product_candidate:
  POSMAC_SUPER

priority:
  P1

missing_information:
  - exact_salinity
  - component
  - thickness
  - coating_mass
  - welding_process
```

---

# 65. Coastal Solar Example

```yaml
industry: ENERGY

application:
  - ONSHORE_SOLAR_STRUCTURE

environment:
  - COASTAL
  - HIGH_CORROSION

product_candidates:
  - product: POSMAC_SUPER
    priority: P1

  - product: POSMAC_3_0
    priority: P2

selection_basis:
  - salinity
  - humidity
  - cut_edge_exposure
  - durability_requirement
```

---

# 66. Industrial Cable Tray Example

```yaml
industry: INDUSTRIAL_PLANT

application:
  - CABLE_TRAY

environment:
  - INDUSTRIAL_POLLUTION

requirements:
  - CHEMICAL_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

product_candidate:
  POSMAC_SUPER
```

---

# 67. Aquaculture Example

```yaml
industry: AQUACULTURE

application:
  - AQUACULTURE_STRUCTURE

environment:
  - MARINE_ATMOSPHERE
  - HIGH_HUMIDITY
  - HIGH_SALINITY

product_candidate:
  POSMAC_SUPER

boundary:
  continuous_seawater_immersion:
    status: SERVICE_CONDITION_REVIEW_REQUIRED
```

---

# 68. Bridge / Road Infrastructure Example

Possible applications:

```text
BRIDGE_SAFETY_BARRIER
GUARDRAIL
ROAD_SIGN
NOISE_BARRIER
```

Strong route when:

```text
COASTAL
or
HIGH_CORROSION
```

conditions are present.

---

# 69. GI Replacement Hypothesis

Input:

```text
current material:
THICK_GI / BATCH_GI

problem:
HIGH_CORROSION
+
CUT_EDGE_CORROSION

environment:
COASTAL
```

Possible opportunity:

```text
POSMAC_SUPER
```

classification:

```text
SUBSTITUTION_CANDIDATE
```

not:

```text
DIRECT_REPLACEMENT
```

---

# 70. PosMAC 3.0 Upgrade Hypothesis

Input:

```text
current material:
POSMAC_3_0

problem:
corrosion requirement increased

environment:
HIGH_SALINITY
HIGH_HUMIDITY
```

Potential opportunity:

```text
POSMAC_SUPER
```

Need:

```text
environment data
coating mass
forming requirement
welding
cost
qualification
```

before recommendation.

---

# 71. Negative Routing Rules

## Ordinary indoor corrosion

Do NOT route:

```text
POSMAC_SUPER
```

GI / EG may be more suitable.

---

## Appliance surface application

Do NOT default to PosMAC Super.

Evaluate:

```text
POSMAC_1_5
EG
GI
```

first.

---

## General outdoor solar

Do NOT automatically select PosMAC Super.

Evaluate actual:

```text
salinity
humidity
coastal distance
cut-edge exposure
```

---

## Chemical process vessel

Do NOT select PosMAC Super only from:

```text
CHEMICAL
```

Stainless, titanium or specialized steel may be required.

---

## Continuous seawater immersion

Do NOT assume PosMAC Super qualification solely from marine-atmosphere applications.

---

# 72. Product Routing Score

Suggested score:

```text
Application Match          15%
Corrosion Severity         25%
Salinity / Humidity        20%
Cut-Edge Requirement       10%
Formed-Section Exposure    10%
Chemical Environment       10%
Fabrication Match           5%
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
DO_NOT_SELECT
```

---

# 73. Product Candidate Object

```yaml
product_family: POSMAC_SUPER

application:
  FLOATING_SOLAR_STRUCTURE

environment:
  - HIGH_SALINITY
  - HIGH_HUMIDITY
  - WATER_SIDE

requirements:
  - EXTREME_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

reason:
  - direct source-supported marine-environment application
  - extreme corrosion requirement
  - cut-edge requirement

missing_information:
  - exact_grade
  - coating_mass
  - thickness
  - width
  - welding_process

final_status:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 74. Grade Candidate Object

```yaml
product_family: POSMAC_SUPER

grade_candidates:
  - PM5HT270CQ
  - PM5HT340R
  - PM5HT400R
  - PM5HT440C
  - PM5HT490C
  - PM5HT540C
  - PM5HY550B

selection_status:
  POSMAC_SUPER_GRADE_UNKNOWN

required_inputs:
  - strength
  - elongation
  - thickness
  - forming
  - structural_load
```

---

# 75. Welding Candidate Object

```yaml
product_family: POSMAC_SUPER

joining_process:
  ARC_WELDING

welding_status:
  WELDING_PARAMETER_OPTIMIZATION_REQUIRED

technical_risks:
  - LIQUID_METAL_EMBRITTLEMENT_CRACKING

required_checks:
  - joint_strength
  - weld_quality
  - component_geometry
  - stress_state
  - heat_input
```

---

# 76. Daily Intelligence Mode

Automated intelligence should normally stop at:

```text
POSMAC_SUPER
```

Do not retrieve automatically:

```text
exact grade
exact coating mass
exact welding parameter
warranty
exact service life
```

Recommended configuration:

```yaml
daily_posmac_super:
  allow_product_family: true
  allow_grade_candidate: false
  allow_exact_coating_mass: false
  allow_service_life_prediction: false
  allow_warranty_claim: false
  allow_pdf_lookup: false
```

---

# 77. Marketing Mode

Marketing analysis may include:

```text
customer environment
current coating
corrosion issue
cut-edge issue
PosMAC Super relevance
PosMAC 3.0 comparison
replacement hypothesis
technical questions
```

Example:

```text
Customer operates coastal solar structures
with high salinity and persistent humidity.

PosMAC Super is a strong candidate because the source
positions it specifically for high-salinity,
high-humidity and coastal structural environments.

Next checks:
actual salt exposure,
component geometry,
cut-edge condition,
coating mass,
welding method.
```

---

# 78. Engineering Mode

Engineering analysis may retrieve:

```text
grade
YP
TS
elongation
CMB
coating mass
post-treatment
thickness
width
welding
cut-edge repair
CCT
chemical resistance
```

from the source.

---

# 79. Warranty Guardrail

The source includes project-specific durability warranty examples.

Do NOT infer:

```text
ALL POSMAC SUPER
→ fixed-year warranty
```

The source indicates warranty conditions depend on:

```text
named customer
specific project
specific environment
surface damage
corrosion exposure
```

and applies to structural durability rather than simply guaranteeing no white/red rust.

Return:

```text
WARRANTY_ELIGIBILITY_CONFIRMATION_REQUIRED
```

---

# 80. EPD / Environmental Information

The source states PosMAC Super has:

```text
EPD
Environmental Product Declaration
```

certification referencing:

```text
ISO 14025
EN 15804
ISO 21930:2017
```

This can be stored as:

```text
ENVIRONMENTAL_PRODUCT_ATTRIBUTE
```

not as a corrosion-performance metric.

---

# 81. Ordering Inputs

Before exact product selection, collect:

```text
final application
environment
salinity
humidity
chemical exposure
grade
mechanical requirement
coating mass
post-treatment
oil
thickness
width
edge type
welding
cut-edge appearance requirement
```

---

# 82. Edge Selection

The source allows:

```text
MILL_EDGE
SLIT_EDGE
```

selection.

When the supplied edge remains exposed in the final product:

```text
SLIT_EDGE
```

may be preferred according to ordering guidance.

Exact selection depends on downstream fabrication.

---

# 83. Weld-Seam Inclusion

Coils may contain:

```text
WELDED_SECTION
```

that can have:

```text
higher hardness
slightly greater thickness
```

than surrounding material.

If customers cannot tolerate such areas:

```text
NO_WELD_SEAM_OPTION
```

should be requested.

---

# 84. Post-Treatment / Oiling

Ordering should consider:

```text
POST_TREATMENT
OILING
```

based on use environment.

The source warns that:

```text
UNTREATED
+
UNOILED
```

conditions can increase white-rust risk.

---

# 85. Product-Use Change

Material ordered for one application should not automatically be transferred to another application.

If:

```text
ORDERED_USE
≠
NEW_USE
```

return:

```text
APPLICATION_REVALIDATION_REQUIRED
```

---

# 86. Numeric Data Classification

Every numeric value should preserve:

```yaml
value:
unit:
value_type:
test_method:
test_condition:
sample_condition:
source_document:
```

Allowed:

```text
SPECIFICATION
MANUFACTURING_RANGE
COMPARATIVE_TEST_RESULT
APPLICATION_TEST_RESULT
```

---

# 87. Source Authority

Canonical source:

```text
2025 PosMAC super.pdf
```

For PosMAC Super claims this source overrides:

```text
generic model knowledge
cross-product summaries
unverified external claims
```

unless a newer approved source is added.

---

# 88. Source Conflict Rule

If another document provides different:

```text
grade
size
coating mass
post-treatment
performance comparison
```

do not silently reconcile.

Use:

```text
SOURCE_CONFLICT
```

and prefer:

```text
LATEST_DEDICATED_PRODUCT_GUIDE
```

---

# 89. Unknown States

Supported:

```text
POSMAC_SUPER_GRADE_UNKNOWN

CORROSION_SEVERITY_UNKNOWN

SALINITY_UNKNOWN

HUMIDITY_UNKNOWN

COATING_MASS_UNKNOWN

POST_TREATMENT_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

CUT_EDGE_REPAIR_REVIEW_REQUIRED

CONTINUOUS_WATER_CONTACT_REVIEW_REQUIRED

CHEMICAL_SERVICE_REVIEW_REQUIRED

WELDING_PARAMETER_OPTIMIZATION_REQUIRED

WARRANTY_ELIGIBILITY_CONFIRMATION_REQUIRED

QUALITY_INQUIRY_SPEC_REVIEW_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 90. Retrieval Keywords

```text
PosMAC Super
POSMAC SUPER
Zn-5Mg-12Al
Zn-5%Mg-12%Al
초고내식강
고염도
고습도
도서해안
해안 구조물
수상태양광
해양환경
Marine atmosphere
Floating solar
Aquaculture
Cable tray
Self-healing
LDH
Layered Double Hydroxide
절단면 내식성
고내식 도금
```

Keywords are retrieval aids only.

---

# 91. Routing Algorithm

```pseudo
function route_posmac_super(context):

    identify application
    identify environment
    identify salinity
    identify humidity
    identify corrosion_severity
    identify cut_edge
    identify formed_sections
    identify chemical_exposure

    if corrosion_severity != EXTREME:
        compare POSMAC_3_0
        do not default POSMAC_SUPER

    if (
        HIGH_SALINITY
        and HIGH_HUMIDITY
        and STRUCTURAL_APPLICATION
    ):
        candidate = POSMAC_SUPER

    if COASTAL or ISLAND_COASTAL or MARINE_ATMOSPHERE:
        increase candidate priority

    if cut_edge or formed_section:
        increase candidate priority

    if chemical_exposure:
        verify source-supported chemical environment
        add CHEMICAL_SERVICE_REVIEW_REQUIRED when needed

    if continuous_water_contact:
        add DESIGN_DETAIL_REVIEW_REQUIRED

    verify:
        grade
        coating_mass
        post_treatment
        thickness
        width
        edge
        welding

    return candidate
```

---

# 92. Weak Example

Bad:

```text
Coastal project
→ PosMAC Super
```

Why weak:

```text
salinity unknown
humidity unknown
application unknown
corrosion severity unknown
```

Better:

```text
Coastal structural project
+
high salinity
+
high humidity
+
exposed cut edges
→ PosMAC Super strong candidate
```

---

# 93. Strong Example

```text
Customer is constructing a floating solar
support structure in a marine environment.

Environment:
high salinity + high humidity

Component:
fabricated structural steel with cut edges

Material requirement:
extreme corrosion resistance
+
cut-edge corrosion resistance

POSCO candidate:
PosMAC Super

Next checks:
grade, thickness, coating mass,
welding process and cut-edge repair requirement.
```

---

# 94. Product Hallucination Guardrail

Never invent:

```text
grade
coating mass
service life
warranty
customer adoption
chemical compatibility
welding parameter
cut-edge performance
project suitability
```

If not supported:

```text
UNKNOWN
```

---

# 95. Final Knowledge Chain

```text
CUSTOMER SIGNAL
↓
APPLICATION
↓
COASTAL / WATER / INDUSTRIAL ENVIRONMENT
↓
SALINITY + HUMIDITY
↓
EXTREME CORROSION
↓
CUT EDGE / FORMED AREA
↓
POSMAC_SUPER
↓
GRADE
↓
COATING MASS
↓
POST-TREATMENT
↓
SIZE / EDGE
↓
WELDING / DESIGN REVIEW
↓
ENGINEERING APPROVAL
↓
MARKETING OPPORTUNITY
```

---

# 96. Final Rule

The purpose of PosMAC Super is NOT:

```text
MOST EXPENSIVE / MOST ADVANCED COATING
→ USE EVERYWHERE
```

The correct product position is:

```text
EXTREME CORROSION
+
HIGH SALINITY
+
HIGH HUMIDITY
+
COASTAL / MARINE ATMOSPHERE
+
CUT-EDGE AND FORMED-SECTION DURABILITY
```

The preferred reasoning order is:

```text
ENVIRONMENT
↓
CORROSION SEVERITY
↓
APPLICATION
↓
CUT / FORM CONDITION
↓
POSMAC SUPER
↓
GRADE / COATING / POST-TREATMENT
```

not:

```text
POSMAC SUPER
↓
find a use for it
```

The responsibility of this file ends at:

```text
DEFENSIBLE POSMAC SUPER PRODUCT CANDIDATE
```

Final customer specification remains subject to product-quality, welding, design and engineering review.
