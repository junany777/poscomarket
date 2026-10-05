# Application Taxonomy and Mapping Rules

## 1. Purpose

This document defines the standard industrial application taxonomy used by the Steel Market Intelligence Platform.

Applications connect industry events and company strategies to physical products, components, material requirements, and steel categories.

The core reasoning chain is:

```text
Industry
↓
Application
↓
Component
↓
Material Requirement
↓
Steel Category
↓
POSCO Product Retrieval
```

Applications must not be confused with industries, technologies, products, or event types.

---

# 2. Core Principle

An Application represents:

```text
where steel or steel-related materials are physically or functionally used
```

Example:

```text
Industry:
AUTOMOTIVE

Application:
EV_MOTOR

Component:
MOTOR_CORE

Material Requirement:
LOW_MAGNETIC_LOSS

Steel Category:
ELECTRICAL_STEEL
```

The application layer exists to prevent direct reasoning such as:

```text
EV investment
→ POSCO product
```

Instead use:

```text
EV investment
→ EV production increase
→ EV motor
→ motor core
→ electrical performance requirement
→ electrical steel
→ POSCO product retrieval
```

---

# 3. Taxonomy Levels

Use the following hierarchy:

```text
LEVEL 1
Industry

LEVEL 2
Application

LEVEL 3
Component

LEVEL 4
Material Requirement

LEVEL 5
Steel Category
```

Industry taxonomy is maintained in:

```text
knowledge/taxonomy/industries.md
```

Material taxonomy is maintained in:

```text
knowledge/taxonomy/materials.md
```

---

# 4. Application Output Structure

Recommended canonical structure:

```json
{
  "industry": "AUTOMOTIVE",
  "application_code": "EV_MOTOR",
  "application_name": "EV Drive Motor",
  "component_code": "MOTOR_CORE",
  "material_requirements": [
    "LOW_MAGNETIC_LOSS",
    "HIGH_MAGNETIC_FLUX_DENSITY"
  ],
  "steel_categories": [
    "ELECTRICAL_STEEL"
  ]
}
```

---

# 5. Application Classification Rules

Applications must be selected based on:

```text
actual end use
physical function
component context
industry context
```

Do not infer application solely from keywords.

Example:

```text
"motor"
```

may refer to:

```text
EV motor
industrial motor
home-appliance motor
robot servo motor
```

Use industry and source context.

---

# 6. Number of Applications Per Event

One event may affect multiple applications.

Default recommendation:

```text
1 Primary Application
+
0 to 3 Secondary Applications
```

Avoid assigning every possible application.

Example:

```text
EV factory expansion
```

may support:

```text
Primary:
EV_BODY_STRUCTURE

Secondary:
EV_MOTOR
BATTERY_PACK
CHASSIS
```

depending on source detail and downstream value.

---

# 7. AUTOMOTIVE Applications

Industry:

```text
AUTOMOTIVE
```

---

# 7.1 VEHICLE_BODY

Application code:

```text
VEHICLE_BODY
```

Korean:

```text
차체
```

Purpose:

Vehicle structural and outer body construction.

Typical components:

```text
BODY_IN_WHITE
DOOR
HOOD
ROOF
FENDER
SIDE_PANEL
FLOOR_PANEL
PILLAR
```

Typical material requirements:

```text
HIGH_STRENGTH
FORMABILITY
WEIGHT_REDUCTION
CRASH_SAFETY
WELDABILITY
SURFACE_QUALITY
CORROSION_RESISTANCE
```

Typical steel categories:

```text
AUTOMOTIVE_SHEET
AHSS
UHSS
GALVANIZED_STEEL
COATED_STEEL
```

---

# 7.2 EV_BODY_STRUCTURE

Application code:

```text
EV_BODY_STRUCTURE
```

Use when vehicle architecture is specifically EV-related.

Components:

```text
BODY_IN_WHITE
FLOOR_STRUCTURE
SIDE_STRUCTURE
CRASH_MEMBER
CROSS_MEMBER
```

Material requirements:

```text
LIGHTWEIGHT
VERY_HIGH_STRENGTH
CRASH_RESISTANCE
FORMABILITY
WELDABILITY
```

Steel categories:

```text
AHSS
UHSS
AUTOMOTIVE_SHEET
```

---

# 7.3 EV_MOTOR

Application code:

```text
EV_MOTOR
```

Korean:

```text
전기차 구동모터
```

Components:

```text
MOTOR_CORE
ROTOR_CORE
STATOR_CORE
MOTOR_HOUSING
```

Key material requirements:

```text
LOW_MAGNETIC_LOSS
HIGH_MAGNETIC_FLUX_DENSITY
HIGH_EFFICIENCY
THIN_GAUGE
DIMENSIONAL_STABILITY
```

Steel categories:

```text
ELECTRICAL_STEEL
NON_ORIENTED_ELECTRICAL_STEEL
```

This application has high strategic relevance for EV growth analysis.

---

# 7.4 BATTERY_CASE

Application code:

```text
BATTERY_CASE
```

Components:

```text
BATTERY_TRAY
BATTERY_ENCLOSURE
COVER
CRASH_PROTECTION_MEMBER
```

Material requirements:

```text
LIGHTWEIGHT
HIGH_STRENGTH
CRASH_RESISTANCE
CORROSION_RESISTANCE
FORMABILITY
THERMAL_SAFETY
```

Steel categories:

```text
AHSS
COATED_STEEL
STAINLESS_STEEL
AUTOMOTIVE_SHEET
```

---

# 7.5 CHASSIS

Application code:

```text
CHASSIS
```

Components:

```text
FRAME
SUBFRAME
CONTROL_ARM
SUSPENSION_MEMBER
CROSS_MEMBER
```

Material requirements:

```text
HIGH_STRENGTH
FATIGUE_RESISTANCE
WELDABILITY
FORMABILITY
WEIGHT_REDUCTION
```

Steel categories:

```text
AHSS
HSLA
AUTOMOTIVE_SHEET
SPECIALTY_STEEL
```

---

# 7.6 POWERTRAIN

Application code:

```text
POWERTRAIN
```

Primarily relevant to ICE and hybrid vehicles.

Components:

```text
ENGINE_COMPONENT
TRANSMISSION_COMPONENT
GEAR
SHAFT
CLUTCH_COMPONENT
```

Material requirements:

```text
WEAR_RESISTANCE
FATIGUE_RESISTANCE
HIGH_STRENGTH
HEAT_RESISTANCE
MACHINABILITY
```

Steel categories:

```text
SPECIALTY_STEEL
BAR_STEEL
ALLOY_STEEL
```

---

# 7.7 FUEL_SYSTEM

Application code:

```text
FUEL_SYSTEM
```

Components:

```text
FUEL_TANK
FUEL_PIPE
EXHAUST_COMPONENT
```

Material requirements:

```text
CORROSION_RESISTANCE
FORMABILITY
CHEMICAL_RESISTANCE
```

Steel categories:

```text
STAINLESS_STEEL
COATED_STEEL
```

---

# 8. SHIPBUILDING Applications

Industry:

```text
SHIPBUILDING
```

---

# 8.1 SHIP_HULL

Application code:

```text
SHIP_HULL
```

Components:

```text
HULL_PLATE
DECK
SIDE_SHELL
BOTTOM_SHELL
BULKHEAD
```

Material requirements:

```text
HIGH_STRENGTH
TOUGHNESS
WELDABILITY
FATIGUE_RESISTANCE
CORROSION_RESISTANCE
```

Steel categories:

```text
SHIPBUILDING_PLATE
THICK_PLATE
HIGH_STRENGTH_PLATE
```

---

# 8.2 LNG_CARRIER

Application code:

```text
LNG_CARRIER
```

Components:

```text
LNG_TANK
HULL
CARGO_CONTAINMENT_SYSTEM
PIPE
STRUCTURAL_MEMBER
```

Material requirements:

```text
CRYOGENIC_TOUGHNESS
LOW_TEMPERATURE_RESISTANCE
WELDABILITY
CORROSION_RESISTANCE
```

Steel categories:

```text
CRYOGENIC_STEEL
STAINLESS_STEEL
THICK_PLATE
HIGH_MANGANESE_STEEL
```

---

# 8.3 LNG_TANK

Application code:

```text
LNG_TANK
```

Components:

```text
TANK_WALL
SUPPORT_STRUCTURE
PIPE_CONNECTION
```

Material requirements:

```text
VERY_LOW_TEMPERATURE_TOUGHNESS
CRACK_RESISTANCE
WELDABILITY
LEAK_RESISTANCE
```

Steel categories:

```text
CRYOGENIC_STEEL
STAINLESS_STEEL
HIGH_MANGANESE_STEEL
```

---

# 8.4 CONTAINER_SHIP

Application code:

```text
CONTAINER_SHIP
```

Components:

```text
HULL
DECK
HATCH_COVER
STRUCTURAL_FRAME
```

Material requirements:

```text
HIGH_STRENGTH
FATIGUE_RESISTANCE
WELDABILITY
WEIGHT_EFFICIENCY
```

Steel categories:

```text
SHIPBUILDING_PLATE
HIGH_STRENGTH_PLATE
```

---

# 8.5 TANKER

Application code:

```text
TANKER
```

Components:

```text
CARGO_TANK
HULL
PIPE_SYSTEM
STRUCTURAL_MEMBER
```

Material requirements:

```text
CORROSION_RESISTANCE
TOUGHNESS
WELDABILITY
CHEMICAL_RESISTANCE
```

Steel categories:

```text
SHIPBUILDING_PLATE
STAINLESS_STEEL
CORROSION_RESISTANT_STEEL
```

---

# 8.6 OFFSHORE_STRUCTURE

Application code:

```text
OFFSHORE_STRUCTURE
```

Components:

```text
JACKET
TOPSIDE
DECK
SUPPORT_STRUCTURE
PIPE
```

Material requirements:

```text
HIGH_STRENGTH
FRACTURE_TOUGHNESS
CORROSION_RESISTANCE
FATIGUE_RESISTANCE
WELDABILITY
```

Steel categories:

```text
OFFSHORE_PLATE
THICK_PLATE
HIGH_STRENGTH_PLATE
```

---

# 8.7 GREEN_SHIP

Application code:

```text
GREEN_SHIP
```

Use for:

```text
AMMONIA_FUELED_SHIP
METHANOL_SHIP
HYDROGEN_SHIP
LOW_CARBON_VESSEL
```

Possible components:

```text
FUEL_TANK
PIPE_SYSTEM
ENGINE_SYSTEM
HULL
```

Material requirements vary by fuel type and must not be assumed without evidence.

Typical possible steel categories:

```text
STAINLESS_STEEL
CRYOGENIC_STEEL
CORROSION_RESISTANT_STEEL
THICK_PLATE
```

Use conservative matching.

---

# 9. ENERGY Applications

Industry:

```text
ENERGY
```

---

# 9.1 OFFSHORE_WIND

Application code:

```text
OFFSHORE_WIND
```

Components:

```text
WIND_TOWER
MONOPILE
JACKET_FOUNDATION
TRANSITION_PIECE
NACELLE_STRUCTURE
```

Material requirements:

```text
HIGH_STRENGTH
THICK_GAUGE
FATIGUE_RESISTANCE
WELDABILITY
CORROSION_RESISTANCE
```

Steel categories:

```text
THICK_PLATE
STRUCTURAL_STEEL
OFFSHORE_PLATE
```

---

# 9.2 ONSHORE_WIND

Application code:

```text
ONSHORE_WIND
```

Components:

```text
WIND_TOWER
BASE_STRUCTURE
NACELLE_STRUCTURE
```

Material requirements:

```text
HIGH_STRENGTH
FATIGUE_RESISTANCE
WELDABILITY
```

Steel categories:

```text
THICK_PLATE
STRUCTURAL_STEEL
```

---

# 9.3 SOLAR_STRUCTURE

Application code:

```text
SOLAR_STRUCTURE
```

Components:

```text
SOLAR_FRAME
MOUNTING_STRUCTURE
SUPPORT_BEAM
```

Material requirements:

```text
CORROSION_RESISTANCE
FORMABILITY
WEATHER_RESISTANCE
LIGHTWEIGHT
```

Steel categories:

```text
COATED_STEEL
GALVANIZED_STEEL
STRUCTURAL_STEEL
```

---

# 9.4 HYDROGEN_PIPELINE

Application code:

```text
HYDROGEN_PIPELINE
```

Components:

```text
PIPE
WELDED_JOINT
VALVE_BODY
```

Material requirements:

```text
HYDROGEN_EMBRITTLEMENT_RESISTANCE
TOUGHNESS
PRESSURE_RESISTANCE
WELDABILITY
```

Steel categories:

```text
PIPELINE_STEEL
SPECIALTY_STEEL
STAINLESS_STEEL
```

Do not claim suitability for hydrogen service without verified product knowledge.

---

# 9.5 HYDROGEN_STORAGE

Application code:

```text
HYDROGEN_STORAGE
```

Components:

```text
PRESSURE_VESSEL
STORAGE_TANK
PIPE
```

Material requirements:

```text
HIGH_PRESSURE_RESISTANCE
HYDROGEN_EMBRITTLEMENT_RESISTANCE
FATIGUE_RESISTANCE
LEAK_TIGHTNESS
```

Steel categories:

```text
PRESSURE_VESSEL_STEEL
SPECIALTY_STEEL
STAINLESS_STEEL
```

---

# 9.6 LNG_INFRASTRUCTURE

Application code:

```text
LNG_INFRASTRUCTURE
```

Components:

```text
LNG_STORAGE_TANK
PIPELINE
TERMINAL_STRUCTURE
PRESSURE_VESSEL
```

Material requirements:

```text
CRYOGENIC_TOUGHNESS
CORROSION_RESISTANCE
WELDABILITY
PRESSURE_RESISTANCE
```

Steel categories:

```text
CRYOGENIC_STEEL
STAINLESS_STEEL
THICK_PLATE
```

---

# 9.7 NUCLEAR_POWER

Application code:

```text
NUCLEAR_POWER
```

Components:

```text
PRESSURE_VESSEL
STEAM_GENERATOR
PIPE
STRUCTURAL_COMPONENT
CONTAINMENT_STRUCTURE
```

Material requirements:

```text
HIGH_TOUGHNESS
HIGH_PRESSURE_RESISTANCE
HEAT_RESISTANCE
WELDABILITY
LONG_TERM_RELIABILITY
```

Steel categories:

```text
PRESSURE_VESSEL_STEEL
SPECIALTY_STEEL
STAINLESS_STEEL
THICK_PLATE
```

---

# 9.8 POWER_TRANSFORMER

Application code:

```text
POWER_TRANSFORMER
```

Components:

```text
TRANSFORMER_CORE
HOUSING
STRUCTURE
```

Material requirements:

```text
LOW_CORE_LOSS
HIGH_MAGNETIC_PERMEABILITY
HIGH_EFFICIENCY
```

Steel categories:

```text
GRAIN_ORIENTED_ELECTRICAL_STEEL
ELECTRICAL_STEEL
```

---

# 9.9 ELECTRIC_GRID

Application code:

```text
ELECTRIC_GRID
```

Components:

```text
TRANSMISSION_TOWER
SUBSTATION_STRUCTURE
TRANSFORMER
PIPE
CABLE_SUPPORT_STRUCTURE
```

Steel categories may include:

```text
STRUCTURAL_STEEL
ELECTRICAL_STEEL
COATED_STEEL
```

---

# 10. BATTERY Applications

Industry:

```text
BATTERY
```

---

# 10.1 BATTERY_CELL_FACTORY

Application code:

```text
BATTERY_CELL_FACTORY
```

Components:

```text
FACTORY_STRUCTURE
PROCESS_EQUIPMENT
PIPE
DUCT
UTILITY_SYSTEM
```

Steel categories:

```text
STRUCTURAL_STEEL
STAINLESS_STEEL
COATED_STEEL
```

This application primarily captures facility-related steel demand.

---

# 10.2 BATTERY_MODULE

Application code:

```text
BATTERY_MODULE
```

Components:

```text
MODULE_CASE
FRAME
SUPPORT_STRUCTURE
```

Material requirements:

```text
LIGHTWEIGHT
STRENGTH
THERMAL_SAFETY
FORMABILITY
```

Steel categories:

```text
AHSS
COATED_STEEL
STAINLESS_STEEL
```

---

# 10.3 ESS

Application code:

```text
ESS
```

Components:

```text
BATTERY_CONTAINER
RACK
ENCLOSURE
SUPPORT_STRUCTURE
```

Material requirements:

```text
FIRE_SAFETY
CORROSION_RESISTANCE
STRUCTURAL_STRENGTH
```

Steel categories:

```text
COATED_STEEL
STAINLESS_STEEL
STRUCTURAL_STEEL
```

---

# 11. SEMICONDUCTOR Applications

Industry:

```text
SEMICONDUCTOR
```

---

# 11.1 SEMICONDUCTOR_FAB

Application code:

```text
SEMICONDUCTOR_FAB
```

Components:

```text
FAB_STRUCTURE
CLEANROOM_STRUCTURE
UTILITY_PIPE
PROCESS_PIPE
EQUIPMENT_FRAME
```

Material requirements:

```text
CORROSION_RESISTANCE
CLEANLINESS
DIMENSIONAL_STABILITY
CHEMICAL_RESISTANCE
```

Steel categories:

```text
STAINLESS_STEEL
STRUCTURAL_STEEL
COATED_STEEL
```

---

# 11.2 HIGH_PURITY_PROCESS_SYSTEM

Application code:

```text
HIGH_PURITY_PROCESS_SYSTEM
```

Components:

```text
HIGH_PURITY_PIPE
VALVE
PROCESS_CHAMBER
```

Material requirements:

```text
HIGH_CLEANLINESS
CORROSION_RESISTANCE
SURFACE_QUALITY
CHEMICAL_RESISTANCE
```

Steel categories:

```text
STAINLESS_STEEL
```

Product matching requires verified specifications.

---

# 12. CONSTRUCTION Applications

Industry:

```text
CONSTRUCTION
```

---

# 12.1 HIGH_RISE_BUILDING

Application code:

```text
HIGH_RISE_BUILDING
```

Components:

```text
COLUMN
BEAM
BRACING
DECK
```

Material requirements:

```text
HIGH_STRENGTH
WELDABILITY
FIRE_PERFORMANCE
STRUCTURAL_STABILITY
```

Steel categories:

```text
STRUCTURAL_STEEL
H_BEAM
THICK_PLATE
```

---

# 12.2 BRIDGE

Application code:

```text
BRIDGE
```

Components:

```text
GIRDER
DECK
CABLE_SUPPORT
PIER_STRUCTURE
```

Material requirements:

```text
HIGH_STRENGTH
FATIGUE_RESISTANCE
CORROSION_RESISTANCE
WELDABILITY
```

Steel categories:

```text
STRUCTURAL_STEEL
THICK_PLATE
WEATHERING_STEEL
```

---

# 12.3 DATA_CENTER_BUILDING

Application code:

```text
DATA_CENTER_BUILDING
```

Components:

```text
BUILDING_STRUCTURE
RACK_STRUCTURE
COOLING_PIPE
POWER_INFRASTRUCTURE
```

Steel categories:

```text
STRUCTURAL_STEEL
STAINLESS_STEEL
COATED_STEEL
ELECTRICAL_STEEL
```

---

# 12.4 MODULAR_BUILDING

Application code:

```text
MODULAR_BUILDING
```

Components:

```text
MODULE_FRAME
WALL_PANEL
ROOF_PANEL
FLOOR_STRUCTURE
```

Material requirements:

```text
HIGH_STRENGTH
LIGHTWEIGHT
FORMABILITY
CORROSION_RESISTANCE
```

Steel categories:

```text
STRUCTURAL_STEEL
COATED_STEEL
COLD_ROLLED_STEEL
```

---

# 13. MACHINERY Applications

Industry:

```text
MACHINERY
```

---

# 13.1 HEAVY_EQUIPMENT

Application code:

```text
HEAVY_EQUIPMENT
```

Components:

```text
BOOM
FRAME
BUCKET
UNDERCARRIAGE
```

Material requirements:

```text
HIGH_STRENGTH
WEAR_RESISTANCE
FATIGUE_RESISTANCE
WELDABILITY
```

Steel categories:

```text
HIGH_STRENGTH_PLATE
WEAR_RESISTANT_STEEL
SPECIALTY_STEEL
```

---

# 13.2 INDUSTRIAL_MOTOR

Application code:

```text
INDUSTRIAL_MOTOR
```

Components:

```text
MOTOR_CORE
ROTOR
STATOR
HOUSING
```

Material requirements:

```text
LOW_MAGNETIC_LOSS
HIGH_EFFICIENCY
DIMENSIONAL_STABILITY
```

Steel categories:

```text
ELECTRICAL_STEEL
NON_ORIENTED_ELECTRICAL_STEEL
```

---

# 13.3 INDUSTRIAL_ROBOT

Application code:

```text
INDUSTRIAL_ROBOT
```

Components:

```text
ROBOT_FRAME
SERVO_MOTOR_CORE
JOINT
GEAR
```

Material requirements:

```text
HIGH_STRENGTH
LIGHTWEIGHT
LOW_MAGNETIC_LOSS
WEAR_RESISTANCE
```

Steel categories:

```text
ELECTRICAL_STEEL
SPECIALTY_STEEL
HIGH_STRENGTH_STEEL
```

---

# 14. HOME_APPLIANCE Applications

Industry:

```text
HOME_APPLIANCE
```

---

# 14.1 REFRIGERATOR

Application code:

```text
REFRIGERATOR
```

Components:

```text
OUTER_PANEL
INNER_STRUCTURE
COMPRESSOR_MOTOR
```

Material requirements:

```text
SURFACE_QUALITY
CORROSION_RESISTANCE
FORMABILITY
MAGNETIC_EFFICIENCY
```

Steel categories:

```text
COATED_STEEL
PREPAINTED_STEEL
ELECTRICAL_STEEL
```

---

# 14.2 WASHING_MACHINE

Application code:

```text
WASHING_MACHINE
```

Components:

```text
DRUM
CABINET
MOTOR_CORE
```

Steel categories:

```text
STAINLESS_STEEL
COATED_STEEL
ELECTRICAL_STEEL
```

---

# 14.3 HVAC

Application code:

```text
HVAC
```

Components:

```text
COMPRESSOR
MOTOR
HEAT_EXCHANGER_STRUCTURE
HOUSING
```

Steel categories:

```text
ELECTRICAL_STEEL
COATED_STEEL
STAINLESS_STEEL
```

---

# 15. DEFENSE Applications

Industry:

```text
DEFENSE
```

---

# 15.1 ARMORED_VEHICLE

Application code:

```text
ARMORED_VEHICLE
```

Components:

```text
ARMOR_PLATE
CHASSIS
STRUCTURAL_FRAME
```

Material requirements:

```text
VERY_HIGH_STRENGTH
BALLISTIC_RESISTANCE
TOUGHNESS
WELDABILITY
```

Steel categories:

```text
ARMOR_STEEL
HIGH_STRENGTH_PLATE
SPECIALTY_STEEL
```

---

# 15.2 NAVAL_VESSEL

Application code:

```text
NAVAL_VESSEL
```

Components:

```text
HULL
DECK
STRUCTURAL_MEMBER
```

Steel categories:

```text
NAVAL_STEEL
HIGH_STRENGTH_PLATE
SHIPBUILDING_PLATE
```

---

# 16. ROBOTICS Applications

Industry:

```text
ROBOTICS
```

---

# 16.1 HUMANOID_ROBOT

Application code:

```text
HUMANOID_ROBOT
```

Components:

```text
FRAME
JOINT
SERVO_MOTOR_CORE
GEAR
```

Potential requirements:

```text
LIGHTWEIGHT
HIGH_STRENGTH
HIGH_EFFICIENCY
WEAR_RESISTANCE
```

Potential steel categories:

```text
ELECTRICAL_STEEL
SPECIALTY_STEEL
HIGH_STRENGTH_STEEL
STAINLESS_STEEL
```

Treat future product matching cautiously due to rapidly changing designs.

---

# 17. DATA_CENTER Applications

Industry:

```text
DATA_CENTER
```

---

# 17.1 AI_DATA_CENTER

Application code:

```text
AI_DATA_CENTER
```

Components:

```text
BUILDING_STRUCTURE
SERVER_RACK
COOLING_PIPE
TRANSFORMER_CORE
POWER_INFRASTRUCTURE
```

Potential material requirements:

```text
STRUCTURAL_STRENGTH
CORROSION_RESISTANCE
LOW_CORE_LOSS
THERMAL_RELIABILITY
```

Steel categories:

```text
STRUCTURAL_STEEL
STAINLESS_STEEL
ELECTRICAL_STEEL
COATED_STEEL
```

The steel-demand reasoning should distinguish:

```text
building steel demand
```

from:

```text
electrical infrastructure steel demand
```

---

# 18. RAILWAY Applications

Industry:

```text
RAILWAY
```

---

# 18.1 RAIL_VEHICLE

Application code:

```text
RAIL_VEHICLE
```

Components:

```text
CAR_BODY
BOGIE
FRAME
MOTOR_CORE
```

Steel categories:

```text
STAINLESS_STEEL
HIGH_STRENGTH_STEEL
ELECTRICAL_STEEL
SPECIALTY_STEEL
```

---

# 18.2 RAIL_INFRASTRUCTURE

Application code:

```text
RAIL_INFRASTRUCTURE
```

Components:

```text
RAIL
BRIDGE_STRUCTURE
STATION_STRUCTURE
```

Steel categories:

```text
RAIL_STEEL
STRUCTURAL_STEEL
SPECIALTY_STEEL
```

---

# 19. STEEL Industry Applications

Industry:

```text
STEEL
```

These applications are useful for competitor intelligence.

---

# 19.1 BLAST_FURNACE

Application code:

```text
BLAST_FURNACE
```

Use for:

```text
blast furnace investment
modernization
shutdown
capacity changes
```

---

# 19.2 ELECTRIC_ARC_FURNACE

Application code:

```text
ELECTRIC_ARC_FURNACE
```

Use for:

```text
EAF construction
EAF conversion
low-carbon steel investment
```

This application is important for competitor decarbonization analysis.

---

# 19.3 HOT_ROLLING

Application code:

```text
HOT_ROLLING
```

Use for:

```text
hot strip mill
plate mill
rolling capacity
```

---

# 19.4 COLD_ROLLING

Application code:

```text
COLD_ROLLING
```

---

# 19.5 GALVANIZING

Application code:

```text
GALVANIZING
```

Relevant to automotive and coated-steel capacity.

---

# 19.6 ELECTRICAL_STEEL_LINE

Application code:

```text
ELECTRICAL_STEEL_LINE
```

Relevant to competitor electrical-steel investment and capacity analysis.

---

# 20. Component Taxonomy Rule

Components should represent physical or functional parts of an application.

Good examples:

```text
MOTOR_CORE
BATTERY_TRAY
HULL_PLATE
WIND_TOWER
PIPE
PRESSURE_VESSEL
```

Bad examples:

```text
EV
ENERGY
PREMIUM
GREEN
```

These are industries, technologies, or strategies.

---

# 21. Material Requirement Rules

Material requirements should describe engineering or functional needs.

Examples:

```text
HIGH_STRENGTH
VERY_HIGH_STRENGTH
TOUGHNESS
CRYOGENIC_TOUGHNESS
LOW_MAGNETIC_LOSS
CORROSION_RESISTANCE
WEAR_RESISTANCE
FORMABILITY
WELDABILITY
FATIGUE_RESISTANCE
HEAT_RESISTANCE
HYDROGEN_EMBRITTLEMENT_RESISTANCE
WEIGHT_REDUCTION
SURFACE_QUALITY
```

Detailed definitions belong in:

```text
materials.md
```

---

# 22. Steel Category Rules

Steel category is not a POSCO product name.

Examples:

```text
ELECTRICAL_STEEL
THICK_PLATE
AHSS
STAINLESS_STEEL
STRUCTURAL_STEEL
PIPELINE_STEEL
CRYOGENIC_STEEL
COATED_STEEL
SPECIALTY_STEEL
```

The next stage retrieves specific POSCO products within these categories.

---

# 23. Application vs Product

Do not treat product names as applications.

Bad:

```text
Application = specific POSCO grade
```

Correct:

```text
Application:
EV_MOTOR

Steel Category:
ELECTRICAL_STEEL

Product:
retrieved later from POSCO knowledge
```

---

# 24. Event-to-Application Mapping

Events may generate application candidates.

Example:

```text
Event:
NEW_FACTORY

Industry:
AUTOMOTIVE

Subtype:
EV_FACTORY
```

Possible applications:

```text
EV_BODY_STRUCTURE
EV_MOTOR
BATTERY_CASE
CHASSIS
```

But application selection should depend on source scope.

A factory announcement alone does not prove all applications are relevant.

---

# 25. Strategy-to-Application Mapping

Strategy may help prioritize application candidates.

Example:

```text
Strategy:
ELECTRIFICATION
```

Likely candidates:

```text
EV_MOTOR
BATTERY_CASE
EV_BODY_STRUCTURE
```

Example:

```text
Strategy:
DECARBONIZATION
```

Possible applications depend on actual operational change and should not be assumed globally.

---

# 26. Primary Application Selection

Choose the Primary Application based on:

```text
explicit source mention
event subject
component relevance
steel-demand significance
company business context
```

Do not choose purely based on expected POSCO sales potential.

---

# 27. Application Confidence

Recommended:

```text
90-100
explicitly identified application

80-89
strong contextual match

70-79
reasonable inference

60-69
weak inference

below 60
use UNKNOWN or omit
```

---

# 28. Application Unknown State

Use:

```text
APPLICATION_UNKNOWN
```

when industry is known but physical application cannot be reliably determined.

Example:

```text
Company announces broad $10B manufacturing investment.
```

Industry may be:

```text
AUTOMOTIVE
```

but application may remain:

```text
APPLICATION_UNKNOWN
```

Do not force product matching.

---

# 29. Application Granularity

Prefer the most specific useful level.

Example:

Bad:

```text
AUTOMOTIVE_GENERAL
```

Better:

```text
EV_MOTOR
```

when evidence supports it.

But do not over-specify.

Example:

```text
EV factory announced
```

does not automatically prove:

```text
MOTOR_CORE
```

unless motor production or sourcing is relevant.

---

# 30. Multi-Application Example

Input:

```text
Automaker announces integrated EV complex including vehicle assembly, motor production, and battery-pack production.
```

Applications:

```text
Primary:
EV_BODY_STRUCTURE

Secondary:
EV_MOTOR
BATTERY_CASE
```

All are independently supported.

---

# 31. Application Deduplication

Avoid creating separate application records for synonymous terms.

Examples:

```text
EV drive motor
traction motor
electric vehicle motor
```

should map to:

```text
EV_MOTOR
```

Use aliases in future taxonomy metadata if needed.

---

# 32. Cross-Industry Application

Some applications may appear across industries.

Example:

```text
INDUSTRIAL_MOTOR
```

may relate to:

```text
MACHINERY
ROBOTICS
HOME_APPLIANCE
ENERGY
```

Preserve primary industry context while reusing appropriate component/material mappings where possible.

---

# 33. Application-to-Steel Reasoning

Use:

```text
Application
↓
Component
↓
Required Property
↓
Steel Category
```

Example:

```text
EV_MOTOR
↓
MOTOR_CORE
↓
LOW_MAGNETIC_LOSS
↓
ELECTRICAL_STEEL
```

Example:

```text
OFFSHORE_WIND
↓
MONOPILE
↓
THICK_GAUGE + FATIGUE_RESISTANCE
↓
THICK_PLATE
```

---

# 34. No Direct Product Jump

Forbidden reasoning:

```text
OFFSHORE_WIND
→ POSCO Product X
```

Required:

```text
OFFSHORE_WIND
→ MONOPILE
→ strength / toughness / weldability requirements
→ thick plate
→ product retrieval
→ product fit evaluation
```

---

# 35. Product Matching Threshold

A specific product should only be retrieved when:

```text
industry known
+
application sufficiently known
+
component or required properties known
```

If only industry is known:

```text
do not recommend specific product
```

Return broader product family or unknown if needed.

---

# 36. Application Mapping Confidence

Application mapping should contribute to Product Fit confidence.

Example:

```text
application confidence = 95
component confidence = 90
material requirement confidence = 85
```

Product matching can proceed.

Example:

```text
application confidence = 55
component = UNKNOWN
```

Specific product recommendation should be restricted.

---

# 37. Future Application Expansion

New applications may be added when:

```text
repeatedly observed in source data
materially different component structure
different steel requirement
different product retrieval path
clear marketing value
```

Do not create new applications merely for naming convenience.

---

# 38. Application Change Rule

Before creating a new canonical application, verify:

```text
1. no existing application fits

2. the physical use case is materially different

3. steel requirements differ meaningfully

4. it appears repeatedly

5. product retrieval benefits from separation
```

Record significant taxonomy changes in:

```text
docs/decisions.md
```

---

# 39. Golden Test Case 1

Input:

```text
Automaker increases EV motor production.
```

Expected:

```text
Industry:
AUTOMOTIVE

Application:
EV_MOTOR

Component:
MOTOR_CORE

Steel Category:
ELECTRICAL_STEEL
```

---

# 40. Golden Test Case 2

Input:

```text
Shipbuilder wins order for LNG carriers.
```

Expected:

```text
Industry:
SHIPBUILDING

Primary Application:
LNG_CARRIER

Possible Components:
HULL
LNG_TANK
```

Do not recommend a specific cryogenic product until application/component evidence is sufficient.

---

# 41. Golden Test Case 3

Input:

```text
Energy company invests in offshore wind project.
```

Expected:

```text
Industry:
ENERGY

Application:
OFFSHORE_WIND

Possible Components:
WIND_TOWER
MONOPILE
JACKET_FOUNDATION
```

---

# 42. Golden Test Case 4

Input:

```text
Utility invests in transformer capacity.
```

Expected:

```text
Industry:
ENERGY

Application:
POWER_TRANSFORMER

Component:
TRANSFORMER_CORE

Steel Category:
GRAIN_ORIENTED_ELECTRICAL_STEEL
```

---

# 43. Golden Test Case 5

Input:

```text
Battery company builds a new cell factory.
```

Expected:

```text
Industry:
BATTERY

Application:
BATTERY_CELL_FACTORY
```

Do not assume:

```text
BATTERY_CASE
```

because battery-cell manufacturing and automotive battery-case production are different applications.

---

# 44. Golden Test Case 6

Input:

```text
Semiconductor company builds new fab.
```

Expected:

```text
Industry:
SEMICONDUCTOR

Application:
SEMICONDUCTOR_FAB
```

Potential steel demand:

```text
facility structure
high-purity piping
stainless process equipment
```

---

# 45. Golden Test Case 7

Input:

```text
Steel competitor builds new electrical-steel production line.
```

Expected:

```text
Company Industry:
STEEL

Application:
ELECTRICAL_STEEL_LINE

Target Customer Industry:
AUTOMOTIVE / ENERGY depending on source
```

---

# 46. Golden Test Case 8

Input:

```text
Company announces broad hydrogen strategy.
```

Expected:

```text
Industry:
HYDROGEN or ENERGY

Application:
APPLICATION_UNKNOWN
```

until source identifies:

```text
pipeline
storage
transport
fuel cell
production facility
```

Do not force a steel category.

---

# 47. Application Extraction Prompt Rules

Application-analysis prompts should explicitly instruct:

```text
Use only canonical application codes.

Determine application from physical end use.

Do not infer a specific component without evidence.

Do not recommend a POSCO product in this stage.

Return APPLICATION_UNKNOWN when evidence is insufficient.

A single event may have one Primary Application and up to three Secondary Applications.

Do not confuse industry, technology, strategy, and application.

Map application to component and material requirement only when evidence supports the mapping.
```

---

# 48. Application Output Example

Recommended AI output:

```json
{
  "primary_application": {
    "application_code": "EV_MOTOR",
    "confidence": 94,
    "reason": "The source explicitly describes expansion of EV drive-motor production."
  },
  "components": [
    {
      "component_code": "MOTOR_CORE",
      "confidence": 88
    }
  ],
  "material_requirements": [
    {
      "requirement_code": "LOW_MAGNETIC_LOSS",
      "confidence": 82
    }
  ],
  "steel_categories": [
    {
      "steel_category": "ELECTRICAL_STEEL",
      "confidence": 90
    }
  ]
}
```

---

# 49. Overclassification Guardrail

Bad:

```text
EV factory
→ EV_BODY_STRUCTURE
→ EV_MOTOR
→ BATTERY_CASE
→ CHASSIS
→ POWERTRAIN
→ FUEL_SYSTEM
```

Correct:

Only include applications explicitly supported or strongly implied by the event scope.

---

# 50. Underclassification Guardrail

If a source explicitly states:

```text
integrated EV facility including vehicle body, motors, and battery packs
```

do not reduce it to only:

```text
EV_BODY_STRUCTURE
```

Preserve materially distinct applications.

---

# 51. Application Priority for MVP

Deep mappings should prioritize:

```text
AUTOMOTIVE

VEHICLE_BODY
EV_BODY_STRUCTURE
EV_MOTOR
BATTERY_CASE
CHASSIS
```

```text
SHIPBUILDING

SHIP_HULL
LNG_CARRIER
LNG_TANK
OFFSHORE_STRUCTURE
GREEN_SHIP
```

```text
ENERGY

OFFSHORE_WIND
HYDROGEN_PIPELINE
HYDROGEN_STORAGE
LNG_INFRASTRUCTURE
NUCLEAR_POWER
POWER_TRANSFORMER
```

These should receive the most testing during Phase 3 and Phase 4.

---

# 52. Application Data Model

Recommended relationship:

```text
industries
↓
applications
↓
components
```

Conceptual application fields:

```text
id
industry_id
code
name_ko
name_en
description
parent_id
is_active
```

Component fields:

```text
id
application_id
code
name_ko
name_en
description
```

Material mappings may use separate relationship tables later if required.

---

# 53. Application-to-Knowledge Retrieval

POSCO knowledge retrieval should use the application as a primary metadata filter.

Example:

```text
Application:
EV_MOTOR

↓

knowledge/posco/automotive/index.md

↓

electrical steel related product documents
```

Example:

```text
Application:
OFFSHORE_WIND

↓

knowledge/posco/energy/index.md

↓

offshore / thick plate related documents
```

---

# 54. Application Alias Support

Future aliases may include:

```text
EV traction motor
drive motor
propulsion motor
```

mapping to:

```text
EV_MOTOR
```

Keep canonical codes stable while allowing flexible source-language matching.

---

# 55. Technology vs Application Rule

Example:

```text
HYDROGEN
```

may be:

```text
industry
technology tag
```

But applications should be more specific:

```text
HYDROGEN_PIPELINE
HYDROGEN_STORAGE
```

Likewise:

```text
EV
```

is not sufficient as final application.

Use:

```text
EV_MOTOR
EV_BODY_STRUCTURE
BATTERY_CASE
```

when evidence permits.

---

# 56. Strategy vs Application Rule

Example:

```text
ELECTRIFICATION
```

is a Strategy.

Possible Applications:

```text
EV_MOTOR
BATTERY_CASE
POWER_TRANSFORMER
```

Do not store ELECTRIFICATION as an application.

---

# 57. Event vs Application Rule

Example:

```text
NEW_FACTORY
```

is an Event.

Example:

```text
EV_MOTOR
```

is an Application.

A source may therefore produce:

```text
Event:
NEW_FACTORY

Strategy:
ELECTRIFICATION

Industry:
AUTOMOTIVE

Application:
EV_MOTOR
```

Each belongs to a different layer.

---

# 58. Application and Competitive Intelligence

Competitor events may also use application mapping.

Example:

```text
Competitor develops advanced EV motor material.
```

Classification:

```text
Company Industry:
STEEL

Target Industry:
AUTOMOTIVE

Application:
EV_MOTOR

Component:
MOTOR_CORE

Steel Category:
ELECTRICAL_STEEL
```

This allows product-level competitor comparison later.

---

# 59. Application Trend Analysis

The system may aggregate events by application.

Example:

```text
Last 12 months

EV_MOTOR
↑ strong activity

OFFSHORE_WIND
↑ moderate activity

LNG_CARRIER
→ stable
```

This can provide more actionable insight than industry-level trends alone.

---

# 60. Final Application Rule

The application taxonomy exists to convert abstract industry activity into physical steel demand.

The system should prefer:

```text
specific physical use
+
known component
+
supported material requirement
```

over:

```text
broad theme
+
keyword association
+
speculative product match
```

The required intelligence chain is:

```text
INDUSTRY
↓
APPLICATION
↓
COMPONENT
↓
MATERIAL REQUIREMENT
↓
STEEL CATEGORY
↓
POSCO PRODUCT RETRIEVAL
↓
PRODUCT MATCH
↓
OPPORTUNITY
```

Application classification is successful when it makes POSCO product retrieval more accurate, explainable, and less dependent on free-form LLM guessing.
