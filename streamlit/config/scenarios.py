"""
PRISMA MVP - Configuración de Escenarios
Caso: Ola de Calor + Incendio Forestal Pirineos
"""

# =============================================================================
# CONTEXTO POR FECHA
# =============================================================================

SCENARIOS = {
    "15_junio": {
        "fecha_display": "15 Junio",
        "poblacion": 350000,
        "perfil_demografico": "Familias, niños/jóvenes",
        "hospital_capacity_pct": 100,
        "contexto_politico": "Bajo",
        "riesgo_principal": "Niños/jóvenes expuestos, familias en exteriores",
        "fire_spread_multiplier": 1.0,
        "narrativa": "Fin de curso escolar, apertura de piscinas municipales. Inicio de temporada de calor."
    },
    
    "1_julio": {
        "fecha_display": "1 Julio",
        "poblacion": 600000,
        "perfil_demografico": "Turistas + locales",
        "hospital_capacity_pct": 95,
        "contexto_politico": "Máximo",
        "riesgo_principal": "¿Se cancela San Fermín? Crisis reputacional internacional",
        "fire_spread_multiplier": 1.2,
        "narrativa": "Pre-San Fermín, turistas llegando. Medios internacionales (CNN, BBC) ya en Pamplona. Máxima tensión política."
    },
    
    "1_agosto": {
        "fecha_display": "1 Agosto",
        "poblacion": 250000,
        "perfil_demografico": "Residentes, población vulnerable",
        "hospital_capacity_pct": 70,  # Vacaciones personal sanitario
        "contexto_politico": "Medio",
        "riesgo_principal": "Personal sanitario reducido, incendio 5ª generación, menos recursos",
        "fire_spread_multiplier": 1.5,  # Más rápido, más intenso
        "narrativa": "Ciudad semi-vacía, pico de calor del verano. Personal sanitario reducido por vacaciones."
    }
}

# Mapeo de selección UI → key
SCENARIO_MAP = {
    "15 Junio": "15_junio",
    "1 Julio (San Fermín)": "1_julio",
    "1 Agosto": "1_agosto"
}

# =============================================================================
# STREAMS DE DATOS (entidades FIWARE)
# =============================================================================

STREAMS = {
    "WeatherObserved": {
        "entity_id": "WeatherObserved:Pamplona:01",
        "attributes": {
            "temperature": {"type": "Number", "unit": "°C", "range": [20, 45]},
            "relativeHumidity": {"type": "Number", "unit": "%", "range": [10, 100]},
            "windSpeed": {"type": "Number", "unit": "m/s", "range": [0, 30]},
            "windDirection": {"type": "Text", "values": ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]},
        }
    },
    
    "AirQualityObserved": {
        "entity_id": "AirQualityObserved:Pamplona:01",
        "attributes": {
            "pm25": {"type": "Number", "unit": "µg/m³", "range": [0, 500]},
            "pm10": {"type": "Number", "unit": "µg/m³", "range": [0, 600]},
            "no2": {"type": "Number", "unit": "µg/m³", "range": [0, 400]},
            "o3": {"type": "Number", "unit": "µg/m³", "range": [0, 300]},
        }
    },
    
    "ForestFire": {
        "entity_id": "ForestFire:Roncal:01",
        "attributes": {
            "status": {"type": "Text", "values": ["inactive", "detected", "active", "contained", "extinguished"]},
            "severity": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
            "affectedArea": {"type": "Number", "unit": "ha", "range": [0, 10000]},
            "spreadRate": {"type": "Number", "unit": "ha/h", "range": [0, 100]},
        }
    },
    
    "EmergencyCalls112": {
        "entity_id": "EmergencyCalls112:Pamplona:01",
        "attributes": {
            "totalCalls": {"type": "Number", "unit": "calls/h", "range": [0, 500]},
            "respiratoryCalls": {"type": "Number", "unit": "calls/h", "range": [0, 100]},
            "heatStrokeCalls": {"type": "Number", "unit": "calls/h", "range": [0, 50]},
            "deltaVsNormal": {"type": "Number", "unit": "%", "range": [-50, 200]},
        }
    },
    
    "HospitalOccupancy": {
        "entity_id": "HospitalOccupancy:HUN:01",
        "attributes": {
            "emergencyOccupancy": {"type": "Number", "unit": "%", "range": [0, 150]},
            "icuOccupancy": {"type": "Number", "unit": "%", "range": [0, 100]},
            "availableBeds": {"type": "Number", "unit": "beds", "range": [0, 200]},
        }
    },
    
    "SocialMediaAlert": {
        "entity_id": "SocialMediaAlert:Pamplona:01",
        "attributes": {
            "mentionCount": {"type": "Number", "unit": "mentions/h", "range": [0, 1000]},
            "sentiment": {"type": "Text", "values": ["positive", "neutral", "negative", "alarm"]},
            "topHashtags": {"type": "Text", "example": "#OlaDeCalor,#Pamplona,#Humo"},
        }
    },
}

