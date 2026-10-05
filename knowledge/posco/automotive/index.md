---
knowledge_domain: POSCO_AUTOMOTIVE
document_type: PRODUCT_ROUTER
industry: AUTOMOTIVE

parent_router:
  - ../index.md

taxonomy_dependencies:
  - ../../taxonomy/industries.md
  - ../../taxonomy/applications.md
  - ../../taxonomy/materials.md

local_product_files:
  - automotive-steel.md
  - atos.md
  - hyper-no.md

cross_domain_routes:
  - ../coated/galvanized.md
  - ../coated/electro-galvanized.md
  - ../coated/posmac-1.5.md
  - ../carbon/high-carbon.md
  - ../carbon/wire-rod.md
  - ../stainless/stainless.md
  - ../future/low-carbon-steel.md

knowledge_status: VERIFIED
---

# POSCO Automotive Product Knowledge Router

## 1. Purpose

This file is the automotive-specific routing layer of the POSCO Product Brain.

It determines which POSCO product knowledge file should be loaded when an industrial event, company strategy, application, or user question relates to the automotive industry.

This file does NOT contain complete product specifications.

Its main task is:

```text
AUTOMOTIVE SIGNAL
↓
VEHICLE SYSTEM
↓
APPLICATION
↓
COMPONENT
↓
REQUIRED PERFORMANCE
↓
MATERIAL REQUIREMENTS
↓
POSCO PRODUCT FAMILY
↓
1~3 PRODUCT KNOWLEDGE FILES
```

The default goal is:

```text
LOAD THE SMALLEST
RELEVANT PRODUCT CONTEXT
```

not:

```text
LOAD ALL AUTOMOTIVE KNOWLEDGE
```

---

# 2. Required Upstream Context

Before using this router, the system should normally know at least:

```text
industry
event
application
```

Preferred context:

```text
industry
event
strategy
application
component
operating environment
required performance
```

Example:

```text
Industry:
AUTOMOTIVE

Event:
CAPACITY_EXPANSION

Strategy:
ELECTRIFICATION

Application:
EV_MOTOR

Component:
MOTOR_CORE
```

This is sufficient to route directly to:

```text
hyper-no.md
```

---

# 3. Automotive Product Knowledge Architecture

Automotive-related POSCO knowledge is divided into seven major material routes.

```text
1. VEHICLE BODY / CRASH / CHASSIS
   → AUTOMOTIVE_STEEL

2. COMMERCIAL VEHICLE / HEAVY STRUCTURAL FRAME
   → ATOS

3. EV TRACTION MOTOR
   → HYPER_NO

4. AUTOMOTIVE CORROSION / SURFACE COATING
   → GALVANIZED / ELECTRO-GALVANIZED / POSMAC

5. EXHAUST / HEAT / CORROSION COMPONENTS
   → STAINLESS_STEEL

6. MECHANICAL AUTOMOTIVE COMPONENTS
   → HIGH_CARBON_STEEL / WIRE_ROD

7. LOW-CARBON PROCUREMENT REQUIREMENT
   → TECHNICAL PRODUCT
   +
   LOW_CARBON_STEEL ATTRIBUTE
```

---

# 4. Main Local Product Files

## 4.1 Automotive Steel

Canonical product family:

```text
AUTOMOTIVE_STEEL
```

Knowledge file:

```text
./automotive-steel.md
```

Use for:

```text
BODY_IN_WHITE
OUTER_PANEL
INNER_PANEL
STRUCTURAL_MEMBER
CRASH_MEMBER
CHASSIS
SUSPENSION
WHEEL
BATTERY_PACK_STRUCTURE
```

Internal product families may include:

```text
BAKE_HARDENING_STEEL
HSLA
REPHOSPHORIZED_STEEL
IF_HSS
DP
TRIP
CP
FB
MART
HPF
PHT
```

The router should first select:

```text
AUTOMOTIVE_STEEL
```

and allow `automotive-steel.md` to perform detailed family or grade routing.

---

# 4.2 ATOS

Canonical product family:

```text
ATOS
```

Knowledge file:

```text
./atos.md
```

Use primarily for:

```text
TRUCK_FRAME
TRAILER_FRAME
COMMERCIAL_VEHICLE_FRAME
HEAVY_AUTOMOTIVE_STRUCTURE
BOOM_ARM
```

Primary material requirements:

```text
HIGH_STRENGTH
COLD_FORMABILITY
WELDABILITY
WEIGHT_REDUCTION
```

Do NOT route ordinary passenger-car body panels to ATOS merely because high strength is required.

---

# 4.3 Hyper NO

Canonical product family:

```text
HYPER_NO
```

Knowledge file:

```text
./hyper-no.md
```

Material category:

```text
NON_ORIENTED_ELECTRICAL_STEEL
```

Use for:

```text
EV_TRACTION_MOTOR
MOTOR_CORE
STATOR_CORE
ROTOR_CORE
```

Primary requirements:

```text
LOW_CORE_LOSS
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_STRENGTH
THIN_GAUGE
ELECTRICAL_INSULATION
```

Do not route generic EV news to Hyper NO unless motor-related demand is supported.

---

# 5. Automotive Application Hierarchy

Use this conceptual hierarchy.

```text
AUTOMOTIVE
│
├── VEHICLE_BODY
│   ├── OUTER_PANEL
│   ├── INNER_PANEL
│   ├── BODY_IN_WHITE
│   ├── STRUCTURAL_MEMBER
│   └── CRASH_MEMBER
│
├── CHASSIS
│   ├── SUSPENSION
│   ├── CONTROL_ARM
│   ├── SUBFRAME
│   └── WHEEL
│
├── EV_DRIVETRAIN
│   └── EV_MOTOR
│       ├── MOTOR_CORE
│       ├── STATOR_CORE
│       └── ROTOR_CORE
│
├── EV_BATTERY_SYSTEM
│   ├── BATTERY_PACK_STRUCTURE
│   ├── BATTERY_TRAY
│   └── BATTERY_ENCLOSURE
│
├── COMMERCIAL_VEHICLE
│   ├── TRUCK_FRAME
│   └── TRAILER_FRAME
│
├── POWERTRAIN
│   ├── CLUTCH
│   ├── GEAR
│   └── MECHANICAL_PART
│
├── EXHAUST_SYSTEM
│
└── AUXILIARY_COMPONENTS
    ├── SEAT_RECLINER
    ├── SAFETY_BELT
    ├── HOSE_CLIP
    ├── SPRING
    └── BEARING
```

---

# 6. Vehicle Body Router

## 6.1 BODY_IN_WHITE

Primary file:

```text
./automotive-steel.md
```

Typical requirements:

```text
HIGH_STRENGTH
FORMABILITY
WEIGHT_REDUCTION
CRASH_RESISTANCE
WELDABILITY
```

Potential internal families:

```text
IF_HSS
DP
TRIP
CP
MART
HSLA
```

Do not load every family independently.

They are sub-routes inside:

```text
automotive-steel.md
```

---

# 6.2 OUTER_PANEL

Examples:

```text
DOOR_OUTER
HOOD
FENDER
ROOF_OUTER
```

Important requirements:

```text
SURFACE_QUALITY
FORMABILITY
DENT_RESISTANCE
PAINTABILITY
CORROSION_RESISTANCE
```

Primary route:

```text
./automotive-steel.md
```

Possible secondary coating route:

```text
../coated/galvanized.md
```

or:

```text
../coated/electro-galvanized.md
```

Only load coating knowledge if:

```text
corrosion
surface
painting
coating
```

is relevant to the analysis.

---

# 6.3 HIGH_FORMABILITY_MEMBER

Example components:

```text
REAR_FLOOR_SIDE_MEMBER
A_PILLAR_REINFORCEMENT
REAR_FLOOR
FLOOR_SIDE_REINFORCEMENT
```

Primary:

```text
./automotive-steel.md
```

Likely internal family:

```text
IF_HSS
```

Do not assume exact grade from component name alone.

---

# 6.4 STRUCTURAL_MEMBER

Examples:

```text
SILL_SIDE_MEMBER
ROOF_REINFORCEMENT
SEAT_RAIL
FRONT_SIDE_MEMBER
CENTER_MEMBER
```

Primary:

```text
./automotive-steel.md
```

Possible families:

```text
HSLA
DP
TRIP
CP
MART
```

Selection depends on:

```text
strength requirement
forming complexity
crash function
thickness
coating requirement
```

---

# 6.5 CRASH_MEMBER

Examples:

```text
BUMPER_BEAM
SIDE_SILL
CRASH_BOX
UNDERBODY_REINFORCEMENT
FRONT_SIDE_MEMBER
```

Priority requirements:

```text
VERY_HIGH_STRENGTH
CRASH_RESISTANCE
ENERGY_ABSORPTION
WEIGHT_REDUCTION
```

Primary:

```text
./automotive-steel.md
```

Likely family candidates:

```text
DP
TRIP
CP
MART
```

Do NOT route directly to a specific strength grade at index level.

---

# 7. AHSS Internal Routing

This router may identify a preferred AHSS family, but the detailed decision belongs to:

```text
automotive-steel.md
```

---

# 7.1 DP

Canonical code:

```text
AUTOMOTIVE_DP
```

Route when requirements emphasize:

```text
HIGH_STRENGTH
GOOD_FORMABILITY
LOW_YIELD_RATIO
BAKE_HARDENABILITY
```

Representative strength families from approved source include:

```text
490
590
780
980 MPa class
```

Primary file:

```text
./automotive-steel.md
```

---

# 7.2 TRIP

Canonical code:

```text
AUTOMOTIVE_TRIP
```

Route when requirements emphasize:

```text
HIGH_STRENGTH
HIGH_ELONGATION
FORMABILITY
ENERGY_ABSORPTION
```

Representative families include:

```text
590TR
780TR
980TR
1180TR
```

Primary file:

```text
./automotive-steel.md
```

---

# 7.3 CP

Canonical code:

```text
AUTOMOTIVE_CP
```

Route when requirements emphasize:

```text
HIGH_YIELD_STRENGTH
HIGH_TENSILE_STRENGTH
BENDABILITY
CRASH_RESISTANCE
```

Primary file:

```text
./automotive-steel.md
```

---

# 7.4 FB

Canonical code:

```text
AUTOMOTIVE_FB
```

Strong routing signals:

```text
SUSPENSION
LOWER_ARM
WHEEL_DISC
CHASSIS
```

Primary requirements:

```text
HIGH_STRENGTH
HOLE_EXPANSION
FORMABILITY
FATIGUE_RESISTANCE
```

Primary file:

```text
./automotive-steel.md
```

---

# 7.5 MART

Canonical code:

```text
AUTOMOTIVE_MART
```

Route when requirement is dominated by:

```text
VERY_HIGH_STRENGTH
CRASH_PROTECTION
STRUCTURAL_REINFORCEMENT
```

Possible applications:

```text
BUMPER_BEAM
SILL_SIDE_MEMBER
CROSS_MEMBER
SIDE_FRAME
BATTERY_PACK_STRUCTURE
```

Primary file:

```text
./automotive-steel.md
```

High strength does not automatically mean MART.

Formability requirements must also be considered.

---

# 8. Chassis Router

## 8.1 Passenger Vehicle Chassis

Applications:

```text
SUSPENSION
CONTROL_ARM
LOWER_ARM
WHEEL_RIM
WHEEL_DISC
```

Primary:

```text
./automotive-steel.md
```

Strong family candidate:

```text
FB
```

Alternative family depends on engineering requirement.

---

# 8.2 Commercial Vehicle Structure

Applications:

```text
TRUCK_FRAME
TRAILER_FRAME
HEAVY_FRAME
```

Primary:

```text
./atos.md
```

Requirements:

```text
HIGH_STRENGTH
WEIGHT_REDUCTION
COLD_FORMABILITY
WELDABILITY
```

---

# 8.3 Heavy Automotive Structural Member

If component is:

```text
truck / trailer / heavy commercial structure
```

route:

```text
ATOS
```

If component is:

```text
passenger vehicle body or crash structure
```

route:

```text
AUTOMOTIVE_STEEL
```

This distinction is mandatory.

---

# 9. EV Motor Router

## 9.1 EV_TRACTION_MOTOR

Primary:

```text
./hyper-no.md
```

Components:

```text
MOTOR_CORE
STATOR_CORE
ROTOR_CORE
```

Requirements:

```text
LOW_CORE_LOSS
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_STRENGTH
```

---

# 9.2 Hyper NO Series Routing

Detailed series selection belongs to:

```text
hyper-no.md
```

This index may use the following directional mapping only.

```text
LOWER_CORE_LOSS
+
HIGHER_STRENGTH
→ NEW_PNX candidate

HIGH_MECHANICAL_STRENGTH
→ PNX_FY candidate

LOW_CORE_LOSS
+
HIGH_STRENGTH
→ PNX candidate

HIGH_FREQUENCY_CORE_LOSS_PRIORITY
→ PNF candidate
```

Do not select exact grades here.

---

# 9.3 EV News Negative Rule

The following terms alone are insufficient for Hyper NO routing:

```text
EV FACTORY
EV SALES
EV BATTERY
CHARGING INFRASTRUCTURE
BATTERY MATERIAL
```

Hyper NO requires evidence related to:

```text
MOTOR
TRACTION MOTOR
MOTOR CORE
STATOR
ROTOR
ELECTRICAL STEEL
```

or a defensible motor-production implication.

---

# 10. EV Battery Structure Router

Applications:

```text
BATTERY_PACK_STRUCTURE
BATTERY_TRAY
BATTERY_ENCLOSURE
CRASH_PROTECTION_MEMBER
```

Possible requirements:

```text
HIGH_STRENGTH
CRASH_RESISTANCE
WEIGHT_REDUCTION
FORMABILITY
CORROSION_RESISTANCE
```

Primary technical route:

```text
./automotive-steel.md
```

Possible coating route:

```text
../coated/galvanized.md
```

Possible special corrosion/surface route:

```text
../coated/posmac-1.5.md
```

Only load coating documents when coating-related requirements exist.

Do not infer a specific battery-case product solely from:

```text
battery plant
```

---

# 11. Automotive Coating Router

Coating must be treated separately from substrate strength.

Concept:

```text
BASE STEEL REQUIREMENT
+
COATING REQUIREMENT
```

not:

```text
COATING = COMPLETE MATERIAL SOLUTION
```

---

# 11.1 GI / GA

Primary file:

```text
../coated/galvanized.md
```

Use when:

```text
CORROSION_RESISTANCE
PAINTABILITY
WELDABILITY
AUTOMOTIVE_PANEL
```

is important.

GA is particularly relevant when:

```text
WELDABILITY
+
PAINTABILITY
```

are emphasized.

---

# 11.2 Electro-Galvanized

Primary file:

```text
../coated/electro-galvanized.md
```

Use when requirements include:

```text
SURFACE_QUALITY
PAINTABILITY
CORROSION_RESISTANCE
FORMABILITY
```

and EG is technically relevant.

---

# 11.3 PosMAC 1.5

Primary file:

```text
../coated/posmac-1.5.md
```

Use when an automotive application requires a combination of:

```text
CORROSION_RESISTANCE
SURFACE_QUALITY
WELDABILITY
FORMABILITY
```

Do not substitute PosMAC 1.5 automatically for GI/GA/EG.

Product and process requirements must be compared.

---

# 12. Exhaust System Router

Application:

```text
AUTOMOTIVE_EXHAUST
```

Primary:

```text
../stainless/stainless.md
```

Components may include:

```text
EXHAUST_MANIFOLD
FRONT_PIPE
CENTER_PIPE
CATALYTIC_CONVERTER
MUFFLER
FLEXIBLE_PIPE
```

Requirements:

```text
HEAT_RESISTANCE
HIGH_TEMPERATURE_STRENGTH
OXIDATION_RESISTANCE
CORROSION_RESISTANCE
FORMABILITY
WELDABILITY
```

Do not select stainless grade in this router.

---

# 13. Mechanical Automotive Component Router

Some automotive opportunities are not sheet-body applications.

---

# 13.1 Clutch

Primary:

```text
../carbon/high-carbon.md
```

Application keys:

```text
MANUAL_CLUTCH
AUTOMATIC_CLUTCH
```

Typical requirements:

```text
HIGH_STRENGTH
HIGH_HARDNESS
WEAR_RESISTANCE
HEAT_TREATABILITY
```

---

# 13.2 Seat Recliner

Primary:

```text
../carbon/high-carbon.md
```

Requirements:

```text
HIGH_STRENGTH
HARDNESS
DIMENSIONAL_CONTROL
```

---

# 13.3 Safety Belt Hardware

Primary:

```text
../carbon/high-carbon.md
```

Do not confuse with:

```text
seat-belt body reinforcement
```

which may route to automotive sheet steel.

---

# 13.4 Automotive Hose Clip

Primary:

```text
../carbon/high-carbon.md
```

---

# 13.5 Tire Reinforcement

Primary:

```text
../carbon/wire-rod.md
```

Preferred internal family:

```text
TIRE_CORD_WIRE_ROD
```

Requirements:

```text
VERY_HIGH_STRENGTH
FINE_DRAWABILITY
FATIGUE_RESISTANCE
CLEANLINESS
```

---

# 13.6 Automotive Spring

Primary:

```text
../carbon/wire-rod.md
```

Internal candidate:

```text
SPRING_STEEL_WIRE_ROD
```

---

# 13.7 Bearing

Primary:

```text
../carbon/wire-rod.md
```

Internal candidate:

```text
BEARING_STEEL_WIRE_ROD
```

Requirements:

```text
WEAR_RESISTANCE
FATIGUE_RESISTANCE
CLEANLINESS
HOMOGENEOUS_MICROSTRUCTURE
```

---

# 14. Vehicle-Level Routing Table

| Vehicle Area | Primary Product Route | Optional Secondary Route |
|---|---|---|
| Outer panel | `automotive-steel.md` | `galvanized.md`, `electro-galvanized.md` |
| Body-in-white | `automotive-steel.md` | coated product if relevant |
| Crash structure | `automotive-steel.md` | none by default |
| Passenger chassis | `automotive-steel.md` | none by default |
| Truck/trailer frame | `atos.md` | none by default |
| EV traction motor | `hyper-no.md` | none |
| Battery pack structure | `automotive-steel.md` | coated product if relevant |
| Exhaust system | `stainless.md` | none |
| Clutch/recliner/hose clip | `high-carbon.md` | none |
| Tire reinforcement | `wire-rod.md` | none |
| Bearing/spring | `wire-rod.md` | `high-carbon.md` only if application requires |

---

# 15. Component Router

## DOOR_OUTER

Primary:

```text
automotive-steel.md
```

Possible coating:

```text
galvanized.md
```

Strong considerations:

```text
FORMABILITY
SURFACE_QUALITY
DENT_RESISTANCE
CORROSION_RESISTANCE
```

---

## SEAT_RAIL

Primary:

```text
automotive-steel.md
```

Requirements:

```text
HIGH_STRENGTH
STRUCTURAL_STABILITY
FORMABILITY
```

---

## SUSPENSION

Primary:

```text
automotive-steel.md
```

Prefer hot-rolled / FB-related investigation where supported.

---

## SIDE_SILL

Primary:

```text
automotive-steel.md
```

Requirements:

```text
CRASH_RESISTANCE
VERY_HIGH_STRENGTH
WEIGHT_REDUCTION
```

---

## FRONT_SIDE_MEMBER

Primary:

```text
automotive-steel.md
```

Requirements:

```text
HIGH_STRENGTH
CRASH_RESISTANCE
FORMABILITY
```

---

## MOTOR_CORE

Primary:

```text
hyper-no.md
```

---

## TRUCK_FRAME

Primary:

```text
atos.md
```

---

## EXHAUST_MANIFOLD

Primary:

```text
../stainless/stainless.md
```

---

# 16. Strength Requirement Router

Strength alone cannot select a product.

Use component context.

```text
HIGH_STRENGTH
+
OUTER / INNER BODY
→ AUTOMOTIVE_STEEL
```

```text
VERY_HIGH_STRENGTH
+
CRASH MEMBER
→ AUTOMOTIVE_STEEL / AHSS
```

```text
HIGH_STRENGTH
+
TRUCK FRAME
→ ATOS
```

```text
HIGH_STRENGTH
+
EV MOTOR CORE
→ HYPER_NO
```

The same material-property word may therefore lead to different products.

---

# 17. Formability Router

```text
HIGH_FORMABILITY
+
BODY MEMBER
→ IF_HSS / AUTOMOTIVE_STEEL
```

```text
HIGH_STRENGTH
+
GOOD_FORMABILITY
→ DP / TRIP candidate
```

```text
HIGH_STRENGTH
+
BENDABILITY
+
CRASH MEMBER
→ CP candidate
```

Detailed family selection remains inside:

```text
automotive-steel.md
```

---

# 18. Crashworthiness Router

Crash-performance related evidence should first identify component function.

Possible families:

```text
DP
TRIP
CP
MART
```

Do not assume:

```text
highest strength = best crash material
```

The correct product depends on:

```text
energy absorption
intrusion resistance
forming complexity
joint design
component geometry
```

Therefore:

```text
ENGINEERING_REVIEW_REQUIRED
```

may be necessary for exact grade recommendation.

---

# 19. Coating and Substrate Dual Routing

A component may require two product knowledge files.

Example:

```text
Door outer
```

could require:

```text
automotive-steel.md
+
galvanized.md
```

because the intelligence chain contains:

```text
SUBSTRATE REQUIREMENT
+
COATING REQUIREMENT
```

Maximum files:

```text
2
```

for normal automotive component analysis.

---

# 20. EV Factory Decomposition Rule

A large EV factory event must not be assigned one POSCO product.

Decompose:

```text
EV FACTORY
│
├── Vehicle Body
│   → AUTOMOTIVE_STEEL
│
├── Chassis
│   → AUTOMOTIVE_STEEL
│
├── Motor Production
│   → HYPER_NO
│
├── Battery Pack Structure
│   → AUTOMOTIVE_STEEL
│
└── Surface / Corrosion
    → COATED PRODUCTS
```

Only create routes supported by project scope or evidence.

---

# 21. Factory vs Vehicle Material Rule

If the news only says:

```text
Automaker builds a new EV factory
```

do NOT immediately load:

```text
automotive-steel.md
hyper-no.md
galvanized.md
high-carbon.md
wire-rod.md
```

Instead:

```text
APPLICATION_SCOPE = UNKNOWN_OR_BROAD
```

Generate potential opportunity areas at high level.

Detailed product retrieval should occur only after:

```text
production scope
component scope
technology scope
```

is identified.

---

# 22. Motor Plant Exception

If source explicitly says:

```text
EV MOTOR PLANT
TRACTION MOTOR CAPACITY
E-MOTOR PRODUCTION
```

route directly:

```text
hyper-no.md
```

This is a high-confidence product-family route.

---

# 23. Chassis Plant Exception

If source explicitly relates to:

```text
CHASSIS
SUSPENSION
CONTROL ARM
WHEEL
```

route:

```text
automotive-steel.md
```

with chassis / FB context.

---

# 24. Commercial Vehicle Exception

If source relates to:

```text
TRUCK
TRAILER
COMMERCIAL VEHICLE FRAME
```

and structural high-strength steel:

route:

```text
atos.md
```

Do not default to passenger-vehicle AHSS.

---

# 25. Coating Trigger Terms

Load coated-product knowledge only if source or inferred material requirement contains:

```text
CORROSION
COATING
GALVANIZED
SURFACE
PAINTING
OUTDOOR
SALT
WELDING + COATING
```

or the product context requires a coated variant.

Do not load coating files merely because automotive steel can be galvanized.

---

# 26. High Carbon Trigger Terms

Route to:

```text
../carbon/high-carbon.md
```

when context contains:

```text
CLUTCH
RECLINER
SAFETY_BELT_BUCKLE
HOSE_CLIP
CHAIN
HIGH_HARDNESS_COMPONENT
HEAT_TREATED_COMPONENT
```

---

# 27. Wire Rod Trigger Terms

Route to:

```text
../carbon/wire-rod.md
```

when context contains:

```text
TIRE_CORD
BEAD_WIRE
SPRING
BEARING
COLD_HEADING
FASTENER
HIGH_STRENGTH_WIRE
```

---

# 28. Stainless Trigger Terms

Route to:

```text
../stainless/stainless.md
```

when context contains:

```text
EXHAUST
MUFFLER
CATALYTIC_CONVERTER
EXHAUST_MANIFOLD
HIGH_TEMPERATURE_CORROSION
```

Do not route generic vehicle corrosion to stainless.

---

# 29. Automotive Low-Carbon Route

When a customer signal includes:

```text
green steel
low carbon steel
Scope 3
vehicle carbon footprint
CBAM
embodied carbon
low-carbon material procurement
```

first identify the technical product.

Example:

```text
Body panel
→ automotive-steel.md
```

Then additionally load:

```text
../future/low-carbon-steel.md
```

Required logic:

```text
TECHNICAL FIT
↓
LOW-CARBON AVAILABILITY CHECK
```

Never reverse this sequence.

---

# 30. Product Family Priority

Use:

```text
P1 = direct component/product relationship
P2 = strong technical alternative
P3 = adjacent possible solution
```

Normal retrieval:

```text
P1 only
```

Comparison request:

```text
P1 + P2
```

Do not load P3 unless needed.

---

# 31. Routing Score

Recommended score:

```text
Application Match       25%
Component Match         25%
Material Requirement    20%
Performance Match       15%
Manufacturing Match     10%
Evidence Completeness    5%
```

Interpretation:

```text
90-100
DIRECT_ROUTE

80-89
STRONG_ROUTE

70-79
POSSIBLE_ROUTE

60-69
WEAK_ROUTE

<60
DO_NOT_LOAD
```

---

# 32. Minimum Route Thresholds

For product-family MD loading:

```text
route_score >= 70
```

For exact grade evaluation:

```text
route_score >= 80
+
detailed product evidence
+
critical operating conditions known
```

For engineering-critical components:

```text
ENGINEERING_REVIEW_REQUIRED
```

may still apply.

---

# 33. Automotive Router Output

Recommended output:

```yaml
industry: AUTOMOTIVE

application: EV_MOTOR

component:
  - MOTOR_CORE

performance_goals:
  - HIGH_EFFICIENCY
  - HIGH_SPEED

material_requirements:
  - LOW_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_STRENGTH

product_candidates:
  - product_family: HYPER_NO
    knowledge_file: ./hyper-no.md
    priority: P1
    route_score: 96

files_to_load:
  - ./hyper-no.md

missing_information: []

confidence: 94
```

---

# 34. Body Structure Output Example

```yaml
industry: AUTOMOTIVE

application: VEHICLE_BODY

component:
  - SIDE_SILL

performance_goals:
  - CRASH_SAFETY
  - WEIGHT_REDUCTION

material_requirements:
  - VERY_HIGH_STRENGTH
  - CRASH_RESISTANCE
  - FORMABILITY

product_candidates:
  - product_family: AUTOMOTIVE_STEEL
    internal_family_candidates:
      - DP
      - CP
      - MART
    knowledge_file: ./automotive-steel.md
    priority: P1

files_to_load:
  - ./automotive-steel.md

missing_information:
  - target_strength
  - forming_complexity
  - coating_requirement
```

---

# 35. Door Outer Output Example

```yaml
industry: AUTOMOTIVE

application: VEHICLE_BODY

component:
  - DOOR_OUTER

requirements:
  - FORMABILITY
  - SURFACE_QUALITY
  - CORROSION_RESISTANCE
  - PAINTABILITY

product_candidates:
  - product_family: AUTOMOTIVE_STEEL
    knowledge_file: ./automotive-steel.md
    priority: P1

  - product_family: GALVANIZED_STEEL
    knowledge_file: ../coated/galvanized.md
    priority: P2

files_to_load:
  - ./automotive-steel.md
  - ../coated/galvanized.md
```

---

# 36. Truck Frame Output Example

```yaml
industry: AUTOMOTIVE

application: COMMERCIAL_VEHICLE

component:
  - TRUCK_FRAME

requirements:
  - HIGH_STRENGTH
  - COLD_FORMABILITY
  - WELDABILITY
  - WEIGHT_REDUCTION

product_candidates:
  - product_family: ATOS
    knowledge_file: ./atos.md
    priority: P1
    route_score: 95

files_to_load:
  - ./atos.md
```

---

# 37. Automotive Exhaust Output Example

```yaml
industry: AUTOMOTIVE

application: AUTOMOTIVE_EXHAUST

component:
  - EXHAUST_MANIFOLD

environment:
  - HIGH_TEMPERATURE

requirements:
  - HEAT_RESISTANCE
  - HIGH_TEMPERATURE_STRENGTH
  - OXIDATION_RESISTANCE

product_candidates:
  - product_family: STAINLESS_STEEL
    knowledge_file: ../stainless/stainless.md
    priority: P1

files_to_load:
  - ../stainless/stainless.md
```

---

# 38. Tire Output Example

```yaml
industry: AUTOMOTIVE

application: TIRE

component:
  - TIRE_REINFORCEMENT

requirements:
  - VERY_HIGH_STRENGTH
  - FATIGUE_RESISTANCE
  - FINE_DRAWABILITY
  - CLEANLINESS

product_candidates:
  - product_family: WIRE_ROD
    internal_family: TIRE_CORD_WIRE_ROD
    knowledge_file: ../carbon/wire-rod.md
    priority: P1

files_to_load:
  - ../carbon/wire-rod.md
```

---

# 39. Negative Routing Rules

## EV ≠ Hyper NO automatically

Do not route:

```text
EV SALES
EV BATTERY
EV CHARGER
EV SUBSIDY
```

directly to Hyper NO.

---

## Battery ≠ Automotive Steel automatically

A:

```text
BATTERY CELL FACTORY
```

does not prove:

```text
BATTERY PACK STRUCTURAL STEEL
```

---

## High Strength ≠ MART automatically

Component function and forming requirement must be considered.

---

## High Strength ≠ ATOS automatically

ATOS is primarily a structural route.

Passenger-car body high-strength needs normally route to:

```text
AUTOMOTIVE_STEEL
```

---

## Corrosion ≠ PosMAC automatically

Automotive panel corrosion may route to:

```text
GI / GA / EG
```

depending on process requirements.

---

## Motor ≠ Hyper NO automatically

Confirm that:

```text
electric traction motor
```

rather than:

```text
engine starter
industrial motor
generic motor
```

is being discussed.

---

# 40. Product Grade Boundary

This router must NOT make final grade decisions.

Allowed:

```text
AUTOMOTIVE_STEEL
→ DP candidate
```

Allowed:

```text
HYPER_NO
→ PNX-FY candidate
```

Not allowed at router stage:

```text
Use 980DP-H.
```

or:

```text
Use 20PNX1250FY.
```

Grade selection belongs inside the detailed product MD.

---

# 41. Supply Form Awareness

Automotive steel may exist in different supply/coating forms.

Examples include:

```text
CR
HR / PO
EG
GI
GA
```

Product-family and coating selection must therefore remain separate decisions.

Do not assume every strength grade exists in every supply form.

Detailed availability must be checked in:

```text
automotive-steel.md
```

and the relevant coating file.

---

# 42. Product Availability Rule

The source catalogs may contain:

```text
COMMERCIAL_PRODUCT
CUSTOMER_TRIAL
PILOT_PRODUCT
```

These states must not be treated as equivalent.

Product-specific MD should preserve:

```text
commercial_status
```

where the source provides it.

---

# 43. Hyper NO Availability Rule

Hyper NO source documentation may include:

```text
pilot development
commercial production
```

grades within the same product tables.

Do not interpret appearance in a catalog as proof that every listed grade has identical commercial status.

Detailed file:

```text
hyper-no.md
```

must preserve this caution.

---

# 44. Marketing Opportunity Logic

Automotive product routing should support opportunity types such as:

```text
NEW_DEMAND
DEMAND_GROWTH
MATERIAL_UPGRADE
LIGHTWEIGHTING
ELECTRIFICATION
CORROSION_UPGRADE
LOCALIZATION
TECHNICAL_PROPOSAL
JOINT_DEVELOPMENT
LOW_CARBON_TRANSITION
```

Product routing itself does not prove a commercial opportunity.

Opportunity generation happens downstream.

---

# 45. Event-to-Automotive Opportunity Examples

## EV Motor Capacity Expansion

```text
CAPACITY_EXPANSION
↓
ELECTRIFICATION
↓
EV_MOTOR
↓
MOTOR_CORE
↓
HYPER_NO
```

---

## New Passenger Vehicle Platform

```text
PRODUCT_LAUNCH / R_AND_D
↓
LIGHTWEIGHTING
↓
BODY_STRUCTURE
↓
AHSS
↓
AUTOMOTIVE_STEEL
```

---

## Truck Production Expansion

```text
CAPACITY_EXPANSION
↓
COMMERCIAL_VEHICLE
↓
TRUCK_FRAME
↓
ATOS
```

---

## Vehicle Corrosion Requirement Tightening

```text
TECHNICAL_REQUIREMENT_CHANGE
↓
AUTOMOTIVE_PANEL
↓
CORROSION + PAINTING
↓
GI / GA / EG candidates
```

---

## Exhaust Regulation Change

```text
REGULATION
↓
EXHAUST_SYSTEM_CHANGE
↓
HIGH_TEMPERATURE / CORROSION
↓
STAINLESS_STEEL
```

---

# 46. Customer Strategy-to-Product Routing

## ELECTRIFICATION

Possible routes:

```text
EV_MOTOR
→ HYPER_NO

EV_BODY
→ AUTOMOTIVE_STEEL

BATTERY_PACK_STRUCTURE
→ AUTOMOTIVE_STEEL
```

Do not return all three without application evidence.

---

## LIGHTWEIGHTING

Possible route:

```text
AUTOMOTIVE_STEEL
```

Relevant families may include:

```text
AHSS
IF_HSS
```

depending on component.

---

## PREMIUMIZATION

Possible effects:

```text
higher crash performance
higher surface requirements
higher corrosion requirement
```

Route based on physical requirement, not strategy label alone.

---

## LOCALIZATION

Localization does not identify product family.

Use:

```text
LOCALIZATION
+
APPLICATION
```

to determine opportunity.

---

## DECARBONIZATION

Use:

```text
technical product file
+
low-carbon-steel.md
```

after technical fit is known.

---

# 47. Executive Retrieval Mode

If persona:

```text
EXECUTIVE
```

load only enough knowledge to identify:

```text
product family
strategic relevance
customer opportunity
competitive risk
```

Normally:

```text
1 product file maximum
```

Avoid grade tables.

---

# 48. Marketing Retrieval Mode

If persona:

```text
MARKETING
```

retrieve:

```text
application fit
product family
customer benefit
major differentiating property
potential sales action
```

Default:

```text
1~2 product files
```

---

# 49. Engineering Retrieval Mode

If persona:

```text
ENGINEERING
```

may retrieve:

```text
product family
grade family
mechanical data
magnetic data
coating availability
dimensions
standards
forming/welding information
```

Detailed source PDF may be consulted where needed.

---

# 50. Daily Intelligence Rule

Daily automated automotive intelligence should NOT load detailed product data for every article.

Required flow:

```text
NEWS / DART
↓
EVENT
↓
AUTOMOTIVE APPLICATION
↓
ROUTE PRODUCT FAMILY
↓
LOAD 1 PRODUCT MD
↓
GENERATE OPPORTUNITY
```

Only load a second product file when:

```text
coating is relevant
alternative product route matters
comparison is required
```

---

# 51. Daily Product Retrieval Limits

Recommended configuration:

```yaml
automotive_daily_intelligence:
  max_product_files: 2
  preferred_product_files: 1
  allow_pdf_lookup: false
  allow_exact_grade_selection: false
```

---

# 52. Interactive Search Limits

For user-initiated Ask Steel AI queries:

```yaml
automotive_interactive_search:
  max_product_files: 3
  allow_grade_detail: true
  allow_pdf_lookup: true
  require_source_traceability: true
```

Exact PDF lookup should occur only when the user needs detailed technical data.

---

# 53. Competitor Comparison Mode

When comparing competing steel companies:

First establish:

```text
APPLICATION
+
COMPONENT
+
POSCO PRODUCT FAMILY
```

Example:

```text
EV_MOTOR
+
MOTOR_CORE
+
HYPER_NO
```

Then compare competitor products within the same application.

Never compare:

```text
POSCO automotive portfolio
vs
competitor entire portfolio
```

as one undifferentiated comparison.

---

# 54. Knowledge Retrieval Search Order

Use:

```text
1. Exact application code
2. Exact component code
3. Requirement match
4. This index
5. Product MD frontmatter
6. Product MD body
7. Source PDF if needed
```

Do not begin with semantic search over all POSCO documents.

---

# 55. File Loading Examples

## Example A — EV Motor

Load:

```text
./hyper-no.md
```

Do not load:

```text
./automotive-steel.md
./atos.md
../coated/
../carbon/
```

---

## Example B — Door Outer

Load:

```text
./automotive-steel.md
```

Optional:

```text
../coated/galvanized.md
```

---

## Example C — Truck Frame

Load:

```text
./atos.md
```

---

## Example D — Clutch

Load:

```text
../carbon/high-carbon.md
```

---

## Example E — Exhaust Manifold

Load:

```text
../stainless/stainless.md
```

---

# 56. Product File Frontmatter Requirement

Every local automotive product file should contain:

```yaml
---
product_family:

industry:
  - AUTOMOTIVE

applications: []

components: []

requirements: []

product_series: []

aliases: []

source_documents: []

knowledge_status: VERIFIED

last_reviewed:
---
```

The router should inspect frontmatter before loading full product content whenever supported.

---

# 57. Recommended automotive-steel.md Frontmatter

```yaml
---
product_family: AUTOMOTIVE_STEEL

industry:
  - AUTOMOTIVE

applications:
  - VEHICLE_BODY
  - EV_BODY_STRUCTURE
  - CHASSIS
  - BATTERY_PACK_STRUCTURE

components:
  - OUTER_PANEL
  - BODY_IN_WHITE
  - STRUCTURAL_MEMBER
  - CRASH_MEMBER
  - SUSPENSION
  - WHEEL
  - BATTERY_PACK_STRUCTURE

internal_families:
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

source_documents:
  - 2025 Automotive Steel.pdf

knowledge_status: VERIFIED
---
```

---

# 58. Recommended atos.md Frontmatter

```yaml
---
product_family: ATOS

industry:
  - AUTOMOTIVE
  - MACHINERY

applications:
  - COMMERCIAL_VEHICLE
  - HEAVY_AUTOMOTIVE_STRUCTURE

components:
  - TRUCK_FRAME
  - TRAILER_FRAME
  - BOOM_ARM

requirements:
  - HIGH_STRENGTH
  - COLD_FORMABILITY
  - WELDABILITY
  - WEIGHT_REDUCTION

source_documents:
  - 2026 ATOS.pdf
  - 2026 Hot Rolled Steel.pdf

knowledge_status: VERIFIED
---
```

---

# 59. Recommended hyper-no.md Frontmatter

```yaml
---
product_family: HYPER_NO

material_category:
  - NON_ORIENTED_ELECTRICAL_STEEL

industry:
  - AUTOMOTIVE

applications:
  - EV_MOTOR

components:
  - MOTOR_CORE
  - STATOR_CORE
  - ROTOR_CORE

requirements:
  - LOW_CORE_LOSS
  - LOW_HIGH_FREQUENCY_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_STRENGTH
  - THIN_GAUGE

product_series:
  - NEW_PNX
  - PNX_FY
  - PNX
  - PNF

source_documents:
  - 2025 Hyper NO.pdf

knowledge_status: VERIFIED
---
```

---

# 60. Automotive Knowledge Status

Current major routes:

```text
AUTOMOTIVE_STEEL
→ VERIFIED

ATOS
→ VERIFIED

HYPER_NO
→ VERIFIED

GALVANIZED_STEEL
→ VERIFIED

ELECTRO_GALVANIZED_STEEL
→ VERIFIED

POSMAC_1_5
→ VERIFIED

HIGH_CARBON_STEEL
→ VERIFIED

WIRE_ROD
→ VERIFIED

STAINLESS_STEEL
→ VERIFIED
```

Detailed commercial availability must still be verified at grade level.

---

# 61. Unknown Handling

Supported outputs:

```text
AUTOMOTIVE_APPLICATION_UNKNOWN

AUTOMOTIVE_COMPONENT_UNKNOWN

AUTOMOTIVE_PRODUCT_FAMILY_UNKNOWN

GRADE_UNKNOWN

COATING_REQUIREMENT_UNKNOWN

ENGINEERING_REVIEW_REQUIRED

DETAIL_SOURCE_REQUIRED
```

Unknown is preferable to loading unrelated files.

---

# 62. Query Example — "현대차 EV 공장 투자"

Input is too broad.

Correct:

```yaml
industry: AUTOMOTIVE
application: EV_PRODUCTION
component: UNKNOWN

possible_opportunity_domains:
  - VEHICLE_BODY
  - CHASSIS
  - EV_MOTOR
  - BATTERY_PACK_STRUCTURE

product_files_to_load: []

reason:
  Production scope is not specific enough for defensible product matching.
```

The system may show opportunity themes without loading detailed product MDs.

---

# 63. Query Example — "현대차 구동모터 생산라인 확대"

```yaml
industry: AUTOMOTIVE

application: EV_MOTOR

component:
  - MOTOR_CORE

product_candidates:
  - HYPER_NO

files_to_load:
  - ./hyper-no.md

confidence: HIGH
```

---

# 64. Query Example — "신형 EV 차체 경량화"

```yaml
industry: AUTOMOTIVE

application: EV_BODY_STRUCTURE

requirements:
  - WEIGHT_REDUCTION
  - HIGH_STRENGTH
  - FORMABILITY

product_candidates:
  - AUTOMOTIVE_STEEL

files_to_load:
  - ./automotive-steel.md
```

---

# 65. Query Example — "트럭 프레임 경량화"

```yaml
industry: AUTOMOTIVE

application: COMMERCIAL_VEHICLE

component:
  - TRUCK_FRAME

requirements:
  - HIGH_STRENGTH
  - WEIGHT_REDUCTION
  - COLD_FORMABILITY

product_candidates:
  - ATOS

files_to_load:
  - ./atos.md
```

---

# 66. Query Example — "자동차 도어 외판 부식성 개선"

```yaml
industry: AUTOMOTIVE

application: VEHICLE_BODY

component:
  - DOOR_OUTER

requirements:
  - FORMABILITY
  - SURFACE_QUALITY
  - CORROSION_RESISTANCE
  - PAINTABILITY

product_candidates:
  - AUTOMOTIVE_STEEL
  - GALVANIZED_STEEL

files_to_load:
  - ./automotive-steel.md
  - ../coated/galvanized.md
```

---

# 67. Query Example — "EV 배터리셀 공장 신설"

Do NOT produce:

```text
AUTOMOTIVE_STEEL
HYPER_NO
```

by default.

Correct:

```yaml
event: NEW_FACTORY
industry: BATTERY
application: BATTERY_CELL_FACTORY

automotive_product_route:
  status: NOT_ENOUGH_EVIDENCE
```

The existence of an EV battery-cell plant does not prove an automotive steel opportunity.

---

# 68. Explainability Requirement

Every route should answer:

```text
Why this product family?
```

Example:

```text
Customer is expanding EV traction-motor production.

→ application = EV_MOTOR

→ component = MOTOR_CORE

→ required functions include low core loss and high magnetic performance

→ material category = NON_ORIENTED_ELECTRICAL_STEEL

→ POSCO product family = HYPER_NO
```

Do not return only:

```text
Recommended: Hyper NO
```

---

# 69. Automotive Product Router Algorithm

```pseudo
function route_automotive(context):

    identify application

    if application uncertain:
        return broad opportunity domains
        do not load product files

    identify component

    identify:
        performance_goal
        material_requirements
        environment
        manufacturing_requirements

    if EV_MOTOR:
        route HYPER_NO

    else if COMMERCIAL_VEHICLE_FRAME:
        route ATOS

    else if BODY / CRASH / CHASSIS / BATTERY_STRUCTURE:
        route AUTOMOTIVE_STEEL

    else if EXHAUST:
        route STAINLESS_STEEL

    else if CLUTCH / RECLINER / HOSE_CLIP:
        route HIGH_CARBON_STEEL

    else if TIRE / SPRING / BEARING:
        route WIRE_ROD

    if coating_requirement exists:
        add best matching coating file

    if low_carbon_requirement exists:
        add LOW_CARBON_STEEL file

    rank candidates

    load top 1~2 files
```

---

# 70. Automotive Retrieval Budget

Default:

```yaml
MAX_PRODUCT_FILES: 2
PREFERRED_PRODUCT_FILES: 1
MAX_PDF_FILES: 0
```

Interactive engineering analysis:

```yaml
MAX_PRODUCT_FILES: 3
PDF_LOOKUP_ALLOWED: true
```

---

# 71. Final Router Principle

This router exists to prevent automotive intelligence from becoming:

```text
AUTOMOTIVE NEWS
↓
ALL AUTOMOTIVE POSCO PRODUCTS
```

The correct behavior is:

```text
AUTOMOTIVE SIGNAL
↓
APPLICATION
↓
COMPONENT
↓
MATERIAL REQUIREMENT
↓
ONE PRIMARY POSCO PRODUCT FAMILY
↓
OPTIONAL SECONDARY PRODUCT FAMILY
```

The preferred output is:

```text
FEWER PRODUCT FILES
+
STRONGER TECHNICAL LOGIC
+
LOWER TOKEN COST
+
BETTER EXPLAINABILITY
```

---

# 72. Final Automotive Knowledge Chain

```text
industries.md
↓
AUTOMOTIVE

events.md
↓
WHAT HAPPENED?

strategies.md
↓
WHY IS THE CUSTOMER DOING IT?

applications.md
↓
WHAT VEHICLE SYSTEM OR COMPONENT CHANGES?

materials.md
↓
WHAT MATERIAL PERFORMANCE IS REQUIRED?

automotive/index.md
↓
WHICH POSCO AUTOMOTIVE PRODUCT KNOWLEDGE SHOULD BE LOADED?

product-specific MD
↓
WHICH PRODUCT / GRADE MAY FIT?

opportunity engine
↓
WHAT SHOULD POSCO MARKETING DO?
```

The responsibility of this file ends at:

```text
SELECT THE RIGHT PRODUCT KNOWLEDGE FILE.
```

It must not replace detailed product engineering evaluation.
