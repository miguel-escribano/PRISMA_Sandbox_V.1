# GeoJSON Resources for PRISMA

This directory contains GeoJSON resources and utilities for working with geospatial data in FIWARE.

## NGSI-v2 Location Format

FIWARE uses GeoJSON for location attributes. The standard format is:

```json
{
  "location": {
    "value": {
      "type": "Point",
      "coordinates": [longitude, latitude]
    },
    "type": "geo:json"
  }
}
```

## Coordinate Order

**CRITICAL**: GeoJSON uses `[longitude, latitude]` order (NOT `[lat, lon]`)

### Examples

#### Point (Pamplona City Center)
```json
{
  "type": "Point",
  "coordinates": [-1.6440304, 42.8125217]
}
```

#### Polygon (Area boundary)
```json
{
  "type": "Polygon",
  "coordinates": [[
    [-1.6440, 42.8125],
    [-1.6430, 42.8125],
    [-1.6430, 42.8135],
    [-1.6440, 42.8135],
    [-1.6440, 42.8125]
  ]]
}
```

#### LineString (Route/Path)
```json
{
  "type": "LineString",
  "coordinates": [
    [-1.6440, 42.8125],
    [-1.6430, 42.8130],
    [-1.6420, 42.8135]
  ]
}
```

## Python Usage

### Using geojson package
```python
from geojson import Point, Feature, FeatureCollection

# Create a point
point = Point((-1.6440304, 42.8125217))  # (lon, lat)

# Create a feature with properties
feature = Feature(
    geometry=point,
    properties={
        "name": "Pamplona City Hall",
        "type": "PointOfInterest"
    }
)

# Convert to NGSI-v2 format
ngsi_location = {
    "value": point,
    "type": "geo:json"
}
```

### Using shapely for geometric operations
```python
from shapely.geometry import Point, Polygon
from shapely.ops import transform
import pyproj

# Create point
point = Point(-1.6440304, 42.8125217)

# Check if point is within polygon
pamplona_boundary = Polygon([...])
is_inside = point.within(pamplona_boundary)

# Calculate distance (in meters)
point1 = Point(-1.6440, 42.8125)
point2 = Point(-1.6430, 42.8130)

# Project to UTM for accurate distance
wgs84 = pyproj.CRS('EPSG:4326')
utm = pyproj.CRS('EPSG:32630')  # UTM zone 30N (for Pamplona)
project = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True).transform

point1_utm = transform(project, point1)
point2_utm = transform(project, point2)
distance_meters = point1_utm.distance(point2_utm)
```

### Using geopandas for data analysis
```python
import geopandas as gpd
from shapely.geometry import Point

# Create GeoDataFrame from FIWARE entities
data = {
    'id': ['Sensor:001', 'Sensor:002'],
    'temperature': [25.3, 26.1],
    'geometry': [
        Point(-1.6440, 42.8125),
        Point(-1.6430, 42.8130)
    ]
}
gdf = gpd.GeoDataFrame(data, crs='EPSG:4326')

# Spatial queries
nearby = gdf[gdf.distance(Point(-1.6440, 42.8125)) < 0.001]

# Export to GeoJSON
gdf.to_file('sensors.geojson', driver='GeoJSON')
```

## Common Coordinate Systems

- **EPSG:4326** - WGS84 (lat/lon) - Used by FIWARE/GeoJSON
- **EPSG:32630** - UTM Zone 30N - Best for Pamplona distance calculations
- **EPSG:25830** - ETRS89 / UTM Zone 30N - Spanish official CRS

## Pamplona Reference Points

```python
PAMPLONA_REFERENCES = {
    "city_hall": {
        "name": "Ayuntamiento de Pamplona",
        "coordinates": [-1.6440304, 42.8125217]
    },
    "cathedral": {
        "name": "Catedral de Pamplona",
        "coordinates": [-1.6443889, 42.8180556]
    },
    "ciudadela": {
        "name": "Ciudadela de Pamplona",
        "coordinates": [-1.6383333, 42.8138889]
    },
    "university": {
        "name": "Universidad de Navarra",
        "coordinates": [-1.6627778, 42.8011111]
    }
}
```

## Validation

### Validate GeoJSON
```python
import geojson

# Validate GeoJSON object
point = geojson.Point((-1.6440304, 42.8125217))
is_valid = point.is_valid
errors = point.errors()
```

### Validate coordinates are in Pamplona area
```python
def is_in_pamplona(lon, lat):
    """Check if coordinates are roughly in Pamplona area"""
    return (
        -1.70 <= lon <= -1.60 and
        42.78 <= lat <= 42.85
    )
```

## Tools & Resources

### Online Tools
- **GeoJSON.io**: https://geojson.io/ - Visualize and edit GeoJSON
- **GeoJSON Validator**: https://geojsonlint.com/
- **Coordinate Converter**: https://epsg.io/

### Data Sources
- **IDENA** (Navarra GIS): https://idena.navarra.es/
- **OpenStreetMap**: https://www.openstreetmap.org/
- **Catastro**: https://www.sedecatastro.gob.es/

### FIWARE Documentation
- **NGSI-v2 Geospatial**: https://fiware-orion.readthedocs.io/en/master/user/geospatial_queries/index.html
- **Smart Data Models Location**: https://github.com/smart-data-models/data-models/blob/master/specs/ngsi-ld_howto.md#geospatial-properties

## Common Patterns

### Query entities near a point
```bash
# Within 1km of city center
curl -X GET "https://cb.iotplatform.telefonica.com:10027/v2/entities?georel=near;maxDistance:1000&geometry=point&coords=42.8125217,-1.6440304"
```

### Query entities within polygon
```bash
curl -X GET "https://cb.iotplatform.telefonica.com:10027/v2/entities?georel=coveredBy&geometry=polygon&coords=42.81,1.64;42.82,-1.64;42.82,-1.63;42.81,-1.63;42.81,-1.64"
```

---

*Last updated: December 5, 2025*

