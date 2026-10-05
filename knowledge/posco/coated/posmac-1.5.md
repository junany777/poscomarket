---
product_family: POSMAC_1_5

name_ko: PosMAC 1.5
name_en: POSCO Magnesium Aluminium Alloy Coating Product 1.5

material_category:
  - COATED_STEEL
  - CORROSION_RESISTANT_ALLOY_COATED_STEEL
  - ZN_MG_AL_ALLOY_COATED_STEEL

coating_system:
  base: Zn
  Mg_percent: 1.5
  Al_percent: 1.5

industries:
  - HOME_APPLIANCE
  - AUTOMOTIVE
  - CONSTRUCTION
  - ENERGY
  - INFRASTRUCTURE

applications:
  - HOME_APPLIANCE_PANEL
  - REFRIGERATOR_DOOR
  - WASHING_MACHINE_PANEL
  - AIR_CONDITIONER_OUTDOOR_UNIT
  - AUTOMOTIVE_OUTER_PANEL
  - AUTOMOTIVE_COMPONENT
  - PRECOATED_STEEL
  - SANDWICH_PANEL
  - ROOFING
  - PIPE
  - SAFETY_FOOTBOARD
  - DECK_PLATE
  - AGRICULTURAL_PIPE
  - GREENHOUSE_PIPE
  - STEEL_EARTH_RETAINING_PLATE
  - PURLIN

requirements:
  - CORROSION_RESISTANCE
  - CUT_EDGE_CORROSION_RESISTANCE
  - FORMED_SECTION_CORROSION_RESISTANCE
  - SURFACE_QUALITY
  - FORMABILITY
  - BENDABILITY
  - WELDABILITY
  - PAINTABILITY
  - PRECOATED_STEEL_COMPATIBILITY
  - GALLING_RESISTANCE
  - WHITE_RUST_RESISTANCE

post_treatments:
  - CL
  - CE
  - SC
  - SD
  - NB

standards:
  - KS_D_3030
  - DIN_EN_10346
  - ASTM_A1046M

source_documents:
  - 2025 POSMAC1.5.pdf

primary_source:
  - 2025 POSMAC1.5.pdf

knowledge_status: VERIFIED

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO PosMAC 1.5 Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO PosMAC 1.5.

It should be loaded after:

```text
knowledge/posco/coated/index.md
```

routes the application to:

```text
POSMAC_1_5
```

The primary purpose of this file is to determine whether PosMAC 1.5 is a technically defensible coated-steel candidate based on:

```text
APPLICATION
↓
CORROSION ENVIRONMENT
↓
SURFACE REQUIREMENT
↓
FORMING REQUIREMENT
↓
WELDING REQUIREMENT
↓
PAINT / PRECOATED REQUIREMENT
↓
POSMAC 1.5
↓
GRADE / COATING MASS / POST-TREATMENT
↓
ENGINEERING VALIDATION
```

This file does NOT automatically approve:

```text
exact grade
exact coating mass
exact post-treatment
exact production size
customer process compatibility
final service life
```

---

# 2. Product Definition

PosMAC 1.5 is a Zn-Mg-Al ternary alloy coated steel.

Canonical coating composition:

```text
Zn
+
1.5% Mg
+
1.5% Al
```

Product-family code:

```text
POSMAC_1_5
```

The source describes it as:

```text
Zn-1.5%Mg-1.5%Al
```

high-corrosion-resistant alloy coated steel.

---

# 3. Core Product Positioning

PosMAC 1.5 is positioned between ordinary galvanized steel and higher-Mg PosMAC products where the application requires a balance of:

```text
CORROSION_RESISTANCE
+
SURFACE_QUALITY
+
WELDABILITY
+
FORMABILITY
```

The source specifically positions it for:

```text
HOME_APPLIANCE
AUTOMOTIVE
PRECOATED_STEEL
```

applications.

---

# 4. Key Source-Supported Advantages

The source identifies the following major product characteristics:

```text
> 2x corrosion resistance
vs ordinary GI / GI(H)
at the same coating mass
under the documented test context

better cut-edge corrosion resistance
than ordinary galvanized steel

GI-compatible processing
assembly
painting

better surface quality and weldability
than PosMAC 3.0

lower coating-layer hardness than PosMAC 3.0
to reduce coating cracking during forming

suitability for pre-coated steel
```

All relative corrosion claims must preserve their test context.

---

# 5. Product Positioning Chain

Use:

```text
GI / GI_H
↓
corrosion requirement increases
↓
surface / welding / forming still important
↓
POSMAC_1_5
```

Do NOT automatically use:

```text
GI
→ POSMAC_3_0
```

when the application is dominated by:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
AUTOMOTIVE_PANEL
HOME_APPLIANCE_PANEL
```

---

# 6. PosMAC 1.5 vs GI

The source states that PosMAC 1.5 has more than twice the corrosion resistance of ordinary:

```text
GI
GI(H)
```

at the same coating mass under the documented comparison.

It also provides better:

```text
CUT_EDGE_CORROSION_RESISTANCE
```

than ordinary hot-dip galvanized steel.

This should be represented as:

```text
GI
↓
need higher corrosion resistance
+
retain familiar processing route
↓
POSMAC_1_5 candidate
```

not:

```text
POSMAC_1_5
= universal GI replacement
```

---

# 7. GI Process Compatibility

The source states that existing GI-type:

```text
PROCESSING
ASSEMBLY
PAINTING
```

processes may be applied to PosMAC 1.5.

This supports:

```text
PROCESS_COMPATIBILITY_CANDIDATE
```

but does NOT mean:

```text
NO_CUSTOMER_VALIDATION_REQUIRED
```

Customer-specific forming, welding and painting must still be verified.

---

# 8. PosMAC 1.5 vs PosMAC 3.0

This distinction is critical.

## PosMAC 1.5

Prioritize:

```text
SURFACE_QUALITY
WELDABILITY
FORMABILITY
PRECOATED_STEEL
AUTOMOTIVE_PANEL
HOME_APPLIANCE
```

## PosMAC 3.0

Prioritize:

```text
MORE_SEVERE_CORROSION
HIGHER_CORROSION_PRIORITY
HARSH_OUTDOOR_ENVIRONMENT
```

The source explains that PosMAC 1.5 reduces Mg and Al content relative to PosMAC 3.0 to strengthen:

```text
SURFACE_QUALITY
WELDABILITY
```

and reduce coating cracking during forming.

---

# 9. PosMAC 1.5 vs PosMAC 3.0 Routing Rule

```text
corrosion severity dominates
+
harsh environment
→ POSMAC_3_0

corrosion + surface + welding + forming balance
→ POSMAC_1_5
```

Do not rank them as:

```text
PosMAC 3.0 > PosMAC 1.5
```

in all applications.

They optimize different requirement combinations.

---

# 10. Coating-Layer Hardness

The catalog shows PosMAC 1.5 coating-layer hardness at approximately:

```text
100–110 Hv
```

within its comparison data.

This must be stored as source-specific comparative data.

Do not use it independently as a forming-limit guarantee.

---

# 11. Galling Resistance

The source states that PosMAC 1.5 has higher coating-layer hardness than ordinary hot-dip galvanized steel and therefore can produce:

```text
LESS COATING POWDER ACCUMULATION
ON PRESS DIES
```

during press forming.

Potential benefit:

```text
LOWER_DIE_CLEANING_FREQUENCY
```

compared with the referenced GI condition.

This is a process benefit under the source comparison, not a universal press-life guarantee.

---

# 12. Galling Routing

Strong signal:

```text
PRESS_FORMING
+
DIE_CONTAMINATION
+
COATING_POWDER
```

may justify:

```text
POSMAC_1_5 evaluation
```

especially when ordinary galvanized products create die-maintenance issues.

---

# 13. Corrosion Mechanism

The source attributes enhanced corrosion resistance to Mg promoting formation of a dense and stable corrosion product.

Representative compound:

```text
Zn5(OH)8Cl2 · H2O
```

This corrosion product forms a film-like layer on the coating surface and suppresses further corrosion of the steel substrate.

---

# 14. Corrosion Product Comparison

The catalog contrasts ordinary GI corrosion products with PosMAC 1.5.

Directional concept:

```text
GI
→ more porous corrosion product

POSMAC_1_5
→ denser / more stable corrosion-product structure
```

This is the source-described corrosion mechanism.

---

# 15. Flat-Surface Corrosion

PosMAC 1.5 is designed for enhanced:

```text
FLAT_SURFACE_CORROSION_RESISTANCE
```

relative to ordinary GI under the documented test conditions.

Do not convert laboratory corrosion results into:

```text
FIELD_SERVICE_LIFE
```

without additional evidence.

---

# 16. Cut-Edge Corrosion

PosMAC 1.5 provides enhanced:

```text
CUT_EDGE_CORROSION_RESISTANCE
```

The source describes a mechanism in which:

```text
coating around the cut edge dissolves
↓
protective corrosion products develop
↓
exposed edge receives corrosion protection
```

However the source explicitly states that exposed substrate may still develop:

```text
RED_RUST
```

initially.

Therefore:

```text
CUT_EDGE_PROTECTED
```

does NOT mean:

```text
CUT_EDGE_NEVER_RUSTS
```

---

# 17. Cut-Edge Guardrail

Forbidden:

```text
PosMAC 1.5 cut edge
→ no red rust
```

Correct:

```text
PosMAC 1.5 provides improved cut-edge corrosion behavior
relative to conventional galvanized steel,
but exposed steel may initially develop red rust.
```

---

# 18. Galvalume Comparison

The source compares PosMAC 1.5 with Galvalume for:

```text
FLAT_SURFACE_CORROSION
CUT_EDGE_CORROSION
FORMED_SECTION_CORROSION
```

Under the documented SST conditions, PosMAC 1.5 demonstrates stronger edge and processed-area corrosion performance than the referenced Galvalume samples.

This must not be converted into:

```text
POSMAC_1_5 > GALVALUME
IN EVERY APPLICATION
```

---

# 19. Corrosion Test Conditions

The source uses salt spray testing such as:

```text
SST
ISO 9227
JIS Z2371
ASTM B117

5% NaCl
35°C
```

for certain comparison tests.

Any quantitative claim must preserve:

```text
TEST_METHOD
EXPOSURE_TIME
COATING_MASS
POST_TREATMENT
SAMPLE_GEOMETRY
```

---

# 20. Corrosion Multiples Guardrail

Allowed:

```text
The catalog reports more than twice the corrosion resistance
of ordinary GI/GI(H) at the same coating mass
under the documented comparison.
```

Forbidden:

```text
PosMAC 1.5 lasts more than twice as long in the field.
```

---

# 21. Pre-Coated Steel Positioning

One of PosMAC 1.5's key source-supported applications is:

```text
PRECOATED_STEEL
```

The source states that its lower coating-layer hardness relative to PosMAC 3.0 reduces coating cracking during processing.

This supports:

```text
COLOR_STEEL
PRECOATED_PANEL
HOME_APPLIANCE_OUTER_PANEL
```

routes.

---

# 22. Painted Corrosion Resistance

The source compares color-coated PosMAC 1.5 with color-coated GI.

It states that PosMAC 1.5 can be applied where an attractive painted appearance is required, including:

```text
HOME_APPLIANCE_OUTER_PANEL
```

and reports better corrosion performance than the referenced GI-based color-coated material under the documented tests.

---

# 23. Paint Guardrail

Do not assume:

```text
POSMAC_1_5
→ paint without process validation
```

The source warns that:

```text
PAINT
PRETREATMENT
```

conditions may create:

```text
BLISTERING
ADHESION_REDUCTION
```

Therefore customer paint systems require prior quality verification.

---

# 24. Excess Repair-Paint Caution

The source does not recommend indiscriminate:

```text
OVERPAINTING
REPAIR_PAINTING
```

because PosMAC 1.5 corrosion behavior and discoloration mechanisms differ according to environment.

If painting is required:

```text
PRETREATMENT_VALIDATION_REQUIRED
```

---

# 25. Surface Quality

A central PosMAC 1.5 differentiation is:

```text
SURFACE_QUALITY
```

especially relative to higher-Mg PosMAC 3.0.

Strong routing applications:

```text
HOME_APPLIANCE_PANEL
AUTOMOTIVE_PANEL
PRECOATED_STEEL
```

---

# 26. Automotive Routing

Strong route:

```text
AUTOMOTIVE
+
PANEL / COMPONENT
+
CORROSION_RESISTANCE
+
SURFACE_QUALITY
+
WELDABILITY
+
FORMABILITY
→ POSMAC_1_5 candidate
```

Do not use PosMAC 1.5 as a replacement for automotive substrate selection.

The substrate mechanical-performance requirement must be determined separately.

---

# 27. Appliance Routing

Strong route:

```text
HOME_APPLIANCE
+
PANEL
+
SURFACE_QUALITY
+
CORROSION_RESISTANCE
+
FORMABILITY
→ POSMAC_1_5
```

Possible source-supported applications include:

```text
REFRIGERATOR_DOOR
REFRIGERATOR_INNER_PART
WASHING_MACHINE_INNER_PANEL
WASHING_MACHINE_OUTER_PANEL
AIR_CONDITIONER_OUTDOOR_UNIT
```

---

# 28. Major Source-Supported Applications

The catalog lists examples including:

```text
REFRIGERATOR_DOOR
REFRIGERATOR_INNER_PART

WASHING_MACHINE_INNER_PANEL
WASHING_MACHINE_OUTER_PANEL

AUTOMOTIVE_OUTER_PANEL
AUTOMOTIVE_COMPONENT

SANDWICH_PANEL
ROOFING
PIPE

AIR_CONDITIONER_OUTDOOR_UNIT
```

as product-use examples.

---

# 29. Structural Applications

The source also lists:

```text
SAFETY_FOOTBOARD
DECK_PLATE
AGRICULTURAL_PIPE
GREENHOUSE_PIPE
STEEL_EARTH_RETAINING_PLATE
PURLIN
```

as major applications.

These broaden PosMAC 1.5 beyond automotive and appliances.

---

# 30. Structural Routing Rule

Use PosMAC 1.5 when:

```text
STRUCTURAL_COMPONENT
+
GENERAL / ENHANCED CORROSION
+
FORMING / WELDING / SURFACE REQUIREMENTS
```

are balanced.

If:

```text
HARSH_CORROSION
```

dominates, evaluate:

```text
POSMAC_3_0
```

or:

```text
POSMAC_SUPER
```

through the parent router.

---

# 31. Solar / Outdoor Caution

The source includes installation precautions relevant to outdoor structures.

PosMAC 1.5 may be considered for some structural/outdoor applications.

However:

```text
SOLAR_STRUCTURE
```

alone is NOT sufficient to choose PosMAC 1.5.

Use:

```text
ENVIRONMENT
CORROSION_SEVERITY
SALINITY
CUT_EDGE
WATER_CONTACT
```

to decide whether PosMAC 1.5, 3.0 or Super is more appropriate.

---

# 32. Continuous Water Contact

The source warns that locations where water continuously contacts the PosMAC 1.5 coating may show:

```text
EARLY_CORROSION
```

It recommends:

```text
DESIGN_DETAIL_IMPROVEMENT
or
ADDITIONAL_PROTECTION
```

to avoid continuous direct water contact.

---

# 33. Water Contact Guardrail

Do NOT infer:

```text
high corrosion resistance
→ suitable for continuous water contact
```

Instead:

```text
CONTINUOUS_WATER_CONTACT
→ DESIGN_REVIEW_REQUIRED
```

---

# 34. Soil Contact

For field-stored structural material, the source advises avoiding:

```text
DIRECT_SOIL_CONTACT
```

because contamination and coating damage may accelerate corrosion.

Use:

```text
PALLET
SUPPORT_BLOCK
```

to isolate material from soil during site storage.

---

# 35. Processing Environment

Avoid press/forming work in environments with:

```text
HIGH_HUMIDITY
SO2
HEAVY_SMOKE
```

where possible.

These conditions may contribute to coating degradation.

---

# 36. Lubricant Caution

The source notes that some lubricants can attack the coating.

Therefore press-forming operations should verify:

```text
LUBRICANT_COMPATIBILITY
```

If incompatible processing lubricant is used:

```text
DEGREASING
+
CORROSION_PROTECTION
```

should be applied promptly after processing.

---

# 37. Degreasing

Preferred:

```text
MILD_ALKALINE_DEGREASER
NEUTRAL_DEGREASER
ORGANIC_SOLVENT
```

where appropriate.

The source warns against:

```text
STRONG_ALKALINE_DEGREASER
```

because strong alkali can corrode zinc.

---

# 38. Welding

During resistance welding, zinc may evaporate and adhere to:

```text
ELECTRODES
```

Therefore:

```text
PERIODIC_ELECTRODE_CLEANING
```

may be necessary.

The source also states that zinc coating may increase:

```text
SPATTER
FUME
```

relative to ordinary CR/HR.

---

# 39. Welding Safety

Welding should be conducted in:

```text
WELL_VENTILATED_AREA
```

because coating-related fumes can increase.

This is a process/safety rule, not a product-performance advantage.

---

# 40. Weldability Positioning

Relative to PosMAC 3.0, PosMAC 1.5 is designed with lower Mg/Al content to improve:

```text
WELDABILITY
```

This makes it especially relevant when:

```text
CORROSION
+
WELDING
```

must coexist.

---

# 41. Spot-Welding Relevance

The source's registered patents include technology associated with:

```text
PHOSPHATE_TREATABILITY
SPOT_WELDABILITY
WELDABILITY
PROCESSED_SECTION_CORROSION
```

This supports welding as an important PosMAC 1.5 design axis.

It does not establish a universal welding procedure.

---

# 42. Galling vs Forming Trade-Off

The coating hardness of PosMAC 1.5 is:

```text
higher than ordinary GI
```

which can improve galling behavior.

At the same time:

```text
lower than PosMAC 3.0
```

which helps reduce coating cracking during forming.

This is a key Product Brain differentiator:

```text
GI
← softer / conventional

POSMAC_1_5
← balanced hardness

POSMAC_3_0
← higher corrosion priority
```

Do not treat this as a universal hardness-performance ranking.

---

# 43. Post-Treatment Architecture

The catalog lists post-treatments including:

```text
CL
CE
SC
SD
NB
```

Exact availability depends on production route/site.

Post-treatment must be modeled separately from:

```text
POSMAC_1_5 COATING
```

---

# 44. NB — Organic Cr-Free

Canonical code:

```text
NB
```

Meaning:

```text
ORGANIC_CR_FREE
```

Primary function:

```text
WHITE_RUST_RESISTANCE
```

The source describes NB as an environmentally friendly coating because it contains:

```text
NO_CHROMIUM
```

---

# 45. NB Performance Direction

Source-supported positioning:

```text
CORROSION_RESISTANCE
WHITE_RUST_RESISTANCE
ENVIRONMENTAL_COMPATIBILITY
```

NB is available in the catalog's manufacturing-spec section.

Exact application suitability requires product/site confirmation.

---

# 46. CE — Cr3+ Treatment

Canonical:

```text
CE
```

Meaning:

```text
TRIVALENT_CHROMIUM_TREATMENT
```

The source explains that CE:

```text
does not contain Cr6+
```

and uses Cr3+-based chemistry to secure corrosion resistance.

This should not be mislabeled as:

```text
CHROMIUM_FREE
```

because:

```text
Cr3+ is still chromium.
```

---

# 47. CL / SC / SD

Catalog manufacturing specifications also list:

```text
CL
= Chromate 6+

SC
= organic film

SD
= organic film / anti-fingerprint
```

Exact product/site availability should be preserved from the source.

Do not recommend Cr6+ treatment where regulatory/customer requirements prohibit it.

---

# 48. Post-Treatment Selection

Suggested sequence:

```text
SERVICE_ENVIRONMENT
↓
WHITE_RUST_REQUIREMENT
↓
ENVIRONMENTAL_RESTRICTION
↓
SURFACE_FUNCTION
↓
POST_TREATMENT
```

Do not select post-treatment based only on product family.

---

# 49. White Rust

The source states post-treated material can improve:

```text
WHITE_RUST_RESISTANCE
```

during temporary protection/storage.

Important:

```text
POST_TREATMENT
= temporary corrosion protection layer
```

and must not be confused with the underlying Zn-Mg-Al coating itself.

---

# 50. Untreated + Unoiled Risk

The ordering guide warns:

```text
UNTREATED
+
UNOILED
```

may lead to:

```text
WHITE_RUST
```

Therefore this order combination should trigger:

```text
WHITE_RUST_RISK_WARNING
```

---

# 51. Post-Treatment + Oiling Caution

The source also warns that ordering:

```text
POST_TREATMENT
+
OILING
```

together may lead to:

```text
SURFACE_DISCOLORATION
```

and requires prior quality consultation.

Return:

```text
QUALITY_CONSULTATION_REQUIRED
```

for this combination.

---

# 52. Coating Mass

Source manufacturing specification:

```text
80–300 g/m²
```

for total coating mass on both sides.

This should be stored as:

```text
SOURCE_MANUFACTURING_RANGE
```

not as a universal orderability guarantee.

Exact availability still depends on:

```text
GRADE
SIZE
PLANT
POST_TREATMENT
```

---

# 53. Coating Mass Selection

The source ordering guide states:

```text
corrosive environment
→ heavier coating is favorable

forming / welding requirement
→ lighter coating is favorable
```

Therefore:

```text
MAXIMUM_COATING_MASS
```

is not the objective.

---

# 54. Coating Mass Decision

Correct:

```text
DURABILITY
vs
FORMABILITY
vs
WELDABILITY
```

trade-off.

Forbidden:

```text
300 g/m²
= automatically best PosMAC 1.5
```

---

# 55. Manufacturing Size

For CQ-class products the catalog provides a general manufacturing range including approximately:

```text
0.3 < t ≤ 2.3 mm
```

with a note that Gwangyang begins from:

```text
0.4 mm
```

for the referenced range.

Width information is shown in the catalog around:

```text
730–1800 mm
```

with plant/range differences also shown.

Do not convert these into one unconditional production envelope.

---

# 56. Mandatory Inquiry Rule

The source explicitly requires pre-order quality inquiry for:

```text
SIZE
GRADE / SPEC
COATING_MASS
PRODUCTION_FEASIBILITY
```

Therefore exact orderability must return:

```text
INQUIRY_SPEC_REVIEW_REQUIRED
```

---

# 57. Grade Architecture

The source includes:

```text
CQ
LQ
DQ
DDQ
STRUCTURAL
```

classes.

Representative POSCO-type grade keys include:

```text
PM1CT270CQ
PM1CT270LQ
PM1CT270DQ
PM1CT270DD

PM1CT340R
PM1CT400R
PM1CT440C
PM1CT490C
```

These should be treated as grade-level data.

---

# 58. Grade Selection Boundary

Normal marketing intelligence should stop at:

```text
POSMAC_1_5
```

or at most:

```text
FORMING_CLASS
STRUCTURAL_CLASS
```

Exact grade selection requires:

```text
required YP
required TS
elongation
forming level
standard
thickness
width
coating mass
```

---

# 59. KS Standard

The source states POSCO obtained certification in April 2022 for:

```text
KS D 3030
```

for PosMAC 1.5.

Standard name:

```text
Hot-dip zinc aluminium magnesium alloy coated steel sheets and coils
```

This should be preserved as a source-supported certification fact.

---

# 60. International Standard References

The source also maps products against standards including:

```text
DIN EN 10346
ASTM A1046M
```

These are reference/equivalent-standard tables in the catalog.

Do not treat mapped standards as:

```text
FULL_TECHNICAL_EQUIVALENCE
```

without detailed specification comparison.

---

# 61. Mechanical Property Tables

The source provides mechanical properties including:

```text
YP
TS
ELONGATION
```

for multiple:

```text
KS
EN
ASTM
```

classes.

These values should be retrieved only when:

```text
EXACT_GRADE_SELECTION
```

is required.

---

# 62. Example KS-Class Data

Source-supported examples include:

```text
PM1CT270CQ
TS ≥ 270 MPa

PM1CT270LQ
TS ≥ 270 MPa

PM1CT270DQ
TS ≥ 270 MPa

PM1CT270DD
TS ≥ 270 MPa
```

with elongation requirements varying by class/thickness.

Structural examples include:

```text
PM1CT340R
YP ≥245 MPa
TS ≥340 MPa

PM1CT400R
YP ≥295 MPa
TS ≥400 MPa

PM1CT440C
YP ≥335 MPa
TS ≥440 MPa

PM1CT490C
YP ≥365 MPa
TS ≥490 MPa
```

Exact use requires source lookup.

---

# 63. Numeric Property Guardrail

Do not infer:

```text
PM1CT270CQ
= suitable for every appliance panel
```

or:

```text
PM1CT490C
= suitable for every automotive structural component
```

Application, forming and customer standards remain necessary.

---

# 64. Application Examples — Appliance

Strong source-supported routing:

```text
REFRIGERATOR_DOOR
REFRIGERATOR_INNER_PART
WASHING_MACHINE_PANEL
AIR_CONDITIONER_OUTDOOR_UNIT
```

Reasoning:

```text
SURFACE_QUALITY
+
CORROSION_RESISTANCE
+
FORMABILITY
→ POSMAC_1_5
```

---

# 65. Application Example — Automotive

Input:

```text
AUTOMOTIVE_OUTER_PANEL
+
CORROSION
+
SURFACE
+
FORMING
+
WELDING
```

Candidate:

```text
POSMAC_1_5
```

But:

```text
AUTOMOTIVE_SUBSTRATE_GRADE
```

must be selected separately.

---

# 66. Automotive Substrate Guardrail

Do not use:

```text
POSMAC_1_5
```

as a substitute for:

```text
DP
TRIP
CP
MART
IF_HSS
```

or another substrate family.

Correct model:

```text
SUBSTRATE
+
POSMAC_1_5 COATING
```

where an approved commercial combination exists.

---

# 67. Pre-Coated Appliance Example

Input:

```text
HOME_APPLIANCE_OUTER
+
COLOR_COATED
+
CORROSION
+
FORMING
```

Strong candidate:

```text
POSMAC_1_5
```

because the source directly positions it for:

```text
PRECOATED_STEEL
```

and provides color-coated corrosion comparisons.

---

# 68. Agricultural / Greenhouse Example

Input:

```text
GREENHOUSE_PIPE
+
OUTDOOR_CORROSION
+
FORMING
```

Candidate:

```text
POSMAC_1_5
```

Source-supported application exists.

If the actual environment is highly saline or unusually severe:

```text
re-route through coated/index.md
```

for PosMAC 3.0 / Super evaluation.

---

# 69. Storage

Avoid storage in:

```text
MOISTURE
WATER_INGRESS
SEVERE_TEMPERATURE_DIFFERENCE
```

conditions.

Recommended:

```text
DRY
VENTILATED
INDOOR_STORAGE
```

The source also recommends short inventory periods.

---

# 70. White Rust During Storage

Even with intact packaging:

```text
LONG_STORAGE
```

can permit slight:

```text
WHITE_RUST
```

development.

Therefore:

```text
FIRST_IN_FIRST_OUT
SHORT_STORAGE
```

are preferred operating principles.

---

# 71. Packaging Guardrail

The source states that if:

```text
BARE_PACKAGING
```

is selected, white-rust quality assurance is not provided.

Therefore bare-packaging requests should trigger:

```text
WHITE_RUST_WARRANTY_WARNING
```

---

# 72. Blackening

The source states that surface gloss may decrease over time and:

```text
BLACKENING
```

may occur.

Blackening is accelerated by:

```text
HIGH_TEMPERATURE
+
HIGH_HUMIDITY
```

The source describes it as a general oxidation phenomenon of zinc coating and notes that, apart from the darker appearance, the material remains equivalent to normal product in the described context.

---

# 73. Blackening Guardrail

Do not automatically classify:

```text
BLACKENING
```

as:

```text
STRUCTURAL_FAILURE
```

or:

```text
LOSS_OF_CORROSION_FUNCTION
```

without additional evidence.

It is first a:

```text
SURFACE_APPEARANCE_PHENOMENON
```

in the source context.

---

# 74. Aging / Forming

The source warns that long storage can lead to:

```text
STRETCHER_STRAIN
FLUTTING
```

in susceptible material.

Therefore:

```text
LONG_STORAGE
+
FORMING_APPLICATION
```

should trigger:

```text
FORMABILITY_RECHECK
```

---

# 75. Edge Selection

Order options include:

```text
MILL_EDGE
SLIT_EDGE
```

The source recommends considering:

```text
SLIT_EDGE
```

when the supplied edge becomes the final-product edge.

Exact choice depends on downstream process and final component.

---

# 76. Weld-Seam Inclusion

Coils may contain welded regions.

These regions may have:

```text
HIGHER_HARDNESS
SLIGHTLY_GREATER_THICKNESS
```

than surrounding material.

If the customer cannot tolerate welded sections:

```text
NO_WELD_SEAM_OPTION
```

should be considered.

---

# 77. Product Use Change

The source warns against switching the material to an application different from the originally ordered use without review.

Therefore:

```text
ORDERED_APPLICATION
≠
NEW_APPLICATION
```

should return:

```text
APPLICATION_REVALIDATION_REQUIRED
```

---

# 78. Marketing Opportunity Types

Potential downstream opportunity categories:

```text
GI_UPGRADE
CORROSION_UPGRADE
SURFACE_QUALITY_UPGRADE
WELDABILITY_UPGRADE
PRECOATED_STEEL_APPLICATION
APPLIANCE_MATERIAL_UPGRADE
AUTOMOTIVE_COATING_UPGRADE
PROCESS_MAINTENANCE_REDUCTION
CUT_EDGE_CORROSION_IMPROVEMENT
```

These are commercial hypotheses, not guaranteed product wins.

---

# 79. GI Upgrade Opportunity

Input:

```text
customer currently uses GI
+
needs greater corrosion resistance
+
wants similar processing route
```

Possible opportunity:

```text
POSMAC_1_5
```

Next checks:

```text
application
forming
welding
paint
coating mass
customer qualification
```

---

# 80. PosMAC 3.0 Downgrade/Optimization Opportunity

A customer using a higher-corrosion product may potentially evaluate PosMAC 1.5 if:

```text
extreme corrosion resistance is not required
+
surface quality
+
welding
+
forming
```

are more important.

This is only:

```text
OPTIMIZATION_HYPOTHESIS
```

not a direct substitution recommendation.

---

# 81. Negative Routing Rules

## Severe coastal environment

Do not automatically route:

```text
POSMAC_1_5
```

Evaluate:

```text
POSMAC_3_0
POSMAC_SUPER
```

---

## Continuous water contact

Do not assume PosMAC 1.5 is ideal.

Return:

```text
DESIGN_REVIEW_REQUIRED
```

---

## Chemical equipment

Do not route PosMAC 1.5 solely because:

```text
CORROSION
```

appears.

Other material families such as:

```text
STAINLESS
TITANIUM
ANCOR
```

may be more relevant depending on medium.

---

## High-strength automotive crash component

Do not route directly from:

```text
HIGH_STRENGTH
```

to PosMAC 1.5.

Select substrate first.

---

## Maximum corrosion priority

Do not assume PosMAC 1.5 is the most corrosion-resistant PosMAC family.

---

# 82. Product Routing Score

Suggested score:

```text
Application Match          20%
Corrosion Requirement      20%
Surface Requirement        15%
Formability                15%
Weldability                15%
Paint / Precoat Match      10%
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

# 83. Product Candidate Object

```yaml
product_family: POSMAC_1_5

application: HOME_APPLIANCE_PANEL

component:
  - REFRIGERATOR_DOOR

requirements:
  - CORROSION_RESISTANCE
  - SURFACE_QUALITY
  - FORMABILITY
  - PAINTABILITY

reason:
  - source-supported appliance application
  - surface-quality priority
  - pre-coated steel compatibility
  - corrosion improvement versus ordinary GI

missing_information:
  - substrate_grade
  - coating_mass
  - post_treatment
  - paint_process

selection_status:
  PRODUCT_FAMILY_MATCH
```

---

# 84. Automotive Candidate Object

```yaml
industry: AUTOMOTIVE

application:
  - AUTOMOTIVE_PANEL

requirements:
  - CORROSION_RESISTANCE
  - WELDABILITY
  - FORMABILITY
  - SURFACE_QUALITY

product_family:
  POSMAC_1_5

substrate:
  status: SUBSTRATE_GRADE_UNKNOWN

coating_mass:
  status: UNKNOWN

post_treatment:
  status: UNKNOWN

final_status:
  ENGINEERING_REVIEW_REQUIRED
```

---

# 85. Structural Candidate Object

```yaml
industry: CONSTRUCTION

application:
  - PURLIN

environment:
  - OUTDOOR_GENERAL

requirements:
  - CORROSION_RESISTANCE
  - FORMABILITY

product_family:
  POSMAC_1_5

escalation_rule:
  severe_corrosion:
    route_to: POSMAC_3_0

  extreme_coastal:
    route_to: POSMAC_SUPER
```

---

# 86. Daily Intelligence Mode

For automated intelligence, normally stop at:

```text
POSMAC_1_5
```

Do not automatically retrieve:

```text
exact grade
exact coating mass
exact post-treatment
exact mechanical properties
```

Recommended:

```yaml
daily_posmac_1_5:
  allow_product_family: true
  allow_grade_class: false
  allow_exact_coating_mass: false
  allow_exact_post_treatment: false
  allow_pdf_lookup: false
```

---

# 87. Marketing Mode

Marketing retrieval may include:

```text
application
GI replacement hypothesis
PosMAC 1.5 benefit
PosMAC 3.0 comparison
surface / welding / forming benefit
customer questions
```

Example:

```text
Customer uses GI for an appliance outer panel
and is seeking higher corrosion resistance
without sacrificing appearance and forming.

PosMAC 1.5 is a strong candidate.

Next checks:
required coating mass,
paint system,
forming severity,
welding process,
customer qualification.
```

---

# 88. Engineering Mode

Engineering analysis may retrieve:

```text
exact grade
KS / EN / ASTM mapping
YP
TS
elongation
coating mass
post-treatment
thickness
width
edge
welding
painting
forming condition
```

from the source PDF.

---

# 89. Numeric Data Rule

Every numeric value should preserve:

```yaml
value:
unit:
value_type:
test_method:
sample_condition:
source_document:
```

Possible value types:

```text
SPECIFICATION
COMPARATIVE_TEST_RESULT
MANUFACTURING_RANGE
```

---

# 90. Test Result Guardrail

Do not mix:

```text
SST
CCT
FIELD_EXPOSURE
```

results.

Do not compare samples unless:

```text
coating mass
post-treatment
geometry
exposure
```

are reasonably aligned.

---

# 91. Source Authority

Canonical product source:

```text
2025 POSMAC1.5.pdf
```

For PosMAC 1.5 claims, this source overrides:

```text
generic model knowledge
cross-product summaries
unverified web claims
```

unless an explicit update/verification workflow is performed.

---

# 92. Source Conflict Rule

If another POSCO catalog provides different:

```text
manufacturing range
grade availability
post-treatment
coating mass
```

do not silently reconcile.

Use:

```text
SOURCE_CONFLICT
```

and prioritize the dedicated PosMAC 1.5 guide unless a newer approved source supersedes it.

---

# 93. Product Knowledge Status

Current:

```yaml
product_family: POSMAC_1_5
knowledge_status: VERIFIED

source:
  2025_POSMAC1_5_PDF: PRIMARY
```

Exact current orderability remains subject to inquiry.

---

# 94. Unknown States

Supported:

```text
POSMAC_1_5_GRADE_UNKNOWN

SUBSTRATE_GRADE_UNKNOWN

COATING_MASS_UNKNOWN

POST_TREATMENT_UNKNOWN

FORMING_SEVERITY_UNKNOWN

WELDING_PROCESS_UNKNOWN

PAINT_PROCESS_UNKNOWN

CORROSION_SEVERITY_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

INQUIRY_SPEC_REVIEW_REQUIRED

CUSTOMER_PROCESS_VALIDATION_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 95. Retrieval Keywords

```text
PosMAC 1.5
POSMAC1.5
PosMAC1.5
Zn-1.5Mg-1.5Al
Zn-1.5%Mg-1.5%Al
고내식 도금강판
마그네슘 알루미늄 합금도금
가전 패널
자동차 패널
칼라강판
Pre-coated Steel
절단면 내식성
Galling
백청
NB Cr-Free
CE Cr3+
KS D 3030
```

Keywords are retrieval aids only.

---

# 96. Routing Algorithm

```pseudo
function route_posmac_1_5(context):

    identify application
    identify environment
    identify corrosion_requirement
    identify surface_requirement
    identify forming
    identify welding
    identify painting

    if extreme_corrosion
       or extreme_coastal:
        evaluate POSMAC_3_0 / POSMAC_SUPER
        do not default POSMAC_1_5

    if application in [
        HOME_APPLIANCE_PANEL,
        AUTOMOTIVE_PANEL,
        PRECOATED_STEEL
    ]
       and corrosion
       and (
          surface_quality
          or weldability
          or formability
       ):
        candidate = POSMAC_1_5

    if application in [
        PURLIN,
        PIPE,
        ROOFING,
        GREENHOUSE_PIPE,
        DECK_PLATE
    ]
       and corrosion_environment is normal_or_enhanced:
        candidate += POSMAC_1_5

    if continuous_water_contact:
        add DESIGN_REVIEW_REQUIRED

    verify:
        substrate_grade
        grade_class
        coating_mass
        post_treatment
        size
        edge
        forming
        welding
        painting

    return candidate
```

---

# 97. Example — Refrigerator Door

```yaml
industry: HOME_APPLIANCE

application:
  - REFRIGERATOR

component:
  - DOOR

requirements:
  - CORROSION_RESISTANCE
  - SURFACE_QUALITY
  - FORMABILITY
  - PAINTABILITY

product_candidate:
  POSMAC_1_5

reason:
  - source-supported appliance use
  - pre-coated steel suitability
  - balanced corrosion and surface performance

missing_information:
  - grade
  - coating_mass
  - post_treatment
  - paint_system
```

---

# 98. Example — Automotive Outer Panel

```yaml
industry: AUTOMOTIVE

application:
  - AUTOMOTIVE_OUTER_PANEL

requirements:
  - CORROSION_RESISTANCE
  - SURFACE_QUALITY
  - FORMABILITY
  - WELDABILITY

product_candidate:
  POSMAC_1_5

substrate:
  status: UNKNOWN

next_action:
  - identify substrate mechanical requirement
  - confirm coating compatibility
  - confirm welding process
  - confirm customer surface approval
```

---

# 99. Example — GI Upgrade

Input:

```text
Current material:
GI

Issue:
corrosion durability

Constraints:
existing forming and assembly process should be retained
```

Possible reasoning:

```text
GI
↓
corrosion upgrade required
↓
process compatibility important
↓
POSMAC_1_5 candidate
```

Result:

```yaml
opportunity_type:
  GI_UPGRADE

product_candidate:
  POSMAC_1_5

status:
  VALIDATION_REQUIRED
```

---

# 100. Example — Harsh Coastal Structure

Input:

```text
COASTAL
+
HIGH_SALINITY
+
STRUCTURAL
```

Do NOT automatically return:

```text
POSMAC_1_5
```

Route back:

```text
coated/index.md
```

and evaluate:

```text
POSMAC_3_0
POSMAC_SUPER
```

---

# 101. Final Knowledge Chain

```text
CUSTOMER SIGNAL
↓
APPLICATION
↓
ENVIRONMENT
↓
CORROSION REQUIREMENT
↓
SURFACE + FORMING + WELDING
↓
POSMAC_1_5
↓
SUBSTRATE / GRADE CLASS
↓
COATING MASS
↓
POST-TREATMENT
↓
SIZE / EDGE
↓
CUSTOMER PROCESS VALIDATION
↓
ENGINEERING APPROVAL
↓
MARKETING OPPORTUNITY
```

---

# 102. Final Rule

The purpose of PosMAC 1.5 is NOT:

```text
MAXIMUM CORROSION RESISTANCE
```

The correct product position is:

```text
HIGHER CORROSION RESISTANCE
THAN ORDINARY GI
+
GOOD SURFACE QUALITY
+
GOOD WELDABILITY
+
GOOD FORMABILITY
+
PRECOATED STEEL SUITABILITY
```

The preferred reasoning order is:

```text
APPLICATION
↓
CORROSION SEVERITY
↓
SURFACE / FORMING / WELDING
↓
POSMAC 1.5
↓
GRADE / COATING / POST-TREATMENT
```

not:

```text
POSMAC 1.5
↓
find a reason to use it
```

The responsibility of this file ends at:

```text
DEFENSIBLE POSMAC 1.5 PRODUCT CANDIDATE
```

Final customer specification remains subject to product-quality and engineering review.
