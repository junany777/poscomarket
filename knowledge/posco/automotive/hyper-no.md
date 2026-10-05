---
product_family: HYPER_NO

name_ko: Hyper NO 무방향성 전기강판
name_en: POSCO Hyper NO

industry:
  - AUTOMOTIVE

secondary_industries:
  - MOBILITY

material_category:
  - ELECTRICAL_STEEL
  - NON_ORIENTED_ELECTRICAL_STEEL

applications:
  - EV_MOTOR
  - EV_TRACTION_MOTOR

components:
  - MOTOR_CORE
  - STATOR_CORE
  - ROTOR_CORE

performance_goals:
  - HIGH_EFFICIENCY
  - HIGH_SPEED
  - HIGH_TORQUE

requirements:
  - LOW_CORE_LOSS
  - LOW_HIGH_FREQUENCY_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_YIELD_STRENGTH
  - ELECTRICAL_INSULATION
  - THIN_GAUGE
  - DIMENSIONAL_STABILITY

product_series:
  - NEW_PNX
  - PNX_FY
  - PNX
  - PNF

source_documents:
  - 2025 Hyper NO.pdf

knowledge_status: VERIFIED

commercial_status_rule:
  exact_grade_status_requires_verification: true
  catalog_contains_pilot_and_commercial_grades: true

parent_router:
  - ./index.md
  - ../index.md
---

# POSCO Hyper NO Product Knowledge

## 1. Purpose

This file defines detailed product knowledge and routing rules for POSCO Hyper NO.

Hyper NO is POSCO's non-oriented electrical steel product family designed for EV traction-motor applications.

This file should be loaded only after the upstream intelligence chain identifies:

```text
INDUSTRY
→ AUTOMOTIVE

APPLICATION
→ EV_MOTOR / EV_TRACTION_MOTOR

COMPONENT
→ MOTOR_CORE / STATOR_CORE / ROTOR_CORE
```

or there is otherwise strong evidence that EV traction-motor electrical steel is relevant.

This file answers:

```text
Which Hyper NO series should be investigated?
```

and, when enough technical information is available:

```text
Which grade candidates should be evaluated?
```

It does NOT independently approve final grade selection.

---

# 2. Core Knowledge Principle

The required reasoning sequence is:

```text
EV SIGNAL
↓
TRACTION MOTOR APPLICATION
↓
MOTOR CORE
↓
MOTOR OPERATING REQUIREMENT
↓
ELECTRICAL / MAGNETIC / MECHANICAL REQUIREMENT
↓
HYPER NO
↓
SERIES
↓
GRADE CANDIDATE
↓
ENGINEERING VALIDATION
```

Never use:

```text
EV
→ Hyper NO
```

as a sufficient reasoning chain.

---

# 3. Hyper NO Positioning

POSCO Hyper NO is designed around material properties required by EV traction motors.

Core material-property directions are:

```text
LOW_CORE_LOSS
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_YIELD_STRENGTH
```

These material properties support motor-level goals such as:

```text
HIGH_EFFICIENCY
HIGH_SPEED
HIGH_TORQUE
```

The relationship should be represented as:

```text
MOTOR PERFORMANCE
↓
MATERIAL REQUIREMENT
```

not as if motor performance were a guaranteed intrinsic steel property.

---

# 4. Motor Performance Mapping

## 4.1 HIGH_EFFICIENCY

Motor goal:

```text
HIGH_EFFICIENCY
```

Primary material implication:

```text
LOW_CORE_LOSS
```

Especially relevant when electromagnetic loss reduction is a primary design objective.

Potential series:

```text
NEW_PNX
PNX
PNF
```

Series ranking depends on operating frequency and mechanical-strength requirements.

---

# 4.2 HIGH_SPEED

Motor goal:

```text
HIGH_SPEED
```

Possible material implications:

```text
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_YIELD_STRENGTH
MECHANICAL_STABILITY
```

Potential series:

```text
NEW_PNX
PNX_FY
PNF
PNX
```

Do not select the highest-strength grade solely because the motor is described as high speed.

Rotational speed, rotor design, stress requirement and electromagnetic operating conditions must be known.

---

# 4.3 HIGH_TORQUE

Motor goal:

```text
HIGH_TORQUE
```

Possible material implication:

```text
HIGH_MAGNETIC_FLUX_DENSITY
```

High torque should not automatically be translated into one grade.

Required analysis may also involve:

```text
motor geometry
current
flux density
speed range
core loss
mechanical strength
```

---

# 5. Hyper NO Product Architecture

The approved catalog defines four principal Hyper NO series:

```text
HYPER_NO
│
├── NEW_PNX
│
├── PNX_FY
│
├── PNX
│
└── PNF
```

Directional positioning:

```text
NEW_PNX
→ lower core loss + higher strength

PNX_FY
→ high strength

PNX
→ low core loss + high strength

PNF
→ low core loss at high frequency
```

These descriptions are routing directions.

They are not substitutes for grade-level specification comparison.

---

# 6. NEW_PNX

Canonical code:

```text
NEW_PNX
```

Primary positioning:

```text
LOWER_CORE_LOSS
+
HIGHER_MECHANICAL_STRENGTH
```

relative to the previous PNX concept as described in the catalog.

Primary application:

```text
EV_TRACTION_MOTOR_CORE
```

---

# 6.1 New PNX Design Intent

Use New PNX as a candidate when the motor design places simultaneous importance on:

```text
CORE_LOSS_REDUCTION
+
MECHANICAL_STRENGTH
```

This may occur in:

```text
HIGH_SPEED_TRACTION_MOTOR
HIGH_EFFICIENCY_TRACTION_MOTOR
```

applications.

Do not infer final suitability without operating-point information.

---

# 6.2 New PNX Representative Grades

Approved source lists:

```text
20PNX1150F
25PNX1200F
27PNX1300F
```

Nominal thicknesses represented by the catalog:

```text
20PNX1150F
→ 0.20 mm

25PNX1200F
→ 0.25 mm

27PNX1300F
→ 0.27 mm
```

Standard width range shown:

```text
950–1250 mm
```

Inner diameter shown:

```text
508 mm
```

For non-standard dimensions:

```text
SIZE_CONFIRMATION_REQUIRED
```

---

# 6.3 New PNX Guaranteed Magnetic Specification Examples

The catalog lists maximum W10/400 core-loss and minimum B50 values.

Representative source values:

```text
20PNX1150F
Core Loss W10/400 max = 11.5 W/kg
B50 min = 1.60 T
Lamination Factor min = 93.0%

25PNX1200F
Core Loss W10/400 max = 12.0 W/kg
B50 min = 1.60 T
Lamination Factor min = 93.5%

27PNX1300F
Core Loss W10/400 max = 13.0 W/kg
B50 min = 1.61 T
Lamination Factor min = 94.0%
```

Definitions:

```text
W10/400
= core loss at 1.0 T and 400 Hz

B50
= magnetic flux density at 5000 A/m
```

Do not compare these values with another test condition as though they were directly equivalent.

---

# 7. PNX_FY

Canonical code:

```text
PNX_FY
```

Primary positioning:

```text
HIGH_MECHANICAL_STRENGTH
```

The catalog describes PNX-FY as a higher-mechanical-strength core optimized for EV traction motors compared with PNX.

---

# 7.1 PNX-FY Routing

Use PNX-FY as a strong candidate when:

```text
EV_TRACTION_MOTOR
+
HIGH_MECHANICAL_STRENGTH_REQUIREMENT
```

is explicitly supported.

Potential signal examples:

```text
higher rotor speed
mechanical stress concern
high-speed traction motor
strength-enhanced motor core
```

These signals only justify evaluation.

They do not prove exact grade selection.

---

# 7.2 PNX-FY Representative Grades

Approved source lists:

```text
20PNX1250FY
25PNX1300FY
27PNX1400FY
30PNX1500FY
```

Nominal thicknesses:

```text
20PNX1250FY
→ 0.20 mm

25PNX1300FY
→ 0.25 mm

27PNX1400FY
→ 0.27 mm

30PNX1500FY
→ 0.30 mm
```

Catalog standard width:

```text
950–1250 mm
```

Inner diameter:

```text
508 mm
```

---

# 7.3 PNX-FY Guaranteed Specification

Source-supported values:

```text
20PNX1250FY
Density = 7.60 kg/dm³
W10/400 max = 12.5 W/kg
B50 min = 1.59 T
Lamination Factor min = 93.0%
Yield Point min = 420 MPa

25PNX1300FY
Density = 7.60 kg/dm³
W10/400 max = 13.0 W/kg
B50 min = 1.60 T
Lamination Factor min = 94.0%
Yield Point min = 420 MPa

27PNX1400FY
Density = 7.60 kg/dm³
W10/400 max = 14.0 W/kg
B50 min = 1.61 T
Lamination Factor min = 94.0%
Yield Point min = 420 MPa

30PNX1500FY
Density = 7.60 kg/dm³
W10/400 max = 15.0 W/kg
B50 min = 1.61 T
Lamination Factor min = 95.0%
Yield Point min = 420 MPa
```

These values should retain their original test conditions.

---

# 7.4 PNX-FY Typical Properties

The catalog additionally provides typical electrical, magnetic and mechanical values.

Important rule:

```text
TYPICAL_VALUE ≠ GUARANTEED_VALUE
```

Typical values may be used for technical comparison only when clearly labeled:

```text
TYPICAL
```

Never render them as specification guarantees.

---

# 8. PNX

Canonical code:

```text
PNX
```

Primary positioning:

```text
LOW_CORE_LOSS
+
HIGH_STRENGTH
```

The catalog describes PNX-Core as optimized for EV traction motors, with:

```text
low core loss at high frequencies
+
high mechanical strength
```

for endurance.

---

# 8.1 PNX Routing

Use PNX when the motor requires a balanced combination of:

```text
LOW_CORE_LOSS
HIGH_FREQUENCY_PERFORMANCE
MECHANICAL_STRENGTH
```

without sufficient evidence that either:

```text
PNX_FY strength priority
```

or:

```text
PNF high-frequency loss priority
```

should dominate.

---

# 8.2 PNX Representative Grades

Approved source lists:

```text
20PNX1200F
25PNX1250F
27PNX1350F
30PNX1450F
```

Nominal thicknesses:

```text
0.20 mm
0.25 mm
0.27 mm
0.30 mm
```

Standard width:

```text
950–1250 mm
```

Inner diameter:

```text
508 mm
```

---

# 8.3 PNX Guaranteed Magnetic Specification

Source-supported examples:

```text
20PNX1200F
W10/400 max = 12.0 W/kg
B50 min = 1.60 T
Lamination Factor min = 93.0%

25PNX1250F
W10/400 max = 12.5 W/kg
B50 min = 1.63 T
Lamination Factor min = 93.5%

27PNX1350F
W10/400 max = 13.5 W/kg
B50 min = 1.63 T
Lamination Factor min = 94.0%

30PNX1450F
W10/400 max = 14.5 W/kg
B50 min = 1.64 T
Lamination Factor min = 94.5%
```

---

# 9. PNF

Canonical code:

```text
PNF
```

Primary positioning:

```text
LOW_CORE_LOSS_AT_HIGH_FREQUENCY
```

The catalog describes PNF-Core as having excellent magnetic properties at high frequencies and being suitable for motors requiring low high-frequency core loss.

---

# 9.1 PNF Routing

Strong route:

```text
EV_TRACTION_MOTOR
+
HIGH_FREQUENCY_OPERATION
+
CORE_LOSS_REDUCTION_PRIORITY
→ PNF candidate
```

This is one of the strongest series-level routing conditions.

Do not select PNF solely because:

```text
motor speed = high
```

unless high-frequency electromagnetic loss is also a relevant requirement.

---

# 9.2 PNF Representative Grades

Source-supported grades:

```text
20PNF1200
20PNF1500
25PNF1400
27PNF1500
30PNF1600
35PNF1800
```

Nominal thickness range shown:

```text
0.20–0.35 mm
```

Representative mapping:

```text
20PNF1200
→ 0.20 mm

20PNF1500
→ 0.20 mm

25PNF1400
→ 0.25 mm

27PNF1500
→ 0.27 mm

30PNF1600
→ 0.30 mm

35PNF1800
→ 0.35 mm
```

Standard width:

```text
950–1250 mm
```

Inner diameter:

```text
508 mm
```

---

# 9.3 PNF Guaranteed Magnetic Specification

Source-supported values:

```text
20PNF1200
Density = 7.60 kg/dm³
W10/400 max = 12.0 W/kg
B50 min = 1.61 T
Lamination Factor min = 93.0%

20PNF1500
Density = 7.65 kg/dm³
W10/400 max = 15.0 W/kg
B50 min = 1.62 T
Lamination Factor min = 93.0%

25PNF1400
Density = 7.60 kg/dm³
W10/400 max = 14.0 W/kg
B50 min = 1.62 T
Lamination Factor min = 93.5%

27PNF1500
Density = 7.60 kg/dm³
W10/400 max = 15.0 W/kg
B50 min = 1.63 T
Lamination Factor min = 94.0%

30PNF1600
Density = 7.60 kg/dm³
W10/400 max = 16.0 W/kg
B50 min = 1.64 T
Lamination Factor min = 94.5%

35PNF1800
Density = 7.60 kg/dm³
W10/400 max = 18.0 W/kg
B50 min = 1.65 T
Lamination Factor min = 95.0%
```

---

# 9.4 PNF High-Frequency Comparison Data

The catalog contains typical loss data at:

```text
50 Hz
400 Hz
800 Hz
1000 Hz
```

These data may be used when engineering analysis specifically compares high-frequency behavior.

They should NOT be loaded into every marketing-intelligence task.

Default retrieval:

```text
series-level description only
```

Engineering retrieval:

```text
high-frequency property table allowed
```

---

# 10. Series Selection Matrix

| Series | Main Routing Priority | Typical Use Logic |
|---|---|---|
| `NEW_PNX` | lower loss + higher strength | high-efficiency/high-speed motor needing combined improvement |
| `PNX_FY` | mechanical strength | high-speed/high-stress traction motor |
| `PNX` | low loss + strength balance | balanced EV motor-core requirement |
| `PNF` | high-frequency low loss | high-frequency electromagnetic-loss priority |

This matrix is directional.

Do not interpret:

```text
NEW_PNX > PNX > PNF
```

as a universal performance ranking.

There is no single "best" Hyper NO series.

---

# 11. Series Decision Rules

## 11.1 Strength-Dominant Case

```text
MOTOR_CORE
+
HIGH_MECHANICAL_STRENGTH
+
high-speed mechanical stress
```

Primary candidate:

```text
PNX_FY
```

Possible alternative:

```text
NEW_PNX
```

---

# 11.2 High-Frequency-Loss-Dominant Case

```text
MOTOR_CORE
+
HIGH_FREQUENCY_OPERATION
+
LOW_HIGH_FREQUENCY_CORE_LOSS
```

Primary candidate:

```text
PNF
```

---

# 11.3 Balanced Loss + Strength

```text
MOTOR_CORE
+
LOW_CORE_LOSS
+
MECHANICAL_STRENGTH
```

Candidate:

```text
PNX
```

---

# 11.4 Enhanced Loss + Strength

When available project evidence indicates demand for:

```text
lower loss than existing PNX concept
+
higher strength
```

candidate:

```text
NEW_PNX
```

---

# 11.5 Insufficient Information

Input:

```text
EV traction motor expansion
```

without operating requirements.

Correct output:

```text
product_family = HYPER_NO

series_candidates:
  - NEW_PNX
  - PNX_FY
  - PNX
  - PNF

series_selection_status:
  SERIES_UNKNOWN
```

Do NOT arbitrarily choose:

```text
PNX_FY
```

or another series.

---

# 12. Grade Naming Interpretation

Grade names contain useful retrieval signals but must not be decoded beyond what the approved source supports.

Examples:

```text
20PNX1250FY
25PNX1300FY
27PNX1400FY
30PNX1500FY
```

and:

```text
20PNF1200
27PNF1500
30PNF1600
```

The leading number corresponds to the catalog's listed nominal sheet thickness:

```text
20 → 0.20 mm
25 → 0.25 mm
27 → 0.27 mm
30 → 0.30 mm
35 → 0.35 mm
```

Do not invent the meaning of all remaining numeric or alphabetic grade-name segments unless explicitly supported by source documentation.

---

# 13. Thickness Routing

Current catalog-supported nominal thicknesses include:

```text
0.20 mm
0.25 mm
0.27 mm
0.30 mm
0.35 mm
```

depending on series/grade.

Thin gauge may be relevant to eddy-current-loss reduction.

However:

```text
THINNER = ALWAYS BETTER
```

is forbidden logic.

Trade-offs may include:

```text
magnetic properties
mechanical properties
lamination factor
manufacturing productivity
motor design
cost
```

These must be evaluated at engineering level.

---

# 14. Standard Dimensions

Catalog standard width for the listed Hyper NO cores is generally:

```text
950–1250 mm
```

with:

```text
508 mm
```

inner diameter.

For non-standard dimensions:

```text
CONTACT / AVAILABILITY_CONFIRMATION_REQUIRED
```

Do not infer manufacturability outside the published range.

---

# 15. Magnetic Property Terminology

Canonical technical terms:

```text
CORE_LOSS
MAGNETIC_FLUX_DENSITY
RESISTIVITY
LAMINATION_FACTOR
```

Important test keys:

```text
W10/400

W15/50

B25
B50
B100
```

Do not compare values measured at different:

```text
frequency
flux density
field strength
```

as if identical.

---

# 16. W10/400

Canonical interpretation:

```text
W10/400
```

means:

```text
core loss
at
1.0 T
and
400 Hz
```

Use only where the source provides this test basis.

---

# 17. B50

Canonical interpretation:

```text
B50
```

means:

```text
magnetic flux density
at
5000 A/m
```

It may support assessment of magnetic-flux capability.

Do not translate B50 directly into a guaranteed motor-torque increase.

---

# 18. Typical vs Guaranteed Values

This distinction is mandatory.

## Guaranteed / Specification

If a table is explicitly identified by the catalog as:

```text
Specification
```

its specified max/min values may be stored as:

```text
GUARANTEED_SPEC
```

with original test conditions.

---

## Typical

If a table is identified as:

```text
Typical Electrical and Magnetic Properties
```

or:

```text
Typical Mechanical Property
```

store as:

```text
TYPICAL_VALUE
```

Never present typical values as contractual guarantees.

---

# 19. Test Standards

The catalog references testing according to standards including:

```text
IEC 60404-2
JIS C 2550-1
JIS Z 2241
JIS Z 2244
```

Do not generalize test results across different test standards without validation.

---

# 20. Insulation Coating

Non-oriented electrical steel receives insulation coating during annealing.

Primary purpose:

```text
reduce eddy-current loss between laminated sheets
```

The catalog states that coating type may differ according to:

```text
final use
customer request
```

Therefore coating is a separate engineering-selection layer.

---

# 20.1 POSCO Hyper NO Coating Types

The supplied catalog lists coating types:

```text
C6-H
C9-H
NS
NM
NT
SP
```

Directional categories include:

```text
GENERAL
→ chromate-based

ECO_FRIENDLY
→ phosphate-based

SELF_BONDING
```

Do not infer exact coating compatibility from product-series name alone.

---

# 20.2 Coating Selection Inputs

Required considerations may include:

```text
insulation resistance
coating thickness
stress relief annealing
heat resistance
weathering / powdering
adhesion
weldability
self-bonding need
manufacturing process
```

Exact coating selection should be:

```text
ENGINEERING_REVIEW_REQUIRED
```

for production proposals.

---

# 20.3 Coating and SRA

The catalog provides insulation-coating behavior before and after:

```text
SRA
Stress Relief Annealing
```

and identifies that some coatings are not suitable for SRA.

Therefore:

```text
SRA_REQUIRED
```

must trigger:

```text
COATING_COMPATIBILITY_CHECK
```

before product recommendation.

---

# 21. Motor Core Manufacturing Considerations

The catalog identifies motor-development and manufacturing activities such as:

```text
SLITTING
PUNCHING
DIE_SET_UP
CORE_BUILDING
WELDING
INTERLOCKING
BONDING
CORE_STACKING_FORCE
SRA
SHRINK_FIT
```

These processes may alter final motor-core performance.

Therefore bulk material properties alone are insufficient for final motor-performance prediction.

---

# 22. Core Building Factor

The system should distinguish:

```text
MATERIAL_MAGNETIC_PROPERTY
```

from:

```text
ASSEMBLED_CORE_PERFORMANCE
```

The catalog explicitly includes:

```text
CORE_BUILDING_FACTOR
```

within POSCO's EV solution-support scope.

This means motor-core performance may differ from simple coupon-test data.

---

# 23. Mechanical / Fatigue Considerations

POSCO's solution-support scope includes:

```text
MECHANICAL_PROPERTY
FATIGUE
```

These become particularly relevant for:

```text
HIGH_SPEED_ROTOR
```

applications.

Do not infer fatigue life from yield strength alone.

---

# 24. Motor Design Support

The catalog identifies POSCO support areas including:

```text
electromagnetic design
mechanical design
noise / vibration
motor performance optimization
drive-system analysis
EV electric-efficiency prediction
```

This may support a marketing opportunity type:

```text
TECHNICAL_COLLABORATION
```

or:

```text
JOINT_DEVELOPMENT
```

when a customer is designing a new traction motor.

Do not interpret these capabilities as evidence of an existing collaboration with a specific customer.

---

# 25. Evaluation Support

Catalog-listed test/evaluation areas include:

```text
MOTOR_PERFORMANCE
EFFICIENCY
HEAT_SHOCK
CONDENSATION
RESONANCE
NOISE_VIBRATION
DURABILITY
FATIGUE
DROP_TEST
```

These may become recommended technical actions when relevant.

---

# 26. Commercial Status Guardrail

The catalog explicitly states:

```text
Pilot development and commercial production grades are included.
```

Therefore appearance in:

```text
line-up chart
property chart
catalog table
```

does NOT independently prove:

```text
COMMERCIAL_PRODUCT
```

For every exact grade recommendation:

```text
COMMERCIAL_STATUS_CHECK_REQUIRED
```

unless another approved source explicitly identifies current commercial status.

---

# 27. Grade Status Representation

Recommended:

```yaml
grade: 20PNX1250FY

series: PNX_FY

catalog_presence: VERIFIED

commercial_status:
  status: UNKNOWN
  reason: >
    The source catalog states that pilot-development
    and commercial-production grades are both included.

source_document:
  - 2025 Hyper NO.pdf
```

Do not invent a commercial/pilot mapping that the source does not provide.

---

# 28. Hyper NO Application Boundary

Strong application:

```text
EV_TRACTION_MOTOR
```

Supported components:

```text
MOTOR_CORE
STATOR_CORE
ROTOR_CORE
```

Do not automatically route Hyper NO to:

```text
BATTERY_CELL
BATTERY_PACK
CHARGER
VEHICLE_BODY
CHASSIS
```

These require other product routes.

---

# 29. Industrial Motor Boundary

If the query is:

```text
INDUSTRIAL_MOTOR
```

do not automatically use this automotive Hyper NO route.

Use:

```text
APPLICATION = INDUSTRIAL_MOTOR
```

and check whether the approved product knowledge supports that use.

This file's strongest source-backed scope is:

```text
EV_TRACTION_MOTOR
```

---

# 30. EV Factory Guardrail

Input:

```text
Automaker builds EV factory.
```

Correct result:

```yaml
product_family: HYPER_NO
routing_status: NOT_ENOUGH_EVIDENCE
reason: >
  EV factory investment does not prove traction-motor
  production or electrical-steel demand.
```

---

# 31. EV Motor Factory Route

Input:

```text
Automaker expands EV traction-motor production.
```

Correct:

```yaml
industry: AUTOMOTIVE

application: EV_MOTOR

component:
  - MOTOR_CORE

material_category:
  - NON_ORIENTED_ELECTRICAL_STEEL

product_family:
  - HYPER_NO

series:
  status: SERIES_UNKNOWN

files_loaded:
  - hyper-no.md
```

Series should remain unknown until motor requirements are known.

---

# 32. High-Speed Motor Route

Input:

```text
Customer develops a higher-speed EV traction motor.
```

Possible reasoning:

```text
HIGH_SPEED
↓
mechanical stress increases
+
electromagnetic operating frequency may increase
↓
HIGH_STRENGTH
+
LOW_HIGH_FREQUENCY_CORE_LOSS
```

Potential candidates:

```text
PNX_FY
PNF
NEW_PNX
```

Do not select one without additional requirements.

---

# 33. High-Efficiency Motor Route

Input:

```text
Customer targets higher traction-motor efficiency.
```

Reasoning:

```text
HIGH_EFFICIENCY
↓
electromagnetic loss reduction
↓
LOW_CORE_LOSS
```

Potential candidates:

```text
NEW_PNX
PNX
PNF
```

Need:

```text
operating frequency
flux density
speed map
strength requirement
```

to narrow.

---

# 34. High-Torque Motor Route

Input:

```text
Customer targets higher low-speed motor torque.
```

Possible requirement:

```text
HIGH_MAGNETIC_FLUX_DENSITY
```

Do not independently select one Hyper NO series.

Additional design information is required.

---

# 35. Grade Selection Required Inputs

Before exact grade selection, collect where available:

```text
motor type
rotor type
stator design
maximum speed
continuous speed
operating frequency
flux density
torque target
efficiency target
core-loss target
mechanical stress
yield-strength target
sheet thickness
stack length
punching process
core joining process
SRA requirement
insulation coating requirement
width requirement
customer qualification requirement
commercial status
```

Missing critical fields should result in:

```text
GRADE_UNKNOWN
```

---

# 36. Grade Selection Boundary

Allowed:

```text
HYPER_NO
→ PNX_FY candidate
```

Allowed with sufficient technical context:

```text
PNX_FY
→ 20PNX1250FY / 25PNX1300FY candidates
```

Not allowed without engineering verification:

```text
20PNX1250FY is the correct grade.
```

Final selection must remain:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 37. Series Scoring

Suggested Series-fit score:

```text
Application Match             20%
Operating Frequency Match     20%
Core Loss Requirement         20%
Mechanical Strength           20%
Magnetic Flux Requirement     10%
Thickness / Manufacturing      5%
Evidence Completeness          5%
```

Interpretation:

```text
90–100
STRONG_SERIES_CANDIDATE

80–89
GOOD_SERIES_CANDIDATE

70–79
POSSIBLE_SERIES_CANDIDATE

60–69
WEAK_SERIES_CANDIDATE

<60
DO_NOT_SELECT_SERIES
```

Do not calculate a high-precision score when the underlying data are qualitative.

---

# 38. Series Candidate Output

Recommended:

```yaml
product_family: HYPER_NO

application:
  - EV_TRACTION_MOTOR

component:
  - MOTOR_CORE

performance_goals:
  - HIGH_SPEED
  - HIGH_EFFICIENCY

requirements:
  - LOW_HIGH_FREQUENCY_CORE_LOSS
  - HIGH_YIELD_STRENGTH

series_candidates:
  - series: PNX_FY
    priority: P1
    reason:
      - mechanical strength is a major requirement

  - series: PNF
    priority: P1
    reason:
      - high-frequency core loss is a major requirement

  - series: NEW_PNX
    priority: P2
    reason:
      - combined lower-loss and higher-strength concept

missing_information:
  - maximum_motor_speed
  - operating_frequency
  - required_yield_strength
  - target_core_loss

grade_selection:
  status: GRADE_UNKNOWN
```

---

# 39. Grade Candidate Output

When requirements are sufficiently detailed:

```yaml
series: PNX_FY

grade_candidates:
  - grade: 20PNX1250FY
    nominal_thickness_mm: 0.20

  - grade: 25PNX1300FY
    nominal_thickness_mm: 0.25

selection_status:
  ENGINEERING_REVIEW_REQUIRED

commercial_status:
  COMMERCIAL_STATUS_CHECK_REQUIRED
```

---

# 40. Product Property Data Model

Recommended property representation:

```yaml
grade: 20PNX1250FY

guaranteed_properties:
  core_loss:
    test_condition: W10/400
    max_W_per_kg: 12.5

  magnetic_flux_density:
    test_condition: B50
    min_T: 1.59

  lamination_factor:
    min_percent: 93.0

  yield_point:
    min_MPa: 420

typical_properties:
  status: AVAILABLE_IN_SOURCE
  use_as_guarantee: false
```

---

# 41. Test Condition Preservation

Every magnetic value must preserve:

```text
flux density
frequency
field strength
test standard
specimen condition
```

Do not store:

```text
core_loss = 12.5
```

without:

```text
W10/400
```

context.

---

# 42. Typical Property Guardrail

The catalog provides typical values for:

```text
CORE_LOSS
MAGNETIC_FLUX_DENSITY
RESISTIVITY
TENSILE_STRENGTH
YIELD_POINT
ELONGATION
HARDNESS
LAMINATION_FACTOR
```

Store these only with:

```text
value_type = TYPICAL
```

They must not be used as:

```text
GUARANTEED_PRODUCT_SPEC
```

---

# 43. Motor Core Processing Risk

Material properties may be affected by:

```text
PUNCHING
SLITTING
STACKING
WELDING
INTERLOCKING
BONDING
STRESS
SHRINK_FIT
SRA
```

Therefore:

```text
catalog material property
≠
finished motor-core property
```

This distinction must be preserved in engineering analysis.

---

# 44. Punching / Stress Effects

The source's solution-support scope includes:

```text
MP under stress
Punchability
Core building factor
```

Therefore, when a customer issue concerns:

```text
magnetic deterioration after punching
core assembly loss
stress-related performance degradation
```

recommended action may be:

```text
TECHNICAL_EVALUATION
```

rather than simply moving to a different grade.

---

# 45. Self-Bonding Knowledge Boundary

The Hyper NO catalog includes:

```text
SELF_BONDING_TECHNOLOGY
```

as part of its product/solution scope.

However this file should not infer detailed self-bonding process specifications unless the corresponding source section is explicitly retrieved.

Use:

```text
SELF_BONDING_DETAIL_REQUIRED
```

when needed.

---

# 46. Insulation Coating Routing

If customer requirements mention:

```text
SRA
WELDING
SELF_BONDING
COATING_THICKNESS
INSULATION_RESISTANCE
```

then the analysis must branch:

```text
Hyper NO Grade
+
Insulation Coating
```

Do not assume coating from grade name.

---

# 47. EV Marketing Opportunity Types

Hyper NO-related opportunity types may include:

```text
NEW_DEMAND
DEMAND_GROWTH
MATERIAL_UPGRADE
EFFICIENCY_UPGRADE
HIGH_SPEED_MOTOR_DEVELOPMENT
MOTOR_DOWNSIZING_SUPPORT
TECHNICAL_PROPOSAL
JOINT_DEVELOPMENT
LOCALIZATION
COMPETITOR_DEFENSE
```

These are downstream business classifications.

They are not product properties.

---

# 48. Event-to-Hyper-NO Examples

## New EV Traction Motor Plant

```text
NEW_FACTORY
↓
ELECTRIFICATION
↓
EV_MOTOR
↓
MOTOR_CORE
↓
NON_ORIENTED_ELECTRICAL_STEEL
↓
HYPER_NO
```

---

## Motor Capacity Expansion

```text
CAPACITY_EXPANSION
↓
EV_MOTOR production increase
↓
potential motor-core demand increase
↓
HYPER_NO demand opportunity
```

Series remains unknown without technical requirements.

---

## High-Speed Motor R&D

```text
R_AND_D
↓
HIGH_SPEED_TRACTION_MOTOR
↓
HIGH_STRENGTH
+
HIGH_FREQUENCY_LOSS requirement
↓
PNX_FY / PNF / NEW_PNX evaluation
```

---

## Efficiency Improvement Program

```text
R_AND_D
↓
HIGH_EFFICIENCY_MOTOR
↓
LOW_CORE_LOSS requirement
↓
NEW_PNX / PNX / PNF evaluation
```

---

# 49. Negative Routing Rules

## EV battery news

Do NOT route:

```text
BATTERY_CELL_FACTORY
→ HYPER_NO
```

---

## EV charging infrastructure

Do NOT route:

```text
CHARGING_STATION
→ HYPER_NO
```

---

## EV body lightweighting

Route:

```text
EV_BODY_STRUCTURE
→ AUTOMOTIVE_STEEL
```

not Hyper NO.

---

## Industrial transformer

Do NOT route:

```text
TRANSFORMER_CORE
→ HYPER_NO
```

Transformer material belongs to a different electrical-steel route.

---

## Generic motor

Do not automatically assume:

```text
GENERIC_MOTOR
→ EV HYPER_NO
```

Confirm application.

---

# 50. Competitor Comparison Boundary

When comparing Hyper NO with competitor electrical steel:

Required comparison unit:

```text
EV_TRACTION_MOTOR
+
MOTOR_CORE
+
NON_ORIENTED_ELECTRICAL_STEEL
```

Comparison dimensions may include:

```text
core loss
high-frequency loss
magnetic flux density
strength
thickness
coating
commercial availability
technical support
local supply
```

Only compare dimensions with evidence for both sides.

If competitor evidence is absent:

```text
COMPETITOR_POSITION_UNKNOWN
```

---

# 51. Executive Retrieval Mode

For:

```text
EXECUTIVE
```

normally retrieve only:

```text
product family
series direction
market relevance
opportunity
risk
confidence
```

Example:

```text
EV motor production expansion may increase demand
for high-performance non-oriented electrical steel.

POSCO relevance:
Hyper NO

Key opportunity:
future motor-core material demand

Series:
not determined without motor operating requirements
```

Avoid grade tables.

---

# 52. Marketing Retrieval Mode

For:

```text
MARKETING
```

retrieve:

```text
customer program
motor application
material requirements
Hyper NO series direction
major customer benefit hypothesis
missing technical information
next customer question
```

Example:

```text
Customer target:
higher-speed traction motor

Likely material needs:
high mechanical strength
+
high-frequency loss reduction

Hyper NO candidates:
PNX-FY / PNF

Next action:
obtain motor speed/frequency/core-loss requirements.
```

---

# 53. Engineering Retrieval Mode

For:

```text
ENGINEERING
```

allow retrieval of:

```text
exact grades
thickness
width
core loss
B50
resistivity
lamination factor
yield strength
tensile strength
elongation
hardness
coating properties
test standards
```

Source context must remain attached.

---

# 54. Daily Intelligence Rule

Daily news processing should stop at:

```text
HYPER_NO
```

or occasionally:

```text
SERIES_CANDIDATE
```

Do not select exact grade during automated daily intelligence.

Recommended configuration:

```yaml
daily_hyper_no_analysis:
  allow_product_family: true
  allow_series_candidate: true
  allow_exact_grade: false
  allow_pdf_lookup: false
```

---

# 55. Interactive Engineering Rule

For user-initiated technical analysis:

```yaml
interactive_hyper_no_analysis:
  allow_series_candidate: true
  allow_exact_grade_candidate: true
  allow_pdf_lookup: true
  require_test_condition: true
  require_commercial_status_check: true
```

---

# 56. Missing Information Checklist

Before series selection:

```text
motor type
speed range
frequency range
efficiency target
torque requirement
mechanical-strength requirement
```

Before exact grade selection:

```text
all above
+
sheet thickness
core-loss target
flux-density target
yield-strength target
core manufacturing process
insulation coating
SRA
width
commercial status
customer specification
```

---

# 57. Unknown States

Supported:

```text
HYPER_NO_SERIES_UNKNOWN

HYPER_NO_GRADE_UNKNOWN

OPERATING_FREQUENCY_UNKNOWN

MOTOR_SPEED_UNKNOWN

CORE_LOSS_TARGET_UNKNOWN

MAGNETIC_FLUX_TARGET_UNKNOWN

MECHANICAL_STRENGTH_TARGET_UNKNOWN

COATING_UNKNOWN

SRA_REQUIREMENT_UNKNOWN

COMMERCIAL_STATUS_UNKNOWN

SIZE_AVAILABILITY_CHECK_REQUIRED

ENGINEERING_REVIEW_REQUIRED
```

---

# 58. Confidence Levels

## Product Family Confidence

```text
EV traction motor explicitly identified
→ HIGH
```

```text
EV motor strongly implied
→ MEDIUM_HIGH
```

```text
generic EV factory only
→ LOW / DO NOT ROUTE
```

---

## Series Confidence

```text
operating requirements explicitly known
→ potentially HIGH

only broad motor objective known
→ MEDIUM

only EV traction-motor application known
→ LOW / SERIES_UNKNOWN
```

---

## Grade Confidence

Exact grade confidence should normally remain below final recommendation level without engineering validation.

---

# 59. Source Traceability

Every exact technical property must retain:

```yaml
source:
  document: 2025 Hyper NO.pdf
  section:
  page:
  value_type:
    - GUARANTEED
    - TYPICAL
```

The knowledge layer should preserve page/section references when product MDs are generated programmatically.

---

# 60. Source Authority Rules

For Hyper NO product claims:

```text
2025 Hyper NO.pdf
```

is the current approved primary source in this knowledge base.

Do not override its product data using:

```text
generic model memory
competitor documentation
unverified web material
```

without an explicit verification workflow.

---

# 61. Product Knowledge Update Rule

If a newer POSCO Hyper NO catalog is added:

```text
1. compare version/year
2. identify changed grades
3. identify new/removed series
4. compare specification changes
5. compare commercial status
6. update this file
7. record changes in docs/decisions.md
```

Do not silently overwrite historical product knowledge.

---

# 62. Representative Hyper NO Registry

## NEW_PNX

```text
20PNX1150F
25PNX1200F
27PNX1300F
```

## PNX_FY

```text
20PNX1250FY
25PNX1300FY
27PNX1400FY
30PNX1500FY
```

## PNX

```text
20PNX1200F
25PNX1250F
27PNX1350F
30PNX1450F
```

## PNF

```text
20PNF1200
20PNF1500
25PNF1400
27PNF1500
30PNF1600
35PNF1800
```

Catalog presence does not equal confirmed commercial status.

---

# 63. Retrieval Keywords

Aliases / search signals:

```text
Hyper NO
HyperNO
NO electrical steel
non-oriented electrical steel
무방향성 전기강판
EV motor steel
traction motor steel
motor core steel
stator core
rotor core
전기차 구동모터
모터코어
고효율 모터
고속 모터
전기강판
저철손
고자속밀도
```

These keywords are retrieval aids.

They do not override application validation.

---

# 64. Family Selection Algorithm

```pseudo
function route_hyper_no(context):

    if context.application != EV_TRACTION_MOTOR:
        return NOT_ENOUGH_EVIDENCE

    if context.component not in [
        MOTOR_CORE,
        STATOR_CORE,
        ROTOR_CORE
    ]:
        component_confidence_check()

    product_family = HYPER_NO

    if technical_requirements are insufficient:
        return {
            product_family: HYPER_NO,
            series: SERIES_UNKNOWN
        }

    candidates = []

    if HIGH_MECHANICAL_STRENGTH is dominant:
        candidates += PNX_FY

    if HIGH_FREQUENCY_CORE_LOSS is dominant:
        candidates += PNF

    if LOW_CORE_LOSS and HIGH_STRENGTH:
        candidates += PNX

    if LOWER_CORE_LOSS and HIGHER_STRENGTH
       relative to PNX concept:
        candidates += NEW_PNX

    rank candidates

    if grade inputs insufficient:
        return top_series_candidates

    retrieve grade properties

    return grade_candidates with:
        ENGINEERING_REVIEW_REQUIRED
        COMMERCIAL_STATUS_CHECK_REQUIRED
```

---

# 65. Marketing Opportunity Example

Input:

```text
현대차가 차세대 고속 구동모터 생산라인을 확대한다.
```

Possible structured reasoning:

```yaml
industry: AUTOMOTIVE

event:
  type: CAPACITY_EXPANSION

strategy:
  - ELECTRIFICATION
  - GROWTH

application:
  - EV_TRACTION_MOTOR

component:
  - MOTOR_CORE

performance_goals:
  - HIGH_SPEED
  - HIGH_EFFICIENCY

material_requirements:
  - HIGH_MECHANICAL_STRENGTH
  - LOW_HIGH_FREQUENCY_CORE_LOSS

material_category:
  - NON_ORIENTED_ELECTRICAL_STEEL

product_family:
  - HYPER_NO

series_candidates:
  - PNX_FY
  - PNF
  - NEW_PNX

grade:
  status: GRADE_UNKNOWN

recommended_action:
  - obtain maximum motor speed
  - obtain electromagnetic operating frequency
  - obtain core loss target
  - obtain mechanical strength requirement
```

This is the desired behavior.

---

# 66. Weak Analysis Example

Bad:

```text
현대차 EV 생산 증가
→ Hyper NO 20PNX1250FY 판매기회
```

Why bad:

```text
motor production not proven
motor-core requirement unknown
series requirement unknown
grade requirement unknown
commercial status not confirmed
```

---

# 67. Good Analysis Example

```text
Customer expands EV traction-motor production.

Evidence supports an increase in motor-core demand.

Motor efficiency and high-speed targets imply
low core loss and mechanical-strength requirements.

POSCO Hyper NO is therefore a relevant
product-family candidate.

PNX-FY / PNF / New PNX should be evaluated
after motor operating conditions are confirmed.

Exact grade:
not yet determined.
```

---

# 68. Product Hallucination Guardrail

Never invent:

```text
Hyper NO grade
commercial status
magnetic value
mechanical value
coating property
customer adoption
motor efficiency improvement percentage
motor torque improvement percentage
mass-production customer
qualification status
```

If not explicitly supported:

```text
UNKNOWN
```

---

# 69. Final Hyper NO Knowledge Chain

```text
CUSTOMER SIGNAL
↓
EV MOTOR EVENT
↓
TRACTION MOTOR APPLICATION
↓
MOTOR CORE
↓
MOTOR PERFORMANCE GOAL
↓
MAGNETIC + MECHANICAL REQUIREMENT
↓
HYPER NO
↓
NEW_PNX / PNX_FY / PNX / PNF
↓
GRADE CANDIDATE
↓
COATING / DIMENSION / PROCESS CHECK
↓
COMMERCIAL STATUS CHECK
↓
ENGINEERING VALIDATION
↓
MARKETING OPPORTUNITY
```

---

# 70. Final Rule

This file must optimize for:

```text
CORRECT MOTOR APPLICATION
+
CORRECT REQUIREMENT
+
CORRECT SERIES DIRECTION
+
SOURCE-BASED GRADE DATA
+
EXPLICIT UNCERTAINTY
```

not:

```text
MOST ADVANCED GRADE
```

or:

```text
LOWEST CORE-LOSS NUMBER
```

The correct sequence is:

```text
MOTOR FIRST
↓
OPERATING REQUIREMENT SECOND
↓
SERIES THIRD
↓
GRADE LAST
```

The responsibility of this file ends at:

```text
DEFENSIBLE HYPER NO PRODUCT / GRADE CANDIDATE
```

Final customer application approval remains an engineering decision.
