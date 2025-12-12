# Entities - FIWARE Entity Management

## Quick Reference
- **Smart Data Models**: Always check first with `list_smart_data_model_domains()` and `get_smart_data_model()`
- **Pattern**: Follow `/sdmenvironment` structure
- **LLM Context**: Add `aiContext` field for AI agents

## Smart Data Models First

**Before creating or modifying entities:**
1. Check Smart Data Models: `list_smart_data_model_domains()`
2. Get model schema: `get_smart_data_model(domain, model)`
3. Use standard fields when available
4. Only create custom fields if no standard alternative exists

## Standard Entity Pattern (from /sdmenvironment)

### Required Fields
```json
{
  "id": "EntityType:UniqueID",
  "type": "EntityType",
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [longitude, latitude]
    }
  }
}
```

### Context Fields (for human readability)
```json
{
  "name": {
    "type": "TextUnrestricted",
    "value": "Human readable name"
  },
  "description": {
    "type": "TextUnrestricted",
    "value": "Short description of purpose"
  },
  "address": {
    "type": "TextUnrestricted",
    "value": "Street address"
  },
  "streetAddress": {
    "type": "TextUnrestricted",
    "value": "Street address (same as address)"
  },
  "measure_id": {
    "type": "Text",
    "value": "Device or measurement ID"
  },
  "measure_type": {
    "type": "Text",
    "value": "Type of measurement/entity"
  }
}
```

### AI Context Field (for LLM agents)

**When to add:** If entity will be consumed by AI agents or LLMs

```json
{
  "aiContext": {
    "type": "Text",
    "value": "Rich semantic context for AI: what it represents, typical values, how to interpret, use cases, limitations"
  }
}
```

**What to include in `aiContext`:**
- What the data represents (clear definition)
- Typical value ranges (min/max, day/night patterns)
- How to interpret the values (units, meaning)
- Common use cases (analysis, predictions, correlations)
- Known limitations (update frequency, geographic scope, data gaps)

**Example:**
```json
{
  "aiContext": {
    "type": "Text",
    "value": "Demanda electrica instantanea de Navarra en MW. Valores tipicos: 200-400 MW noche, 400-600 MW dia, picos 700 MW invierno. Actualizacion cada 5 min desde REE. Util para detectar anomalias, correlacionar con meteorologia, identificar patrones horarios. Limitaciones: datos agregados de Navarra."
  }
}
```

## Complete Example: EnergyDemand:Navarra:REE

```json
{
  "id": "EnergyDemand:Navarra:REE",
  "type": "EnergyDemandObserved",
  
  // Data attributes
  "demand": {
    "type": "Number",
    "value": 450.5
  },
  "dateObserved": {
    "type": "DateTime",
    "value": "2025-12-06T22:00:00Z"
  },
  
  // Location
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [-1.7125, 42.8367]
    }
  },
  
  // Context fields (pattern /sdmenvironment)
  "name": {
    "type": "TextUnrestricted",
    "value": "Demanda Electrica Navarra"
  },
  "description": {
    "type": "TextUnrestricted",
    "value": "Subestacion de Orkoien - Demanda electrica en tiempo real"
  },
  "address": {
    "type": "TextUnrestricted",
    "value": "Subestacion de Orkoien, Navarra"
  },
  "streetAddress": {
    "type": "TextUnrestricted",
    "value": "Subestacion de Orkoien, Navarra"
  },
  "measure_id": {
    "type": "Text",
    "value": "EnergyDemand:Navarra:REE"
  },
  "measure_type": {
    "type": "Text",
    "value": "EnergyDemandObserved"
  },
  
  // AI Context
  "aiContext": {
    "type": "Text",
    "value": "Demanda electrica instantanea de Navarra en MW. Valores tipicos: 200-400 MW noche, 400-600 MW dia, picos 700 MW invierno. Actualizacion cada 5 min desde REE. Util para detectar anomalias, correlacionar con meteorologia, identificar patrones horarios. Limitaciones: datos agregados de Navarra."
  }
}
```

## Creating Entities

### Via Context Broker (Direct)
```bash
POST https://cb.iotplatform.telefonica.com:10027/v2/entities
Headers:
  - Fiware-Service: sc_pamplona_sandbox
  - Fiware-ServicePath: /02_Escribano
  - X-Auth-Token: <TOKEN>
  - Content-Type: application/json

Body: [entity JSON]
```

### Via IoT Agent (Recommended for sensor data)
See: `iot-agent.md` for autoprovision pattern

## Adding Attributes to Existing Entity

```bash
POST https://cb.iotplatform.telefonica.com:10027/v2/entities/{entityId}/attrs
Headers: [same as above]

Body:
{
  "newAttribute": {
    "type": "Text",
    "value": "value"
  }
}
```

## Querying Entities

### Get specific entity
```bash
GET /v2/entities/{entityId}
```

### List all entities
```bash
GET /v2/entities
```

### Filter by type
```bash
GET /v2/entities?type=EnergyDemandObserved
```

### Filter by location (geo-query)
```bash
GET /v2/entities?georel=near;maxDistance:1000&geometry=point&coords=42.8367,-1.7125
```

## Best Practices

1. **Always check Smart Data Models first** before creating custom fields
2. **Follow /sdmenvironment pattern** for consistency
3. **Add aiContext** if entity will be used by AI agents
4. **Use geo:json** for all location data
5. **Include measure_id and measure_type** for traceability
6. **Keep descriptions concise** but informative
7. **Document units** in aiContext (MW, °C, µg/m³, etc.)

## References

- Smart Data Models: https://github.com/smart-data-models
- NGSI-v2 Spec: https://fiware.github.io/specifications/nGSI/v2/stable/
- Config: `config.py` (lines 22-82)
- IoT Agent: `iot-agent.md`
