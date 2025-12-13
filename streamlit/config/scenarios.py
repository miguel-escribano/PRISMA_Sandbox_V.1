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
        "capacidad_operativa_pct": 100,  # % personal sanitario disponible
        "contexto_politico": "Bajo",
        "riesgo_principal": "Niños/jóvenes expuestos, familias en exteriores",
        "fire_spread_multiplier": 1.0,
        "narrativa": "Fin de curso escolar, apertura de piscinas municipales. Inicio de temporada de calor."
    },
    
    "6_julio": {
        "fecha_display": "6 Julio",
        "poblacion": 1000000,
        "perfil_demografico": "Turistas internacionales + locales + medios",
        "capacidad_operativa_pct": 90,  # % personal sanitario disponible
        "contexto_politico": "Máximo",
        "riesgo_principal": "Chupinazo en horas. ¿Se cancela San Fermín? Crisis reputacional internacional",
        "fire_spread_multiplier": 1.2,
        "narrativa": "Día del Chupinazo. 1 millón de personas en la ciudad. Medios internacionales (CNN, BBC) en directo. Máxima tensión política."
    },
    
    "1_agosto": {
        "fecha_display": "1 Agosto",
        "poblacion": 250000,
        "perfil_demografico": "Residentes, población vulnerable",
        "capacidad_operativa_pct": 70,  # % personal sanitario disponible (vacaciones)
        "contexto_politico": "Medio",
        "riesgo_principal": "Personal sanitario reducido, incendio 5ª generación, menos recursos",
        "fire_spread_multiplier": 1.5,  # Más rápido, más intenso
        "narrativa": "Ciudad semi-vacía, pico de calor del verano. Personal sanitario reducido por vacaciones."
    }
}

# Mapeo de selección UI → key
SCENARIO_MAP = {
    "15 Junio": "15_junio",
    "6 Julio (San Fermín)": "6_julio",
    "1 Agosto": "1_agosto"
}

# =============================================================================
# STREAMS DE DATOS (entidades FIWARE)
# =============================================================================

STREAMS = {
    "WeatherObserved": {
        "entity_id": "WeatherObserved:Pamplona:01",
        "location": {"lat": 42.8125, "lon": -1.6458, "name": "Estación Meteo Pamplona"},
        "attributes": {
            "temperature": {"type": "Number", "unit": "°C", "range": [20, 45]},
            "relativeHumidity": {"type": "Number", "unit": "%", "range": [10, 100]},
            "windSpeed": {"type": "Number", "unit": "m/s", "range": [0, 30]},
            "windDirection": {"type": "Text", "values": ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]},
            "forecast6h": {"type": "Text", "values": ["stable", "worsening", "rain_expected", "wind_change"]},
            "forecastConfidence": {"type": "Number", "unit": "%", "range": [0, 100]},
        }
    },
    
    "AirQualityObserved": {
        "entity_id": "AirQualityObserved:Pamplona:01",
        "location": {"lat": 42.8168, "lon": -1.6432, "name": "Estación Calidad Aire Pamplona"},
        "attributes": {
            "pm25": {"type": "Number", "unit": "µg/m³", "range": [0, 500]},
            "pm10": {"type": "Number", "unit": "µg/m³", "range": [0, 600]},
        }
    },
    
    "ForestFire": {
        "entity_id": "ForestFire:Roncal:01",
        "location": {"lat": 42.7892, "lon": -0.9561, "name": "Valle de Roncal (Pirineos)"},
        "attributes": {
            "status": {"type": "Text", "values": ["inactive", "detected", "active", "contained", "extinguished"]},
            "severity": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
            "affectedArea": {"type": "Number", "unit": "ha", "range": [0, 10000]},
            "distanceToPamplona": {"type": "Number", "unit": "km", "range": [0, 100]},
        }
    },
    
    "EmergencyCalls112": {
        "entity_id": "EmergencyCalls112:Pamplona:01",
        "location": {"lat": 42.8055, "lon": -1.6460, "name": "SOS Navarra 112"},
        "attributes": {
            "respiratoryCalls": {"type": "Number", "unit": "calls/h", "range": [0, 100]},
            "heatStrokeCalls": {"type": "Number", "unit": "calls/h", "range": [0, 50]},
            "deltaVsNormal": {"type": "Number", "unit": "%", "range": [-50, 200]},
        }
    },
    
    "HospitalOccupancy": {
        "entity_id": "HospitalOccupancy:HUN:01",
        "location": {"lat": 42.8063, "lon": -1.6544, "name": "Hospital Universitario de Navarra"},
        "attributes": {
            "emergencyOccupancy": {"type": "Number", "unit": "%", "range": [0, 150]},
            "icuOccupancy": {"type": "Number", "unit": "%", "range": [0, 100]},
        }
    },
    
    "SocialMediaAlert": {
        "entity_id": "SocialMediaAlert:Pamplona:01",
        "location": {"lat": 42.8125, "lon": -1.6458, "name": "Pamplona (agregado)"},
        "attributes": {
            "mentionCount": {"type": "Number", "unit": "mentions/h", "range": [0, 1000]},
            "sentiment": {"type": "Text", "values": ["positive", "neutral", "negative", "alarm"]},
        }
    },
}

