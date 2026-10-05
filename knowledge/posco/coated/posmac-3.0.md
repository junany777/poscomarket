---
product_family: POSMAC_3_0

name_ko: PosMAC 3.0
name_en: POSCO Magnesium Aluminium Alloy Coating Product 3.0

material_category:
  - COATED_STEEL
  - CORROSION_RESISTANT_ALLOY_COATED_STEEL
  - ZN_MG_AL_ALLOY_COATED_STEEL

coating_system:
  base: Zn
  Mg_percent: 3.0
  Al_percent: 2.5

base_materials:
  - HOT_ROLLED_STEEL
  - COLD_ROLLED_STEEL

industries:
  - ENERGY
  - CONSTRUCTION
  - INFRASTRUCTURE
  - AGRICULTURE
  - AQUACULTURE
  - HOME_APPLIANCE
  - ELECTRICAL_EQUIPMENT

applications:
  - SOLAR_STRUCTURE
  - FLOATING_SOLAR_STRUCTURE
  - SOLAR_C_CHANNEL
  - SOLAR_THERMAL_SUPPORT
  - COOLING_TOWER
  - SILO
  - PEB_BUILDING
  - SOUND_BARRIER_BACK_PANEL
  - WATER_TANK
  - ROCK_BOLT
  - SANDWICH_PANEL
  - CORRUGATED_PIPE
  - GUARDRAIL
  - BUILDING_ROOF
  - BUILDING_WALL
  - MOTOR_CASE
  - GREENHOUSE
  - POULTRY_FARM
  - AQUACULTURE_FACILITY
  - SWITCHBOARD
  - PIPE
  - PLANT_FACTORY_STRUCTURE
  - CABLE_TRAY
  - GREENHOUSE_PAD
  - GUTTER
  - STEEL_CURTAIN_WALL

requirements:
  - HIGH_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE
  - BENDING_SECTION_CORROSION_RESISTANCE
  - CUP_FORMED_SECTION_CORROSION_RESISTANCE
  - CHEMICAL_RESISTANCE
  - WHITE_RUST_RESISTANCE
  - GALLING_RESISTANCE
  - SCRATCH_RESISTANCE
  - FORMABILITY
  - WELDABILITY
  - PAINTABILITY
  - CONDUCTIVITY

special_products:
  - M630

post_treatments:
  - NB
  - NT
  - CE
  - CL

standards:
  - KS_D_3030
  - DIN_EN_10346
  - ASTM_A1046M

source_documents:
  - 2025 POSMAC3.0.pdf

primary_source:
  - 2025 POSMAC3.0.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO PosMAC 3.0 Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO PosMAC 3.0.

It should be loaded after:

```text
knowledge/posco/coated/index.md
```

selects:

```text
POSMAC_3_0
```

as a relevant product family.

Its responsibility is to determine whether PosMAC 3.0 is a defensible candidate based on:

```text
APPLICATION
↓
BASE MATERIAL
↓
OPERATING ENVIRONMENT
↓
CORROSION SEVERITY
↓
CUT / BEND / FORM CONDITION
↓
CHEMICAL / WATER / SALT EXPOSURE
↓
POSMAC_3_0
↓
STANDARD PRODUCT or M630
↓
COATING MASS
↓
POST-TREATMENT
↓
SIZE / GRADE
↓
ENGINEERING VALIDATION
```

This file does NOT independently approve:

```text
exact service life
exact coating mass
exact grade
exact post-treatment
exact orderable dimension
final customer specification
```

---

# 2. Product Definition

PosMAC 3.0 is a ternary Zn-Mg-Al alloy coated steel developed by POSCO.

Canonical composition:

```text
Zn
+
3% Mg
+
2.5% Al
```

Canonical code:

```text
POSMAC_3_0
```

The product should be treated as a distinct coated-steel family rather than a generic galvanized product.

---

# 3. Core Product Positioning

The core role of PosMAC 3.0 is:

```text
HIGH_CORROSION_RESISTANCE
+
CUT_EDGE_CORROSION_RESISTANCE
+
FORMED_SECTION_CORROSION_RESISTANCE
```

with the additional ability to use processing concepts similar to ordinary GI.

Strong routing domains include:

```text
SOLAR
OUTDOOR_STRUCTURE
BUILDING
INFRASTRUCTURE
AGRICULTURE
AQUACULTURE
```

---

# 4. Core Source Position

The approved product source states that PosMAC 3.0 provides:

```text
5–10x higher corrosion resistance
```

than ordinary GI / GI(H) at the same coating mass in the documented comparisons.

It also identifies particularly strong:

```text
CROSS_SECTION / CUT_EDGE CORROSION RESISTANCE
```

and states that thick conventional zinc coatings may in some applications be replaced by a PosMAC 3.0 solution.

This is an application-development opportunity, not an automatic substitution rule.

---

# 5. Corrosion Claim Guardrail

Allowed:

```text
The POSCO catalog reports 5–10x higher
corrosion resistance than ordinary GI/GI(H)
in the documented SST/CCT comparisons.
```

Forbidden:

```text
PosMAC 3.0 lasts 5–10x longer in service.
```

The following must remain attached to quantitative comparison:

```text
TEST_METHOD
TEST_CONDITION
COATING_MASS
EXPOSURE_DURATION
SAMPLE_GEOMETRY
POST_TREATMENT
```

---

# 6. PosMAC 3.0 vs GI

Strong transition logic:

```text
GI / GI_H
↓
corrosion resistance insufficient
↓
cut edge or formed area becomes critical
↓
POSMAC_3_0 candidate
```

Advantages described by the source include:

```text
FLAT_SURFACE_CORROSION
BENDING_AREA_CORROSION
CUP_AREA_CORROSION
CUT_EDGE_CORROSION
```

relative to the referenced GI conditions.

---

# 7. GI-Compatible Processing

The source states that PosMAC 3.0 may use processing comparable to conventional GI for:

```text
PROCESSING
ASSEMBLY
PAINTING
```

This supports:

```text
PROCESS_COMPATIBILITY_CANDIDATE
```

but not:

```text
NO_VALIDATION_REQUIRED
```

Customer-specific:

```text
forming
joining
painting
surface treatment
```

must still be validated.

---

# 8. PosMAC 3.0 vs PosMAC 1.5

This distinction must remain explicit.

## PosMAC 1.5

Prioritize:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
PRECOATED_STEEL
AUTOMOTIVE
HOME_APPLIANCE
```

## PosMAC 3.0

Prioritize:

```text
HIGHER_CORROSION_PRIORITY
CUT_EDGE_CORROSION
OUTDOOR_STRUCTURE
HARSHER_ENVIRONMENT
```

Do not represent PosMAC 3.0 as universally superior.

---

# 9. PosMAC 3.0 vs PosMAC Super

PosMAC 3.0 should normally cover:

```text
HIGH_CORROSION
SEVERE_OUTDOOR
CUT_EDGE
STRUCTURAL_APPLICATION
```

PosMAC Super should be separately evaluated when:

```text
EXTREME_CORROSION
HIGH_SALINITY
HIGH_HUMIDITY
COASTAL / MARINE ATMOSPHERE
```

dominates.

Use the parent:

```text
coated/index.md
```

for this escalation.

---

# 10. Corrosion Mechanism

Mg in the coating promotes formation of a dense and stable corrosion product such as:

```text
Zn5(OH)8Cl2 · H2O
```

The source describes this corrosion product as forming a film-like layer that helps suppress corrosion of the underlying steel.

Conceptual chain:

```text
Zn-Mg-Al coating
↓
corrosion begins
↓
dense Mg-related corrosion products form
↓
protective film develops
↓
substrate corrosion is suppressed
```

---

# 11. Cut-Edge Protection Mechanism

When the cut edge exposes bare steel:

```text
adjacent coating dissolves
↓
corrosion products migrate / form
↓
protective film develops on exposed area
↓
further corrosion is reduced
```

This behavior is sometimes described as:

```text
SELF_HEALING
```

within the product source.

---

# 12. Self-Healing Guardrail

`SELF_HEALING` does NOT mean:

```text
original metallic coating is restored
```

and does NOT mean:

```text
cut edge never develops rust
```

It means protective corrosion products can develop around the exposed section and reduce subsequent corrosion progression.

---

# 13. Initial Red Rust

The source explicitly states that cut edges can show:

```text
INITIAL_RED_RUST
```

because the steel substrate is exposed.

With time, PosMAC 3.0-specific corrosion products may cover the area and reduce the initial red-rust area.

Therefore:

```text
initial red rust
≠
automatic product failure
```

but visual requirements must be considered.

---

# 14. Cut-Edge Thickness Caution

For base-metal thickness:

```text
> 1.6 mm
```

the source recommends consideration of:

```text
REPAIR_PAINT
```

because the cut section may not become fully covered by corrosion products within the documented outdoor-exposure period.

This is a critical engineering rule.

---

# 15. Initial Appearance Caution

Even where thickness is:

```text
≤ 1.6 mm
```

if red rust is unacceptable from the beginning of service:

```text
REPAIR_PAINT
```

may still be selected according to customer requirements.

Therefore cut-edge visual acceptance must be treated separately from long-term corrosion behavior.

---

# 16. Flat-Surface Corrosion

The source reports PosMAC 3.0 as having significantly stronger flat-surface corrosion resistance than ordinary GI / GI(H) in:

```text
SST
CCT
```

comparisons.

Strong requirement:

```text
HIGH_FLAT_SURFACE_CORROSION_RESISTANCE
```

supports PosMAC 3.0 routing.

---

# 17. CCT Comparison

The source uses:

```text
ISO 14993
```

cyclic corrosion testing.

Representative cycle:

```text
salt spray
2 hr
5% NaCl

→ drying
4 hr
25% RH / 60°C

→ humid
2 hr
95% RH / 50°C
```

Any CCT claim must preserve the original conditions.

---

# 18. SST Comparison

The source also uses SST under standards including:

```text
ISO 9227
JIS Z2371
ASTM B117
```

with:

```text
5% NaCl
35°C
```

in the documented comparisons.

Do not compare SST hours directly with field-service years.

---

# 19. Formed-Section Corrosion

PosMAC 3.0 is not only a flat-sheet corrosion product.

The source contains separate evaluations for:

```text
BENDING
CUP_FORMING
CUSTOMER-FORMED COMPONENTS
```

This makes:

```text
FORMED_SECTION_CORROSION_RESISTANCE
```

a strong product-routing attribute.

---

# 20. Bending Corrosion Comparison

The source reports the referenced PosMAC 3.0 sample as having approximately:

```text
2–3x
```

better bending-area corrosion performance than GI(H) under the documented tests.

This value is:

```text
COMPARATIVE_TEST_RESULT
```

not a universal application multiplier.

---

# 21. Cup-Formed Corrosion Comparison

The source also reports approximately:

```text
2–3x
```

better corrosion performance in cup-formed areas than the compared GI material under the documented CCT.

Use this when customer problems concern:

```text
STAMPED_COMPONENT
DEEP_FORMED_SECTION
FORMED_EDGE
```

but preserve the test context.

---

# 22. Batch-GI Comparison

The source includes comparisons between PosMAC 3.0 and:

```text
BATCH_HOT_DIP_GALVANIZED
```

products.

It reports stronger flat corrosion performance under the referenced SST conditions.

This supports potential:

```text
BATCH_GI_REPLACEMENT_HYPOTHESIS
```

but not unconditional replacement.

---

# 23. Thick-Coating Replacement Hypothesis

Because PosMAC 3.0 provides high corrosion resistance at lower coating mass in some source comparisons, it may enable evaluation of:

```text
THICK_GI
→
POSMAC_3_0
```

for selected applications.

Before recommending this transition, check:

```text
corrosion target
cut edge
forming
welding
cost
customer specification
service environment
qualification
```

---

# 24. M630

Canonical special-product code:

```text
M630
```

M630 is a specific PosMAC 3.0 route associated with high coating mass and demanding corrosion applications.

It must remain separate from generic PosMAC 3.0.

---

# 25. M630 Core Positioning

The source reports M630 as demonstrating:

```text
high flat corrosion resistance
high cut-edge corrosion resistance
high formed-area corrosion resistance
```

and compares it with batch-galvanized products.

Strong routing environment:

```text
SALT_DAMAGE_ENVIRONMENT
```

---

# 26. M630 Floating Solar Example

The source provides a direct application example:

```text
FLOATING_SOLAR_POWER_STRUCTURE
+
SALT-DAMAGE ENVIRONMENT
+
C-CHANNEL
```

where M630 was evaluated.

This is a high-confidence application reference.

---

# 27. M630 Routing

Strong route:

```text
FLOATING_SOLAR
+
C_CHANNEL
+
CUT_EDGE
+
SALT_EXPOSURE
→ M630 evaluation
```

This is much stronger than:

```text
SOLAR
→ M630
```

because generic solar structures can use several coated-product families.

---

# 28. M630 Thickness Limitation

The source states that M630 manufacturing thickness is limited to:

```text
maximum 2.0 mm
```

in the referenced product guidance.

Therefore:

```text
M630
+
t > 2.0 mm
```

must return:

```text
SIZE_NOT_SUPPORTED_BY_CURRENT_SOURCE
or
PRE_ORDER_REVIEW_REQUIRED
```

Do not silently route thicker material to M630.

---

# 29. M630 Ordering Guardrail

Even within the nominal range:

```text
M630
```

requires pre-order review.

Return:

```text
M630_PRODUCT_REVIEW_REQUIRED
```

for exact size and orderability.

---

# 30. Solar Structure Routing

Generic solar-support signal:

```text
SOLAR_STRUCTURE
```

is not enough to choose PosMAC 3.0.

Evaluate:

```text
OUTDOOR_ENVIRONMENT
CUT_EDGE
HUMIDITY
SALT
COATING_DURABILITY
PRODUCT_FORM
```

Possible routes:

```text
GI_H
POSMAC_3_0
POSMAC_SUPER
```

depending on severity.

---

# 31. Strong Solar Route

```text
SOLAR_STRUCTURE
+
C_CHANNEL
+
CUT_EDGE_EXPOSURE
+
HIGH_CORROSION_REQUIREMENT
→ POSMAC_3_0
```

This is one of the strongest Product Brain routes.

---

# 32. Main Source-Supported Applications

The catalog includes applications such as:

```text
SOLAR_THERMAL_SUPPORT
FLOATING_SOLAR_SUPPORT
COOLING_TOWER
SILO
PEB_BUILDING
SOUND_BARRIER_BACK_PANEL
WATER_TANK
ROCK_BOLT
SANDWICH_PANEL
CORRUGATED_PIPE
GUARDRAIL
BUILDING_ROOF
BUILDING_WALL
MOTOR_CASE
GREENHOUSE_EQUIPMENT
POULTRY_FARM
AQUACULTURE_FACILITY
SWITCHBOARD
PIPE
PLANT_FACTORY_STRUCTURE
CABLE_TRAY
GREENHOUSE_PAD
GUTTER
STEEL_CURTAIN_WALL
```

These are application examples, not automatic product prescriptions.

---

# 33. Construction Routing

Strong route:

```text
CONSTRUCTION
+
OUTDOOR_STRUCTURE
+
HIGH_CORROSION
+
CUT / BEND / FORM
→ POSMAC_3_0
```

Examples:

```text
ROOF
WALL
CURTAIN_WALL
PURLIN-LIKE STRUCTURE
CABLE_TRAY
SANDWICH_PANEL
```

---

# 34. Infrastructure Routing

Possible source-supported routes:

```text
GUARDRAIL
SOUND_BARRIER
CORRUGATED_PIPE
ROCK_BOLT
```

Use PosMAC 3.0 where:

```text
HIGH_CORROSION
+
FABRICATED_STRUCTURE
```

is the relevant requirement.

---

# 35. Agriculture Routing

Possible applications include:

```text
GREENHOUSE
GREENHOUSE_OPENING_EQUIPMENT
POULTRY_FARM
PLANT_FACTORY
GUTTER
```

Environmental factors such as:

```text
humidity
fertilizer
ammonia
water
```

must be considered separately.

---

# 36. Aquaculture Routing

The source includes:

```text
AQUACULTURE_FACILITY
```

as an application example.

Do not interpret this as proof of suitability for:

```text
CONTINUOUS_SEAWATER_IMMERSION
```

without further service-condition validation.

---

# 37. Chemical Resistance

The source evaluates PosMAC 3.0 over:

```text
pH 1–14
```

using sulfuric acid, NaOH and ammonia-based solutions in the specified immersion test.

It reports favorable weight-loss behavior relative to some compared coated products in acidic/alkaline ranges.

This supports:

```text
CHEMICAL_RESISTANCE
```

as a product characteristic.

---

# 38. Chemical Resistance Guardrail

Do NOT infer:

```text
pH test success
→ suitable for all chemical process equipment
```

Chemical service depends on:

```text
chemical species
concentration
temperature
exposure duration
immersion vs atmosphere
mechanical stress
```

For aggressive chemical process equipment, other product families may be required.

---

# 39. Ammonia Environment

The product guide includes dedicated evaluation in:

```text
10% AMMONIA SOLUTION
```

and agricultural environments are among its application domains.

Use this as supporting evidence when ammonia exposure is relevant.

Do not generalize beyond the documented concentration/test conditions.

---

# 40. Acid-Rain Simulation

The source includes artificial acid-rain testing using a cycle containing:

```text
0.1% NaCl solution + H2SO4
pH 4
```

followed by drying and humid exposure.

This supports PosMAC 3.0 evaluation for:

```text
BUILDING_EXTERIOR
OUTDOOR_STRUCTURE
```

under acidic atmospheric exposure.

---

# 41. Acid-Rain Guardrail

The catalog's acid-rain simulation is:

```text
LAB_SIMULATION
```

not proof of a guaranteed field lifespan.

Preserve:

```text
cycle count
sample coating mass
edge condition
test environment
```

with any numerical comparison.

---

# 42. White Rust

The source explicitly states that PosMAC 3.0 can develop:

```text
WHITE_RUST
```

like other zinc-coated products.

Its high red-rust resistance does NOT mean white rust cannot occur.

---

# 43. White-Rust Mechanism

PosMAC 3.0 forms dense white corrosion products that can contribute to protection of the steel substrate.

Therefore:

```text
WHITE_RUST
```

should not automatically be interpreted as:

```text
SUBSTRATE_RED_RUST
```

However visible appearance and storage quality requirements still matter.

---

# 44. White-Rust Prevention

Before installation, materials should be stored:

```text
DRY
+
WELL_VENTILATED
```

and protected from water/moisture accumulation.

Storage management remains important despite the product's high corrosion resistance.

---

# 45. Galling

The source evaluates PosMAC 3.0 for:

```text
GALLING_RESISTANCE
```

during forming.

Its harder coating layer can reduce certain coating-transfer/die-contamination behaviors compared with conventional galvanized products.

This is a processing benefit under documented conditions.

---

# 46. Scratch Resistance

The source also evaluates:

```text
SCRATCH_RESISTANCE
```

as a PosMAC 3.0 characteristic.

Do not treat this as proof that coating damage cannot occur.

Actual scratch behavior depends on:

```text
forming tool
pressure
lubrication
surface condition
```

---

# 47. Coating-Layer Hardness

The catalog shows representative PosMAC 3.0 coating hardness around:

```text
110–130 Hv
```

in its comparison table.

This value should be treated as:

```text
SOURCE_COMPARATIVE_DATA
```

not a universal specification for every delivered product.

---

# 48. Weldability

The source's comparison table rates weldability as an important PosMAC 3.0 property.

However final welding behavior depends on:

```text
coating mass
base material
thickness
welding process
electrode
current
```

Therefore:

```text
WELDING_PROCEDURE_REVIEW_REQUIRED
```

for exact recommendations.

---

# 49. HR Base

PosMAC 3.0 is available with:

```text
HOT_ROLLED_BASE
```

for structural applications.

This is a major routing branch and should remain separate from CR-base PosMAC 3.0.

---

# 50. HR Base Manufacturing Range

The source provides a CQ-reference manufacturing range of approximately:

```text
thickness:
1.2–6.0 mm

width:
800–1650 mm
```

for the referenced HR-base range.

Total coating mass:

```text
80–630 g/m²
```

may be represented in the source, subject to product/order restrictions.

---

# 51. HR Base M630 Caution

The full HR product family may extend to thicker dimensions, but:

```text
M630
```

has its own restriction.

Do not confuse:

```text
HR PosMAC 3.0 maximum thickness
```

with:

```text
M630 maximum thickness
```

They are separate rules.

---

# 52. HR Post-Treatments

The source lists HR-base post-treatment options including:

```text
NT
CL
CE
```

within the referenced manufacturing range.

Availability must still be checked by:

```text
grade
size
plant
coating mass
```

---

# 53. CR Base

PosMAC 3.0 is also available on:

```text
COLD_ROLLED_BASE
```

for thinner/forming-oriented applications.

Do not treat CR-base and HR-base manufacturing ranges as one.

---

# 54. CR Base Manufacturing Range

Source CQ-reference range:

```text
thickness:
0.5–2.3 mm

width:
720–1860 mm
```

Total coating mass:

```text
80–350 g/m²
```

under the referenced CR-base product range.

---

# 55. CR Base Post-Treatment

The source identifies:

```text
CE
```

as a CR-base post-treatment in the referenced manufacturing specification.

Do not infer HR treatment options automatically apply to CR base.

---

# 56. Mill Edge / Slit Edge

The source's manufacturing-range charts are based on:

```text
MILL_EDGE
```

For some HR-base ranges:

```text
SLIT_EDGE
```

reduces available width relative to the Mill Edge chart.

Therefore edge condition must be part of exact size validation.

---

# 57. Pre-Order Review

The source repeatedly requires:

```text
PRODUCT / QUALITY SPEC REVIEW
```

before order placement.

Exact:

```text
GRADE
SIZE
COATING MASS
POST-TREATMENT
```

must not be inferred from the catalog overview alone.

Return:

```text
PRE_ORDER_SPEC_REVIEW_REQUIRED
```

for exact orderability.

---

# 58. Grade Architecture

HR and CR PosMAC 3.0 include product classes such as:

```text
CQ
DQ
DDQ
STRUCTURAL
```

with multiple strength levels.

Normal market intelligence should stop at:

```text
POSMAC_3_0
+
HR_BASE / CR_BASE
```

unless component-level engineering data are needed.

---

# 59. Representative HR Grade Keys

Source examples include:

```text
PM3HT270CQ
PM3HT270DQ
PM3HT340R
PM3HT400R
PM3HY340C
PM3HT440C
PM3HT490C
PM3HT540C
```

These are retrieval keys.

They are not a complete current approval list.

---

# 60. Representative CR Grade Keys

Source examples include:

```text
PM3CT270CQ
PM3CT270DQ
PM3CT270DD
PM3CT340R
PM3CT400R
PM3CY340C
PM3CT440C
PM3CT490C
PM3CT570C
```

Exact properties must be retrieved from the appropriate source table.

---

# 61. Grade Selection Inputs

Before exact grade selection, collect:

```text
base type: HR or CR
component
required YP
required TS
required elongation
forming severity
bend requirement
thickness
width
coating mass
post-treatment
environment
joining process
customer standard
```

If insufficient:

```text
POSMAC_3_0_GRADE_UNKNOWN
```

---

# 62. Standards Mapping

The source includes mapping/reference tables for:

```text
KS D 3030
DIN EN 10346
ASTM A1046M
```

Do not interpret catalog mapping as:

```text
FULL_EQUIVALENCE
```

without checking:

```text
mechanical properties
coating
dimensions
test requirements
```

---

# 63. NB Post-Treatment

Canonical code:

```text
NB
```

Meaning:

```text
ORGANIC_CR_FREE
```

Primary functions include:

```text
WHITE_RUST_RESISTANCE
ENVIRONMENTAL_COMPATIBILITY
```

where supported by the product source.

---

# 64. NT Post-Treatment

Canonical code:

```text
NT
```

Meaning:

```text
INORGANIC_CR_FREE
```

The source highlights:

```text
LOW_ELECTRICAL_RESISTANCE
HIGH_SURFACE_CONDUCTIVITY
NO_CHROMIUM
```

as important NT characteristics.

---

# 65. NT Routing

Strong route:

```text
POSMAC_3_0
+
CONDUCTIVITY_REQUIREMENT
+
CR_FREE
→ NT candidate
```

Possible applications may include electrical equipment where surface conductivity matters.

Exact process compatibility must still be verified.

---

# 66. CE Post-Treatment

Canonical code:

```text
CE
```

Meaning:

```text
CR3+ TREATMENT
```

Primary characteristics:

```text
WHITE_RUST_RESISTANCE
NO_CR6+
```

Important:

```text
CE ≠ CHROMIUM_FREE
```

because it contains trivalent chromium.

---

# 67. CL Post-Treatment

Canonical:

```text
CL
```

The HR manufacturing source lists CL as a chromate option.

Regulatory/customer restrictions must be verified before recommendation.

Do not recommend automatically where Cr6+ restrictions apply.

---

# 68. Painted PosMAC 3.0

The source shows applications such as:

```text
GENERAL_HOUSE
APARTMENT_ROOF
COASTAL_RESORT_WALL
```

with polyester or fluoropolymer/PVDF-type painted PosMAC 3.0 examples.

This confirms that painted product systems are part of the application space.

---

# 69. Painted-System Guardrail

Do not infer:

```text
PosMAC 3.0
→ any paint system compatible
```

Paint system selection requires:

```text
pretreatment
adhesion
environment
coating
customer process
```

validation.

---

# 70. Water Tank Application

The catalog includes:

```text
WATER_TANK
```

among major applications.

Do not automatically generalize this to:

```text
POTABLE_WATER
FOOD_CONTACT
CONTINUOUS_IMMERSION
```

unless those conditions are specifically supported.

---

# 71. Motor Case Application

The source includes:

```text
MOTOR_CASE
```

among use examples.

Do not confuse:

```text
MOTOR_CASE
```

with:

```text
EV_MOTOR_CORE
```

EV motor cores route to:

```text
HYPER_NO
```

not PosMAC 3.0.

---

# 72. Severe Coastal Boundary

For:

```text
COASTAL
+
HIGH_SALINITY
+
HIGH_HUMIDITY
```

do not assume PosMAC 3.0 is automatically the strongest coated option.

Route back to:

```text
coated/index.md
```

to compare:

```text
POSMAC_3_0
vs
POSMAC_SUPER
```

---

# 73. Continuous Immersion Boundary

Do not infer:

```text
FLOATING_SOLAR
→ continuous immersion suitability
```

The structural support can be in a floating-solar project without the steel product necessarily operating under continuous immersion.

Exact exposure must be identified.

---

# 74. Product Substitution Rule

Possible opportunity:

```text
THICK_GI
or
BATCH_GI
↓
high corrosion requirement
↓
POSMAC_3_0
```

This must be represented as:

```text
SUBSTITUTION_CANDIDATE
```

not:

```text
DIRECT_REPLACEMENT
```

until validated.

---

# 75. Selection vs PosMAC 1.5

Choose PosMAC 1.5 first when:

```text
AUTOMOTIVE / APPLIANCE
+
SURFACE
+
WELDING
+
FORMABILITY
```

dominates.

Choose PosMAC 3.0 first when:

```text
OUTDOOR STRUCTURE
+
CORROSION
+
CUT EDGE
+
FORMED SECTION
```

dominates.

---

# 76. Selection vs PosMAC Super

Choose PosMAC 3.0 first when:

```text
HIGH_CORROSION
+
STRUCTURAL / OUTDOOR
```

is the primary need.

Escalate to PosMAC Super when:

```text
EXTREME_CORROSION
+
HIGH_SALINITY / HIGH_HUMIDITY
```

requires stronger environmental resistance.

---

# 77. Negative Routing Rules

## Generic corrosion

Do not immediately select PosMAC 3.0.

GI may be adequate.

---

## Appliance panel

Do not automatically use PosMAC 3.0.

PosMAC 1.5 or EG may fit surface/forming requirements better.

---

## Automotive outer panel

Do not default to PosMAC 3.0.

Use:

```text
automotive substrate
+
GI / GA / EG / PosMAC 1.5
```

routing first.

---

## Chemical equipment

Do not select PosMAC 3.0 from:

```text
CHEMICAL_RESISTANCE
```

alone.

Stainless, titanium or ANCOR may be more appropriate depending on service medium.

---

## Extreme coastal

Do not stop at PosMAC 3.0 without comparing PosMAC Super.

---

# 78. Product Routing Score

Suggested score:

```text
Application Match             20%
Corrosion Severity            25%
Cut-Edge Requirement          15%
Formed-Section Requirement    10%
Environment Match             15%
Fabrication Match             10%
Evidence Completeness          5%
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

# 79. Solar C-Channel Example

```yaml
industry: ENERGY

application:
  - SOLAR_STRUCTURE

component:
  - C_CHANNEL

environment:
  - OUTDOOR

requirements:
  - HIGH_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

product_candidate:
  family: POSMAC_3_0
  priority: P1

reason:
  - direct structural corrosion relevance
  - cut-edge requirement
  - formed-section requirement

missing_information:
  - salinity
  - coating_mass
  - base_type
  - thickness
```

---

# 80. Floating Solar M630 Example

```yaml
industry: ENERGY

application:
  - FLOATING_SOLAR_STRUCTURE

component:
  - C_CHANNEL

environment:
  - SALT_DAMAGE_ENVIRONMENT

requirements:
  - HIGH_CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

product_family:
  POSMAC_3_0

special_product_candidate:
  M630

constraints:
  max_thickness_mm:
    source_value: 2.0

next_action:
  - verify exact thickness
  - verify project environment
  - confirm product feasibility before order
```

---

# 81. Guardrail Example — M630

Bad:

```text
Floating solar
→ M630
```

Better:

```text
Floating solar
+
salt-damage environment
+
C-channel
+
cut-edge requirement
+
t ≤ source-supported limit
→ M630 candidate
```

---

# 82. Guardrail Example — Cut Edge

Bad:

```text
PosMAC 3.0 cut edge does not rust.
```

Correct:

```text
The exposed cut edge can initially develop red rust.

Over time, characteristic corrosion products may form
and reduce progression of corrosion.

Repair painting may still be recommended depending on
thickness and appearance requirements.
```

---

# 83. Market Intelligence Opportunity Types

Potential downstream classifications:

```text
GI_UPGRADE
BATCH_GI_REPLACEMENT
THICK_COATING_REDUCTION
CORROSION_UPGRADE
CUT_EDGE_IMPROVEMENT
FORMED_SECTION_CORROSION_UPGRADE
SOLAR_STRUCTURE_OPPORTUNITY
FLOATING_SOLAR_OPPORTUNITY
INFRASTRUCTURE_MATERIAL_UPGRADE
MAINTENANCE_REDUCTION
```

These are hypotheses.

They do not guarantee sales or technical approval.

---

# 84. Daily Intelligence Mode

Automated intelligence should normally stop at:

```text
POSMAC_3_0
```

or:

```text
M630_CANDIDATE
```

when direct M630 application evidence exists.

Recommended:

```yaml
daily_posmac_3_0:
  allow_product_family: true
  allow_special_product_candidate: true
  allow_exact_grade: false
  allow_exact_coating_mass: false
  allow_service_life_prediction: false
  allow_pdf_lookup: false
```

---

# 85. Marketing Mode

Marketing analysis may retrieve:

```text
application
corrosion problem
current material
PosMAC 3.0 relevance
GI replacement hypothesis
M630 relevance
cut-edge benefit
technical questions
```

Example:

```text
Customer uses batch-galvanized C-channel
for a solar structure and is experiencing
cut-edge corrosion.

PosMAC 3.0 is a relevant substitution candidate.

If the application is a salt-exposed floating solar
C-channel and size requirements fit,
M630 should also be evaluated.
```

---

# 86. Engineering Mode

Engineering retrieval may include:

```text
HR / CR base
grade
YP
TS
elongation
coating-metal bending
coating mass
post-treatment
thickness
width
edge
cut-edge repair requirement
SST / CCT results
chemical resistance
paint system
```

Original source PDF should be consulted.

---

# 87. Service-Life Prediction Guardrail

The source includes a KOBELCO laboratory-based service-life prediction evaluation.

These numbers must NOT be presented as unconditional POSCO product life.

Any service-life estimate must preserve:

```text
test methodology
environment assumption
coating mass
post-treatment
sample thickness
model assumptions
```

Default intelligence output should avoid numerical service-life prediction.

---

# 88. Durability Warranty Guardrail

The source includes a durability-warranty section.

Do NOT infer:

```text
all PosMAC 3.0 products
→ fixed durability warranty
```

Eligibility depends on:

```text
application
environment
project
specification
customer conditions
```

Return:

```text
WARRANTY_ELIGIBILITY_CONFIRMATION_REQUIRED
```

---

# 89. Numeric Data Classification

Every numerical value should include:

```yaml
value:
unit:
value_type:
test_method:
test_condition:
sample_condition:
source_document:
```

Allowed categories:

```text
SPECIFICATION
MANUFACTURING_RANGE
COMPARATIVE_TEST_RESULT
APPLICATION_TEST_RESULT
LAB_PREDICTION
```

---

# 90. Source Authority

Canonical source:

```text
2025 POSMAC3.0.pdf
```

Do not override source-supported product data using:

```text
generic model knowledge
cross-product summaries
unverified web material
```

unless a newer approved source is deliberately added.

---

# 91. Source Conflict Rule

If another document provides different:

```text
grade
size
coating mass
post-treatment
availability
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

unless project governance specifies otherwise.

---

# 92. Unknown States

Supported:

```text
POSMAC_3_0_GRADE_UNKNOWN

BASE_MATERIAL_UNKNOWN

CORROSION_SEVERITY_UNKNOWN

COATING_MASS_UNKNOWN

POST_TREATMENT_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

M630_PRODUCT_REVIEW_REQUIRED

CUT_EDGE_REPAIR_REVIEW_REQUIRED

CHEMICAL_SERVICE_REVIEW_REQUIRED

PAINT_SYSTEM_VALIDATION_REQUIRED

WELDING_PROCEDURE_REVIEW_REQUIRED

WARRANTY_ELIGIBILITY_CONFIRMATION_REQUIRED

PRE_ORDER_SPEC_REVIEW_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 93. Retrieval Keywords

```text
PosMAC 3.0
POSMAC3.0
Zn-3Mg-2.5Al
Zn-3%Mg-2.5%Al
Zn-Mg-Al
고내식도금강판
절단면 내식성
단면부 내식성
가공부 내식성
C-channel
C형강
수상태양광
태양광 구조물
M630
Batch GI
후도금 대체
Self healing
고염해
SST
CCT
KS D 3030
```

Keywords support retrieval only.

---

# 94. Routing Algorithm

```pseudo
function route_posmac_3_0(context):

    identify application
    identify component
    identify base_type
    identify environment
    identify corrosion_severity
    identify cut_edge
    identify formed_section

    if corrosion_severity == EXTREME
       and (
         HIGH_SALINITY
         or HIGH_HUMIDITY
         or severe coastal exposure
       ):
        compare POSMAC_SUPER
        do not finalize POSMAC_3_0

    if application in [
        SOLAR_STRUCTURE,
        OUTDOOR_STRUCTURE,
        BUILDING_STRUCTURE,
        INFRASTRUCTURE,
        AGRICULTURAL_STRUCTURE
    ]
       and HIGH_CORROSION_RESISTANCE:
        candidate = POSMAC_3_0

    if cut_edge
       or bending_area
       or formed_section:
        increase POSMAC_3_0 priority

    if application == FLOATING_SOLAR_STRUCTURE
       and component == C_CHANNEL
       and salt_damage_environment:
        evaluate M630

    if M630:
        verify thickness <= supported limit
        require pre_order_review

    verify:
        HR_or_CR
        grade
        coating_mass
        post_treatment
        size
        edge
        joining
        painting

    return candidate
```

---

# 95. GI Replacement Example

```yaml
current_material:
  GI_H

application:
  OUTDOOR_STRUCTURAL_COMPONENT

problem:
  - CORROSION
  - CUT_EDGE_CORROSION

opportunity_type:
  GI_UPGRADE

product_candidate:
  POSMAC_3_0

reason:
  - high corrosion requirement
  - cut-edge performance requirement
  - GI-compatible fabrication concept

validation_required:
  - coating_mass
  - forming_process
  - joining_process
  - customer_standard
```

---

# 96. Agriculture Example

```yaml
industry: AGRICULTURE

application:
  - GREENHOUSE_STRUCTURE

environment:
  - HUMID

requirements:
  - CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE

product_candidate:
  POSMAC_3_0

missing_information:
  - ammonia_exposure
  - continuous_water_contact
  - coating_mass
  - base_type
```

---

# 97. Building Exterior Example

```yaml
industry: CONSTRUCTION

application:
  - BUILDING_WALL

environment:
  - OUTDOOR
  - ACIDIC_ATMOSPHERE_POSSIBLE

requirements:
  - HIGH_CORROSION_RESISTANCE

product_candidate:
  POSMAC_3_0

optional_system:
  PAINTED_POSMAC_3_0

next_action:
  - confirm paint system
  - confirm pretreatment
  - confirm project environment
```

---

# 98. Negative Example — Appliance

Input:

```text
Refrigerator outer panel requires
high surface appearance and press formability.
```

Do not automatically return:

```text
POSMAC_3_0
```

Compare:

```text
POSMAC_1_5
EG
GI
```

because surface quality and forming may dominate over extreme corrosion resistance.

---

# 99. Negative Example — Extreme Coastal

Input:

```text
island coastal structure
+
high salinity
+
high humidity
```

Correct:

```text
POSMAC_3_0
vs
POSMAC_SUPER
comparison required
```

Do not stop routing prematurely.

---

# 100. Final Knowledge Chain

```text
CUSTOMER SIGNAL
↓
APPLICATION
↓
COMPONENT
↓
HR / CR BASE
↓
ENVIRONMENT
↓
CORROSION SEVERITY
↓
CUT EDGE / BENDING / FORMING
↓
POSMAC_3_0
↓
STANDARD PRODUCT / M630
↓
GRADE
↓
COATING MASS
↓
POST-TREATMENT
↓
SIZE / EDGE
↓
PROCESS VALIDATION
↓
ENGINEERING APPROVAL
↓
MARKETING OPPORTUNITY
```

---

# 101. Final Rule

The purpose of PosMAC 3.0 is NOT:

```text
USE THE MOST CORROSION-RESISTANT COATING
FOR EVERY APPLICATION
```

The proper product position is:

```text
HIGH CORROSION RESISTANCE
+
STRONG CUT-EDGE PERFORMANCE
+
STRONG FORMED-SECTION PERFORMANCE
+
STRUCTURAL / OUTDOOR APPLICATION FIT
+
GI-COMPATIBLE PROCESSING CONCEPT
```

The preferred reasoning sequence is:

```text
APPLICATION
↓
ENVIRONMENT
↓
CORROSION SEVERITY
↓
CUT / FORM CONDITION
↓
POSMAC 3.0
↓
M630 only if justified
↓
GRADE / COATING / POST-TREATMENT
```

not:

```text
M630
↓
find an application
```

The responsibility of this file ends at:

```text
DEFENSIBLE POSMAC 3.0 PRODUCT CANDIDATE
```

Final customer specification remains subject to engineering, quality and product-feasibility review.
