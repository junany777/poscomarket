---
product_family: AUTOMOTIVE_STEEL

industry:
  - AUTOMOTIVE

material_categories:
  - AUTOMOTIVE_STEEL
  - HIGH_STRENGTH_AUTOMOTIVE_STEEL
  - ADVANCED_HIGH_STRENGTH_STEEL

applications:
  - VEHICLE_BODY
  - BODY_IN_WHITE
  - EV_BODY_STRUCTURE
  - CHASSIS
  - CRASH_STRUCTURE
  - BATTERY_PACK_STRUCTURE

components:
  - OUTER_PANEL
  - INNER_PANEL
  - DOOR_OUTER
  - HOOD
  - FLOOR
  - A_PILLAR
  - SIDE_SILL
  - FRONT_SIDE_MEMBER
  - CENTER_MEMBER
  - SEAT_RAIL
  - ROOF_REINFORCEMENT
  - UNDERBODY_REINFORCEMENT
  - SUSPENSION
  - LOWER_ARM
  - WHEEL_DISC
  - BUMPER_BEAM
  - CROSS_MEMBER
  - BATTERY_PACK_STRUCTURE

internal_families:
  - MILD_STEEL
  - BAKE_HARDENING_STEEL
  - HSLA
  - REPHOSPHORIZED_STEEL
  - IF_HSS
  - DP
  - TRIP
  - CP
  - FB
  - MART
  - HPF
  - PHT

supply_forms:
  - CR
  - PO
  - EG
  - GI
  - GA
  - AL_SI_COATED

source_documents:
  - 2025 Automotive Steel.pdf

knowledge_status: VERIFIED
---

# POSCO Automotive Steel Product Knowledge

## 1. Purpose

This file defines the product knowledge and internal routing rules for POSCO automotive steels.

It is loaded only after:

```text
industry = AUTOMOTIVE
```

and:

```text
product_family = AUTOMOTIVE_STEEL
```

have already been selected by:

```text
knowledge/posco/index.md
```

and:

```text
knowledge/posco/automotive/index.md
```

This file answers:

```text
Which automotive steel family should be investigated?
```

It does NOT automatically answer:

```text
Which exact grade should be supplied?
```

---

# 2. Core Product Selection Chain

Use:

```text
APPLICATION
↓
COMPONENT
↓
COMPONENT FUNCTION
↓
PERFORMANCE REQUIREMENTS
↓
FORMABILITY REQUIREMENTS
↓
STRENGTH REQUIREMENTS
↓
COATING / SURFACE REQUIREMENTS
↓
AUTOMOTIVE STEEL FAMILY
↓
GRADE FAMILY
↓
SPECIFIC GRADE
```

Never select automotive steel based only on:

```text
strength number
```

or:

```text
vehicle type
```

---

# 3. Automotive Steel Architecture

The product portfolio should be interpreted in four broad layers.

```text
LEVEL 1
MILD / FORMABLE STEEL

LEVEL 2
CONVENTIONAL HIGH STRENGTH STEEL

LEVEL 3
ADVANCED HIGH STRENGTH STEEL

LEVEL 4
HEAT-TREATED ULTRA-HIGH-STRENGTH STEEL
```

Suggested internal grouping:

```text
MILD / FORMABLE
├── CQ
├── DQ
├── DDQ
├── EDDQ
└── S-EDDQ

CONVENTIONAL HSS
├── BAKE_HARDENING_STEEL
├── HSLA
├── REPHOSPHORIZED_STEEL
└── IF_HSS

AHSS
├── DP
├── TRIP
├── CP
├── FB
└── MART

HOT / POST HEAT TREATMENT
├── HPF
└── PHT
```

---

# 4. Supply Form Codes

Canonical internal codes:

```text
CR
EG
GI
GA
PO
HR
AL_SI
```

Meanings:

```text
CR
= uncoated cold rolled

EG
= electrogalvanized

GI
= hot-dip galvanized

GA
= hot-dip galvannealed

PO
= pickled and oiled hot rolled

HR
= hot rolled

AL_SI
= Al-Si coated
```

Do not assume that every automotive steel grade is available in every supply form.

Availability must be checked at grade level.

---

# 5. Availability Status

Catalog symbols may distinguish:

```text
COMMERCIAL_PRODUCT
CUSTOMER_TRIAL
NOT_LISTED
```

These statuses are materially different.

Rules:

```text
COMMERCIAL_PRODUCT
→ catalog indicates commercial availability

CUSTOMER_TRIAL
→ trial status; do not present as normal commercial availability

NOT_LISTED
→ do not assume availability
```

If uncertain:

```text
COMMERCIAL_STATUS_UNKNOWN
```

---

# 6. Mild / Formable Automotive Steel

General forming-quality classes referenced in the automotive catalog include:

```text
CQ
LQ
DQ
DDQ
EDDQ
S_EDDQ
```

These classes emphasize increasing forming capability rather than ultra-high strength.

Use when the component requirement is dominated by:

```text
FORMABILITY
DEEP_DRAWABILITY
SURFACE_QUALITY
```

rather than high crash strength.

---

# 7. Bake Hardening Steel

Canonical code:

```text
BAKE_HARDENING_STEEL
```

Alias:

```text
BH
```

## 7.1 Core Concept

Bake-hardening steel is designed so that yield strength increases after paint baking.

The source describes approximately:

```text
30 MPa or more
```

increase through the bake-hardening effect.

The steel combines:

```text
INITIAL_FORMABILITY
+
POST_FORMING_STRENGTH_INCREASE
```

This makes it especially relevant to automotive outer panels.

---

# 7.2 BH Key Requirements

```text
FORMABILITY
DENT_RESISTANCE
SURFACE_QUALITY
WEIGHT_REDUCTION
BAKE_HARDENABILITY
```

The catalog specifically notes improved dent resistance, allowing sheet-thickness reduction while maintaining comparable dent resistance.

---

# 7.3 BH Applications

Strong source-supported applications:

```text
HOOD
DOOR_OUTER
OUTER_PANEL
```

Use BH when:

```text
outer panel
+
forming required
+
dent resistance important
```

Do not route structural crash members to BH simply because a strength increase is desired.

---

# 7.4 BH Representative Grades

Source-supported grade keys include:

```text
340BH

180YB
210YB
240YB
270YB
```

Do not treat:

```text
340BH
```

and:

```text
YB series
```

as identical specification systems.

---

# 7.5 BH Supply Availability

The supplied catalog shows examples including:

```text
CR
EG
GI
GA
```

with availability varying by grade.

For example, the catalog lists 340BH with uncoated and hot-dip coated options, while several YB grades show different combinations of EG/GI/GA availability.

Always verify exact grade/supply-form combination.

---

# 7.6 BH Selection Rule

Strong route:

```text
OUTER_PANEL
+
DENT_RESISTANCE
+
FORMABILITY
→ BH
```

Weak route:

```text
CRASH_MEMBER
+
VERY_HIGH_STRENGTH
→ NOT BH
```

---

# 8. HSLA

Canonical code:

```text
HSLA
```

Full name:

```text
HIGH_STRENGTH_LOW_ALLOY_STEEL
```

## 8.1 Core Concept

The POSCO catalog describes HSLA as low-carbon steel strengthened with precipitation-forming alloying elements such as:

```text
Ti
Nb
```

The fine precipitates increase:

```text
YIELD_STRENGTH
IMPACT_RESISTANCE
```

HSLA tends to exhibit a relatively high:

```text
YS / TS ratio
```

---

# 8.2 HSLA Primary Use

The catalog states that HSLA is generally used for automotive reinforcement components requiring high strength.

Typical routing concepts:

```text
REINFORCEMENT
STRUCTURAL_MEMBER
CHASSIS
```

---

# 8.3 HSLA Requirements

```text
HIGH_YIELD_STRENGTH
HIGH_STRENGTH
IMPACT_RESISTANCE
STRUCTURAL_STABILITY
```

Possible manufacturing considerations:

```text
FORMABILITY
WELDABILITY
```

must still be verified at grade level.

---

# 8.4 HSLA Grade Families

The catalog separates:

```text
C_CLASS
YS_GUARANTEED_CLASS
```

Representative grades include:

```text
440C
590C

220YC
260YC
300YC
340YC
```

Do not infer that the numeric prefix always has the same guaranteed-property meaning across C and YC classes.

---

# 8.5 HSLA Application Examples

Source-supported examples include:

```text
CENTER_MEMBER
FRONT_SUSPENSION_MODULE
REAR_SUSPENSION_MODULE
SIDE_SILL
CHASSIS
WHEEL_RIM
WHEEL_DISC
```

The catalog specifically connects cold-rolled / galvanized HSLA to parts requiring crashworthiness and stiffness, and hot-rolled products to chassis and wheel applications.

---

# 8.6 HSLA Selection Rule

Strong route:

```text
STRUCTURAL_REINFORCEMENT
+
HIGH_YIELD_STRENGTH
+
STIFFNESS
→ HSLA
```

Do not prefer HSLA when:

```text
very high elongation
```

or:

```text
ultra-high crash strength
```

is the dominant need without comparing AHSS families.

---

# 9. Rephosphorized Steel

Canonical code:

```text
REPHOSPHORIZED_STEEL
```

Alias:

```text
R_CLASS
```

## 9.1 Product Positioning

The catalog includes Rephosphorized Steel as one of its conventional automotive high-strength steel families.

Representative tensile-strength grade keys include:

```text
340R
390R
440R
```

Hot-rolled / PO variants shown include:

```text
310R
370R
400R
440R
```

---

# 9.2 Supply Forms

Catalog-supported combinations vary by grade and may include:

```text
CR
EG
GI
GA
PO
```

The 340R / 390R / 440R cold-rolled family is shown across multiple coated and uncoated forms.

Some PO variants have more limited coated availability.

---

# 9.3 Application Direction

The catalog associates this family with high-strength automotive body components such as:

```text
COWL
WHEEL_APRON
FRONT_SIDE_MEMBER
```

Use when:

```text
moderate high strength
+
body structure
+
forming capability
```

is needed.

Do not treat Rephosphorized Steel as a direct substitute for DP/CP/MART in very-high-strength crash applications.

---

# 10. IF HSS

Canonical code:

```text
IF_HSS
```

Expanded name:

```text
INTERSTITIAL_FREE_HIGH_STRENGTH_STEEL
```

Families:

```text
E_CLASS
ES_CLASS
YE_CLASS
```

---

# 10.1 IF HSS Core Concept

POSCO describes IF HSS as ultra-low-carbon steel with Ti added to bind interstitial elements.

Strength is increased through substitutional solid-solution elements such as:

```text
P
Mn
```

while maintaining strong deep-drawing performance.

---

# 10.2 IF HSS Primary Benefit

Core combination:

```text
HIGH_STRENGTH
+
HIGH_R_VALUE
+
DEEP_DRAWABILITY
```

This makes IF HSS especially suitable where:

```text
complex forming
```

and:

```text
higher strength
```

must coexist.

---

# 10.3 IF HSS Applications

Source-supported examples:

```text
REAR_FLOOR_SIDE_MEMBER
A_PILLAR_OUTER_REINFORCEMENT
REAR_FLOOR
FLOOR_SIDE_REINFORCEMENT
```

The catalog explicitly describes use in parts requiring high formability such as members, floors, and A-pillar outer reinforcement.

---

# 10.4 IF HSS Representative Grades

```text
340E
390E
440E
340ES

180YE
220YE
260YE
```

Do not infer equivalence between:

```text
E
ES
YE
```

grade concepts.

---

# 10.5 IF HSS Supply Forms

The catalog shows the listed E/ES/YE products in combinations including:

```text
CR
EG
GI
GA
```

with commercial availability indicated for the listed products.

---

# 10.6 IF HSS Selection Rule

Use when:

```text
BODY_MEMBER
+
DEEP_DRAWING
+
HIGH_R_VALUE
+
MODERATE_HIGH_STRENGTH
```

is the dominant requirement.

Consider another family when:

```text
CRASH_STRENGTH
```

or:

```text
ULTRA_HIGH_STRENGTH
```

dominates.

---

# 11. Advanced High Strength Steel

Canonical parent:

```text
AHSS
```

Subfamilies:

```text
DP
TRIP
CP
FB
MART
```

These families must remain separate.

Do not represent AHSS as one single material.

---

# 12. DP Steel

Canonical code:

```text
DP
```

Full name:

```text
DUAL_PHASE_STEEL
```

## 12.1 Microstructure

The source describes DP steel as:

```text
FERRITE MATRIX
+
MARTENSITE SECOND PHASE
```

---

# 12.2 DP Characteristics

Key characteristics:

```text
LOW_YIELD_RATIO
GOOD_FORMABILITY
HIGH_STRENGTH
GOOD_ELONGATION
BAKE_HARDENABILITY
```

The catalog describes a yield ratio roughly in the:

```text
0.5–0.6 range
```

and states that DP provides relatively high elongation, second to TRIP among the described steels.

---

# 12.3 DP Strength Classes

Representative families:

```text
490DP
590DP
780DP
980DP
```

Additional catalog variants include:

```text
590DH
780DH

980DP_M
980DP_EL
980DP_H
```

These suffix variants must not be merged automatically.

---

# 12.4 DP Supply Forms

Depending on grade:

```text
CR
EG
GI
GA
PO
```

may be available.

The catalog notes that many DP products are manufactured as:

```text
GI / GA
```

and also provides cold-rolled and hot-rolled variants.

---

# 12.5 DP Source-Supported Applications

Examples:

```text
DOOR_OUTER
SEAT_RAIL
SUSPENSION
SILL_SIDE_MEMBER
ROOF_REINFORCEMENT
SEAT_BELT_REINFORCEMENT
SILL_SIDE_PANEL
UNDERBODY_REINFORCEMENT
```

Specific examples include:

```text
DOOR_OUTER
→ GA 490DP

SEAT_RAIL
→ CR 980DP

SUSPENSION
→ PO 590DP
```

These examples are source-supported examples, not universal grade prescriptions.

---

# 12.6 DP Routing

Use DP when:

```text
HIGH_STRENGTH
+
GOOD_FORMABILITY
```

must be balanced.

Possible use contexts:

```text
BODY_STRUCTURE
CRASH_STRUCTURE
SEAT_STRUCTURE
SUSPENSION
```

---

# 12.7 DP Exclusion Rule

Do not automatically select DP if the requirement is dominated by:

```text
MAXIMUM_ELONGATION
→ consider TRIP

HIGH_YIELD_RATIO + BENDABILITY
→ consider CP

HOLE_EXPANSION / STRETCH_FLANGEABILITY
→ consider FB

EXTREME_TENSILE_STRENGTH
→ consider MART / HPF
```

---

# 13. TRIP Steel

Canonical code:

```text
TRIP
```

Full name:

```text
TRANSFORMATION_INDUCED_PLASTICITY_STEEL
```

---

# 13.1 TRIP Microstructure

The source describes TRIP steel as:

```text
FERRITE
+
BAINITE
+
RETAINED_AUSTENITE
```

and in some cases a small quantity of martensite.

---

# 13.2 TRIP Characteristics

Primary strengths:

```text
HIGH_STRENGTH
HIGH_ELONGATION
GOOD_FORMABILITY
```

The source describes TRIP as particularly suitable for parts requiring:

```text
HIGH_FORMABILITY
```

---

# 13.3 TRIP Strength Families

Source-supported grades include:

```text
590TR
780TR
980TR
1180TR
```

---

# 13.4 TRIP Supply Forms

Catalog examples include:

```text
CR
GA
EG
```

depending on grade.

Important caution:

The source notes that higher-strength TRIP steels may be difficult to manufacture as hot-dip galvanized products because of Si and other alloying elements that can adversely affect coating quality.

Therefore:

```text
TRIP
+
GI requirement
```

must not be assumed to be available.

---

# 13.5 TRIP Routing

Strong route:

```text
HIGH_STRENGTH
+
HIGH_ELONGATION
+
COMPLEX_FORMING
→ TRIP
```

Consider TRIP where deformation capacity is critical.

---

# 14. CP Steel

Canonical code:

```text
CP
```

Full name:

```text
COMPLEX_PHASE_STEEL
```

---

# 14.1 CP Microstructure

Source-supported structure:

```text
FERRITE
+
BAINITE
+
MARTENSITE
+
Ti / Nb precipitates
```

---

# 14.2 CP Characteristics

Key properties:

```text
HIGH_YIELD_RATIO
HIGH_STRENGTH
GOOD_BENDABILITY
CRASH_RESISTANCE
```

The catalog attributes these characteristics primarily to bainitic and martensitic phases.

---

# 14.3 CP Representative Grades

```text
780CP
980CP
1180CP
```

The catalog also shows a hot-rolled / PO:

```text
780CP
```

variant.

---

# 14.4 CP Supply Forms

Depending on grade:

```text
CR
GI
GA
PO
```

may be shown.

Commercial status varies by grade.

For example, the catalog marks some combinations as:

```text
COMMERCIAL_PRODUCT
```

and at least some CP combinations as:

```text
CUSTOMER_TRIAL
```

This status must be preserved.

---

# 14.5 CP Applications

Source-supported applications:

```text
SILL_SIDE_PANEL
UNDERBODY_REINFORCEMENT
CRASHWORTHINESS_COMPONENT
```

The catalog gives:

```text
GA 1180CP
```

for sill-side panel as an application example.

Do not generalize that grade to every sill application.

---

# 14.6 CP Routing

Use when:

```text
CRASH_STRUCTURE
+
HIGH_YIELD_STRENGTH
+
BENDABILITY
```

are dominant.

---

# 15. FB Steel

Canonical code:

```text
FB
```

Full name:

```text
FERRITE_BAINITE_STEEL
```

---

# 15.1 FB Microstructure

The source describes FB as a two-phase structure consisting of:

```text
FERRITE
+
BAINITE
```

---

# 15.2 FB Characteristics

The soft ferrite contributes:

```text
ELONGATION
```

while bainite contributes strong:

```text
STRETCH_FLANGEABILITY
```

The resulting steel exhibits good:

```text
HOLE_EXPANSION
```

performance.

---

# 15.3 FB Representative Grades

```text
440FB
540FB
590FB
780FB
```

Catalog supply form:

```text
PO
```

for the listed grades.

---

# 15.4 FB Applications

Strong source-supported components:

```text
LOWER_ARM
WHEEL_DISC
SUSPENSION
```

The source explicitly states that hot-rolled FB steel is used for:

```text
suspensions
wheel discs
```

---

# 15.5 FB Routing

Strong route:

```text
CHASSIS
+
HOLE_EXPANSION
+
STRETCH_FLANGEABILITY
+
FORMABILITY
→ FB
```

Do not route outer panels to FB.

---

# 16. MART Steel

Canonical code:

```text
MART
```

Full name:

```text
MARTENSITIC_STEEL
```

---

# 16.1 MART Microstructure

The catalog describes MART steel as consisting predominantly of:

```text
MARTENSITE
```

with smaller amounts of:

```text
BAINITE
or
FERRITE
```

---

# 16.2 MART Characteristics

Primary benefit:

```text
VERY_HIGH_TENSILE_STRENGTH
```

Primary trade-off:

```text
VERY_LOW_DUCTILITY
```

The catalog states that martensitic steels show the highest tensile strength among the carbon steels described in this context.

---

# 16.3 MART Representative Grades

```text
1300M
1500M
1700M
```

---

# 16.4 MART Supply / Status

The catalog shows:

```text
1300M
→ uncoated commercial

1500M
→ uncoated / EG commercial

1700M
→ customer trial in uncoated / EG
```

Interpret catalog status carefully.

Do not present:

```text
1700M
```

as ordinary commercial availability based solely on its appearance in the catalog.

---

# 16.5 MART Applications

Source-supported examples include:

```text
BUMPER_BEAM
SILL_SIDE_MEMBER
INNER_CROSS_MEMBER
SIDE_FRAME
BATTERY_PACK_STRUCTURE
```

---

# 16.6 MART Routing

Strong route:

```text
INTRUSION_RESISTANCE
+
VERY_HIGH_STRENGTH
+
LIMITED_FORMING_COMPLEXITY
→ MART
```

Do not route highly complex deep-drawing parts to MART solely because high strength is required.

---

# 17. HPF Steel

Canonical code:

```text
HPF
```

Full name:

```text
HOT_PRESS_FORMING_STEEL
```

Aliases:

```text
HOT_STAMPING
PRESS_HARDENING
```

---

# 17.1 HPF Core Concept

The source describes HPF steel as being formed at elevated temperature and rapidly cooled to achieve ultra-high-strength components.

Boron is added to improve hardenability.

---

# 17.2 HPF Key Benefit

HPF allows:

```text
COMPLEX_HIGH_TEMPERATURE_FORMING
+
POST_QUENCH_ULTRA_HIGH_STRENGTH
```

This makes it fundamentally different from ordinary cold-formed AHSS.

---

# 17.3 HPF Representative Families

Source-supported grade concepts include:

```text
550HPF
1500HPF
1800HPF
2000HPF
```

The source shows both pre-heat-treatment and post-heat-treatment mechanical properties.

Do not compare the before-heat-treatment strength values directly with final component strength.

---

# 17.4 HPF Coating / Supply Forms

The catalog describes:

```text
AL_SI_COATED
CR
PO
```

routes.

Al-Si coating is widely used to reduce oxidation during heating.

For uncoated CR / PO material, the catalog states that:

```text
SHOT_BLASTING
```

may be required after HPF to remove surface oxide.

---

# 17.5 HPF Routing

Strong route:

```text
ULTRA_HIGH_STRENGTH
+
COMPLEX_COMPONENT_GEOMETRY
+
HOT_STAMPING_PROCESS
→ HPF
```

Do not route cold-forming-only production lines to HPF without process evidence.

---

# 18. PHT Steel

Canonical code:

```text
PHT
```

Full name:

```text
POST_HEAT_TREATMENT_STEEL
```

---

# 18.1 PHT Core Concept

The catalog describes PHT as a POSCO automotive steel product concept used in components such as:

```text
DOOR_IMPACT_BEAM
STABILIZER
```

The steel is formed first and subsequently heat-treated to obtain tempered martensitic structure.

---

# 18.2 PHT Performance Direction

The catalog states that after forming and heat treatment, tensile strength of approximately:

```text
1500 MPa or higher
```

can be obtained.

---

# 18.3 PHT Representative Product Keys

Source-supported examples include:

```text
STAB
AUTOBEAM
```

Do not infer detailed supply conditions beyond those supported by the catalog.

---

# 18.4 PHT Routing

Use when:

```text
FORM_FIRST
+
POST_HEAT_TREATMENT
+
ULTRA_HIGH_FINAL_STRENGTH
```

is the manufacturing route.

Do not confuse:

```text
PHT
```

with:

```text
HPF
```

HPF forms the component during hot processing.

PHT forms first and heat-treats afterward.

---

# 19. Family Comparison Summary

| Family | Dominant Strength | Dominant Forming / Functional Character |
|---|---|---|
| BH | moderate | formability + dent resistance + bake hardening |
| HSLA | high yield strength | reinforcement / stiffness |
| Rephosphorized | moderate-high | body structure + forming |
| IF HSS | moderate-high | deep drawing + high r-value |
| DP | high to very high | strength + formability |
| TRIP | high to very high | strength + high elongation |
| CP | very high | high yield ratio + bendability |
| FB | high | hole expansion / stretch flangeability |
| MART | ultra-high | maximum tensile strength, low ductility |
| HPF | ultra-high after hot forming | complex hot-stamped part |
| PHT | ultra-high after post heat treatment | formed-then-heat-treated part |

This table is a routing summary only.

It is not a substitute for engineering selection.

---

# 20. Component-to-Family Routing

## HOOD / DOOR OUTER

Primary candidates:

```text
BH
```

Possible alternatives:

```text
DP
IF_HSS
```

depending on design requirements.

Dominant criteria:

```text
FORMABILITY
DENT_RESISTANCE
SURFACE_QUALITY
```

---

## FLOOR / A-PILLAR REINFORCEMENT

Primary candidate:

```text
IF_HSS
```

when deep drawing is dominant.

Possible alternatives:

```text
DP
HSLA
```

when strength rises.

---

## COWL / WHEEL APRON

Possible candidate:

```text
REPHOSPHORIZED_STEEL
```

Source catalog associates these high-strength body applications with R-class steel.

---

## CENTER MEMBER / REINFORCEMENT

Possible candidates:

```text
HSLA
DP
CP
```

Select according to:

```text
YIELD_STRENGTH
CRASH_FUNCTION
FORMING_COMPLEXITY
```

---

## SILL SIDE / UNDERBODY REINFORCEMENT

Possible candidates:

```text
DP
CP
MART
HPF
```

This is a high-ambiguity route.

Exact family selection requires component-function and manufacturing-process evidence.

---

## SEAT RAIL

Source-supported example:

```text
DP
```

with 980DP shown in the catalog as an application example.

Do not treat 980DP as universally required.

---

## SUSPENSION / LOWER ARM

Priority:

```text
FB
```

Possible:

```text
DP
HSLA
```

depending on geometry and requirements.

---

## WHEEL DISC

Priority:

```text
FB
```

---

## BUMPER BEAM

Potential routes:

```text
MART
HPF
PHT
```

Selection depends on manufacturing route.

---

## DOOR IMPACT BEAM

Potential route:

```text
PHT
```

based on the source catalog.

---

## BATTERY PACK STRUCTURE

Potential route:

```text
MART
```

Source catalog shows POSCO Steel Battery Pack as a MART application example.

Other AHSS routes may still require project-specific analysis.

---

# 21. Performance-Based Routing

## DENT_RESISTANCE

```text
→ BH
```

especially for outer panels.

---

## DEEP_DRAWABILITY

```text
→ IF_HSS
```

when strength is also required.

---

## HIGH_YIELD_STRENGTH

Possible:

```text
HSLA
CP
```

depending on required strength level and forming route.

---

## STRENGTH + FORMABILITY BALANCE

```text
→ DP
```

---

## HIGH_STRENGTH + HIGH_ELONGATION

```text
→ TRIP
```

---

## HIGH_STRENGTH + BENDABILITY + CRASH

```text
→ CP
```

---

## HOLE_EXPANSION / STRETCH_FLANGEABILITY

```text
→ FB
```

---

## MAXIMUM_COLD_ROLLED_STRENGTH

```text
→ MART
```

subject to low ductility.

---

## ULTRA_HIGH_STRENGTH + HOT_FORMING

```text
→ HPF
```

---

## FORM_THEN_HEAT_TREAT

```text
→ PHT
```

---

# 22. Strength Is Not Enough

Forbidden logic:

```text
Need 1000+ MPa
→ MART
```

Correct logic:

```text
Need 1000+ MPa
+
component function
+
forming method
+
elongation need
+
bendability need
+
coating need
↓
DP / TRIP / CP / MART / HPF candidate comparison
```

---

# 23. Coating Is a Separate Decision Layer

Base material and coating must be treated separately.

Example:

```text
DP
+
GI
```

means:

```text
DP substrate
+
hot-dip galvanized coating
```

not a separate strength family.

Possible supply-form codes:

```text
CR
EG
GI
GA
PO
AL_SI
```

The exact combination depends on grade.

---

# 24. Coating Routing Rule

If the component requires:

```text
CORROSION_RESISTANCE
PAINTABILITY
SURFACE_QUALITY
```

then after selecting the substrate family:

```text
check supply-form availability
```

Example:

```text
DP selected
↓
need coating
↓
check DP grade compatibility with:
EG / GI / GA
```

Do not load coating knowledge before substrate family is identified unless the user's question is specifically about coating.

---

# 25. DP Coating Caution

The catalog shows that DP availability varies considerably by grade.

Examples:

```text
490DP
→ CR / GI / GA

590DP
→ CR / EG / GI / GA

780DP
→ CR / GI / GA

980DP variants
→ combinations differ by variant
```

Therefore:

```text
DP + coating
```

must always be checked at exact grade level.

---

# 26. TRIP Coating Caution

The source explicitly notes coating difficulty for high-strength TRIP steels.

Therefore:

```text
TRIP
+
HOT_DIP_GALVANIZED
```

should trigger:

```text
AVAILABILITY_CHECK_REQUIRED
```

rather than a confident assumption.

---

# 27. MART Commercial Status Caution

The catalog lists:

```text
1300M
1500M
1700M
```

but:

```text
1700M
```

is shown with customer-trial status in the supplied availability table.

Therefore:

```text
1700M
```

must not be represented as ordinary commercial availability without updated confirmation.

---

# 28. Grade-Level Selection Inputs

Before selecting an exact grade, collect:

```text
component
required tensile strength
required yield strength
required elongation
forming method
bend radius
hole expansion requirement
crash function
coating requirement
sheet thickness
sheet width
joining process
customer specification
commercial status
```

If critical fields are missing:

```text
GRADE_UNKNOWN
```

or:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 29. Grade Naming Rule

Preserve grade names exactly as supported by source.

Examples:

```text
340BH
440C
590C
340R
440E
590DP
980DP-M
1180TR
1180CP
590FB
1500M
1500HPF
```

Do not normalize away meaningful suffixes such as:

```text
M
H
EL
DH
E
ES
Y
```

unless a formal mapping exists.

---

# 30. Grade Status Object

Recommended representation:

```yaml
grade: 1700M
family: MART

availability:
  uncoated: CUSTOMER_TRIAL
  electrogalvanized: CUSTOMER_TRIAL
  galvanized: NOT_LISTED
  galvannealed: NOT_LISTED

source:
  document: 2025 Automotive Steel.pdf
```

---

# 31. Product Family Object

Recommended structure:

```yaml
family: DP

characteristics:
  - HIGH_STRENGTH
  - GOOD_FORMABILITY
  - LOW_YIELD_RATIO
  - BAKE_HARDENABILITY

strength_classes:
  - 490
  - 590
  - 780
  - 980

applications:
  - OUTER_PANEL
  - STRUCTURAL_MEMBER
  - CRASH_MEMBER
  - SEAT_RAIL
  - SUSPENSION

supply_forms:
  - CR
  - EG
  - GI
  - GA
  - PO

knowledge_status: VERIFIED
```

---

# 32. Family Ranking Logic

When multiple families are possible, rank on:

```text
Component Function        25%
Strength Requirement      20%
Formability Requirement   20%
Crash Requirement         15%
Manufacturing Process     10%
Coating Requirement        5%
Evidence Strength          5%
```

Do not calculate exact scores if inputs are incomplete.

---

# 33. Family Selection Confidence

```text
90-100
DIRECT_FAMILY_MATCH

80-89
STRONG_FAMILY_MATCH

70-79
POSSIBLE_FAMILY_MATCH

60-69
WEAK_FAMILY_MATCH

<60
FAMILY_UNKNOWN
```

---

# 34. Example — Door Outer

Input:

```text
component = DOOR_OUTER
requirements:
  FORMABILITY
  DENT_RESISTANCE
  SURFACE_QUALITY
```

Primary candidate:

```text
BH
```

Possible additional check:

```text
coating requirement
```

Output example:

```yaml
family_candidates:
  - family: BAKE_HARDENING_STEEL
    priority: P1
    reason:
      - outer panel
      - dent resistance
      - forming requirement
```

---

# 35. Example — Deep-Drawn Structural Member

Input:

```text
component = A_PILLAR_REINFORCEMENT

requirements:
  HIGH_STRENGTH
  DEEP_DRAWABILITY
```

Candidate:

```text
IF_HSS
```

Reason:

```text
high strength
+
high r-value
+
deep drawing
```

---

# 36. Example — General Crash Member

Input:

```text
component = SILL_SIDE_PANEL

requirements:
  VERY_HIGH_STRENGTH
  CRASH_RESISTANCE
  BENDABILITY
```

Candidate:

```text
CP
```

Potential alternative:

```text
DP
MART
HPF
```

depending on manufacturing requirements.

Do not select one exact grade yet.

---

# 37. Example — Suspension Lower Arm

Input:

```text
component = LOWER_ARM

requirements:
  HIGH_STRENGTH
  FORMABILITY
  HOLE_EXPANSION
```

Primary:

```text
FB
```

---

# 38. Example — Bumper Beam

Input:

```text
component = BUMPER_BEAM

requirements:
  VERY_HIGH_STRENGTH
  INTRUSION_RESISTANCE
```

Potential families:

```text
MART
HPF
PHT
```

Need:

```text
manufacturing_process
```

before narrowing.

---

# 39. Example — Battery Pack Structural Member

Input:

```text
component = BATTERY_PACK_STRUCTURE

requirements:
  VERY_HIGH_STRENGTH
  CRASH_RESISTANCE
```

Source-supported candidate:

```text
MART
```

Potential alternatives must be evaluated using project-specific forming and design information.

---

# 40. Example — Hot-Stamped Safety Part

Input:

```text
forming_process = HOT_STAMPING

requirements:
  COMPLEX_SHAPE
  ULTRA_HIGH_FINAL_STRENGTH
```

Primary:

```text
HPF
```

Do not route MART solely because final strength is high.

---

# 41. Example — Door Impact Beam with Post Heat Treatment

Input:

```text
component = DOOR_IMPACT_BEAM
process = FORMING_THEN_HEAT_TREATMENT
```

Primary:

```text
PHT
```

---

# 42. Broad EV Platform Event

Input:

```text
new EV platform
```

Do not return:

```text
DP
TRIP
CP
FB
MART
HPF
```

all at once.

Correct output:

```text
AUTOMOTIVE_STEEL opportunity identified

component-level information required
```

Return:

```text
AUTOMOTIVE_COMPONENT_REQUIRED
```

---

# 43. New Lightweight Vehicle Platform

Possible analysis:

```text
LIGHTWEIGHTING
↓
BODY_STRUCTURE
↓
higher strength to reduce gauge
↓
AHSS opportunity
```

But family remains unknown until:

```text
component
forming
crash role
```

are identified.

---

# 44. Crash Safety Regulation Event

Do not immediately recommend MART.

Use:

```text
REGULATION
↓
CRASH_REQUIREMENT_CHANGE
↓
affected components
↓
component-specific AHSS routing
```

Possible families:

```text
DP
TRIP
CP
MART
HPF
```

depending on application.

---

# 45. Product Family Comparison

When user asks to compare families, compare only on source-supported directional criteria.

Example:

| Family | Strength | Formability / Ductility | Typical Routing Feature |
|---|---|---|---|
| BH | moderate | high | outer panel + dent resistance |
| IF HSS | moderate-high | very strong deep drawing | deep-drawn members |
| DP | high | good | strength/formability balance |
| TRIP | high | high elongation | demanding forming |
| CP | very high | bending-focused | crash + high yield ratio |
| FB | high | flangeability-focused | chassis |
| MART | ultra-high | low | intrusion-resistant structure |
| HPF | ultra-high after processing | hot forming | complex UHSS part |

Do not convert this qualitative table into guaranteed comparative numerical performance.

---

# 46. Selection vs Exclusion Matrix

## Select BH when:

```text
OUTER_PANEL
DENT_RESISTANCE
FORMABILITY
```

Avoid when:

```text
ULTRA_HIGH_CRASH_STRENGTH
```

---

## Select IF HSS when:

```text
DEEP_DRAWING
HIGH_R_VALUE
MODERATE_HIGH_STRENGTH
```

Avoid when:

```text
VERY_HIGH_STRENGTH dominates
```

---

## Select DP when:

```text
STRENGTH
+
FORMABILITY
```

must be balanced.

---

## Select TRIP when:

```text
STRENGTH
+
HIGH_ELONGATION
```

are both important.

---

## Select CP when:

```text
HIGH_YIELD_RATIO
+
BENDABILITY
+
CRASH_RESISTANCE
```

are important.

---

## Select FB when:

```text
STRETCH_FLANGEABILITY
+
HOLE_EXPANSION
```

are important.

---

## Select MART when:

```text
VERY_HIGH_STRENGTH
```

dominates and limited ductility is acceptable.

---

## Select HPF when:

```text
HOT_FORMING
+
ULTRA_HIGH_FINAL_STRENGTH
```

is required.

---

## Select PHT when:

```text
FORM_FIRST
+
POST_HEAT_TREATMENT
```

defines the production route.

---

# 47. Marketing Interpretation

The intelligence engine may transform customer signals into opportunities such as:

```text
NEW_PLATFORM
→ AHSS demand opportunity

LIGHTWEIGHTING
→ higher-strength steel upgrade opportunity

CRASH_REGULATION
→ AHSS / HPF upgrade opportunity

EV BATTERY PACK REDESIGN
→ MART / AHSS structural opportunity

OUTER_PANEL THINNING
→ BH opportunity

CHASSIS WEIGHT REDUCTION
→ FB / high-strength hot-rolled opportunity
```

These are opportunity hypotheses.

They are not guaranteed product wins.

---

# 48. Marketing Question Examples

## "고객이 차체 경량화를 추진한다"

Return:

```text
AUTOMOTIVE_STEEL opportunity
```

Do not return exact grade.

Next required data:

```text
affected body component
target strength
forming method
coating requirement
```

---

## "사이드실 충돌강성을 높인다"

Likely candidate families:

```text
CP
MART
DP
HPF
```

Need manufacturing process to narrow.

---

## "도어 외판 두께를 줄이면서 덴트성 유지"

Likely:

```text
BH
```

This is a comparatively strong family-level route.

---

## "하부 서스펜션 부품의 구멍확장성이 중요"

Likely:

```text
FB
```

---

# 49. Engineering Guardrail

This document must not be used to certify:

```text
final grade suitability
forming limit
crash performance
weldability under customer process
coating compatibility
fatigue life
joining performance
```

without detailed engineering validation.

Return:

```text
ENGINEERING_REVIEW_REQUIRED
```

where appropriate.

---

# 50. Numeric Data Rule

Do not preload all chemistry and mechanical-property tables into normal intelligence context.

Retrieve exact numeric data only when asked for:

```text
specific grade
strength comparison
chemical composition
coating availability
thickness range
width range
mechanical property
```

This file should primarily act as:

```text
FAMILY ROUTER
```

with representative grade awareness.

---

# 51. Source Notes

The source catalog uses:

```text
Guaranteed value
Commercial product
Customer trial
```

notations.

Do not rewrite:

```text
typical value
```

as:

```text
guaranteed value
```

or vice versa.

---

# 52. Dimensions Rule

Catalog production-range figures are shown only for selected grades in several sections.

The source repeatedly instructs users to contact POSCO for information on other grades.

Therefore:

```text
absence from displayed size chart
```

does not necessarily mean:

```text
not manufacturable
```

but it also must not be interpreted as:

```text
available
```

Correct state:

```text
SIZE_AVAILABILITY_CHECK_REQUIRED
```

---

# 53. Commercial Status Rule

If the source uses:

```text
▲ Customer trial
```

store:

```text
CUSTOMER_TRIAL
```

Never transform this into:

```text
COMMERCIAL_PRODUCT
```

---

# 54. Automotive Steel Retrieval Object

Recommended structured output:

```yaml
product_family: AUTOMOTIVE_STEEL

component: SIDE_SILL

requirements:
  - VERY_HIGH_STRENGTH
  - CRASH_RESISTANCE
  - BENDABILITY

family_candidates:
  - family: CP
    priority: P1
    confidence: 88

  - family: MART
    priority: P2
    confidence: 78

missing_information:
  - forming_process
  - target_strength
  - coating_requirement

grade_selection:
  status: GRADE_UNKNOWN
```

---

# 55. Grade Retrieval Object

When enough information exists:

```yaml
family: DP

candidate_grades:
  - grade: 590DP
    supply_forms:
      - CR
      - EG
      - GI
      - GA

commercial_status:
  source_required: true

selection_status:
  ENGINEERING_REVIEW_REQUIRED
```

Do not assume application suitability solely from strength class.

---

# 56. Product Family Registry

| Canonical Code | Source Family | Core Routing Signal |
|---|---|---|
| BAKE_HARDENING_STEEL | Bake Hardening | outer panel / dent resistance |
| HSLA | HSLA | high yield strength / reinforcement |
| REPHOSPHORIZED_STEEL | Rephosphorized | moderate-high strength body structure |
| IF_HSS | IF HSS | deep drawing + strength |
| DP | Dual Phase | strength + formability |
| TRIP | Transformation Induced Plasticity | strength + high elongation |
| CP | Complex Phase | high yield ratio + bending + crash |
| FB | Ferrite-Bainite | hole expansion / chassis |
| MART | Martensite | ultra-high tensile strength |
| HPF | Hot Press Forming | hot stamping + UHSS |
| PHT | Post Heat Treatment | form then heat treat |

---

# 57. Representative Grade Registry

## BH

```text
340BH
180YB
210YB
240YB
270YB
```

## HSLA

```text
440C
590C

220YC
260YC
300YC
340YC
```

## Rephosphorized

```text
340R
390R
440R
310R
370R
400R
```

## IF HSS

```text
340E
390E
440E
340ES
180YE
220YE
260YE
```

## DP

```text
490DP
590DP
590DH
780DP
780DH
980DP-M
980DP-EL
980DP-H
```

## TRIP

```text
590TR
780TR
980TR
1180TR
```

## CP

```text
780CP
980CP
1180CP
```

## FB

```text
440FB
540FB
590FB
780FB
```

## MART

```text
1300M
1500M
1700M
```

## HPF

```text
550HPF
1500HPF
1800HPF
2000HPF
```

## PHT

```text
STAB
AUTOBEAM
```

This registry is for retrieval.

It is not an approval list.

---

# 58. Source-Supported Application Examples

Examples explicitly shown or described in the catalog include:

```text
BH
→ Hood
→ Door outer

HSLA
→ Center member
→ Front / rear suspension module
→ Side sill

Rephosphorized
→ Cowl
→ Wheel apron
→ Front side member

IF HSS
→ Rear floor side member
→ Reinforced A-pillar outer
→ Rear floor

DP
→ Door outer
→ Seat rail
→ Suspension
→ Structural reinforcement
→ Crashworthiness reinforcement

CP
→ Sill side panel
→ Underbody reinforcement

FB
→ Lower arm
→ Wheel disc
→ Suspension

MART
→ Bumper beam
→ Sill side member
→ Inner cross member
→ Side frame
→ Battery pack

PHT
→ Door impact beam
→ Stabilizer
```

Do not convert examples into universal grade assignments.

---

# 59. Evidence Strength Hierarchy

Use:

```text
DIRECT_APPLICATION_EXAMPLE
>
EXPLICIT_PRODUCT_DESCRIPTION
>
MATERIAL_PROPERTY_MATCH
>
GENERAL_FAMILY_INFERENCE
```

Example:

```text
Lower arm
→ FB
```

has strong evidence because the catalog explicitly shows lower-arm application.

Example:

```text
new EV body platform
→ MART
```

has weak evidence unless specific component requirements are known.

---

# 60. Unknown Handling

Supported statuses:

```text
AUTOMOTIVE_FAMILY_UNKNOWN

GRADE_UNKNOWN

COMMERCIAL_STATUS_UNKNOWN

COATING_AVAILABILITY_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

CUSTOMER_SPECIFICATION_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

Use them freely.

Do not force every automotive opportunity into one grade.

---

# 61. Search / Retrieval Rules

Default sequence:

```text
automotive/index.md
↓
automotive-steel.md
↓
family section
↓
grade information only if required
```

Do not open the source PDF unless:

```text
exact numeric property
exact chemistry
size range
coating availability
commercial status
customer standard equivalence
```

must be verified.

---

# 62. Daily Intelligence Mode

For automated market intelligence:

Do not select exact grade.

Preferred output:

```text
Customer:
New EV platform

Component:
Body structural member

Material Requirement:
High strength + forming

POSCO Product Family:
Automotive Steel

Likely Family:
DP / CP

Next Action:
Identify target body component and required strength class.
```

---

# 63. Marketing Mode

Marketing output may include:

```text
family
representative applications
product-value hypothesis
customer questions
technical information required
```

Example:

```text
Potential family:
FB

Reason:
Customer is redesigning suspension lower arms and emphasizing stretch-flange performance.

Next question:
What tensile strength and hole-expansion target is required?
```

---

# 64. Engineering Mode

Engineering analysis may proceed to:

```text
grade
supply form
mechanical properties
chemistry
thickness
width
customer standard
commercial status
```

and may retrieve the original catalog section.

---

# 65. Questions to Ask Before Grade Selection

For body sheet:

```text
Which exact component?
What is the target tensile strength?
What is the target yield strength?
What elongation is required?
Is deep drawing required?
Is hole expansion required?
Is bending dominant?
Does the part absorb crash energy or prevent intrusion?
What coating is required?
What thickness?
What joining process?
```

For HPF/PHT:

```text
What thermal process is used?
Is the part formed hot or heat-treated after forming?
Is Al-Si coating required?
What final tensile-strength level is required?
```

---

# 66. AI Prompt Guardrails

Product-matching prompts using this file must include:

```text
Use only product families and grades supported by supplied POSCO knowledge.

Do not select a grade from strength alone.

Separate substrate family from coating.

Treat commercial products and customer-trial products differently.

Application examples are evidence, not universal prescriptions.

If forming process or component function is missing, stop at family level.

Return GRADE_UNKNOWN when exact grade selection is unsupported.

Use ENGINEERING_REVIEW_REQUIRED for safety-critical final selection.
```

---

# 67. Family Selection Algorithm

```pseudo
function select_automotive_family(context):

    component = context.component
    requirements = context.requirements
    process = context.forming_process

    if component in OUTER_PANEL
       and DENT_RESISTANCE:
        return BH

    if DEEP_DRAWABILITY
       and HIGH_STRENGTH:
        return IF_HSS

    if HOLE_EXPANSION
       or STRETCH_FLANGEABILITY:
        return FB

    if HOT_STAMPING:
        return HPF

    if POST_HEAT_TREATMENT:
        return PHT

    if VERY_HIGH_STRENGTH
       and very_low_ductility_acceptable:
        return MART

    if HIGH_YIELD_RATIO
       and BENDABILITY
       and CRASH_RESISTANCE:
        return CP

    if HIGH_STRENGTH
       and HIGH_ELONGATION:
        return TRIP

    if HIGH_STRENGTH
       and FORMABILITY:
        return DP

    if HIGH_YIELD_STRENGTH
       and reinforcement_component:
        return HSLA

    return AUTOMOTIVE_FAMILY_UNKNOWN
```

This is directional routing logic, not an engineering design algorithm.

---

# 68. Final Knowledge Chain

```text
Customer Signal
↓
Automotive Event
↓
Vehicle Application
↓
Component
↓
Functional Requirement
↓
Automotive Steel
↓
BH / HSLA / R / IF HSS / DP / TRIP / CP / FB / MART / HPF / PHT
↓
Grade Family
↓
Supply Form
↓
Exact Grade
↓
Engineering Validation
↓
Marketing Opportunity
```

---

# 69. Final Rule

This file must optimize for:

```text
CORRECT FAMILY
+
CORRECT APPLICATION LOGIC
+
CORRECT SOURCE STATUS
+
MINIMAL PRODUCT RETRIEVAL
```

not:

```text
MOST ADVANCED STEEL
```

or:

```text
HIGHEST STRENGTH GRADE
```

The best candidate is the one whose:

```text
strength
forming behavior
component function
manufacturing route
coating requirement
commercial status
```

best match the customer's actual application.

The preferred behavior is:

```text
COMPONENT FIRST
↓
PROPERTY SECOND
↓
FAMILY THIRD
↓
GRADE LAST
```

not:

```text
GRADE FIRST
↓
JUSTIFY LATER
```
