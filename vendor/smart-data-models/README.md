# Smart Data Models - Local Reference

This directory contains cloned Smart Data Models repositories for local reference and offline access.

## Available Data Models

### Core Environmental & Safety

#### 🌍 Environment
**Path**: `dataModel.Environment/`  
**Models**: AirQualityObserved, FloodMonitoring, NoiseLevelObserved, WaterQualityObserved, etc.  
**Use for**: Environmental sensors, air quality, noise monitoring

#### ⛈️ Weather
**Path**: `dataModel.Weather/`  
**Models**: WeatherObserved, WeatherForecast, WeatherAlert  
**Use for**: Weather stations, meteorological data, forecasts

#### 🚨 Alert
**Path**: `dataModel.Alert/`  
**Models**: Alert, Anomaly  
**Use for**: Emergency alerts, anomaly detection, warnings

#### ⚠️ Risk Management
**Path**: `dataModel.RiskManagement/`  
**Models**: Risk, Hazard, Vulnerability, Mitigation, Asset  
**Use for**: Risk assessment, hazard tracking, vulnerability analysis

### Urban Infrastructure

#### 💡 Streetlighting
**Path**: `dataModel.Streetlighting/`  
**Models**: Streetlight, StreetlightGroup, StreetlightControlCabinet  
**Use for**: Street lighting infrastructure, energy management

#### 🏗️ Building
**Path**: `dataModel.Building/`  
**Models**: Building, BuildingOperation  
**Use for**: Building structures, occupancy, operations

#### 🌳 Parks and Gardens
**Path**: `dataModel.ParksAndGardens/`  
**Models**: Garden, GreenspaceRecord, FlowerBed  
**Use for**: Parks, green spaces, urban gardens

#### 🗑️ Waste Management
**Path**: `dataModel.WasteManagement/`  
**Models**: WasteContainer, WasteContainerIsle, WasteContainerModel  
**Use for**: Waste collection, bin monitoring

#### 💧 Water Distribution
**Path**: `dataModel.WaterDistribution/`  
**Models**: Junction, Pipe, Pump, Reservoir, Tank, Valve  
**Use for**: Water network management, hydraulic systems

#### ⚡ Energy
**Path**: `dataModel.Energy/`  
**Models**: ThreePhaseAcMeasurement, ACMeasurement  
**Use for**: Energy consumption, generation, grid monitoring

### Transportation & Mobility

#### 🚗 Transportation
**Path**: `dataModel.Transportation/`  
**Models**: TrafficFlowObserved, CrowdFlowObserved, Road, RoadSegment, Vehicle  
**Use for**: Traffic monitoring, road conditions, vehicle tracking

#### 🚌 Urban Mobility
**Path**: `dataModel.UrbanMobility/`  
**Models**: GtfsAgency, GtfsRoute, GtfsStop, PublicTransportStop  
**Use for**: Public transport, mobility services, GTFS data

### Community & Services

#### 📍 Point of Interest
**Path**: `dataModel.PointOfInterest/`  
**Models**: PointOfInterest, Beach, Museum, etc.  
**Use for**: Location-based entities, POIs, landmarks

#### 📱 Social Media
**Path**: `dataModel.SocialMedia/`  
**Models**: SMPost, SMAnalysis, SMCollection  
**Use for**: Social media monitoring, sentiment analysis

### IoT & Devices

#### 🔌 Smart Sensoring
**Path**: `Smart-Sensoring/`  
**Models**: Device, Sensor  
**Use for**: IoT devices, sensor configurations

## Usage

### Finding a Model
1. Navigate to the appropriate domain folder
2. Look for the entity type folder (e.g., `AirQualityObserved/`)
3. Read the `schema.json` for attribute definitions
4. Check `README.md` for examples and documentation

### Example: AirQualityObserved
```bash
vendor/smart-data-models/dataModel.Environment/AirQualityObserved/
├── schema.json          # JSON Schema definition
├── README.md            # Documentation and examples
├── examples/            # Example entities
└── model.yaml          # YAML specification
```

### Converting to NGSI-v2
Smart Data Models use JSON Schema. Convert to NGSI-v2 format:

**Schema attribute:**
```json
"pm25": {
  "type": "number",
  "description": "PM2.5 concentration"
}
```

**NGSI-v2 format:**
```json
"pm25": {
  "value": 12.5,
  "type": "Number"
}
```

## Python Package

For programmatic access, install:
```bash
pip install pysmartdatamodels
```

See `requirements.txt` in project root.

## Updates

To update the models:
```bash
cd vendor/smart-data-models/dataModel.Environment
git pull

cd ../dataModel.Weather
git pull

# etc...
```

## References

- **Official Repository**: https://github.com/orgs/smart-data-models/repositories
- **Documentation**: https://smartdatamodels.org/
- **FIWARE Catalog**: https://github.com/FIWARE/data-models

---

*Last updated: December 5, 2025*

