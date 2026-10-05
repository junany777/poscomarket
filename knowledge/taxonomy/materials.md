# POSCO Material Taxonomy & Product Knowledge Routing

## 1. Purpose

This document defines the canonical material taxonomy and POSCO product-family routing rules for the Steel Market Intelligence Platform.

This is the core material knowledge layer of the system.

Its purpose is to convert industrial intelligence into defensible POSCO product opportunities.

The required reasoning chain is:

```text
INDUSTRY
↓
COMPANY EVENT
↓
STRATEGY
↓
APPLICATION
↓
COMPONENT
↓
OPERATING ENVIRONMENT
↓
FUNCTIONAL REQUIREMENT
↓
MATERIAL REQUIREMENT
↓
MATERIAL CATEGORY
↓
POSCO PRODUCT FAMILY
↓
PRODUCT KNOWLEDGE RETRIEVAL
↓
GRADE / PRODUCT FIT
↓
MARKETING OPPORTUNITY
```

Never skip directly from:

```text
NEWS
→ POSCO PRODUCT
```

or:

```text
INDUSTRY
→ PRODUCT GRADE
```

---

# 2. Knowledge Authority

Product information in this system must be grounded primarily in approved POSCO documents.

Source priority:

```text
1. POSCO Product Catalog
2. POSCO Technical Product Guide
3. POSCO Sustainability / Official Corporate Document
4. Structured knowledge derived from approved sources
5. General model knowledge only for non-product background interpretation
```

If POSCO product information conflicts with general model knowledge:

```text
POSCO APPROVED KNOWLEDGE WINS
```

Never use general model knowledge to invent:

```text
product grade
chemical composition
strength
magnetic property
coating amount
dimension
certification
availability
customer adoption
production status
```

---

# 3. Source Documents

The current Material Brain is based on the following approved source set.

## 3.1 Electrical / Special Materials

```text
2025 Hyper NO.pdf
Notice_GO Catalog.pdf
Notice_NO Catalog.pdf
2025 Stainless Steel.pdf
2025 Titanium.pdf
2025 Titanium Application.pdf
```

## 3.2 Coated Products

```text
2025 Galvanized Steel.pdf
2025 Electro Galvanized Steel.pdf
2025 POSMAC1.5.pdf
2025 POSMAC3.0.pdf
2025 PosMAC super.pdf
```

## 3.3 Carbon Steel / Sheet

```text
2026 Hot Rolled Steel.pdf
2025 Cold Rolled Steel.pdf
2025 High Carbon Steel.pdf
2025 Automotive Steel.pdf
2026 ATOS.pdf
```

## 3.4 Plate / Heavy Industry Products

```text
2025 Steel Plates.pdf
2025 High Tensle Steel Plate.pdf
2025 Wear Resistant Steel.pdf
2025 API STEEL.pdf
2025 Tube Core PosLoop355.pdf
```

## 3.5 Wire Products

```text
2025 Wire Rod.pdf
```

## 3.6 Corrosion Resistant Specialty Product

```text
2025 ANCOR.pdf
```

## 3.7 Sustainability / Low Carbon Context

```text
2025_POSCO_SustainabilityReport.pdf
```

---

# 4. Knowledge Architecture

Material knowledge is divided into five layers.

```text
LEVEL 1
MATERIAL REQUIREMENT

LEVEL 2
MATERIAL CATEGORY

LEVEL 3
PRODUCT FAMILY

LEVEL 4
PRODUCT SERIES / GRADE FAMILY

LEVEL 5
SPECIFIC GRADE
```

Example:

```text
LOW_CORE_LOSS
↓
NON_ORIENTED_ELECTRICAL_STEEL
↓
HYPER_NO
↓
PNX_FY
↓
20PNX1250FY
```

Another example:

```text
WEAR_RESISTANCE
↓
WEAR_RESISTANT_PLATE
↓
POS_AR
↓
POS_AR400 / POS_AR450 / POS_AR500
```

The system should normally stop at Product Family during intelligence generation.

Specific grade selection requires detailed product retrieval.

---

# 5. Product Matching Rule

The intelligence system must distinguish:

```text
MATERIAL MATCH
```

from:

```text
PRODUCT FAMILY MATCH
```

from:

```text
GRADE MATCH
```

Example:

```text
EV motor
→ NON_ORIENTED_ELECTRICAL_STEEL
```

is a Material Match.

```text
EV motor
→ HYPER_NO
```

is a Product Family Match.

```text
EV motor
→ 20PNX1250FY
```

is a Grade Match.

A Grade Match requires significantly more evidence.

---

# 6. Canonical Material Requirement Taxonomy

## 6.1 Mechanical Requirements

```text
HIGH_STRENGTH
VERY_HIGH_STRENGTH
HIGH_YIELD_STRENGTH
HIGH_TENSILE_STRENGTH
HIGH_SPECIFIC_STRENGTH
IMPACT_TOUGHNESS
LOW_TEMPERATURE_TOUGHNESS
CRYOGENIC_TOUGHNESS
FRACTURE_TOUGHNESS
FATIGUE_RESISTANCE
WEAR_RESISTANCE
ABRASION_RESISTANCE
PRESSURE_RESISTANCE
CRASH_RESISTANCE
BUCKLING_RESISTANCE
STRUCTURAL_STABILITY
```

---

# 6.2 Weight / Efficiency Requirements

```text
LIGHTWEIGHT
WEIGHT_REDUCTION
THIN_GAUGE
HIGH_STRENGTH_TO_WEIGHT
```

---

# 6.3 Forming / Manufacturing Requirements

```text
FORMABILITY
DEEP_DRAWABILITY
BENDABILITY
COLD_FORMABILITY
HOT_FORMABILITY
WELDABILITY
HIGH_HEAT_INPUT_WELDABILITY
MACHINABILITY
CUTTING_PERFORMANCE
PRESS_FORMABILITY
DIMENSIONAL_STABILITY
SURFACE_QUALITY
PAINTABILITY
COATING_ADHESION
```

---

# 6.4 Corrosion Requirements

```text
CORROSION_RESISTANCE
ATMOSPHERIC_CORROSION_RESISTANCE
WEATHER_RESISTANCE
SEAWATER_CORROSION_RESISTANCE
COASTAL_CORROSION_RESISTANCE
SEVERE_ENVIRONMENT_CORROSION_RESISTANCE
CUT_EDGE_CORROSION_RESISTANCE
FORMED_SECTION_CORROSION_RESISTANCE
CHEMICAL_RESISTANCE
SULFURIC_ACID_CORROSION_RESISTANCE
COMPOSITE_ACID_CORROSION_RESISTANCE
DEW_POINT_CORROSION_RESISTANCE
INTERGRANULAR_CORROSION_RESISTANCE
```

---

# 6.5 Oil / Gas / Hydrogen Environment Requirements

```text
HIC_RESISTANCE
SSCC_RESISTANCE
SOUR_SERVICE
HYDROGEN_INDUCED_CRACKING_RESISTANCE
PRESSURE_SERVICE
ARCTIC_SERVICE
LOW_TEMPERATURE_PIPELINE_SERVICE
```

Do not infer hydrogen service suitability from generic corrosion resistance.

---

# 6.6 Thermal Requirements

```text
HEAT_RESISTANCE
HIGH_TEMPERATURE_STRENGTH
OXIDATION_RESISTANCE
LOW_THERMAL_EXPANSION
THERMAL_CYCLING_RESISTANCE
CRYOGENIC_SERVICE
```

---

# 6.7 Electrical / Magnetic Requirements

```text
LOW_CORE_LOSS
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_MAGNETIC_PERMEABILITY
HIGH_ELECTROMAGNETIC_EFFICIENCY
ELECTRICAL_INSULATION
NON_MAGNETIC
```

---

# 6.8 Surface / Coating Requirements

```text
SURFACE_QUALITY
COATING_DURABILITY
CUT_EDGE_DURABILITY
PAINTABILITY
LUBRICITY
SCRATCH_RESISTANCE
GALLING_RESISTANCE
WHITE_RUST_RESISTANCE
```

---

# 6.9 Purity / Internal Quality Requirements

```text
CLEANLINESS
LOW_INCLUSION
HOMOGENEOUS_MICROSTRUCTURE
LOW_DECARBURIZATION
SURFACE_DEFECT_CONTROL
DIMENSIONAL_PRECISION
```

These requirements are especially relevant to:

```text
WIRE_ROD
HIGH_CARBON_STEEL
BEARING_STEEL
SPRING_STEEL
```

---

# 7. Application Performance vs Material Property

Do not confuse product/system performance with material properties.

Application-performance goals include:

```text
HIGH_EFFICIENCY
HIGH_SPEED
HIGH_TORQUE
LONG_SERVICE_LIFE
LOW_MAINTENANCE
WEIGHT_REDUCTION
CRASH_SAFETY
ENERGY_EFFICIENCY
LOW_CARBON_FOOTPRINT
```

Example:

```text
HIGH_EFFICIENCY MOTOR
↓
LOW_CORE_LOSS
↓
ELECTRICAL_STEEL
```

`HIGH_EFFICIENCY` is not itself a steel property.

---

# 8. Operating Environment Taxonomy

Use environment metadata before product matching.

```text
INDOOR
OUTDOOR
ATMOSPHERIC
COASTAL
MARINE
SEAWATER
HIGH_SALINITY
HIGH_HUMIDITY
CHEMICAL
SULFURIC_ACID
COMPOSITE_ACID
SOUR_GAS
HIGH_TEMPERATURE
LOW_TEMPERATURE
CRYOGENIC
HIGH_PRESSURE
ABRASIVE
IMPACT
CYCLIC_LOAD
UNKNOWN
```

---

# 9. Canonical Material Categories

Primary categories:

```text
HOT_ROLLED_STEEL
COLD_ROLLED_STEEL
AUTOMOTIVE_STEEL
HIGH_CARBON_STEEL
WIRE_ROD

GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
CORROSION_RESISTANT_ALLOY_COATED_STEEL

ELECTRICAL_STEEL
NON_ORIENTED_ELECTRICAL_STEEL
GRAIN_ORIENTED_ELECTRICAL_STEEL

STEEL_PLATE
SHIPBUILDING_PLATE
OFFSHORE_PLATE
LINE_PIPE_PLATE
PRESSURE_VESSEL_PLATE
CRYOGENIC_PLATE
CONSTRUCTION_PLATE
MECHANICAL_STRUCTURAL_PLATE
WEAR_RESISTANT_PLATE

API_STEEL

STAINLESS_STEEL
TITANIUM

ACID_CORROSION_RESISTANT_STEEL

HYPERLOOP_TUBE_STEEL
```

---

# 10. HOT_ROLLED_STEEL

Canonical code:

```text
HOT_ROLLED_STEEL
```

Hot-rolled coils may be used directly or as intermediate material for cold-rolled and electrical steel products. The catalog identifies broad applications including high-carbon steel, weathering steel, pipe steel, line-pipe steel, automotive structural steel and structural steel.

Core requirement profile:

```text
HIGH_STRENGTH
FORMABILITY
WELDABILITY
STRUCTURAL_STABILITY
```

Application-dependent requirements may include:

```text
WEATHER_RESISTANCE
LOW_TEMPERATURE_TOUGHNESS
HIC_RESISTANCE
PRESSURE_RESISTANCE
```

---

# 10.1 Hot Rolled Application Families

```text
GENERAL_HOT_ROLLED
STRUCTURAL_HOT_ROLLED
PIPE_HOT_ROLLED
LINE_PIPE_HOT_ROLLED
AUTOMOTIVE_STRUCTURAL_HOT_ROLLED
WEATHERING_HOT_ROLLED
HIGH_CARBON_HOT_ROLLED
COLD_ROLLING_FEEDSTOCK
PRESSURE_VESSEL_HOT_ROLLED
```

The hot-rolled catalog specifically describes line-pipe products as requiring good weldability, cryogenic toughness and resistance to hydrogen-induced cracking.

---

# 11. COLD_ROLLED_STEEL

Canonical code:

```text
COLD_ROLLED_STEEL
```

Core characteristics:

```text
SURFACE_QUALITY
FORMABILITY
DIMENSIONAL_PRECISION
```

POSCO describes cold rolled steel as having a smooth surface and good machinability, and uses it across home appliances, industrial equipment, building materials and automotive applications.

---

# 11.1 Cold Rolled Product Families

```text
GENERAL_COLD_ROLLED
HSS_COLD_ROLLED
STRUCTURAL_COLD_ROLLED
ENAMEL_STEEL
WELDING_ELECTRODE_STEEL
ACID_CORROSION_RESISTANT_COLD_ROLLED
WEATHERING_COLD_ROLLED
```

---

# 11.2 General Cold Rolled

Typical applications:

```text
REFRIGERATOR
HOME_APPLIANCE_PANEL
DRUM
FURNITURE
AUTOMOTIVE_OIL_FILTER
FRAME
```

Product concepts include:

```text
COMMERCIAL_QUALITY
DRAWING_QUALITY
DEEP_DRAWING_QUALITY
EXTRA_DEEP_DRAWING_QUALITY
```

POSCO's catalog separates normal forming, drawing, deep-drawing and extra-deep-drawing grades.

---

# 11.3 HSS Cold Rolled

Requirement:

```text
HIGH_STRENGTH
+
FORMABILITY
```

Use where ordinary cold rolled steel does not provide sufficient structural strength.

---

# 11.4 Enamel Steel

Canonical product concept:

```text
ENAMEL_STEEL
```

Requirements:

```text
FORMABILITY
HEAT_RESISTANCE
IMPACT_RESISTANCE
SURFACE_QUALITY
ENAMEL_ADHESION
```

Applications include:

```text
HOME_APPLIANCE
KITCHEN_EQUIPMENT
BATHTUB
ARCHITECTURAL_PANEL
```

The catalog describes enamel steel as combining steel strength/formability with enamel heat, wear and surface properties.

---

# 12. AUTOMOTIVE_STEEL

Canonical code:

```text
AUTOMOTIVE_STEEL
```

This is a major strategic material family.

Do not treat it as one grade.

Primary product architecture:

```text
FORMABLE_AUTOMOTIVE_STEEL
HIGH_STRENGTH_AUTOMOTIVE_STEEL
ADVANCED_HIGH_STRENGTH_STEEL
COATED_AUTOMOTIVE_STEEL
```

---

# 12.1 Automotive Steel Functional Requirements

```text
FORMABILITY
DEEP_DRAWABILITY
HIGH_STRENGTH
VERY_HIGH_STRENGTH
CRASH_RESISTANCE
WEIGHT_REDUCTION
WELDABILITY
COATING_COMPATIBILITY
SURFACE_QUALITY
```

---

# 12.2 IF HSS

Canonical family:

```text
IF_HSS
```

Key combination:

```text
HIGH_STRENGTH
+
HIGH_R_VALUE
+
DEEP_DRAWABILITY
```

The POSCO catalog describes IF HSS as being used for components requiring both high strength and deep drawing capability.

Representative classes include:

```text
E_CLASS
ES_CLASS
YE_CLASS
```

---

# 12.3 Advanced High Strength Steel

Canonical code:

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

These must remain independent product-family codes.

---

# 12.4 DP — Dual Phase Steel

Canonical code:

```text
AUTOMOTIVE_DP
```

Typical characteristics:

```text
HIGH_STRENGTH
FORMABILITY
LOW_YIELD_RATIO
BAKE_HARDENABILITY
```

POSCO's automotive catalog identifies tensile-strength families including 490, 590, 780 and 980 MPa classes, with availability across CR/EG/GI/GA depending on grade.

Representative grade keys:

```text
490DP
590DP
780DP
980DP-M
980DP-H
980DP-EL
```

---

# 12.5 TRIP Steel

Canonical code:

```text
AUTOMOTIVE_TRIP
```

Core positioning:

```text
HIGH_STRENGTH
+
HIGH_ELONGATION
+
FORMABILITY
```

Representative retrieval keys:

```text
590TR
780TR
980TR
1180TR
```

The catalog contains TRIP grades reaching 1180 MPa class while retaining defined elongation requirements.

---

# 12.6 CP — Complex Phase Steel

Canonical code:

```text
AUTOMOTIVE_CP
```

Typical requirements:

```text
HIGH_YIELD_STRENGTH
HIGH_TENSILE_STRENGTH
BENDABILITY
CRASH_RESISTANCE
```

Representative retrieval keys:

```text
780CP
980CP
1180CP
```

CP is described as having a composite ferrite/bainite/martensite microstructure with high yield ratio and good bending performance.

---

# 12.7 FB — Ferrite Bainite Steel

Canonical code:

```text
AUTOMOTIVE_FB
```

Typical applications:

```text
SUSPENSION
LOWER_ARM
WHEEL_DISC
CHASSIS
```

Representative grade keys:

```text
440FB
540FB
590FB
780FB
```

The catalog explicitly associates FB hot-rolled products with suspensions and wheel discs.

---

# 12.8 MART — Martensitic Steel

Canonical code:

```text
AUTOMOTIVE_MART
```

Primary requirement:

```text
VERY_HIGH_STRENGTH
```

Trade-off:

```text
LOWER_DUCTILITY
```

Representative grade keys:

```text
1300M
1500M
1700M
```

Applications shown include:

```text
BUMPER_BEAM
SILL_SIDE_MEMBER
INNER_CROSS_MEMBER
SIDE_FRAME
BATTERY_PACK_STRUCTURE
```

POSCO lists martensitic automotive grades up to 1700 MPa class in the supplied catalog.

---

# 13. ATOS

Canonical product family:

```text
ATOS
```

Meaning:

```text
AUTOMOBILE_STRUCTURAL_HIGH_STRENGTH_STEEL
```

Primary application:

```text
TRUCK_FRAME
TRAILER_FRAME
BOOM_ARM
AUTOMOTIVE_STRUCTURE
```

Primary requirements:

```text
HIGH_STRENGTH
COLD_FORMABILITY
WEIGHT_REDUCTION
WELDABILITY
```

POSCO describes ATOS as automotive structural steel with tensile strength above 500 MPa and yield strength above 300 MPa, with ATOS780 specifically highlighted for high strength and cold formability.

Representative retrieval keys:

```text
ATOS540
ATOS590
ATOS780
```

ATOS is also referenced in the hot-rolled catalog for frames and wheels.

---

# 14. GALVANIZED_STEEL

Canonical code:

```text
GALVANIZED_STEEL
```

Primary requirements:

```text
CORROSION_RESISTANCE
FORMABILITY
WELDABILITY
PAINTABILITY
```

POSCO's catalog identifies galvanized steel use in automotive, electrical equipment, machinery, civil engineering and construction.

---

# 14.1 Galvanized Product Families

```text
GI
GA
GI_H
```

## GI

```text
HOT_DIP_GALVANIZED
```

Good surface uniformity and broad application.

Typical applications:

```text
AUTOMOTIVE_PANEL
HOME_APPLIANCE
BUILDING_MATERIAL
METAL_FURNITURE
PIPE
```

## GA

```text
GALVANNEALED
```

Important requirements:

```text
WELDABILITY
PAINTABILITY
PAINTED_CORROSION_RESISTANCE
```

The catalog states GA has better weldability and paintability than standard galvanized sheet due to its alloyed Zn-Fe coating.

## GI_H

Hot-rolled base galvanized steel.

Typical applications:

```text
BUILDING_MATERIAL
PIPE
ELECTRICAL_PANEL
SOLAR_SUPPORT
```

---

# 14.2 Galvanized Selection Rule

Product selection should consider:

```text
FINAL_USE
CORROSION_ENVIRONMENT
FORMING_METHOD
WELDING_REQUIREMENT
PAINTING_REQUIREMENT
COATING_WEIGHT
SURFACE_TREATMENT
```

The catalog explicitly notes that heavier coatings favor corrosion durability while lighter coatings favor formability and weldability.

---

# 15. ELECTRO_GALVANIZED_STEEL

Canonical code:

```text
ELECTRO_GALVANIZED_STEEL
```

Coating types supported by the supplied catalog:

```text
PURE_ZN
ZN_NI_ALLOY
```

Post-treatment concepts:

```text
PHOSPHATE
CR_FREE_RESIN
ANTI_CORROSION_OIL
```

Core requirements:

```text
CORROSION_RESISTANCE
FORMABILITY
WELDABILITY
PAINTABILITY
SURFACE_QUALITY
```

Applications include:

```text
AUTOMOTIVE
HOME_APPLIANCE
BUILDING_INTERIOR
METAL_FURNITURE
```

The catalog explicitly associates electrogalvanized products with these application areas.

---

# 16. POSMAC FAMILY

Parent code:

```text
POSMAC
```

Material category:

```text
ZN_MG_AL_ALLOY_COATED_STEEL
```

Subfamilies:

```text
POSMAC_1_5
POSMAC_3_0
POSMAC_SUPER
```

Never treat these three as identical products.

---

# 16.1 POSMAC_1_5

Canonical code:

```text
POSMAC_1_5
```

Source-defined coating:

```text
Zn - 1.5%Mg - 1.5%Al
```

Primary positioning:

```text
CORROSION_RESISTANCE
+
SURFACE_QUALITY
+
FORMABILITY
+
WELDABILITY
```

Particularly relevant to:

```text
AUTOMOTIVE
HOME_APPLIANCE
PRECOATED_STEEL
```

POSCO describes PosMAC 1.5 as having more than twice the corrosion resistance of ordinary hot-dip galvanized sheet at equivalent coating weight, while improving surface quality and weldability relative to PosMAC 3.0 for automotive/appliance applications.

---

# 16.2 POSMAC_3_0

Canonical code:

```text
POSMAC_3_0
```

Primary requirements:

```text
HIGH_CORROSION_RESISTANCE
CUT_EDGE_CORROSION_RESISTANCE
FORMED_SECTION_CORROSION_RESISTANCE
```

Strong application contexts:

```text
OUTDOOR_STRUCTURE
SOLAR_STRUCTURE
COASTAL_STRUCTURE
CORROSIVE_ENVIRONMENT
```

POSCO reports corrosion resistance of approximately 5–10 times ordinary hot-dip galvanized sheet in the documented comparative tests.

---

# 16.3 POSMAC_SUPER

Canonical code:

```text
POSMAC_SUPER
```

Source-defined coating concept:

```text
Zn - 5%Mg - 12%Al
```

Primary positioning:

```text
EXTREME_CORROSION_RESISTANCE
```

Relevant environments:

```text
HIGH_SALINITY
HIGH_HUMIDITY
MARINE
COASTAL
FLOATING_STRUCTURE
```

POSCO describes PosMAC Super as providing more than ten times the corrosion resistance of GI under the documented conditions, and positions it for high-salinity/high-humidity and coastal environments.

---

# 16.4 PosMAC Routing Rule

```text
CORROSION + SURFACE / WELDABILITY
→ POSMAC_1_5

SEVERE_CORROSION
→ POSMAC_3_0

EXTREME_MARINE / HIGH_SALINITY
→ POSMAC_SUPER
```

This is candidate routing only.

Detailed product-fit analysis is still required.

---

# 17. ELECTRICAL_STEEL

Parent code:

```text
ELECTRICAL_STEEL
```

Subcategories:

```text
NON_ORIENTED_ELECTRICAL_STEEL
GRAIN_ORIENTED_ELECTRICAL_STEEL
```

These must never be merged.

---

# 17.1 HYPER_NO

Canonical product family:

```text
HYPER_NO
```

Material category:

```text
NON_ORIENTED_ELECTRICAL_STEEL
```

Primary application:

```text
EV_TRACTION_MOTOR
```

Primary component:

```text
MOTOR_CORE
ROTOR_CORE
STATOR_CORE
```

Required properties:

```text
LOW_CORE_LOSS
LOW_HIGH_FREQUENCY_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_STRENGTH
THIN_GAUGE
ELECTRICAL_INSULATION
```

POSCO's Hyper NO catalog explicitly links low core loss, high yield strength and high flux density to EV motor efficiency, speed and torque requirements.

---

# 17.2 Hyper NO Series

```text
NEW_PNX
PNX_FY
PNX
PNF
```

Routing concept:

```text
NEW_PNX
→ LOWER_CORE_LOSS + HIGHER_STRENGTH

PNX_FY
→ HIGH_STRENGTH

PNX
→ LOW_CORE_LOSS + HIGH_STRENGTH

PNF
→ LOW_CORE_LOSS_AT_HIGH_FREQUENCY
```

Representative grades include:

```text
20PNX1250FY
25PNX1300FY
27PNX1400FY
30PNX1500FY
```

The PNX-FY section identifies these as high-strength cores optimized for EV traction motors.

Never select one specific Hyper NO grade only from an EV news article.

---

# 17.3 GRAIN_ORIENTED_ELECTRICAL_STEEL

Canonical code:

```text
GRAIN_ORIENTED_ELECTRICAL_STEEL
```

Knowledge status:

```text
DETAIL_SOURCE_PENDING
```

Reason:

The supplied GO document only states that the catalog is being revised.

Do not invent:

```text
grade
core loss
thickness
transformer-specific specification
```

until an approved detailed catalog is provided.

---

# 18. STEEL_PLATE

Parent code:

```text
STEEL_PLATE
```

This category must never be used alone for final product recommendations if the actual application is known.

Subcategories:

```text
SHIPBUILDING_PLATE
OFFSHORE_PLATE
LINE_PIPE_PLATE
PRESSURE_VESSEL_PLATE
CRYOGENIC_PLATE
CONSTRUCTION_PLATE
MECHANICAL_STRUCTURAL_PLATE
WEAR_RESISTANT_PLATE
HIGH_TENSILE_PLATE
MILITARY_PLATE
```

The POSCO plate catalog explicitly separates these product/application areas.

---

# 19. SHIPBUILDING_PLATE

Canonical code:

```text
SHIPBUILDING_PLATE
```

Applications:

```text
SHIP_HULL
CONTAINER_SHIP
LNG_CARRIER
TANKER
MARINE_STRUCTURE
```

Core requirements:

```text
HIGH_STRENGTH
TOUGHNESS
LOW_TEMPERATURE_TOUGHNESS
WELDABILITY
FATIGUE_RESISTANCE
BRITTLE_CRACK_RESISTANCE
```

Representative families include:

```text
A / B / D / E
AH32~EH40
EH47
LOW_TEMPERATURE_SERVICE_GRADES
EXTRA_HIGH_STRENGTH_GRADES
```

POSCO's catalog includes EH47 and high-heat-input welding products developed as ships become larger and demand increases for structural stability and weight reduction.

---

# 20. OFFSHORE_PLATE

Canonical code:

```text
OFFSHORE_PLATE
```

Applications:

```text
OIL_GAS_OFFSHORE_STRUCTURE
TOPSIDE
OFFSHORE_PLATFORM
OFFSHORE_WIND
TIDAL_POWER
PIPE_LAYING_VESSEL
```

Core requirements:

```text
HIGH_STRENGTH
FRACTURE_TOUGHNESS
CTOD
LOW_TEMPERATURE_TOUGHNESS
WELDABILITY
THROUGH_THICKNESS_PERFORMANCE
```

POSCO states offshore plates are used for oil/gas exploration, drilling, production and storage structures as well as offshore wind, tidal power and pipe-laying vessels.

---

# 21. LINE_PIPE_PLATE

Canonical code:

```text
LINE_PIPE_PLATE
```

Primary application:

```text
OIL_PIPELINE
GAS_PIPELINE
ENERGY_TRANSPORT_PIPELINE
```

Primary requirements:

```text
HIGH_STRENGTH
WELDABILITY
LOW_TEMPERATURE_TOUGHNESS
HIC_RESISTANCE
SOUR_SERVICE
```

Representative API grade families:

```text
B
X42
X46
X52
X56
X60
X65
X70
X80
X100
```

POSCO's plate catalog separately records non-sour and sour-service line-pipe supply and mechanical property classes.

---

# 22. API_STEEL

Canonical code:

```text
API_STEEL
```

Primary specification families:

```text
API_5L
API_5CT
API_2W
API_2H
```

Application routing:

```text
API_5L
→ PIPELINE

API_5CT
→ OILWELL_CASING_TUBING

API_2W / API_2H
→ OFFSHORE_STRUCTURE
```

Service classes:

```text
GENERAL_SERVICE
SOUR_SERVICE
ARCTIC_SERVICE
HIGH_STRENGTH_SERVICE
```

POSCO's API catalog identifies API-5L for pipelines, API-5CT for casing/tubing and API-2W/2H for offshore structures.

---

# 23. PRESSURE_VESSEL_PLATE

Canonical code:

```text
PRESSURE_VESSEL_PLATE
```

Applications:

```text
PRESSURE_VESSEL
BOILER
PETROCHEMICAL_VESSEL
ENERGY_PROCESS_EQUIPMENT
STORAGE_VESSEL
```

Important requirements:

```text
PRESSURE_RESISTANCE
WELDABILITY
IMPACT_TOUGHNESS
PWHT_COMPATIBILITY
HIC_RESISTANCE
```

Representative specification families include:

```text
A516
A537
A387
A299
A302
```

The supplied plate catalog contains both HIC-guaranteed and non-HIC variants and supplementary low-temperature/through-thickness requirements. 

---

# 24. CRYOGENIC_PLATE

Canonical code:

```text
CRYOGENIC_PLATE
```

Primary applications:

```text
LNG_STORAGE_TANK
LNG_CARRIER
CRYOGENIC_VESSEL
```

Subfamilies:

```text
9_PERCENT_NI_STEEL
5_PERCENT_NI_STEEL
3_5_PERCENT_NI_STEEL
HIGH_MN_CRYOGENIC_STEEL
```

Key requirements:

```text
CRYOGENIC_TOUGHNESS
HIGH_STRENGTH
FRACTURE_TOUGHNESS
WELDABILITY
```

POSCO's 9% Ni steel is identified for LNG storage tank inner-shell and bottom-plate applications with cryogenic performance at -196°C.

---

# 25. CONSTRUCTION_PLATE

Canonical code:

```text
CONSTRUCTION_PLATE
```

Subfamilies:

```text
BUILDING_STRUCTURE_PLATE
BRIDGE_PLATE
WEATHERING_PLATE
SEISMIC_PLATE
HIGH_PERFORMANCE_ARCHITECTURAL_PLATE
MARINE_PORT_CORROSION_RESISTANT_PLATE
```

Representative POSCO families:

```text
PILAC
HSB
HSA
HSM380
```

The plate catalog maps PILAC to building structures, HSB to bridge structures and HSM380 to port/offshore corrosion-resistant structures.

HSA is described as combining high strength with seismic performance for architectural structures.

---

# 26. MECHANICAL_STRUCTURAL_PLATE

Canonical code:

```text
MECHANICAL_STRUCTURAL_PLATE
```

Applications:

```text
HEAVY_EQUIPMENT
CRANE
BOOM
FRAME
INDUSTRIAL_MACHINE
MOLD
```

Core requirements:

```text
HIGH_STRENGTH
WELDABILITY
BENDABILITY
TOUGHNESS
```

---

# 27. POS_TEN

Canonical product family:

```text
POS_TEN
```

Material category:

```text
HIGH_TENSILE_PLATE
```

Primary applications:

```text
HEAVY_EQUIPMENT
CRANE
BOOM
HIGH_LOAD_STRUCTURE
```

Representative grades:

```text
PosTen690
PosTen780
PosTen780MT
```

The supplied product guide is specifically positioned as high-performance high-tensile plate for heavy equipment.

Routing requirements:

```text
HIGH_STRENGTH
BENDABILITY
WELDABILITY
TOUGHNESS
WEIGHT_REDUCTION
```

---

# 28. POS_AR

Canonical product family:

```text
POS_AR
```

Material category:

```text
WEAR_RESISTANT_PLATE
```

Representative grades:

```text
POS_AR400
POS_AR450
POS_AR500
```

Primary requirements:

```text
WEAR_RESISTANCE
ABRASION_RESISTANCE
HIGH_HARDNESS
HIGH_STRENGTH
IMPACT_TOUGHNESS
```

Primary applications:

```text
EXCAVATOR
DUMP_BODY
BUCKET
CHUTE
LINER
HEAVY_EQUIPMENT
```

The PosAR catalog presents 400/450/500 hardness-class grades for high-performance wear-resistant heavy-equipment plate.

---

# 29. HIGH_MN_WEAR_RESISTANT_STEEL

Canonical code:

```text
HIGH_MN_WEAR_RESISTANT_STEEL
```

Representative product key:

```text
POSM_XD70
```

Primary characteristics:

```text
HIGH_STRENGTH
WORK_HARDENING
ABRASION_RESISTANCE
EROSION_RESISTANCE
```

Applications:

```text
ORE_SLURRY_PIPE
COAL_SLURRY_PIPE
CHUTE
LINER
SCREEN
MINING_EQUIPMENT
```

POSCO describes this high-Mn steel as improving wear resistance through high strength and work hardening in severe erosion environments.

---

# 30. HIGH_CARBON_STEEL

Canonical code:

```text
HIGH_CARBON_STEEL
```

Primary requirements:

```text
HIGH_STRENGTH
HIGH_HARDNESS
WEAR_RESISTANCE
HEAT_TREATABILITY
FATIGUE_RESISTANCE
```

POSCO states that high-carbon steel is primarily used in mechanical parts requiring high strength/hardness and often achieves its final properties through quenching and tempering.

---

# 30.1 High Carbon Application Families

```text
AUTOMOTIVE_CLUTCH
SEAT_RECLINER
SAFETY_BELT
HOSE_CLIP
SAW_BLADE
CHAIN
KNITTING_NEEDLE
CUTTER
FARM_TOOL
SPRING_COMPONENT
BEARING_COMPONENT
```

Representative retrieval grades include:

```text
S45C
S50C
S55C
SK85
SK105
SCM435
SNCM220
50CrV4
51CrV4
SAE1055
SAE1078
POS10B35
POS10B50
AUTOBEAM
```

POSCO's catalog lists a broad grade structure across machine structural, tool and alloy high-carbon steels.

---

# 31. WIRE_ROD

Canonical code:

```text
WIRE_ROD
```

Do not treat wire rod as one generic product.

Major families:

```text
LOW_CARBON_WIRE_ROD
HIGH_CARBON_WIRE_ROD
PIANO_WIRE_ROD
TIRE_CORD_WIRE_ROD
PC_WIRE_ROD
FREE_CUTTING_WIRE_ROD
COLD_HEADING_WIRE_ROD
BEARING_STEEL_WIRE_ROD
SPRING_STEEL_WIRE_ROD
MACHINE_STRUCTURAL_WIRE_ROD
```

---

# 31.1 Low Carbon Wire Rod

Applications:

```text
GALVANIZED_WIRE
GENERAL_WIRE
```

Representative retrieval keys:

```text
POSFIS5M1
POSFIS6M1
POSFIS6B
```

---

# 31.2 High Carbon Wire Rod

Applications:

```text
WIRE_ROPE
PRECISION_SPRING
BEAD_WIRE
PC_WIRE
```

Requirements:

```text
HIGH_STRENGTH
DRAWABILITY
FATIGUE_RESISTANCE
MICROSTRUCTURE_CONTROL
```

POSCO states that high-carbon wire rod requires fine-pearlite control to maintain strength and wire-drawing performance.

---

# 31.3 Piano Wire Rod

Applications:

```text
BEAD_WIRE
PC_WIRE
BRIDGE_CABLE
```

Requirements:

```text
VERY_HIGH_STRENGTH
FINE_WIRE_DRAWABILITY
FATIGUE_RESISTANCE
CLEANLINESS
```

Representative retrieval keys:

```text
POSCABLE82
POSCABLE86
POSCABLE90
POSCABLE92
POSMICRO62
POSCABLE98
```

---

# 31.4 Tire Cord Wire Rod

Canonical code:

```text
TIRE_CORD_WIRE_ROD
```

Application:

```text
TIRE_REINFORCEMENT
```

Requirements:

```text
HIGH_STRENGTH
FINE_DRAWABILITY
FATIGUE_RESISTANCE
CLEANLINESS
DYNAMIC_LOAD_RESISTANCE
```

Representative retrieval keys:

```text
POSCORD60M
POSCORD70
POSCORD80
POSCORD86
POSCORD92
```

The catalog describes tire-cord wire rod as ultra-fine drawn wire required to withstand high-speed processing and dynamic tire loads.

---

# 31.5 Bearing Steel Wire Rod

Canonical code:

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

Representative retrieval keys:

```text
POS55CR
POSWIND100
SUJ2
100CR6
SAE52100
```

POSCO states that bearings operating under high load and high speed require wear resistance, fatigue performance, cleanliness and homogeneous internal structure.

---

# 32. STAINLESS_STEEL

Canonical code:

```text
STAINLESS_STEEL
```

Primary subfamilies:

```text
AUSTENITIC_STAINLESS
FERRITIC_STAINLESS
MARTENSITIC_STAINLESS
DUPLEX_STAINLESS
```

Never choose a stainless grade solely from the word:

```text
CORROSION
```

Environment, temperature, forming and welding requirements must be considered.

---

# 32.1 Austenitic Stainless

Representative keys:

```text
301
301L
304
304L
316
316L
316Ti
321
```

Typical requirements:

```text
CORROSION_RESISTANCE
FORMABILITY
LOW_TEMPERATURE_PERFORMANCE
INTERGRANULAR_CORROSION_RESISTANCE
HEAT_RESISTANCE
```

304/304L are shown across household, automotive, medical, construction, chemical, food, ship and LNG/heat-exchanger applications.

316/316L are associated with chemical, food, piping, heat exchangers and corrosive coastal environments.

---

# 32.2 Automotive Exhaust Stainless

Relevant grade keys include:

```text
409L
429EM
430J1L
436L
439
AL439
441
304L
316L
310S
```

Applications:

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

The catalog explicitly maps these grade families to individual automotive exhaust components.

---

# 33. TITANIUM

Canonical code:

```text
TITANIUM
```

Material class:

```text
NON_FERROUS_METAL
```

Key source-supported properties:

```text
LIGHTWEIGHT
HIGH_SPECIFIC_STRENGTH
CORROSION_RESISTANCE
SEAWATER_CORROSION_RESISTANCE
LOW_THERMAL_EXPANSION
NON_MAGNETIC
FORMABILITY
NON_TOXIC
```

POSCO's catalog describes titanium as roughly 60% of steel's specific gravity, with steel-like strength, strong seawater corrosion resistance and non-magnetic characteristics.

---

# 33.1 Titanium Industries

```text
AEROSPACE
DEFENSE
AUTOMOTIVE
SHIPBUILDING
MARINE
NUCLEAR_POWER
CHEMICAL
FOOD
CONSTRUCTION
BIOMEDICAL
SPORTS
CONSUMER_PRODUCTS
```

The Titanium Application guide explicitly spans these industrial sectors.

---

# 33.2 Titanium Aerospace

Key requirements:

```text
LIGHTWEIGHT
HIGH_SPECIFIC_STRENGTH
FATIGUE_RESISTANCE
FRACTURE_TOUGHNESS
CORROSION_RESISTANCE
```

Example applications:

```text
LANDING_GEAR_STRUCTURE
PYLON
FLAP_TRACK
SPAR
FASTENER
ENGINE_NACELLE
AIRCRAFT_ENGINE
```

The aerospace guide specifically cites Ti-6Al-4V for several high-strength structural applications.

---

# 33.3 Titanium Heat Exchanger

Representative standard-grade keys:

```text
ASTM_B265_GR1
ASTM_B265_GR2
ASME_SB265_GR1
ASME_SB265_GR2
JIS_H4600_CLASS1
JIS_H4600_CLASS2
```

POSCO states that HR/CR titanium coils are used for heat-exchanger tubes in nuclear/thermal power and plate heat exchangers in marine applications.

---

# 34. ANCOR

Canonical product family:

```text
ANCOR
```

Parent category:

```text
ACID_CORROSION_RESISTANT_STEEL
```

Subfamilies:

```text
ANCOR
ANCOR_S
ANCOR_C
ANCOR_CS
ANCOR_H
```

Naming differs according to product form/catalog context.

Do not automatically treat every ANCOR suffix as interchangeable.

---

# 34.1 ANCOR Requirements

```text
SULFURIC_ACID_CORROSION_RESISTANCE
COMPOSITE_ACID_CORROSION_RESISTANCE
DEW_POINT_CORROSION_RESISTANCE
WELDABILITY
```

Primary applications:

```text
THERMAL_POWER_PLANT
BOILER
AIR_PREHEATER
DESULFURIZATION
SCR
ELECTROSTATIC_PRECIPITATOR
DUCT
GGH
EXHAUST_GAS_SYSTEM
```

POSCO states that ANCOR targets sulfuric-acid and sulfuric/hydrochloric composite-acid corrosion, particularly low-temperature dew-point corrosion in power-generation exhaust environments.

Cold-rolled ANCOR-C/CS is also mapped to boiler ducts, SCR, air preheaters, GGH, ESP and desulfurization systems.

---

# 35. POSLOOP355

Canonical code:

```text
POSLOOP355
```

Parent category:

```text
HYPERLOOP_TUBE_STEEL
```

Primary application:

```text
HYPERLOOP_TUBE
```

Key requirements:

```text
STRUCTURAL_STRENGTH
WELDABILITY
IMPACT_TOUGHNESS
DIMENSIONAL_PRECISION
VIBRATION_DAMPING
LARGE_DIAMETER_TUBE_MANUFACTURABILITY
```

The supplied guide defines PosLoop355 with minimum yield strength of 355 MPa, tensile strength 470–630 MPa, elongation and -20°C impact requirements and specific tube-tolerance criteria.

The product development also includes spiral-pipe manufacturability and full-scale vibration-damping evaluation.

Do not generalize PosLoop355 to ordinary pipeline applications.

---

# 36. LOW_CARBON_STEEL_ATTRIBUTE

Low-carbon steel should be modeled as a cross-cutting product attribute rather than a standalone mechanical material category.

Canonical attribute:

```text
LOW_CARBON_STEEL
```

Supporting production routes may include:

```text
SCRAP_DOUBLE_CHARGING
EAF_ROUTE
FUTURE_HYREX_ROUTE
```

POSCO reports that sales of steel produced using double scrap charging began in 2025, with a target of roughly 10% carbon reduction versus the referenced baseline; the company also plans expanded scrap-based steel production via the Gwangyang EAF.

The sustainability report separately identifies:

```text
double scrap charging
→ target ~10% reduction

large EAF
→ target up to ~75% reduction
```

subject to the stated calculation assumptions.

---

# 36.1 Low Carbon Guardrail

Do not claim that every grade is automatically available as:

```text
LOW_CARBON
```

Availability must be verified by:

```text
product
production route
period
customer specification
carbon-footprint verification
```

---

# 37. Material Family Registry

Use this compact registry for first-stage retrieval.

| Code | Product / Material Family | Primary Requirement |
|---|---|---|
| HOT_ROLLED_STEEL | 열연강재 | strength / forming / structural |
| COLD_ROLLED_STEEL | 냉연강판 | surface / forming |
| AUTOMOTIVE_STEEL | 자동차강판 | lightweight / crash / forming |
| AUTOMOTIVE_DP | DP강 | strength + forming |
| AUTOMOTIVE_TRIP | TRIP강 | strength + elongation |
| AUTOMOTIVE_CP | CP강 | yield strength + bendability |
| AUTOMOTIVE_FB | FB강 | chassis forming / strength |
| AUTOMOTIVE_MART | MART강 | ultra-high strength |
| ATOS | 자동차구조용 고강도강 | structural strength / weight reduction |
| HIGH_CARBON_STEEL | 고탄소강 | hardness / heat treatment |
| WIRE_ROD | 선재 | drawing / fatigue / cleanliness |
| GALVANIZED_STEEL | GI / GA / GI(H) | corrosion + forming |
| ELECTRO_GALVANIZED_STEEL | EG | surface + corrosion + painting |
| POSMAC_1_5 | PosMAC 1.5 | corrosion + surface + weldability |
| POSMAC_3_0 | PosMAC 3.0 | severe corrosion |
| POSMAC_SUPER | PosMAC Super | extreme corrosion |
| HYPER_NO | Hyper NO | EV motor electromagnetic performance |
| SHIPBUILDING_PLATE | 조선용 후판 | toughness + weldability |
| OFFSHORE_PLATE | 해양구조용 후판 | CTOD + low-temp toughness |
| LINE_PIPE_PLATE | 라인파이프 후판 | strength + HIC / sour service |
| API_STEEL | API Steel | energy transport / extraction |
| PRESSURE_VESSEL_PLATE | 압력용기 후판 | pressure + toughness |
| CRYOGENIC_PLATE | 극저온용강 | cryogenic toughness |
| CONSTRUCTION_PLATE | 건설구조용 후판 | structure / seismic |
| POS_TEN | PosTen | high tensile heavy equipment |
| POS_AR | PosAR | wear resistance |
| HIGH_MN_WEAR_RESISTANT_STEEL | 고망간 내마모강 | erosion / abrasion |
| STAINLESS_STEEL | 스테인리스 | corrosion / heat |
| TITANIUM | 티타늄 | lightweight / corrosion |
| ANCOR | 내황산강 | acid corrosion |
| POSLOOP355 | Hyperloop tube steel | tube structure / vibration |
| LOW_CARBON_STEEL | 탄소저감 강재 속성 | embodied carbon reduction |

---

# 38. Industry-to-Material Routing

## AUTOMOTIVE

Primary material candidates:

```text
AUTOMOTIVE_STEEL
AUTOMOTIVE_DP
AUTOMOTIVE_TRIP
AUTOMOTIVE_CP
AUTOMOTIVE_FB
AUTOMOTIVE_MART
ATOS
HYPER_NO
GALVANIZED_STEEL
ELECTRO_GALVANIZED_STEEL
POSMAC_1_5
STAINLESS_STEEL
HIGH_CARBON_STEEL
WIRE_ROD
```

Do not retrieve all candidates at once.

Application and component must narrow the list.

---

# 39. Automotive Component Routing

```text
BODY_IN_WHITE
→ AUTOMOTIVE_STEEL / AHSS

CRASH_MEMBER
→ CP / MART / DP candidates

OUTER_PANEL
→ FORMABLE_AUTOMOTIVE_STEEL / COATED_AUTOMOTIVE_STEEL

CHASSIS
→ FB / ATOS / HOT_ROLLED_HIGH_STRENGTH

EV_MOTOR_CORE
→ HYPER_NO

BATTERY_PACK_STRUCTURE
→ AHSS / MART candidates

EXHAUST_SYSTEM
→ STAINLESS_STEEL

CLUTCH / RECLINER / SAFETY_COMPONENT
→ HIGH_CARBON_STEEL

TIRE_REINFORCEMENT
→ TIRE_CORD_WIRE_ROD
```

---

# 40. SHIPBUILDING Routing

```text
HULL
→ SHIPBUILDING_PLATE

HIGH_STRENGTH_HULL
→ HIGH_STRENGTH_SHIPBUILDING_PLATE

OFFSHORE_STRUCTURE
→ OFFSHORE_PLATE

LNG_TANK
→ CRYOGENIC_PLATE / STAINLESS / TITANIUM depending component

LNG_STORAGE_INNER_SHELL
→ 9_PERCENT_NI_STEEL candidate

MARINE_HEAT_EXCHANGER
→ TITANIUM candidate
```

---

# 41. ENERGY Routing

```text
OIL_GAS_PIPELINE
→ API_STEEL / LINE_PIPE_PLATE

SOUR_PIPELINE
→ HIC / SOUR_SERVICE LINE_PIPE

OFFSHORE_PLATFORM
→ OFFSHORE_PLATE

LNG_STORAGE
→ CRYOGENIC_PLATE

POWER_PLANT_EXHAUST
→ ANCOR

PRESSURE_VESSEL
→ PRESSURE_VESSEL_PLATE

TRANSFORMER_CORE
→ GRAIN_ORIENTED_ELECTRICAL_STEEL
```

GO detailed product matching remains:

```text
DETAIL_SOURCE_PENDING
```

---

# 42. CONSTRUCTION Routing

```text
BUILDING_STRUCTURE
→ CONSTRUCTION_PLATE

SEISMIC_BUILDING
→ PILAC / HSA candidate

BRIDGE
→ HSB candidate

WEATHERING_STRUCTURE
→ WEATHERING_STEEL

COASTAL_STRUCTURE
→ HSM / POSMAC candidate depending geometry

SOLAR_SUPPORT
→ GALVANIZED / POSMAC candidate
```

---

# 43. MACHINERY Routing

```text
HEAVY_EQUIPMENT_STRUCTURE
→ POS_TEN / ATOS

ABRASIVE_COMPONENT
→ POS_AR

MINING_CHUTE / LINER
→ POS_AR / HIGH_MN_WEAR_RESISTANT_STEEL

GEAR / SHAFT / CHAIN
→ HIGH_CARBON_STEEL / WIRE_ROD

BEARING
→ BEARING_STEEL_WIRE_ROD
```

---

# 44. Product Candidate Selection Rules

Use the following order.

```text
1. APPLICATION
2. COMPONENT
3. OPERATING ENVIRONMENT
4. REQUIRED PERFORMANCE
5. MATERIAL REQUIREMENTS
6. PRODUCT FAMILY
7. SPECIFIC PRODUCT DOCUMENT
8. GRADE
```

Do not reverse this logic.

---

# 45. Material Candidate Score

Suggested candidate-scoring logic:

```text
Application Match          25%
Component Match            20%
Required Property Match    25%
Environment Match          15%
Manufacturing Match        10%
Evidence Completeness       5%
```

Total:

```text
0 - 100
```

Recommended interpretation:

```text
90-100
STRONG_CANDIDATE

80-89
GOOD_CANDIDATE

70-79
POSSIBLE_CANDIDATE

60-69
WEAK_CANDIDATE

<60
DO_NOT_RECOMMEND
```

---

# 46. Grade Recommendation Threshold

Do not recommend a specific grade unless:

```text
application confidence >= 80
AND
component confidence >= 75
AND
product evidence exists
AND
critical operating conditions are known
```

For safety-critical or highly technical applications:

```text
engineering review required
```

---

# 47. Unknown Handling

Supported states:

```text
MATERIAL_UNKNOWN

MATERIAL_MATCH_UNKNOWN

PRODUCT_FAMILY_UNKNOWN

GRADE_UNKNOWN

DETAIL_SOURCE_PENDING

ENGINEERING_REVIEW_REQUIRED

APPLICATION_CONDITION_REQUIRED
```

Unknown is preferable to hallucination.

---

# 48. Product Knowledge Status

Use:

```text
VERIFIED
PARTIAL
DETAIL_SOURCE_PENDING
SUPERSEDED
DEPRECATED
UNKNOWN
```

Current status examples:

```text
HYPER_NO
→ VERIFIED

POSMAC_1_5
→ VERIFIED

POSMAC_3_0
→ VERIFIED

POSMAC_SUPER
→ VERIFIED

ATOS
→ VERIFIED

POS_TEN
→ VERIFIED

POS_AR
→ VERIFIED

ANCOR
→ VERIFIED

POSLOOP355
→ VERIFIED

GRAIN_ORIENTED_ELECTRICAL_STEEL
→ DETAIL_SOURCE_PENDING
```

---

# 49. Product Source Metadata

Every product-family record should eventually contain:

```yaml
code:
name_ko:
name_en:

material_category:

requirements:
applications:
industries:

product_series:
representative_grades:

knowledge_status:

source:
  document:
  year:
  page:
  section:

last_reviewed:
```

---

# 50. Retrieval Metadata

Every POSCO product MD should contain frontmatter.

Recommended format:

```yaml
---
product_family: HYPER_NO

material_category:
  - NON_ORIENTED_ELECTRICAL_STEEL

industries:
  - AUTOMOTIVE

applications:
  - EV_MOTOR

components:
  - MOTOR_CORE
  - ROTOR_CORE
  - STATOR_CORE

requirements:
  - LOW_CORE_LOSS
  - HIGH_MAGNETIC_FLUX_DENSITY
  - HIGH_STRENGTH

source:
  - 2025 Hyper NO.pdf

status: VERIFIED
---
```

---

# 51. Recommended Product Knowledge Folder

Do not store all product knowledge in this one taxonomy file.

Recommended structure:

```text
knowledge/
├── taxonomy/
│   ├── industries.md
│   ├── events.md
│   ├── strategies.md
│   ├── applications.md
│   └── materials.md
│
└── posco/
    ├── index.md
    │
    ├── automotive/
    │   ├── index.md
    │   ├── automotive-steel.md
    │   ├── atos.md
    │   └── hyper-no.md
    │
    ├── coated/
    │   ├── index.md
    │   ├── galvanized.md
    │   ├── electro-galvanized.md
    │   ├── posmac-1.5.md
    │   ├── posmac-3.0.md
    │   └── posmac-super.md
    │
    ├── plate/
    │   ├── index.md
    │   ├── shipbuilding.md
    │   ├── offshore.md
    │   ├── line-pipe.md
    │   ├── pressure-vessel.md
    │   ├── cryogenic.md
    │   ├── construction.md
    │   ├── posten.md
    │   └── posar.md
    │
    ├── carbon/
    │   ├── hot-rolled.md
    │   ├── cold-rolled.md
    │   ├── high-carbon.md
    │   └── wire-rod.md
    │
    ├── stainless/
    │   └── stainless.md
    │
    ├── titanium/
    │   ├── titanium.md
    │   └── titanium-applications.md
    │
    ├── energy/
    │   ├── api-steel.md
    │   └── ancor.md
    │
    └── future/
        ├── posloop355.md
        └── low-carbon-steel.md
```

---

# 52. Retrieval Cost Rule

Never recursively scan:

```text
knowledge/posco/
```

Required routing:

```text
materials.md
↓
knowledge/posco/index.md
↓
industry/product index
↓
1-3 candidate product documents
```

Example:

```text
EV MOTOR
↓
materials.md
↓
NON_ORIENTED_ELECTRICAL_STEEL
↓
HYPER_NO
↓
knowledge/posco/automotive/hyper-no.md
```

Do not read:

```text
plate/
stainless/
titanium/
posmac/
wire rod
```

for an EV motor-core question.

---

# 53. Product Search Example — EV Investment

Input:

```text
Hyundai Motor expands EV production.
```

Analysis:

```text
INDUSTRY
AUTOMOTIVE

STRATEGY
ELECTRIFICATION
GROWTH

APPLICATION
EV_MOTOR

COMPONENT
MOTOR_CORE

REQUIREMENTS
LOW_CORE_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_STRENGTH

MATERIAL
NON_ORIENTED_ELECTRICAL_STEEL

PRODUCT FAMILY
HYPER_NO
```

Only then retrieve:

```text
hyper-no.md
```

---

# 54. Product Search Example — Offshore Wind

Input:

```text
Customer invests in offshore wind foundations.
```

Analysis:

```text
INDUSTRY
ENERGY

APPLICATION
OFFSHORE_WIND

COMPONENT
MONOPILE / JACKET

ENVIRONMENT
MARINE

REQUIREMENTS
HIGH_STRENGTH
FATIGUE_RESISTANCE
WELDABILITY
CORROSION_RESISTANCE

MATERIAL CANDIDATES
OFFSHORE_PLATE
CONSTRUCTION_PLATE
```

Do not automatically recommend PosMAC.

Geometry and thickness may favor plate rather than coated sheet.

---

# 55. Product Search Example — Coastal Solar

```text
APPLICATION
SOLAR_STRUCTURE

ENVIRONMENT
COASTAL

COMPONENT
SUPPORT_FRAME

REQUIREMENTS
CORROSION_RESISTANCE
CUT_EDGE_CORROSION_RESISTANCE
LONG_SERVICE_LIFE

CANDIDATES
POSMAC_3_0
POSMAC_SUPER
GALVANIZED_STEEL
```

Use environment severity to rank candidates.

---

# 56. Product Search Example — Mining

```text
APPLICATION
MINING_EQUIPMENT

COMPONENT
CHUTE / LINER

ENVIRONMENT
ABRASIVE

REQUIREMENT
WEAR_RESISTANCE

CANDIDATES
POS_AR
HIGH_MN_WEAR_RESISTANT_STEEL
```

The system must not recommend a structural high-tensile product merely because it has high strength.

---

# 57. Product Search Example — LNG Tank

```text
APPLICATION
LNG_STORAGE

ENVIRONMENT
CRYOGENIC

COMPONENT
INNER_SHELL / BOTTOM

REQUIREMENTS
CRYOGENIC_TOUGHNESS
HIGH_STRENGTH
FRACTURE_TOUGHNESS

CANDIDATES
9_PERCENT_NI_STEEL
HIGH_MN_CRYOGENIC_STEEL
```

Do not automatically select stainless or titanium without component-specific evidence.

---

# 58. Product Search Example — Power Plant Exhaust

```text
APPLICATION
THERMAL_POWER_EXHAUST

ENVIRONMENT
SULFURIC_ACID_DEW_POINT

REQUIREMENT
SULFURIC_ACID_CORROSION_RESISTANCE

PRODUCT FAMILY
ANCOR
```

If HCl is also significant:

```text
COMPOSITE_ACID_CORROSION_RESISTANCE
```

must be included.

---

# 59. Product Search Example — Heavy Equipment

```text
APPLICATION
CRANE_BOOM

REQUIREMENTS
HIGH_STRENGTH
WEIGHT_REDUCTION
BENDABILITY
WELDABILITY

CANDIDATE
POS_TEN
```

For:

```text
EXCAVATOR_BUCKET
```

requirements change to:

```text
WEAR_RESISTANCE
ABRASION_RESISTANCE
```

candidate:

```text
POS_AR
```

This distinction is critical.

---

# 60. Low Carbon Opportunity Layer

Low-carbon attributes are applied after technical fit.

Required sequence:

```text
Technical Material Fit
↓
Product Family Fit
↓
Low Carbon Availability Check
↓
Carbon Reduction Opportunity
```

Do not do:

```text
customer wants low carbon
→ recommend arbitrary low-carbon steel
```

---

# 61. Marketing Intelligence Fields

For each matched material opportunity, return:

```json
{
  "application": "",
  "component": "",
  "environment": [],
  "required_properties": [],
  "material_category": "",
  "product_family_candidates": [],
  "technical_fit_score": 0,
  "commercial_relevance": "",
  "missing_information": [],
  "confidence": 0,
  "sources": []
}
```

---

# 62. Missing Information

Before detailed recommendation, check for missing:

```text
component
operating temperature
corrosion environment
required strength
required thickness
forming method
welding process
surface requirement
regulatory specification
service life
pressure
fatigue condition
customer qualification
```

When critical:

```text
ENGINEERING_REVIEW_REQUIRED
```

---

# 63. Product Recommendation Language

Allowed:

```text
candidate
potential fit
relevant product family
should be evaluated
appears aligned with
```

Avoid without verified evidence:

```text
perfect fit
best product
guaranteed
fully suitable
must use
```

---

# 64. Numeric Data Rule

Do not copy large specification tables into intelligence output.

Numeric values should only be loaded when required for:

```text
specific grade comparison
engineering evaluation
customer specification
technical proposal
```

This keeps context cost low.

---

# 65. Material Brain vs Product Brain

`materials.md` is:

```text
MATERIAL BRAIN
```

It answers:

```text
What kind of material or POSCO product family should be investigated?
```

Detailed product MD files are:

```text
PRODUCT BRAIN
```

They answer:

```text
Which exact product / grade / specification may fit?
```

These two layers must remain separate.

---

# 66. Evidence Rule

Every final product recommendation must preserve:

```text
EVENT EVIDENCE
+
APPLICATION REASONING
+
MATERIAL REQUIREMENT
+
POSCO PRODUCT EVIDENCE
```

Required explainability chain:

```text
Customer expands EV motor production

→ motor-core demand may increase

→ low core loss and magnetic performance required

→ non-oriented electrical steel relevant

→ Hyper NO identified in approved POSCO catalog

→ specific grade requires motor-condition review
```

---

# 67. Product Hallucination Guardrail

Never invent:

```text
POSCO product name
POSCO grade
yield strength
tensile strength
coating amount
core loss
magnetic flux
temperature rating
certification
production status
customer adoption
```

If unavailable:

```text
UNKNOWN
```

---

# 68. Taxonomy Expansion Rule

Before adding a new material family, verify:

```text
1. It is supported by approved product evidence.
2. Existing taxonomy cannot represent it.
3. It changes product retrieval.
4. It has distinct material requirements.
5. It has repeated business relevance.
```

Record important changes in:

```text
docs/decisions.md
```

---

# 69. Final Material Intelligence Chain

The platform must use:

```text
INDUSTRY SIGNAL
↓
EVENT
↓
STRATEGY
↓
APPLICATION
↓
COMPONENT
↓
ENVIRONMENT
↓
REQUIRED PERFORMANCE
↓
MATERIAL REQUIREMENTS
↓
MATERIAL CATEGORY
↓
POSCO PRODUCT FAMILY
↓
PRODUCT DOCUMENT
↓
GRADE / TECHNICAL FIT
↓
COMMERCIAL OPPORTUNITY
```

---

# 70. Final Rule

This file is not designed to make the AI recommend as many POSCO products as possible.

It is designed to make the AI recommend only products that have a defensible technical and business relationship to the customer's industrial change.

The preferred behavior is:

```text
FEW CANDIDATES
+
STRONG APPLICATION LOGIC
+
APPROVED PRODUCT EVIDENCE
+
CLEAR UNCERTAINTY
+
TRACEABLE REASONING
```

rather than:

```text
MANY PRODUCTS
+
KEYWORD MATCHING
+
UNSUPPORTED SPECIFICATIONS
+
CONFIDENT HALLUCINATION
```

The goal of the Material Brain is:

```text
INDUSTRY CHANGE
→ PHYSICAL DEMAND CHANGE
→ MATERIAL REQUIREMENT
→ POSCO CAPABILITY
→ MARKETING OPPORTUNITY
```

with minimum search cost and maximum explainability.
