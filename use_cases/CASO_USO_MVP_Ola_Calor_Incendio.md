# CASO DE USO MVP: Ola de Calor + Incendio Forestal Pirineos

**Inspirado en:** Everbridge Critical Event Management  
**Diferencial PRISMA:** No solo notificamos crisis, **prevenimos cascadas sistémicas**  
**Fecha objetivo demo:** 19 diciembre 2025 (Elevator Pitch TwIN Lab)

> 📋 **MVP:** Enfocado en este único escenario. Caso cyber aplazado a v2.

---

## 🎯 Resumen Ejecutivo

### Por qué este caso de uso

**Ventajas estratégicas:**
- ✅ **Evento recurrente y predecible** → Cada verano hay olas de calor (mercado garantizado)
- ✅ **Cascada multi-sistema** → Calor + Humo → Hospitales → Mortalidad → Crisis política
- ✅ **Referencias conocidas** → Ola calor 2023 (47.000 muertos Europa), incendios Grecia 2024
- ✅ **Contexto temporal dramático** → San Fermín amplifica todo x10
- ✅ **Diferencial claro** → Planes de calor actuales son reactivos, PRISMA predice
- ✅ **Fusión multi-fuente heterogénea** → El verdadero valor de PRISMA:
  - 🌡️ **AEMET** (pronóstico temperatura, viento, humedad)
  - 🔥 **EFFIS/Bomberos** (detección incendios, propagación)
  - 💨 **Calidad aire** (sensores Pamplona, satélite)
  - 🏥 **Ocupación urgencias** (hospitales, centros salud)
  - 📞 **112** (llamadas, patrones, geolocalización)
  - 🐦 **Twitter/X** (hashtags, quejas, alertas ciudadanas)
  - 🗺️ **Gemelos digitales** (Tracasa urbano, Tesicnor/RRD industrial)

### Mensaje clave

> **"No gestionamos eventos. Prevenimos cascadas."**
> 
> - Detectamos los triggers (temperatura + incendio + humo)
> - Predecimos la cascada (qué fallará después)
> - Coordinamos la respuesta (CECOPI informado, ciudadanía alertada)

---

## 📋 Ficha Técnica del Escenario

### Geografía y contexto

**Pamplona y valles pirenaicos:**
- 🏙️ **Cuenca de Pamplona:** 350.000 habitantes (hasta 1M+ en San Fermín)
- 🏔️ **Pirineos navarros:** 30 km al norte, valles de Roncal, Salazar, Baztán
- 🌲 **Masa forestal:** 600.000 hectáreas forestales en Navarra
- 🌡️ **Clima:** Continental, veranos 35-40°C, viento sur (bochorno)

### El escenario: Tormenta perfecta

**Secuencia de eventos:**
```
Día -3: Ola calor extrema (40°C), viento sur (bochorno), humedad <20%
        → Condiciones perfectas para ignición
Día -1: Incendio forestal Valle de Roncal (origen: rayo seco)
        → Humo se dispersa hacia Francia (viento sur)
Día 0:  Viento gira a NORTE/NOROESTE + inversión térmica
        → Humo baja hacia Pamplona, atrapado a baja altura
        → Calidad aire se degrada (PM2.5 >150)
        → Urgencias empiezan a saturarse
        → Twitter explota con quejas
        → CECOPI debe decidir: ¿San Fermín sigue adelante?
```

### El factor temporal: 3 escenarios predefinidos

**El mismo evento tiene impacto radicalmente diferente según cuándo ocurre.**

El simulador ofrece 3 fechas predefinidas (no calendario libre):

| Fecha | Contexto | Población | Cap. Operativa | Riesgo principal |
|-------|----------|-----------|----------------|------------------|
| **15 Junio** | Fin curso escolar, piscinas | 350k | 100% | Niños/jóvenes expuestos, familias en exteriores |
| **6 Julio** | Día Chupinazo San Fermín | 1M | 90% | **Máxima tensión**: ¿se cancela? Crisis internacional |
| **1 Agosto** | Ciudad semi-vacía, pico calor | 250k | 70% | Personal reducido, incendio 5ª generación |

**En el simulador:** El usuario selecciona una de las 3 fechas y el sistema ajusta automáticamente:
- Población y perfil demográfico
- Capacidad hospitalaria disponible
- Contexto político y mediático
- Velocidad de propagación del incendio
- Texto narrativo del escenario

### Cascada de impactos

| Fase | Trigger | Impacto directo | Cascada |
|------|---------|-----------------|---------|
| **1** | Ola calor 40°C | Golpes de calor | Urgencias +30% |
| **2** | Incendio Pirineos | Evacuación valles | Carreteras cortadas |
| **3** | Humo en Pamplona | PM2.5 >150 | Problemas respiratorios |
| **4** | Calor + Humo | Mortalidad vulnerable | Residencias colapsadas |
| **5** | Pre-San Fermín | Decisión política | ¿Cancelar? Crisis internacional |

### Dependencias críticas

**Sistema sanitario:**
- 🏥 **Hospital Universitario de Navarra** + Hospital Virgen del Camino
- 🏨 **Centros de salud** (saturación consultas)
- 👴 **12 residencias mayores** (población más vulnerable)
- 🚑 **SAMUR/DYA** (ambulancias limitadas)

**Infraestructura urbana:**
- 🚗 **Tráfico** (evacuación valles, acceso limitado)
- 💧 **Fuentes públicas** (hidratación)
- 🏛️ **Espacios refrigerados** (bibliotecas, centros cívicos)

**Contexto San Fermín:**
- 🎪 **Infraestructura fiestas** (escenarios, carpas)
- 🏃 **Encierros** (¿se pueden correr con 45°C?)
- 📺 **Medios internacionales** (CNN, BBC ya en Pamplona)

### Referencias reales

**Humo en Pamplona - Precedentes documentados:**
- **Febrero 2023:** Incendios en Saint-Jean-Pied-de-Port (Francia, junto a Roncesvalles) → humo llegó a Pamplona por vientos del noroeste. Población notó olor a quemado. ([noticiasdenavarra.com](https://www.noticiasdenavarra.com/sucesos/2023/02/16/incendios-forestales-sur-francia-ahuman-6454657.html))
- **Julio 2022:** Incendio en Gironda (Francia) → humo llegó a Pamplona por vientos del noreste + **inversión térmica** que atrapó el humo a baja altura. ([noticiasdenavarra.com](https://www.noticiasdenavarra.com/sociedad/2022/07/15/humo-viajo-pamplona-5821053.html))

**Ola de calor Europa 2023:**
- 47.000 muertes atribuidas al calor
- España: 6.800 muertos
- Problema: Planes de calor reactivos, no predictivos

**Incendios Grecia agosto 2024:**
- Evacuaciones caóticas
- Humo en Atenas durante días
- Turismo afectado

**Lección:** Los datos existían. Nadie fusionó información para ver la cascada.

---

## 📊 Fuentes de Datos (Tiempo Real)

### Meteorología
- **AEMET Open Data** → Temperatura, humedad, viento, pronóstico 7 días
- **Meteoclimatic** → Estaciones amateur (más densidad)
- **Modelo propio** → Índice de riesgo combinado

### Calidad del aire
- **Sensores Gobierno Navarra** → PM2.5, PM10, NO2, O3
- **Copernicus CAMS** → Satélite, plumas de humo
- **PurpleAir** → Sensores ciudadanos (si los hay)

### Incendios
- **EFFIS** (European Forest Fire Information System) → Detección satélite
- **Bomberos Navarra** → Datos operativos
- **Cámaras vigilancia forestal** → Detección temprana

### Sanitarios
- **Ocupación urgencias** → HUN, Virgen del Camino
- **Centros de salud** → Consultas por golpe calor
- **Residencias** → Incidencias reportadas

### Emergencias
- **112** → Llamadas, categorización, geolocalización
- **Patrones** → Picos de llamadas = señal temprana

### Social
- **Twitter/X** → Hashtags #OlaDeCalor #Pamplona #SanFermin
- **Quejas ciudadanas** → App municipal

### Gemelos digitales
- **Tracasa** → Gemelo urbano Pamplona, IDENA
- **Tesicnor/RRD** → Simulación industrial, riesgos

---

## 🏛️ CECOPI: Centro de Coordinación

### Composición
- 🏛️ **Delegación Gobierno** (mando único)
- 🚒 **Bomberos Navarra** (director técnico)
- 🏥 **Salud Pública** (epidemiología)
- 🚔 **Policía Foral** (orden público)
- 📢 **Comunicación** (notas prensa, X)
- 🏙️ **Ayuntamiento** (servicios municipales)

### Lo que PRISMA aporta al CECOPI
- 📊 **Dashboard consolidado** → Todos los datos en una vista
- 🔮 **Predicción cascada** → "Si no actuamos en 2h, urgencias colapsan"
- ✅ **Recomendaciones priorizadas** → Qué hacer primero
- 📝 **Borradores comunicación** → Notas prensa pre-redactadas
- ⏱️ **Trazabilidad** → Quién decidió qué, cuándo

---

## 🔗 Integración con Ecosistema Existente (SOS Navarra 112)

### El Módulo de Grandes Emergencias (Tracasa)

Navarra ya cuenta con uno de los mejores sistemas de gestión de emergencias de España: el **Módulo de Grandes Emergencias** del SOS Navarra 112, desarrollado por **Tracasa Instrumental** y premiado en los USEC Awards 2025.

**Lo que el Módulo YA tiene:**
- ✅ Visualización de incidencias en tiempo real
- ✅ Geolocalización de recursos (aéreos, terrestres)
- ✅ Integración GIS con capas (incluida AEMET)
- ✅ Guiado por fases de planes de protección civil
- ✅ Trazabilidad de acciones
- ✅ Apoyo al CAE (Comité Asesor de Emergencia)

**Fuente:** [Navarra.es](https://www.navarra.es/es/-/nota-prensa/sos-navarra-112-galardonado-por-una-herramienta-para-mejorar-la-coordinacion-y-comunicacion-entre-los-diferentes-servicios-que-intervienen-en-grandes-emergencias)

### Lo que el Módulo NO tiene (y PRISMA aporta)

El Módulo del 112 es un **excelente sistema de registro**: tiene los datos, tiene las capas, tiene la trazabilidad. Pero **no tiene inteligencia situacional**.

| Módulo SOS Navarra 112 | PRISMA |
|------------------------|--------|
| Tiene datos (AEMET, GIS, recursos) | Tiene **inteligencia** |
| **Registra** eventos/incidencias | **Predice** lo que va a pasar |
| Reactivo: "Ha pasado X" | Proactivo: "Va a pasar X en 2h" |
| Capas de información separadas | **Correlación** entre capas |
| Operadores interpretan | IA interpreta y recomienda |
| Actúa cuando se declara emergencia | Actúa **antes** de que se declare |

> **"El Módulo del 112 es la memoria. PRISMA es el cerebro."**

### Posicionamiento: Complemento, no competencia

```
┌─────────────────────────────────────────────────────────────────┐
│                    CICLO DE UNA EMERGENCIA                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ANTES              DURANTE                DESPUÉS              │
│   ══════             ════════               ════════             │
│                                                                  │
│   🔮 PRISMA          🚨 Módulo Tracasa      🔮 PRISMA            │
│   - Predicción       - Coordinación         - Análisis           │
│   - Detección        - Recursos             - Aprendizaje        │
│     temprana         - GIS operativo                             │
│   - Alertas          - Fases protocolos                          │
│     preventivas      - CAE                                       │
│                                                                  │
│   "2h antes de       "Durante la            "Qué aprendimos"     │
│    que explote"       emergencia"                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Tracasa como socio tecnológico natural

- Tracasa ya desarrolló el Módulo de Grandes Emergencias
- Conocen la operativa de SOS Navarra 112
- PRISMA podría ser un **módulo adicional** que se integra
- Flujo: **PRISMA detecta → alerta al Módulo → Módulo gestiona**

### El pitch ajustado

> **"Navarra ya tiene uno de los mejores sistemas de gestión de emergencias de España. Pero gestiona emergencias DECLARADAS.**
>
> **PRISMA actúa ANTES: correlaciona datos, predice cascadas, y te da 2 horas de ventaja para que la emergencia no llegue a declararse."**

---

## 📢 Sistema de Alertas y Comunicación

### Realidad operativa actual (SOS Navarra 112)

Existe **un único responsable de comunicación** autorizado a comunicar externamente, trabajando **24/7**, que genera:

| Canal | Formato | Destino |
|-------|---------|---------|
| **Notas de prensa oficiales** | Formal, institucional | Medios nacionales/regionales |
| **Mensajes prensa local** | Formato estándar | WhatsApp a periodistas locales |
| **Twitter/X** | Corto, directo | [@112_na](https://x.com/112_na) (público) |

### El problema: cuello de botella

Una sola persona gestionando 3 canales, 24/7, en situaciones de máximo estrés. Cualquier retraso en comunicación puede costar vidas o generar crisis de confianza.

### Lo que PRISMA aporta al responsable de comunicación

| Tarea actual (manual) | Con PRISMA (asistido) |
|-----------------------|----------------------|
| Redactar nota de prensa desde cero | **Borrador pre-generado** basado en datos actuales |
| Formatear mensaje WhatsApp manualmente | **Plantilla auto-rellenada** con formato estándar |
| Escribir tweet bajo presión | **Sugerencia de tweet** lista para aprobar |
| Decidir qué comunicar primero | **Priorización automática** según gravedad |
| Buscar datos en múltiples fuentes | **Resumen consolidado** en una vista |

**Human-in-the-loop:** PRISMA genera borradores, el responsable valida y publica. Nunca se publica sin aprobación humana.

### Canales de salida (ampliados)

| Canal | Audiencia | Contenido | Validación |
|-------|-----------|-----------|------------|
| **Nota de prensa** | Medios | Comunicado formal | ✅ Humano valida |
| **WhatsApp prensa** | Periodistas locales | Formato estándar | ✅ Humano valida |
| **Twitter/X @112_na** | Público general | Alertas oficiales | ✅ Humano valida |
| **SMS masivo** | Población general | Instrucciones (hidratación, refugios) | ✅ Humano valida |
| **SMS personalizado** | Responsables políticos | Situación + decisiones | Automático (pre-aprobado) |
| **Telegram interno** | Equipo CECOPI | Coordinación rápida | Automático |

**Ejemplo mensaje Telegram CECOPI:**
```
🔴 PRISMA ALERTA - 14:32h

Situación: Calor extremo + humo incendio
Riesgo: CRÍTICO
Predicción: Urgencias >100% en 3h

Acciones recomendadas:
1. Abrir refugios climatizados
2. SMS población vulnerable  
3. Refuerzo urgencias

[Ver en PRISMA]
```

**Ejemplo SMS población (si se aprueba):**
```
AVISO 112 NAVARRA: Calor extremo y mala 
calidad del aire. Evite exteriores 12h-20h.
Refugios climatizados: [enlace]. 
Hidratación. 112 si emergencia.
```

### Formato estándar WhatsApp → Medios (referencia operativa)

El 112 Navarra usa un formato estructurado para comunicar a periodistas locales:

```
[TIPO]/[Subtipo]
[Hora] [UBICACIÓN] (Municipio), [Dirección]

MEDIOS MOVILIZADOS
- [Lista recursos: Bomberos X, Policía Foral, Ambulancia SVA x2...]

[TRASLADO al HUN / SIN TRASLADO]
[Estado víctimas/afectados]

DETALLES
[Narrativa del incidente en 2-4 líneas]
```

**Tipos comunes:** INCENDIO/urbano, ACCIDENTE/Vial/Con heridos, ASISTENCIA TÉCNICA/Fuga de gas, AMPLIACIÓN [seguimiento]

**Recursos típicos:** Bomberos (Cordovilla, Trinitarios, Oronoz...), Policía Foral, Policía Local, Ambulancia SVA/SVB, Equipo Médico, Técnicos especializados

**Implicación para PRISMA:** Este formato es 100% estructurado → PRISMA puede generar borradores automáticos mapeando desde entidades FIWARE. El responsable de comunicación solo valida y envía.

---

## 🧠 Base de Conocimiento del Agente

### Qué "sabe" sin RAG complejo

**Normativa Navarra:**
- Ley Foral 8/2005 de Protección Civil
- Plan Territorial de Emergencias (PLATENA)
- Plan Especial Incendios Forestales (PLANINFONA)
- Plan de Actuación ante Altas Temperaturas

**Protocolos:**
- Activación CECOPI (niveles 0, 1, 2, 3)
- Umbrales de alerta (temperatura, calidad aire)
- Capacidad hospitalaria (camas, UCI)
- Rutas de evacuación valles pirenaicos

**Embebido en:** Prompts del LLM + variables n8n (~2.000-3.000 tokens de contexto fijo)

> **Decisión:** No RAG para MVP. La knowledge base cabe en el system prompt. RAG añade latencia, complejidad y puntos de fallo. Guardar para v2 cuando haya documentación real de planes de emergencia que requiera búsqueda semántica.

---

## 🎯 Prompting del Agente (Corazón del Sistema)

### Las 3 tareas del LLM en cada respuesta

El agente debe hacer tres cosas en cada interacción:

| Tarea | Pregunta que responde | Output |
|-------|----------------------|--------|
| **1. Interpretar** | ¿Qué está pasando ahora? | Resumen situacional |
| **2. Predecir** | ¿Qué va a pasar si no actuamos? | Cascada de impactos + ventana temporal |
| **3. Recomendar** | ¿Qué debemos hacer? | Acciones priorizadas + responsable |

### Estructura del System Prompt

```
[CONTEXTO FIJO]
- Rol: Eres PRISMA, sistema de anticipación de emergencias
- Normativa Navarra (resumen)
- Umbrales de alerta
- Capacidades hospitalarias

[ESTADO ACTUAL - Inyectado dinámicamente]
- JSON con estado de todas las entidades FIWARE
- Fecha/hora simulada
- Predicciones anteriores (CascadePrediction)

[INSTRUCCIONES]
1. Analiza el estado actual
2. Identifica triggers activos
3. Predice cascada si no se actúa
4. Recomienda acciones priorizadas
5. Estima ventana temporal

[FORMATO DE RESPUESTA]
- Situación: [resumen en 2-3 líneas]
- Riesgo: [BAJO/MEDIO/ALTO/CRÍTICO]
- Predicción: [qué pasará en X horas]
- Acciones recomendadas:
  1. [Acción] - [Responsable] - [Urgencia]
  2. ...
```

### Ejemplo de razonamiento (few-shot)

Incluir 1-2 ejemplos de razonamiento completo en el prompt para guiar al LLM:

```
EJEMPLO:
Estado: Temp 42°C, PM2.5 180, Urgencias 85%, Incendio activo Valle Roncal
Fecha: 3 julio (vísperas San Fermín)

Razonamiento:
- Temperatura extrema + calidad aire degradada = doble estrés sanitario
- Urgencias al 85% = margen mínimo
- Incendio activo = humo seguirá llegando
- Vísperas San Fermín = 400k personas, presión política máxima

Predicción: En 4h urgencias superarán 100%. Sin intervención, habrá que decidir sobre San Fermín en 6h.

Acciones:
1. Abrir refugios climatizados - Ayuntamiento - URGENTE
2. SMS población: evitar exteriores - Comunicación - URGENTE
3. Refuerzo urgencias - Salud - ALTA
4. Preparar comunicado San Fermín - CECOPI - MEDIA
```

### Manejo de casos edge (en el prompt)

| Situación | Respuesta PRISMA |
|-----------|------------------|
| Pregunta fuera de ámbito ("¿Capital de Francia?") | "PRISMA está especializado en anticipación de emergencias. ¿Puedo ayudarte con la situación actual?" |
| Acción no catalogada ("Envía un helicóptero") | "Esa acción no está en mi catálogo actual. Puedo recomendar: [alternativas]. ¿Contacto con CECOPI para solicitud especial?" |
| Datos contradictorios (temp baja + urgencias subiendo) | "Detecto inconsistencia: [explicar]. Posibles causas: [hipótesis]. Recomiendo verificar fuente X." |
| Petición de justificación ("¿Por qué recomiendas eso?") | "Mi razonamiento: [mostrar cadena causal]. Basado en: [datos específicos]. Confianza: [%]." |

> **Tiempo de iteración:** Dedicar más tiempo a iterar el prompt que a la arquitectura de infraestructura. El prompt ES el producto.

---

## 🎬 ESTRUCTURA DEMO (7 minutos)

### ACTO 1: El Problema (1 minuto)

> "Europa, verano 2023. 47.000 muertos por olas de calor.
>
> El problema NO fue el calor. Fue que nadie conectó los puntos:
> - Temperatura subiendo
> - Urgencias llenándose
> - Residencias sin climatización
> - Información en silos separados
>
> Los planes de calor son **reactivos**. Cuando actúas, ya es tarde."

### ACTO 2: La Demo PRISMA (4 minutos)

**[Streamlit Chat + Selector de Fecha]**

1. Usuario selecciona: "1 de julio" (pre-San Fermín)
2. Click "Iniciar Escenario"
3. Eventos van apareciendo en el panel lateral
4. **EL MOMENTO WOW** - PRISMA dice algo así:

> "⚠️ Detectando correlación inusual: las llamadas al 112 por problemas respiratorios han aumentado un 40% en la última hora, pero la calidad del aire oficial aún muestra valores aceptables (PM2.5=85).
>
> **Inferencia:** La pluma de humo del incendio de Roncal está llegando a zonas no cubiertas por los sensores fijos (barrios norte de Pamplona).
>
> **Predicción:** En 2-3 horas los sensores oficiales confirmarán PM2.5 >150. Para entonces, urgencias estarán al 90%+.
>
> **Recomiendo:** Activar alerta preventiva AHORA en barrios norte, antes de confirmación oficial."

5. Usuario pregunta: "¿Por qué estás tan seguro?"
6. PRISMA explica su razonamiento (trazabilidad)
7. Usuario aprueba → Telegram de prueba enviado

> **Esto es predicción de cascada real:** No esperar a que el sensor oficial confirme, sino inferir de señales indirectas. Es lo que diferencia a PRISMA de un dashboard.

### ACTO 3: El Diferencial (1 minuto)

| Tradicional | PRISMA |
|-------------|--------|
| Datos en silos | Fusión multi-fuente |
| Reacción | Predicción |
| Humano interpreta | IA razona |
| "Alerta calor" genérica | "2h para colapso urgencias" |

### ACTO 4: Roadmap (1 minuto)

**MVP (ahora):** Demo funcional, 1 escenario  
**v1 (6 meses):** 3 escenarios, integración real Navarra  
**v2 (12 meses):** Multi-región, marketplace alertas

---

## 🏗️ Arquitectura Técnica MVP

### Decisión: Streamlit + CSVs + Runner + n8n (agente)

```
┌──────────────────────────────────────────────────────────┐
│                      STREAMLIT                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │
│  │ Config      │  │   Chat      │  │ Razonamiento    │   │
│  │ Escenario   │  │   PRISMA    │  │ (trazabilidad)  │   │
│  └─────────────┘  └─────────────┘  └─────────────────┘   │
│         │                 │                               │
│         ▼                 ▼                               │
│  ┌─────────────┐    ┌─────────────────────────────────┐  │
│  │ CSV         │    │         n8n (agente)            │  │
│  │ timeline_*  │    │   LLM + Knowledge Base          │  │
│  │ + Runner    │    │   + Cascadas few-shot           │  │
│  └──────┬──────┘    └───────────────┬─────────────────┘  │
└─────────┼───────────────────────────┼────────────────────┘
          │                           │
          ▼                           ▼
┌──────────────────────────────────────────────────────────┐
│                 FIWARE Context Broker                     │
│  WeatherObserved | AirQuality | ForestFire | Calls112    │
│  HospitalOccupancy | SocialMediaAlert                    │
└──────────────────────────────────────────────────────────┘
```

**Datos sintéticos:** CSVs pre-scripted con nomenclatura `{EntityType}_{attribute}`. Runner lee CSV y envía secuencialmente a FIWARE con velocidad configurable (6x = 30 min demo simulan 3h reales).

---

## 🔄 Flujo de Información

### FASE 1: Iniciar escenario
1. Usuario selecciona fecha (15 Jun / 6 Jul / 1 Ago)
2. Click "Iniciar" → Script Python carga contexto + inicia streams
3. Script inyecta datos a FIWARE vía MCP con delays

### FASE 2: Consultar
1. Usuario pregunta en chat
2. Streamlit → n8n (agente) con contexto + datos actuales
3. LLM razona con Knowledge Base + Cascadas few-shot
4. Respuesta con predicción y recomendaciones

### FASE 3: Aprobar/Rechazar
1. Usuario aprueba → n8n ejecuta (Telegram real, SMS simulado)
2. Usuario rechaza → queda registrado (trazabilidad)

**Trazabilidad (lección DANA):** Todo queda registrado. Quién decidió qué, cuándo, con qué información.

---

## 🎯 Componentes a Construir

### Estado actual (en código)

| Componente | Estado | Archivo |
|------------|--------|---------|
| UI Streamlit | ✅ Layout + tabs | `streamlit/app.py` |
| Contexto escenarios | ✅ 3 fechas | `streamlit/config/scenarios.py` |
| Streams/entidades | ✅ 6 entidades FIWARE | `streamlit/config/scenarios.py` |
| Knowledge Base | ✅ Definido | `streamlit/config/knowledge_base.py` |
| Cascadas few-shot | ✅ Definido | `streamlit/config/knowledge_base.py` |
| **CSVs timeline** | ✅ 3 escenarios | `streamlit/data/timeline_*.csv` |
| **Runner FIWARE** | ✅ Inyección secuencial | `streamlit/scenario_runner.py` |
| Conexión n8n agente | ⏳ Pendiente | Webhook definido en .env |

### CSVs de datos sintéticos

Nomenclatura: `{EntityType}_{attribute}` compatible con Smart Data Models.

```
streamlit/data/
├── timeline_15_junio.csv   # Viento puede girar S → mejora
├── timeline_6_julio.csv    # Sin esperanza, decidir YA
└── timeline_1_agosto.csv   # Lluvia en 6h → aguantar
```

**Uso runner:**
```bash
python streamlit/scenario_runner.py 6_julio --speed 6
```

### Curva narrativa (20 min demo = 3h simuladas)

| Demo | Sim | Evento clave |
|------|-----|--------------|
| 0:00 | 09:00 | Estado base, incendio activo al N, viento S |
| 0:04 | 09:24 | Viento gira N → humo empieza a bajar |
| 0:08 | 09:48 | PM2.5 130, urgencias 78% |
| 0:12 | 10:12 | PM2.5 195, Twitter "alarm" |
| 0:16 | 10:36 | PM2.5 245, urgencias 96% |
| 0:20 | 11:00 | **PUNTO DECISIÓN** 🎯 |

### n8n Agente (PRISMA_2_Situational_Intelligence)
- Recibe: contexto + datos actuales + pregunta
- LLM con: Knowledge Base + Cascadas few-shot
- Devuelve: respuesta + razonamiento + acciones recomendadas

### Prompting activo (importante)

El prompt del agente debe incluir **preguntas que fuercen análisis situacional**:

```
Dado el estado actual de los datos, responde:
1. ¿Hay alguna combinación de factores que por separado no alarman pero juntos sí?
2. ¿Algún cambio reciente (viento, temperatura) altera el riesgo de datos anteriores?
3. ¿Qué pasará en 1-2h si la tendencia continúa?
4. ¿Hay ventana de acción que se esté cerrando?
```

**Por qué:** Sin estas preguntas, el LLM puede limitarse a describir datos. Con ellas, forzamos **razonamiento predictivo** sobre cascadas.

---

## ⚡ Plan de Ejecución (Semana 12-19 dic)

| Día | Foco | Entregable |
|-----|------|------------|
| **Jue 12** | UI layout + config escenarios | ✅ Hecho |
| **Vie 13** | CSVs timeline + Runner | ✅ Hecho |
| **Sáb 14** | Conexión chat → n8n agente | Flujo completo |
| **Dom 15** | Pulir agente + respuestas | Calidad LLM |
| **Lun 16** | Mapa + visualización | Contexto geográfico |
| **Mar 17** | Ensayo demo completa | End-to-end |
| **Mié 18** | Buffer + Plan B | Video backup |
| **Jue 19** | **PITCH** | 🎤 |

---

## ⚠️ El antipatrón: DANA Valencia (octubre 2024)

**Lo que pasó:**
- Información fragmentada
- Decisiones políticas retrasadas
- Comunicación confusa a ciudadanía
- Resultado: tragedia evitable

**Lo que PRISMA habría cambiado:**
- ✅ Fusión de datos en tiempo real
- ✅ Predicción de cascada clara
- ✅ Recomendaciones priorizadas al CECOPI
- ✅ Trazabilidad de decisiones

---

## 💰 ROI Específico del Caso de Uso

**Coste de NO actuar (ola calor + incendio en San Fermín):**
- 💀 Vidas: Incalculable
- 📺 Crisis reputacional internacional
- 🎪 Cancelación San Fermín: 100M€+ impacto económico
- ⚖️ Responsabilidades políticas

**Coste de PRISMA:**
- SaaS mensual << 1% del impacto evitado

---

## 🆚 Análisis Competitivo: Everbridge

> **Expandir en v2.** Resumen clave abajo.

**Everbridge** = líder mundial CEM (NASDAQ: EVBG, +6.500 clientes). Valida modelo B2G+B2B.

**Diferencial PRISMA:**
- Everbridge: "Know Earlier" (notifica) → PRISMA: "Predict Cascades" (predice)
- Everbridge: reglas IF-THEN → PRISMA: razonamiento IA few-shot
- Everbridge: 🇺🇸 USA, CLOUD Act → PRISMA: 🇪🇺 100% europeo, FIWARE, Data Spaces

**Regulación favorable:** NIS2, CER, AI Act, DORA → compliance by design.

**ROI:** Cancelación San Fermín evitada = 100M€+. Coste PRISMA << 1%.

---

## 🎯 Target del MVP

### Cliente Primario (Piloto)
- **Gobierno de Navarra** (Protección Civil, SOS Navarra 112)
- **Ayuntamiento de Pamplona** (Seguridad)

### Socio Tecnológico Clave
- **Tracasa Instrumental** → Ya desarrollaron el Módulo de Grandes Emergencias
  - Conocen la operativa del 112
  - Integración natural con sistemas existentes
  - PRISMA como módulo de inteligencia adicional

---

## 💰 Modelo de Negocio: B2G + B2B

> **Expandir en v2.** Resumen clave abajo.

**B2G** (piloto/credibilidad): 112 Navarra, Ayuntamientos, Protección Civil  
**B2B** (escalabilidad): Utilities, seguros, eventos, industria, logística

**Target especial:** Empresas de gemelos digitales (Tracasa, iris360) → PRISMA como módulo de inteligencia.

**Data Spaces:** Monetización futura vía marketplace europeo de alertas.

| Fase | Cliente | Valor |
|------|---------|-------|
| MVP | 112 Navarra | Piloto, credibilidad |
| v1 | Utilities Navarra | Primeros ingresos B2B |
| v2 | Data Space multi-sector | Escalabilidad |

---

## 🌍 Valor Expandido

- Tesicnor/RRD como integrador industrial (ya venden al sector privado)
- Modelo replicable a otras CCAA (el 112 existe en todas)
- Potencial de estandarización nacional/europea

---

## 🔗 Data Space Ready

> **Expandir en v2.**

PRISMA = FIWARE-native desde día 1: NGSI-v2/LD, Smart Data Models, Context Broker, MCP FIWARE (activo propio operativo).

Preparado para: GAIA-X, IDSA, Data Spaces sectoriales.

**Mensaje inversores:** PRISMA = nodo en ecosistema europeo de datos.

---

## 📋 Decisiones Tomadas

| Decisión | Resultado |
|----------|-----------|
| LLM | GPT-4o (Mistral v2) |
| Datos | Sintéticos via FIWARE MCP |
| Escenarios | 3 fechas (15 Jun, 6 Jul, 1 Ago) |
| n8n-1 | ❌ Eliminado → script directo |
| Caso cyber | Aplazado a v2 |

### Pendiente
- [ ] Mapa: ¿mostrar o solo chat?
- [ ] Narrativa pitch: ¿DANA o calor 2023 primero?

### Plan B (si algo falla)
- Video pregrabado
- Modo offline con datos hardcodeados
- Script de respuestas manual

---

## 💡 Principios de Trabajo

1. **No overengineer** → MVP funcional > feature completo
2. **Datos sintéticos OK** → Lo importante es demostrar el concepto
3. **Human-in-the-loop** → PRISMA sugiere, humano decide
4. **Trazabilidad** → Todo queda registrado

### Principio arquitectónico: Inteligencia Situacional vs Dominio

| Capa | Qué es | Cambia por evento? |
|------|--------|-------------------|
| **Inteligencia Situacional** | Motor de razonamiento: interpreta, predice, recomienda | **NO** (agnóstico) |
| **Dominio** | Conocimiento específico: entidades, umbrales, protocolos, acciones | **SÍ** (inyectado) |

**La promesa de valor:** PRISMA no sigue flujos prediseñados por tipo de evento. El mismo motor de inteligencia situacional interpreta cualquier escenario si se le inyecta el dominio correcto.

**Inteligencia Situacional (fija):**
- Interpretar estado actual
- Detectar anomalías y correlaciones
- Predecir cascada de impactos
- Priorizar acciones
- Justificar razonamiento

**Dominio (inyectado según escenario):**
- Entidades FIWARE relevantes
- Umbrales de alerta específicos
- Protocolos aplicables (CECOPI, NIS2...)
- Catálogo de acciones disponibles
- Stakeholders y roles

**Implicación para MVP:** El prompt base es genérico. Lo que cambia entre escenarios es el conocimiento de dominio inyectado en el contexto.

---

## 🎤 Meta-Argumento del Pitch

> **"Donde otros necesitan 18 meses y 2M€, nosotros entregamos en 6 meses con 250k€."**

**Ventaja:** Low-code (n8n, Streamlit) + AI-assisted dev (Cursor) + Estándares abiertos (FIWARE, MCP).

**Activos operativos:** MCP FIWARE ✅ | Sandbox FIWARE ✅ | Conocimiento dominio ✅

---

## 📍 Estado del Proyecto

**Fecha:** Diciembre 2025  
**Objetivo:** Elevator Pitch TwIN Lab (19 dic 2025)  
**Próximo hito:** Demo funcional con escenario Ola Calor + Incendio

### El ask post-pitch (qué pedir si va bien)

| Ask | Para qué |
|-----|----------|
| Intro a **Tracasa** | Explorar integración con gemelo Pamplona |
| Contacto **Gobierno Navarra** | Proyecto I+D conjunto |
| Acceso a **datos reales** | Piloto con datos históricos 112 |
| **Mentoría técnica** | IA/ML, escalabilidad |
| Intro a **inversores seed** | Siguiente fase de financiación |

> **Importante:** El pitch sin ask concreto es solo una presentación. Tener claro qué pedir.

