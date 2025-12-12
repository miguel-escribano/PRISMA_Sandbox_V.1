"""
PRISMA MVP - Knowledge Base del Agente
Información estática para que el LLM razone sobre el escenario.
"""

KNOWLEDGE_BASE = {
    "infraestructura_critica": {
        "hospitales": [
            {"nombre": "Hospital Universitario de Navarra (HUN)", "camas_urgencias": 80, "uci": 24},
            {"nombre": "Hospital Virgen del Camino", "camas_urgencias": 40, "uci": 12},
        ],
        "residencias_mayores": 12,
        "centros_salud": 15,
        "colegios": 47,
    },
    
    "umbrales_alerta": {
        "temperatura": {"amarillo": 38, "naranja": 40, "rojo": 42, "unit": "°C"},
        "pm25": {"bueno": 50, "moderado": 100, "malo": 150, "peligroso": 200, "unit": "µg/m³"},
        "urgencias_ocupacion": {"normal": 70, "alto": 85, "critico": 95, "unit": "%"},
        "llamadas_112_delta": {"normal": 20, "alerta": 40, "critico": 60, "unit": "%"},
    },
    
    "acciones_disponibles": [
        {"accion": "Activar alerta SMS población", "responsable": "Comunicación 112", "urgencia": "alta"},
        {"accion": "Abrir refugios climatizados", "responsable": "Ayuntamiento", "urgencia": "alta"},
        {"accion": "Refuerzo personal urgencias", "responsable": "Salud", "urgencia": "alta"},
        {"accion": "Suspender actividades exteriores", "responsable": "Ayuntamiento", "urgencia": "media"},
        {"accion": "Comunicado San Fermín", "responsable": "CECOPI", "urgencia": "media"},
        {"accion": "Activar protocolo evacuación valles", "responsable": "Protección Civil", "urgencia": "alta"},
    ],
    
    "stakeholders": {
        "CECOPI": "Centro de Coordinación Operativa - mando único en emergencias",
        "Delegación Gobierno": "Autoridad máxima, activa niveles de alerta",
        "Bomberos Navarra": "Director técnico de operaciones",
        "Salud Pública": "Epidemiología, coordinación sanitaria",
        "Policía Foral": "Orden público, evacuaciones",
        "Ayuntamiento Pamplona": "Servicios municipales, refugios",
        "112 Navarra": "Central de emergencias, comunicación pública",
    },
    
    "protocolos": {
        "PLATENA": "Plan Territorial de Emergencias de Navarra",
        "PLANINFONA": "Plan Especial de Incendios Forestales",
        "Plan Calor": "Actuación ante Altas Temperaturas",
    },
    
    "geografia": {
        "ubicacion": "Cuenca de Pamplona, Navarra",
        "pirineos": "30 km al norte",
        "valles_riesgo": ["Roncal", "Salazar", "Baztán"],
        "viento_sur": "Bochorno - crea condiciones de ignición",
        "viento_norte": "Trae humo de incendios pirenaicos a Pamplona",
    }
}

