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
    # -------------------------------------------------------------------------
    # WEATHER
    # -------------------------------------------------------------------------
    "WeatherObserved": {
        "entity_id": "WeatherObserved:AEMET_API_Pamplona_Noain",
        "location": {"lat": 42.8184, "lon": -1.6442, "name": "AEMET Pamplona/Noain"},
        "attributes": {
            "temperature": {"type": "Number", "unit": "°C", "range": [20, 45]},
            "relativeHumidity": {"type": "Number", "unit": "%", "range": [10, 100]},
            "windSpeed": {"type": "Number", "unit": "m/s", "range": [0, 30]},
            "windDirection": {"type": "Text", "values": ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]},
            "forecast6h": {"type": "Text", "values": ["stable", "worsening", "rain_expected", "wind_change"]},
            "forecastConfidence": {"type": "Number", "unit": "%", "range": [0, 100]},
        }
    },
    
    # -------------------------------------------------------------------------
    # AIR QUALITY - 3 sensors
    # -------------------------------------------------------------------------
    "AirQualityObserved_FelisaMunarriz": {
        "entity_id": "AirQualityObserved:ThinkingCities_FelisaMunarriz",
        "location": {"lat": 42.8069, "lon": -1.6441, "name": "Aire Felisa Munarriz (sur)"},
        "attributes": {
            "pm25": {"type": "Number", "unit": "µg/m³", "range": [0, 500]},
            "pm10": {"type": "Number", "unit": "µg/m³", "range": [0, 600]},
            "co": {"type": "Number", "unit": "mg/m³", "range": [0, 50]},
            "airQualityIndex": {"type": "Number", "unit": "index", "range": [1, 6]},
        }
    },
    "AirQualityObserved_Rochapea": {
        "entity_id": "AirQualityObserved:ThinkingCities_Rochapea",
        "location": {"lat": 42.8300, "lon": -1.6500, "name": "Aire Rochapea (norte)"},
        "attributes": {
            "pm25": {"type": "Number", "unit": "µg/m³", "range": [0, 500]},
            "pm10": {"type": "Number", "unit": "µg/m³", "range": [0, 600]},
            "co": {"type": "Number", "unit": "mg/m³", "range": [0, 50]},
            "airQualityIndex": {"type": "Number", "unit": "index", "range": [1, 6]},
        }
    },
    "AirQualityObserved_Iturrama": {
        "entity_id": "AirQualityObserved:GobNavarra_Iturrama",
        "location": {"lat": 42.8062, "lon": -1.6525, "name": "Aire GobNavarra Iturrama (oficial)"},
        "attributes": {
            "pm25": {"type": "Number", "unit": "µg/m³", "range": [0, 500]},
            "pm10": {"type": "Number", "unit": "µg/m³", "range": [0, 600]},
            "co": {"type": "Number", "unit": "mg/m³", "range": [0, 50]},
        }
    },
    
    # -------------------------------------------------------------------------
    # FOREST FIRES - 3 fronts
    # -------------------------------------------------------------------------
    "ForestFire_Baztan": {
        "entity_id": "ForestFire:EFFIS_API_Baztan",
        "location": {"lat": 43.1478, "lon": -1.5167, "name": "Incendio Baztan (40km N)"},
        "attributes": {
            "status": {"type": "Text", "values": ["inactive", "detected", "active", "high", "extreme", "contained", "extinguished"]},
            "intensity": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
            "sizeHectares": {"type": "Number", "unit": "ha", "range": [0, 10000]},
            "distanceToPamplona": {"type": "Number", "unit": "km", "range": [0, 100]},
            "evacuatedPeople": {"type": "Number", "unit": "personas", "range": [0, 5000]},
            "propagationRisk": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
        }
    },
    "ForestFire_Ultzama": {
        "entity_id": "ForestFire:EFFIS_API_Ultzama",
        "location": {"lat": 42.9500, "lon": -1.6500, "name": "Incendio Ultzama (20km N)"},
        "attributes": {
            "status": {"type": "Text", "values": ["inactive", "detected", "active", "high", "extreme", "contained", "extinguished"]},
            "intensity": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
            "sizeHectares": {"type": "Number", "unit": "ha", "range": [0, 10000]},
            "distanceToPamplona": {"type": "Number", "unit": "km", "range": [0, 100]},
            "evacuatedPeople": {"type": "Number", "unit": "personas", "range": [0, 5000]},
            "propagationRisk": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
        }
    },
    "ForestFire_Roncal": {
        "entity_id": "ForestFire:EFFIS_API_Roncal",
        "location": {"lat": 42.8000, "lon": -0.9500, "name": "Incendio Roncal (50km NE)"},
        "attributes": {
            "status": {"type": "Text", "values": ["inactive", "detected", "active", "high", "extreme", "contained", "extinguished"]},
            "intensity": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
            "sizeHectares": {"type": "Number", "unit": "ha", "range": [0, 10000]},
            "distanceToPamplona": {"type": "Number", "unit": "km", "range": [0, 100]},
            "evacuatedPeople": {"type": "Number", "unit": "personas", "range": [0, 5000]},
            "propagationRisk": {"type": "Text", "values": ["low", "medium", "high", "extreme"]},
        }
    },
    
    # -------------------------------------------------------------------------
    # EMERGENCY & HEALTH
    # -------------------------------------------------------------------------
    "EmergencyCalls": {
        "entity_id": "EmergencyCalls:ThinkingCities_SOS112",
        "location": {"lat": 42.8084, "lon": -1.6356, "name": "SOS Navarra 112"},
        "attributes": {
            "respiratoryCalls": {"type": "Number", "unit": "calls/h", "range": [0, 100]},
            "heatRelatedCalls": {"type": "Number", "unit": "calls/h", "range": [0, 50]},
            "totalCalls": {"type": "Number", "unit": "calls/h", "range": [0, 200]},
            "trafficCalls": {"type": "Number", "unit": "calls/h", "range": [0, 50]},
            "trend": {"type": "Text", "values": ["stable", "rising", "falling"]},
        }
    },
    "HospitalStatus": {
        "entity_id": "HospitalStatus:ThinkingCities_HUN_Urgencias",
        "location": {"lat": 42.8044, "lon": -1.6662, "name": "Hospital Universitario de Navarra"},
        "attributes": {
            "emergencyOccupancy": {"type": "Number", "unit": "%", "range": [0, 150]},
            "respiratoryAdmissions": {"type": "Number", "unit": "patients/h", "range": [0, 50]},
            "occupiedBeds": {"type": "Number", "unit": "%", "range": [0, 100]},
            "staffLevel": {"type": "Number", "unit": "%", "range": [0, 100]},
        }
    },
    
    # -------------------------------------------------------------------------
    # SOCIAL MEDIA
    # -------------------------------------------------------------------------
    "SocialMediaAlert": {
        "entity_id": "SocialMediaAlert:SocialMedia_API_Pamplona",
        "location": {"lat": 42.8180, "lon": -1.6432, "name": "Plaza del Castillo (centro)"},
        "attributes": {
            "mentions": {"type": "Number", "unit": "mentions/h", "range": [0, 1000]},
            "sentiment": {"type": "Text", "values": ["positive", "neutral", "negative", "alarm"]},
            "trendingHashtags": {"type": "StructuredValue", "description": "Lista de hashtags trending"},
        }
    },
    
    # -------------------------------------------------------------------------
    # TRAFFIC ALERTS - 3 roads
    # -------------------------------------------------------------------------
    "TrafficAlert_N121A": {
        "entity_id": "TrafficAlert:DGT_API_N121A_Baztan",
        "location": {"lat": 43.10, "lon": -1.52, "name": "N-121-A Baztán"},
        "attributes": {
            "status": {"type": "Text", "values": ["open", "restricted", "closed"]},
        }
    },
    "TrafficAlert_NA411": {
        "entity_id": "TrafficAlert:DGT_API_NA411_Ultzama",
        "location": {"lat": 42.9191, "lon": -1.6228, "name": "NA-411 Ultzama"},
        "attributes": {
            "status": {"type": "Text", "values": ["open", "restricted", "closed"]},
        }
    },
    "TrafficAlert_NA137": {
        "entity_id": "TrafficAlert:DGT_API_NA137_Roncal",
        "location": {"lat": 42.7148, "lon": -1.0079, "name": "NA-137 Roncal"},
        "attributes": {
            "status": {"type": "Text", "values": ["open", "restricted", "closed"]},
        }
    },
}
