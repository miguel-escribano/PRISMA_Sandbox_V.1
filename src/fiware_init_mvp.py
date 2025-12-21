"""
PRISMA MVP - FIWARE Entity Initialization

Creates all necessary entities in the /02_Escribano (Miguel) subservice
for the Heat Wave + Forest Fire demo scenario.

Run this ONCE to set up the initial state, then use scenario_runner.py 
to update values during the demo.

=============================================================================
ATTRIBUTE TYPES (static vs dynamic)
=============================================================================

STATIC attributes: Set once at entity creation, don't change during simulation
  - id, type, name, location, dateObserved, source
  - detectedAt (fire detection timestamp)
  - cause, roadName, direction (traffic alerts)

DYNAMIC attributes: Updated by scenario_runner.py from CSV timeline
  WeatherObserved:
    - temperature, relativeHumidity, windSpeed, windDirection
    - forecast6h, forecastConfidence
  AirQualityObserved:
    - pm25, pm10, airQualityIndex
  ForestFire:
    - status, intensity, sizeHectares, distanceToPamplona
    - evacuatedPeople, propagationRisk
  EmergencyCalls:
    - respiratoryCalls, heatRelatedCalls, totalCalls, trafficCalls, trend
  HospitalStatus:
    - emergencyOccupancy, respiratoryAdmissions, occupiedBeds, staffLevel
  SocialMediaAlert:
    - mentions, sentiment, trendingHashtags
  TrafficAlert:
    - status, estimatedReopenTime (calculated)

=============================================================================
ID FORMAT: Tipo:Fuente_Instancia
=============================================================================
Examples:
  WeatherObserved:AEMET_API_Pamplona_Noain
  ForestFire:EFFIS_API_Baztan
  AirQualityObserved:ThinkingCities_FelisaMunarriz
  TrafficAlert:DGT_API_N121A_Baztan
"""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fiware_client import FIWAREClient
from config import config

# Subservice for MVP (Miguel)
MVP_SUBSERVICE = "/02_Escribano"

# =============================================================================
# LOCATIONS - Distributed for realistic map visualization
# =============================================================================

# Forest fire locations (north/northeast flank)
LOC_FIRE_BAZTAN = [-1.5167, 43.1478]    # Valle Baztán - 40km north
LOC_FIRE_ULTZAMA = [-1.6500, 42.9500]   # Valle Ultzama - 20km north
LOC_FIRE_RONCAL = [-0.9500, 42.8000]    # Valle Roncal - 50km northeast

# Air quality sensors (Kunak TwIN Lab + GobNavarra)
LOC_AIR_KUNAK_BAJANAVARRA = [-1.6316, 42.8141]  # Kunak sensor - Baja Navarra
LOC_AIR_KUNAK_ROCHAPEA = [-1.6500, 42.8300]     # Kunak sensor - Rochapea north
LOC_AIR_ITURRAMA = [-1.6525, 42.8062]           # Iturrama - official GobNavarra station

# Drone locations (Bravodrones TwIN Lab) - Base en Policía Foral
LOC_DRONE_BASE = [-1.6253845194510725, 42.81405730745419]  # Sede Policía Foral Navarra

# Indoor Air Quality sensors (inBiot MICA_WELL TwIN Lab)
LOC_IAQ_HUN = [-1.6662, 42.8044]                           # Hospital HUN Urgencias
LOC_IAQ_INBIOT = [-1.6136467398333465, 42.79765365222666]  # Oficinas inBiot Mutilva
LOC_IAQ_ITAROA = [-1.5826414164837532, 42.82926658081576]  # CC Itaroa Huarte

# Other Pamplona locations
LOC_METEO_NOAIN = [-1.6442, 42.8184]    # AEMET station Pamplona
LOC_HUN = [-1.6662, 42.8044]            # Hospital Universitario Navarra
LOC_SOS_112 = [-1.6356, 42.8084]        # SOS Navarra 112 HQ
LOC_PLAZA_CASTILLO = [-1.6432, 42.8180] # City center (social media)

# Traffic alert locations (roads affected by fires)
LOC_TRAFFIC_N121A = [-1.52, 43.10]      # N-121-A near Baztán
LOC_TRAFFIC_NA411 = [-1.6228, 42.9191]  # NA-411 Ultzama valley
LOC_TRAFFIC_NA137 = [-1.0079, 42.7148]  # NA-137 Roncal access


def get_initial_entities():
    """
    Define all MVP entities with initial values for scenario start.
    
    Scenario: 6 July (pre-San Fermín), 09:00h
    Initial state: Hot but not critical yet
    """
    timestamp = "2025-07-06T09:00:00.000Z"
    
    return [
        # =====================================================================
        # WEATHER - Datos AEMET (estación Pamplona/Noain)
        # =====================================================================
        {
            "id": "WeatherObserved:AEMET_API_Pamplona_Noain",
            "type": "WeatherObserved",
            "name": {"type": "Text", "value": "Meteo AEMET Noain"},
            "agentContext": {"type": "Text", "value": "Datos de AEMET, Agencia Estatal de Meteorologia de Espana, organismo publico oficial. Estacion en Pamplona. Atributos: temperature en grados Celsius, relativeHumidity en porcentaje, windSpeed en km por hora, windDirection indica origen del viento donde N es norte y S es sur, forecast6h es prevision proximas 6 horas, forecastConfidence es fiabilidad de la prevision en porcentaje. Viento del norte empuja humo de incendios hacia la ciudad."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_METEO_NOAIN}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "temperature": {"type": "Number", "value": 35},
            "relativeHumidity": {"type": "Number", "value": 40},
            "windSpeed": {"type": "Number", "value": 5},
            "windDirection": {"type": "Text", "value": "S"},
            "forecast6h": {"type": "Text", "value": "stable"},
            "forecastConfidence": {"type": "Number", "value": 80},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # AIR QUALITY - Kunak Baja Navarra (TwIN Lab)
        # =====================================================================
        {
            "id": "AirQualityObserved:ThinkingCities_Kunak_BajaNavarra",
            "type": "AirQualityObserved",
            "name": {"type": "Text", "value": "Kunak BajaNavarra"},
            "agentContext": {"type": "Text", "value": "Sensor de calidad del aire de Kunak, empresa navarra del ecosistema TwIN Lab especializada en monitorizacion ambiental de alta precision. Integrado en el Gemelo Digital via ThinkingCities. Ubicado en zona Baja Navarra de Pamplona. Atributos: pm25 son particulas finas PM2.5 en microgramos por metro cubico, pm10 son particulas PM10, co es monoxido de carbono en mg por metro cubico, airQualityIndex es indice de 1 bueno a 6 peligroso. Detecta contaminacion por humo de incendios. Comparar con sensor Kunak norte para determinar direccion del humo."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_AIR_KUNAK_BAJANAVARRA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 28},
            "pm10": {"type": "Number", "value": 40},
            "co": {"type": "Number", "value": 0.5},
            "airQualityIndex": {"type": "Number", "value": 2},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # AIR QUALITY - Kunak Rochapea Norte (TwIN Lab)
        # =====================================================================
        {
            "id": "AirQualityObserved:ThinkingCities_Kunak_Rochapea",
            "type": "AirQualityObserved",
            "name": {"type": "Text", "value": "Kunak Rochapea"},
            "agentContext": {"type": "Text", "value": "Sensor de calidad del aire de Kunak, empresa navarra del ecosistema TwIN Lab. Ubicado en zona NORTE de Pamplona, barrio Rochapea, mas cercano a los incendios forestales. Atributos: pm25 son particulas finas PM2.5 en microgramos por metro cubico, pm10 son particulas PM10, co es monoxido de carbono en mg por metro cubico, airQualityIndex es indice de 1 bueno a 6 peligroso. Detecta humo ANTES que sensores del sur cuando el viento viene del norte. Sensor critico para alertas tempranas."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_AIR_KUNAK_ROCHAPEA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 32},
            "pm10": {"type": "Number", "value": 48},
            "co": {"type": "Number", "value": 0.6},
            "airQualityIndex": {"type": "Number", "value": 2},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # AIR QUALITY - Estacion oficial Gobierno de Navarra (Iturrama)
        # =====================================================================
        {
            "id": "AirQualityObserved:GobNavarra_Iturrama",
            "type": "AirQualityObserved",
            "name": {"type": "Text", "value": "Aire GobNavarra Iturrama"},
            "agentContext": {"type": "Text", "value": "Estacion oficial de calidad del aire del Gobierno de Navarra, red publica de vigilancia de la calidad del aire. Ubicada en barrio Iturrama, zona centro-sur de Pamplona. Datos oficiales validados. Atributos: pm25 son particulas finas PM2.5 en microgramos por metro cubico, pm10 son particulas PM10, co es monoxido de carbono en mg por metro cubico. Referencia oficial para alertas sanitarias."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_AIR_ITURRAMA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 25},
            "pm10": {"type": "Number", "value": 38},
            "co": {"type": "Number", "value": 0.4},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # INDOOR AIR QUALITY - Hospital HUN Urgencias (inBiot MICA_WELL TwIN Lab)
        # =====================================================================
        {
            "id": "IndoorAirQuality:inBiot_MICA_HUN_Urgencias",
            "type": "IndoorAirQuality",
            "name": {"type": "Text", "value": "IAQ Hospital HUN"},
            "agentContext": {"type": "Text", "value": "Sensor de calidad de aire INTERIOR modelo MICA_WELL de inBiot, empresa navarra del ecosistema TwIN Lab especializada en monitorizacion de calidad de aire interior para edificios saludables. Ubicado en Urgencias del Hospital Universitario de Navarra. Atributos: pm25 son particulas finas PM2.5 en interior que DEBEN SER MENORES que exterior si la filtracion funciona, co2 es dioxido de carbono en ppm que indica calidad de ventilacion donde 400-800 es bueno y mas de 1000 indica mala ventilacion. ALERTA CRITICA: Si pm25 interior sube mientras co2 tambien sube significa que el sistema de ventilacion esta introduciendo humo del exterior al intentar renovar aire. En ese caso CERRAR ventilacion externa y activar recirculacion con filtros HEPA."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_IAQ_HUN}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 8},
            "co2": {"type": "Number", "value": 450},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # INDOOR AIR QUALITY - Oficinas inBiot Mutilva (inBiot MICA_WELL TwIN Lab)
        # =====================================================================
        {
            "id": "IndoorAirQuality:inBiot_MICA_Oficinas_Mutilva",
            "type": "IndoorAirQuality",
            "name": {"type": "Text", "value": "IAQ Oficinas inBiot"},
            "agentContext": {"type": "Text", "value": "Sensor de calidad de aire INTERIOR modelo MICA_WELL de inBiot, empresa navarra del ecosistema TwIN Lab. Ubicado en las propias oficinas de inBiot en Mutilva, edificio de oficinas moderno con certificacion de calidad de aire. Atributos: pm25 son particulas PM2.5 interior que deben ser menores que exterior, co2 es dioxido de carbono en ppm indicador de ventilacion. REFERENCIA de edificio bien gestionado: si este sensor muestra problemas, la situacion exterior es muy grave. Comparar con sensores Kunak exteriores."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_IAQ_INBIOT}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 6},
            "co2": {"type": "Number", "value": 420},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # INDOOR AIR QUALITY - CC Itaroa Huarte (inBiot MICA_WELL TwIN Lab)
        # =====================================================================
        {
            "id": "IndoorAirQuality:inBiot_MICA_CC_Itaroa",
            "type": "IndoorAirQuality",
            "name": {"type": "Text", "value": "IAQ CC Itaroa"},
            "agentContext": {"type": "Text", "value": "Sensor de calidad de aire INTERIOR modelo MICA_WELL de inBiot, empresa navarra del ecosistema TwIN Lab. Ubicado en Centro Comercial Itaroa en Huarte, al NORTE de Pamplona mas cerca de los incendios. Gran afluencia de publico. Atributos: pm25 son particulas PM2.5 interior, co2 es dioxido de carbono en ppm. SENSOR CENTINELA: Por su ubicacion norte detectara antes la infiltracion de humo en interiores. Si pm25 sube aqui antes que en HUN o inBiot, confirma que el humo esta llegando desde el norte. Espacio con alta densidad de personas vulnerables."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_IAQ_ITAROA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "pm25": {"type": "Number", "value": 10},
            "co2": {"type": "Number", "value": 520},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FOREST FIRE 1 - Valle del Baztán (40km north)
        # =====================================================================
        {
            "id": "ForestFire:EFFIS_API_Baztan",
            "type": "ForestFire",
            "name": {"type": "Text", "value": "Incendio Baztan"},
            "agentContext": {"type": "Text", "value": "Datos de EFFIS, European Forest Fire Information System, sistema oficial de la Union Europea para monitorizacion de incendios forestales. Frente de incendio en Valle del Baztan, 40km al norte de Pamplona, zona boscosa pirenaica. Atributos: status es estado donde active significa activo y contained significa contenido, intensity es nivel de baja a extrema, sizeHectares son hectareas quemadas, distanceToPamplona es distancia a la ciudad en km, evacuatedPeople son personas evacuadas, propagationRisk es riesgo de expansion de bajo a extremo."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_BAZTAN}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "detectedAt": {"type": "DateTime", "value": "2025-07-05T14:30:00.000Z"},
            "status": {"type": "Text", "value": "active"},
            "intensity": {"type": "Text", "value": "medium"},
            "sizeHectares": {"type": "Number", "value": 200},
            "distanceToPamplona": {"type": "Number", "value": 65},
            "evacuatedPeople": {"type": "Number", "value": 50},
            "propagationRisk": {"type": "Text", "value": "medium"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FOREST FIRE 2 - Valle de Ultzama (20km north - closest to Pamplona)
        # =====================================================================
        {
            "id": "ForestFire:EFFIS_API_Ultzama",
            "type": "ForestFire",
            "name": {"type": "Text", "value": "Incendio Ultzama"},
            "agentContext": {"type": "Text", "value": "Datos de EFFIS, European Forest Fire Information System, sistema oficial de la Union Europea. Frente de incendio en Valle de Ultzama, solo 20km al norte de Pamplona. ATENCION: ES EL FRENTE MAS CERCANO A LA CIUDAD, maxima prioridad de monitorizacion. Atributos: status es estado, intensity es nivel, sizeHectares son hectareas, distanceToPamplona es distancia en km, evacuatedPeople son evacuados, propagationRisk es riesgo expansion. Vigilar especialmente distancia y propagacion."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_ULTZAMA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "detectedAt": {"type": "DateTime", "value": "2025-07-05T18:00:00.000Z"},
            "status": {"type": "Text", "value": "active"},
            "intensity": {"type": "Text", "value": "medium"},
            "sizeHectares": {"type": "Number", "value": 45},
            "distanceToPamplona": {"type": "Number", "value": 20},
            "evacuatedPeople": {"type": "Number", "value": 30},
            "propagationRisk": {"type": "Text", "value": "high"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FOREST FIRE 3 - Valle de Roncal (50km northeast)
        # =====================================================================
        {
            "id": "ForestFire:EFFIS_API_Roncal",
            "type": "ForestFire",
            "name": {"type": "Text", "value": "Incendio Roncal"},
            "agentContext": {"type": "Text", "value": "Datos de EFFIS, European Forest Fire Information System, sistema oficial de la Union Europea. Frente de incendio en Valle de Roncal, 50km al noreste de Pamplona. Zona turistica pirenaica con alta ocupacion en verano y acceso al Pirineo aragones. Atributos: status es estado, intensity es nivel, sizeHectares son hectareas, distanceToPamplona es distancia en km, evacuatedPeople son evacuados, propagationRisk es riesgo expansion."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_RONCAL}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "detectedAt": {"type": "DateTime", "value": "2025-07-05T12:00:00.000Z"},
            "status": {"type": "Text", "value": "active"},
            "intensity": {"type": "Text", "value": "high"},
            "sizeHectares": {"type": "Number", "value": 200},
            "distanceToPamplona": {"type": "Number", "value": 50},
            "evacuatedPeople": {"type": "Number", "value": 120},
            "propagationRisk": {"type": "Text", "value": "high"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # EMERGENCY CALLS - SOS Navarra 112
        # =====================================================================
        {
            "id": "EmergencyCalls:ThinkingCities_SOS112",
            "type": "EmergencyCalls",
            "name": {"type": "Text", "value": "112 SOS Navarra"},
            "agentContext": {"type": "Text", "value": "Datos del Gemelo Digital de Pamplona via ThinkingCities. Centro SOS Navarra 112, servicio publico de emergencias del Gobierno de Navarra que coordina bomberos, ambulancias y policia. Indicador temprano de crisis. Atributos: totalCalls son llamadas totales por hora, respiratoryCalls son llamadas por problemas respiratorios relacionados con humo, heatRelatedCalls son llamadas por golpes de calor, trafficCalls son llamadas por incidentes de trafico, trend indica tendencia donde rising es subiendo y stable es estable."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_SOS_112}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "totalCalls": {"type": "Number", "value": 0},
            "respiratoryCalls": {"type": "Number", "value": 8},
            "heatRelatedCalls": {"type": "Number", "value": 3},
            "trafficCalls": {"type": "Number", "value": 5},
            "trend": {"type": "Text", "value": "stable"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # HOSPITAL STATUS - HUN Urgencias
        # =====================================================================
        {
            "id": "HospitalStatus:ThinkingCities_HUN_Urgencias",
            "type": "HospitalStatus",
            "name": {"type": "Text", "value": "Hospital HUN Urgencias"},
            "agentContext": {"type": "Text", "value": "Datos del Gemelo Digital de Pamplona via ThinkingCities. Hospital Universitario de Navarra HUN, principal centro hospitalario publico de Pamplona perteneciente al Servicio Navarro de Salud. Servicio de Urgencias. Atributos: emergencyOccupancy es porcentaje de ocupacion de urgencias, occupiedBeds es porcentaje de camas ocupadas en el hospital, respiratoryAdmissions son ingresos por hora por problemas respiratorios, staffLevel es porcentaje de personal sanitario disponible. Coordinar derivaciones con 112."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_HUN}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "emergencyOccupancy": {"type": "Number", "value": 55},
            "respiratoryAdmissions": {"type": "Number", "value": 62},
            "occupiedBeds": {"type": "Number", "value": 65},
            "staffLevel": {"type": "Number", "value": 100},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # SOCIAL MEDIA - Analítica RRSS
        # =====================================================================
        {
            "id": "SocialMediaAlert:SocialMedia_API_Pamplona",
            "type": "SocialMediaAlert",
            "name": {"type": "Text", "value": "Social Pamplona"},
            "agentContext": {"type": "Text", "value": "Datos de servicio comercial de analitica de redes sociales en tiempo real. Monitoriza Twitter, Facebook e Instagram para Pamplona y Navarra. Indicador de percepcion publica y alarma social. Atributos: mentions son menciones por hora sobre la emergencia, sentiment es sentimiento general donde alarm es panico y negative es descontento, trendingHashtags son los hashtags mas usados. Util para detectar desinformacion, bulos y necesidad de comunicacion oficial urgente."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_PLAZA_CASTILLO}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "mentions": {"type": "Number", "value": 50},
            "sentiment": {"type": "Text", "value": "neutral"},
            "trendingHashtags": {
                "type": "StructuredValue",
                "value": ["#SanFermin2025", "#Pamplona", "#Navarra"]
            },
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # TRAFFIC ALERT 1 - N-121-A (Baztán access)
        # =====================================================================
        {
            "id": "TrafficAlert:DGT_API_N121A_Baztan",
            "type": "TrafficAlert",
            "name": {"type": "Text", "value": "Trafico N121A Baztan"},
            "agentContext": {"type": "Text", "value": "Datos de DGT, Direccion General de Trafico, organismo del Ministerio del Interior de Espana. Estado del trafico en carretera N-121-A, ruta principal Pamplona-Francia via Valle del Baztan. Atributos: status es estado donde open es abierta, restricted es restricciones y closed es cerrada, estimatedReopenTime es hora prevista de reapertura, cause es motivo del corte. Si esta cerrada impide evacuacion hacia norte y entrada de bomberos franceses."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_TRAFFIC_N121A}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "roadName": {"type": "Text", "value": "N-121-A"},
            "direction": {"type": "Text", "value": "Pamplona-Francia"},
            "status": {"type": "Text", "value": "open"},
            "estimatedReopenTime": {"type": "Text", "value": ""},
            "cause": {"type": "Text", "value": "forest_fire_smoke"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # TRAFFIC ALERT 2 - NA-411 (Ultzama valley)
        # =====================================================================
        {
            "id": "TrafficAlert:DGT_API_NA411_Ultzama",
            "type": "TrafficAlert",
            "name": {"type": "Text", "value": "Trafico NA411 Ultzama"},
            "agentContext": {"type": "Text", "value": "Datos de DGT, Direccion General de Trafico, organismo del Ministerio del Interior de Espana. Estado del trafico en carretera NA-411 al Valle de Ultzama. Ruta critica de evacuacion de poblaciones cercanas al frente de incendio de Ultzama. Atributos: status es estado donde open es abierta, restricted es restricciones y closed es cerrada, estimatedReopenTime es hora prevista de reapertura, cause es motivo del corte."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_TRAFFIC_NA411}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "roadName": {"type": "Text", "value": "NA-411"},
            "direction": {"type": "Text", "value": "Pamplona-Ultzama"},
            "status": {"type": "Text", "value": "open"},
            "estimatedReopenTime": {"type": "Text", "value": ""},
            "cause": {"type": "Text", "value": "evacuation"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # TRAFFIC ALERT 3 - NA-137 (Roncal access)
        # =====================================================================
        {
            "id": "TrafficAlert:DGT_API_NA137_Roncal",
            "type": "TrafficAlert",
            "name": {"type": "Text", "value": "Trafico NA137 Roncal"},
            "agentContext": {"type": "Text", "value": "Datos de DGT, Direccion General de Trafico, organismo del Ministerio del Interior de Espana. Estado del trafico en carretera NA-137 al Valle de Roncal. Acceso principal a zona turistica del Pirineo navarro y conexion con Aragon. Atributos: status es estado donde open es abierta, restricted es restricciones y closed es cerrada, estimatedReopenTime es hora prevista de reapertura, cause es motivo del corte. Coordinar con autoridades aragonesas si hay turistas atrapados."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_TRAFFIC_NA137}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "roadName": {"type": "Text", "value": "NA-137"},
            "direction": {"type": "Text", "value": "Pamplona-Roncal"},
            "status": {"type": "Text", "value": "open"},
            "estimatedReopenTime": {"type": "Text", "value": ""},
            "cause": {"type": "Text", "value": "forest_fire_smoke"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # DRONE - Inspector de Incendios (Bravodrones TwIN Lab)
        # Base: Sede Policía Foral de Navarra
        # =====================================================================
        {
            "id": "Drone:Bravodrones_Fire_001",
            "type": "Drone",
            "name": {"type": "Text", "value": "Dron Inspector Incendios"},
            "agentContext": {"type": "Text", "value": "Dron de inspeccion de incendios de Bravodrones, empresa del ecosistema TwIN Lab especializada en computer vision y drones para emergencias. Base en sede de Policia Foral de Navarra. Equipado con camara termica para detectar focos de calor en el suelo. Atributos: status es estado donde idle es en base Policia Foral, en_route es volando hacia destino, inspecting es inspeccionando incendio y returning es regresando a base, altitude es altura de vuelo en metros, groundTemperature es temperatura del suelo detectada en grados Celsius, hotspotCount es numero de focos secundarios detectados, assignedToFire es ID del incendio al que esta asignado. Proporciona datos que satelites no pueden ver."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_DRONE_BASE}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "status": {"type": "Text", "value": "idle"},
            "altitude": {"type": "Number", "value": 0},
            "groundTemperature": {"type": "Number", "value": 35},
            "hotspotCount": {"type": "Number", "value": 0},
            "assignedToFire": {"type": "Text", "value": ""},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # DRONE - Vigilancia de Masas (Bravodrones TwIN Lab)
        # Base: Sede Policía Foral de Navarra
        # =====================================================================
        {
            "id": "Drone:Bravodrones_Crowd_001",
            "type": "Drone",
            "name": {"type": "Text", "value": "Dron Vigilancia Masas"},
            "agentContext": {"type": "Text", "value": "Dron de vigilancia de masas de Bravodrones, empresa del ecosistema TwIN Lab. Base en sede de Policia Foral de Navarra. Equipado con computer vision para analisis de multitudes en eventos masivos como San Fermin. Atributos: status es estado donde idle es en base Policia Foral, monitoring es vigilando zona asignada y alert es alerta detectada, altitude es altura de vuelo en metros, crowdDensity es densidad de personas por metro cuadrado, panicIndicator es puntuacion de 0 a 100 donde valores altos indican movimiento caotico o estampida potencial, flowDirection indica hacia donde se mueve la masa o si esta dispersing. CRITICO para San Fermin con 1 millon de personas."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_DRONE_BASE}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "status": {"type": "Text", "value": "idle"},
            "altitude": {"type": "Number", "value": 0},
            "crowdDensity": {"type": "Number", "value": 0},
            "panicIndicator": {"type": "Number", "value": 0},
            "flowDirection": {"type": "Text", "value": "stable"},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FIRE FORECAST - Baztan (TESICNOR RRD TwIN Lab)
        # =====================================================================
        {
            "id": "FireForecast:TESICNOR_RRD_Baztan",
            "type": "FireForecast",
            "name": {"type": "Text", "value": "Prediccion Baztan TESICNOR"},
            "agentContext": {"type": "Text", "value": "Prediccion de evolucion del incendio generada por modelos de TESICNOR RRD, empresa del ecosistema TwIN Lab especializada en reduccion de riesgo de desastres naturales. Modelos Python que procesan datos meteorologicos y generan predicciones geoespaciales. Atributos: predictedSizeHectares es tamano predicho del incendio en hectareas en horizonte 2h, predictedPropagation es direccion prevista de expansion, arrivalToPamplona es hora estimada de llegada del HUMO a la ciudad NO del fuego ya que el fuego tardaria dias en llegar, confidence es fiabilidad del modelo en porcentaje. COMPARAR con datos EFFIS actuales para anticipar evolucion. El humo viaja mucho mas rapido que el fuego."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_BAZTAN}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "predictedSizeHectares": {"type": "Number", "value": 250},
            "predictedPropagation": {"type": "Text", "value": "S"},
            "arrivalToPamplona": {"type": "Text", "value": ""},
            "confidence": {"type": "Number", "value": 75},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FIRE FORECAST - Ultzama (TESICNOR RRD TwIN Lab)
        # =====================================================================
        {
            "id": "FireForecast:TESICNOR_RRD_Ultzama",
            "type": "FireForecast",
            "name": {"type": "Text", "value": "Prediccion Ultzama TESICNOR"},
            "agentContext": {"type": "Text", "value": "Prediccion de evolucion del incendio de Ultzama por TESICNOR RRD. ATENCION: Este es el frente MAS CERCANO a Pamplona a solo 20km, las predicciones de este modelo son CRITICAS. Atributos: predictedSizeHectares es tamano predicho en 2h, predictedPropagation es direccion, arrivalToPamplona es hora llegada del HUMO a Pamplona NO del fuego porque el fuego tardaria 1-2 dias en llegar pero el humo con viento norte llega en 1-2 horas, confidence es fiabilidad. IMPORTANTE: Si el modelo predice llegada de humo, ACTUAR PREVENTIVAMENTE antes de que sensores Kunak lo confirmen."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_ULTZAMA}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "predictedSizeHectares": {"type": "Number", "value": 60},
            "predictedPropagation": {"type": "Text", "value": "S"},
            "arrivalToPamplona": {"type": "Text", "value": ""},
            "confidence": {"type": "Number", "value": 80},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
        # =====================================================================
        # FIRE FORECAST - Roncal (TESICNOR RRD TwIN Lab)
        # =====================================================================
        {
            "id": "FireForecast:TESICNOR_RRD_Roncal",
            "type": "FireForecast",
            "name": {"type": "Text", "value": "Prediccion Roncal TESICNOR"},
            "agentContext": {"type": "Text", "value": "Prediccion de evolucion del incendio de Roncal por TESICNOR RRD, empresa del ecosistema TwIN Lab. Zona turistica pirenaica a 50km. Atributos: predictedSizeHectares es tamano predicho en 2h, predictedPropagation es direccion de expansion, arrivalToPamplona es hora estimada de llegada del HUMO NO del fuego, confidence es fiabilidad del modelo. El incendio de Roncal esta mas lejos y con viento SW el humo no suele afectar directamente a Pamplona."},
            "location": {
                "type": "geo:json",
                "value": {"type": "Point", "coordinates": LOC_FIRE_RONCAL}
            },
            "dateObserved": {"type": "DateTime", "value": timestamp},
            "predictedSizeHectares": {"type": "Number", "value": 280},
            "predictedPropagation": {"type": "Text", "value": "SW"},
            "arrivalToPamplona": {"type": "Text", "value": ""},
            "confidence": {"type": "Number", "value": 70},
            "source": {"type": "Text", "value": "PRISMA_MVP_SYNTHETIC"}
        },
        
    ]


def init_fiware_entities():
    """Initialize all MVP entities in FIWARE Context Broker."""
    
    print("=" * 60)
    print("PRISMA MVP - FIWARE Entity Initialization")
    print("=" * 60)
    print(f"Subservice: {MVP_SUBSERVICE}")
    print(f"Service: {config.SERVICE}")
    print()
    
    # Create client for MVP subservice
    client = FIWAREClient(subservice=MVP_SUBSERVICE)
    
    # Refresh token first
    print("Authenticating...")
    try:
        client.refresh_token()
        print("[OK] Authentication successful")
    except Exception as e:
        print(f"[ERROR] Authentication failed: {e}")
        return False
    
    # Get entities to create
    entities = get_initial_entities()
    print(f"\nCreating {len(entities)} entities...")
    print("-" * 40)
    
    created = 0
    updated = 0
    errors = 0
    
    for entity in entities:
        entity_id = entity["id"]
        entity_type = entity["type"]
        
        try:
            # Try to create entity
            client.create_entity(entity)
            print(f"[+] Created: {entity_id} ({entity_type})")
            created += 1
            
        except Exception as create_error:
            # If entity exists, try to update it
            if "Already Exists" in str(create_error) or "422" in str(create_error):
                try:
                    # Remove id and type for update
                    update_data = {k: v for k, v in entity.items() if k not in ["id", "type"]}
                    client.update_entity(entity_id, update_data)
                    print(f"[~] Updated: {entity_id} ({entity_type})")
                    updated += 1
                except Exception as update_error:
                    print(f"[X] Error updating {entity_id}: {update_error}")
                    errors += 1
            else:
                print(f"[X] Error creating {entity_id}: {create_error}")
                errors += 1
    
    print("-" * 40)
    print(f"\nResults:")
    print(f"  Created: {created}")
    print(f"  Updated: {updated}")
    print(f"  Errors:  {errors}")
    print()
    
    # Verify by querying
    print("Verifying entities...")
    try:
        all_entities = client.query_entities(limit=100)
        types = {}
        for e in all_entities:
            t = e.get("type", "Unknown")
            types[t] = types.get(t, 0) + 1
        
        print(f"\nEntities in {MVP_SUBSERVICE}:")
        for t, count in sorted(types.items()):
            print(f"  - {t}: {count}")
        print(f"\nTotal: {len(all_entities)} entities")
        
    except Exception as e:
        print(f"Warning: Could not verify entities: {e}")
    
    return errors == 0


def cleanup_entities():
    """Remove all MVP entities (for testing)."""
    
    print("=" * 60)
    print("PRISMA MVP - Cleanup Entities")
    print("=" * 60)
    
    client = FIWAREClient(subservice=MVP_SUBSERVICE)
    client.refresh_token()
    
    entities = get_initial_entities()
    
    for entity in entities:
        entity_id = entity["id"]
        try:
            client.delete_entity(entity_id)
            print(f"[-] Deleted: {entity_id}")
        except Exception as e:
            print(f"- Not found or error: {entity_id}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Initialize FIWARE entities for PRISMA MVP")
    parser.add_argument("--cleanup", action="store_true", help="Remove all MVP entities")
    parser.add_argument("--verify", action="store_true", help="Only verify existing entities")
    
    args = parser.parse_args()
    
    if args.cleanup:
        cleanup_entities()
    elif args.verify:
        client = FIWAREClient(subservice=MVP_SUBSERVICE)
        client.refresh_token()
        entities = client.query_entities(limit=100)
        print(f"Found {len(entities)} entities in {MVP_SUBSERVICE}")
        for e in entities:
            print(f"  - {e['id']} ({e['type']})")
    else:
        success = init_fiware_entities()
        if success:
            print("\n[SUCCESS] Initialization complete!")
        else:
            print("\n[FAILED] Initialization had errors")
            sys.exit(1)

