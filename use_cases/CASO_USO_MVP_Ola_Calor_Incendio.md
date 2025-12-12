# CASO DE USO MVP: Ola de Calor + Incendio Forestal Pirineos

**Inspirado en:** Everbridge Critical Event Management  
**Diferencial PRISMA:** No solo notificamos crisis, **prevenimos cascadas sistémicas**  
**Fecha objetivo demo:** 19 diciembre 2025 (Elevator Pitch TwIN Lab)

> 📋 **Estrategia dual:** Este caso se presenta junto con [Ciberataque Infraestructura Agua](./CASO_USO_MVP_Ciberataque_Depuradora.md) para demostrar que **el mismo motor de inteligencia situacional** funciona en dominios completamente diferentes (ambiental vs cyber).

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

| Fecha | Contexto | Población | Riesgo principal |
|-------|----------|-----------|------------------|
| **15 Junio** | Fin curso escolar, apertura piscinas municipales | 350k | Niños/jóvenes expuestos, familias en exteriores, inicio temporada calor |
| **1 Julio** | Pre-San Fermín, turistas llegando | 600k+ | **Máxima tensión política**: ¿se cancela San Fermín? Crisis reputacional internacional |
| **1 Agosto** | Ciudad semi-vacía, pico de calor | 250k | Personal sanitario reducido, incendio de 5ª generación (más rápido, más intenso), menos recursos disponibles |

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

### Decisión: Chat Conversacional + FIWARE Event-Driven

Streamlit (UI) + n8n (orquestación + IA) + FIWARE (Context Broker)

### Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                      STREAMLIT                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Scenario    │  │   Chat      │  │  Panel Estado       │  │
│  │ Context     │  │   PRISMA    │  │  (KPIs tiempo real) │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │                 ▲                    ▲
         ▼                 ▼                    │
┌─────────────────────────────────────────────────────────────┐
│        n8n-1                          n8n-2                 │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │ Generador       │    │ Agente Conversacional           │ │
│  │ Escenarios      │    │ (LLM + Knowledge Base)          │ │
│  │ (con selector   │    │                                 │ │
│  │ fecha)          │    │                                 │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
│           │                          │                      │
│           ▼                          ▼                      │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Alertas: SMS masivo | SMS VIP | Twitter | Telegram      ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
         │                              ▲
         ▼                              │ (Suscripciones)
┌─────────────────────────────────────────────────────────────┐
│                    FIWARE Context Broker                    │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐  │
│  │ Weather    │ │ AirQuality │ │ Emergency  │ │ Ocupancy │  │
│  │ Observed   │ │ Observed   │ │ Calls112   │ │ Urgencia │  │
│  └────────────┘ └────────────┘ └────────────┘ └──────────┘  │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐               │
│  │ Forest     │ │ Twitter    │ │  Weather   │               │
│  │ Fire (Has) │ │ Mentions   │ │  Forecast  │               │
│  └────────────┘ └────────────┘ └────────────┘               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flujo de Información

### FASE 1: Usuario selecciona fecha e inicia

1. Usuario elige fecha en selector (ej: "3 julio")
2. Click "Iniciar Escenario"
3. Streamlit → Webhook n8n (Generador Escenarios)
4. n8n calcula parámetros según fecha:
   - Población (350k vs 1M)
   - Capacidad hospitalaria
   - Contexto político
5. n8n actualiza entidades FIWARE con datos iniciales
6. FIWARE notifica a n8n (suscripción)
7. Eventos empiezan a "suceder" con delays

### FASE 2: Usuario consulta

1. Usuario pregunta en chat: "¿Cuál es la situación?"
2. Streamlit → Webhook n8n (Agente)
3. n8n consulta FIWARE (estado actual)
4. LLM genera respuesta contextualizada
5. Respuesta incluye predicción y recomendaciones

### FASE 3: Aprobar y ejecutar

1. Usuario: "Envía alerta a población"
2. n8n valida intención
3. n8n ejecuta: SMS masivo (simulado) + Telegram (real)
4. Confirmación al usuario

### FASE 4: Flujo de rechazo (Human-in-the-Loop)

**Qué pasa cuando el operador dice "NO" a una recomendación:**

| Situación | Acción PRISMA | Registro |
|-----------|---------------|----------|
| Rechazo simple | Registra, sigue monitorizando | "Operador X rechazó Y a HH:MM" |
| Sin alternativa dada | Ofrece opciones: "¿Prefieres A, B, o ninguna?" | Opciones ofrecidas |
| Situación crítica | Pide confirmación + motivo | "¿Confirmas? Motivo: ___" |
| Situación empeora tras rechazo | Re-propone con datos actualizados | "Situación empeoró. ¿Reconsideras?" |
| Múltiples rechazos críticos | Escala a nivel superior (si configurado) | Notifica a responsable jerárquico |

**Trazabilidad obligatoria:**

Cada rechazo queda registrado en entidad `OperatorDecision`:
- `recommendation_id`: qué se recomendó
- `action`: acción propuesta
- `status`: APPROVED / REJECTED / DEFERRED
- `decided_by`: quién decidió
- `decided_at`: cuándo
- `reason`: motivo del rechazo (texto libre)
- `situation_snapshot`: estado FIWARE en ese momento
- `follow_up`: si se re-propuso después

**Por qué importa (lección DANA Valencia):**

> En DANA Valencia, nadie sabe exactamente quién decidió qué, cuándo, y con qué información disponible.
>
> PRISMA garantiza **trazabilidad total**: si el operador rechaza, queda registrado con contexto completo. No para culpar, sino para aprender y para que las decisiones sean **auditables**.

**Para MVP:** Registrar rechazos es suficiente. Escalado automático es v2.

---

## 🎯 Componentes a Construir

### 1. FIWARE (Entidades)

**Datos de entrada:**
- `WeatherObserved` (temperatura, humedad, viento)
- `AirQualityObserved` (PM2.5, PM10, O3)
- `ForestFire` (ubicación, estado, propagación)
- `EmergencyCalls112` (contador, categorías)
- `HospitalCapacity` (ocupación urgencias, UCI)
- `TwitterMentions` (contador, sentiment)
- `ScenarioContext` (fecha, población, fase)

**Salida del agente (trazabilidad):**
- `CascadePrediction` → Lo que PRISMA predice en cada análisis:
  - `timestamp`: cuándo se hizo la predicción
  - `trigger`: qué evento lo activó
  - `prediction`: qué va a pasar si no actuamos
  - `confidence`: nivel de certeza
  - `recommended_actions[]`: acciones priorizadas
  - `window_hours`: tiempo disponible para actuar

> **Por qué:** Trazabilidad de las predicciones del sistema, no solo de los datos de entrada. Útil para post-mortem y para mostrar el "razonamiento" de PRISMA.

### 2. n8n Workflows

**Workflow A: Generador de Escenarios**
- Recibe fecha seleccionada
- Calcula parámetros según fecha
- Actualiza FIWARE con delays (simula tiempo real)
- **Modo Demo:** Toggle para acelerar delays (minutos simulados → segundos reales)
- **Reset:** Endpoint para limpiar FIWARE y volver a estado inicial

**Curva narrativa scripted (ejemplo 1 Julio - San Fermín):**

```
T+0min:  Estado inicial (35°C, PM2.5=50, urgencias 60%)
T+2min:  AEMET actualiza pronóstico → 42°C mañana
T+4min:  EFFIS detecta incendio Valle Roncal
T+6min:  Primeras quejas Twitter (+20 menciones)
T+8min:  PM2.5 empieza a subir (50→80)
T+10min: Urgencias suben (60%→70%)
T+12min: PM2.5 crítico (80→150)
T+14min: 112 reporta +40% llamadas respiratorias
T+16min: Urgencias al límite (85%)
T+18min: PUNTO DE DECISIÓN: ¿Alerta? ¿San Fermín?
```

> **Importante:** Sin secuencia scripted, la demo puede ser aburrida o caótica. Cada escenario necesita su guion con tiempos exactos.

**Workflow B: Agente Conversacional**
- Recibe pregunta usuario
- Consulta FIWARE
- LLM genera respuesta + recomendaciones
- Ejecuta acciones aprobadas

### 3. Streamlit UI

- **Selector de escenario** (3 botones: 15 Junio / 1 Julio / 1 Agosto)
- Botón "Iniciar Escenario"
- **Toggle "Modo Demo"** (acelera simulación para pitch)
- **Botón "Reset"** (limpia FIWARE, vuelve a estado inicial)
- Chat conversacional (con streaming para evitar esperas)
- Panel lateral con KPIs (jerarquía visual)
- Indicador de fecha/contexto activo
- **Spinner con mensaje** mientras LLM procesa ("PRISMA analizando 7 fuentes...")

**Jerarquía visual de KPIs:**

| Nivel | KPIs | Tamaño/Color |
|-------|------|--------------|
| **1 (críticos)** | Temperatura, Calidad aire (🟢🟡🔴), Ocupación urgencias % | Grande, siempre visible |
| **2 (secundarios)** | Llamadas 112 (Δ vs normal), Estado incendio, Menciones Twitter | Medio |
| **3 (contexto)** | Fecha simulada, Población estimada, Fase CECOPI | Pequeño, gris |

### 4. Knowledge Base

- Normativa Navarra (texto en prompt)
- Umbrales de alerta (variables n8n)
- Protocolos CECOPI (texto en prompt)

---

## ⚡ Plan de Ejecución (1 Semana)

### Lunes: FIWARE + Entidades Base
- Crear entidades en Context Broker
- Configurar suscripciones
- Probar flujo básico

### Martes: Generador de Escenarios
- Workflow n8n con selector fecha
- Lógica de parámetros por fecha
- Delays para simular tiempo real

### Miércoles: Agente Conversacional
- Workflow n8n con LLM
- Integrar consulta FIWARE
- Knowledge base en prompts

### Jueves: Streamlit + Alertas
- UI con selector fecha y chat
- Conexión webhooks n8n
- Telegram de prueba

### Viernes: Pulir y Ensayar
- Demo completa end-to-end
- Preparar narrativa pitch
- Backup por si algo falla

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

### Qué es Everbridge

**El líder mundial en Critical Event Management (CEM)**
- NASDAQ: EVBG
- +6.500 clientes globales
- Clientes: Goldman Sachs, Siemens, Johnson Controls, **112** (algún país EU), State of Oregon
- Claim: "Know Earlier, Respond Faster, Improve Continuously"
- Nuevo: "High Velocity CEM" con "Purpose-built AI"

**Fuente:** [everbridge.com](https://www.everbridge.com/)

### Validación de nuestro modelo

**Everbridge vende B2G + B2B** → Nuestro modelo dual es correcto.

| Sus sectores B2B | ¿PRISMA? |
|------------------|----------|
| Energy & Utilities | ✅ |
| Insurance | ✅ |
| Healthcare/Hospitals | ✅ |
| Manufacturing | ✅ |
| Commercial Real Estate | ✅ |
| Transportation | ✅ |
| Financial Services | ⚠️ Futuro |
| Pharmaceutical | ⚠️ Futuro |

**El 112 es cliente de Everbridge** → Valida que nuestro target B2G es correcto.

### Diferencial de producto

| Aspecto | Everbridge | PRISMA |
|---------|------------|--------|
| **Claim** | "Know Earlier" | **"Predict Cascades"** |
| **Foco** | Notificación cuando pasa | **Predicción antes de que pase** |
| **IA** | Analytics post-evento | **Razonamiento sobre cascadas** |
| **Lógica** | Reglas IF-THEN | IA con ejemplos (few-shot) |
| **Datos** | Los que configures | **Fusión multi-fuente automática** |
| **Salida** | "Alerta: ola de calor" | **"2h para colapso urgencias, haz X"** |

### Diferencial estratégico: Soberanía Tecnológica

| Aspecto | Everbridge | PRISMA |
|---------|------------|--------|
| **Origen** | 🇺🇸 USA (NASDAQ: EVBG) | 🇪🇺 **100% europeo** |
| **Datos** | Servidores US, CLOUD Act | **Soberanía total** |
| **Estándares** | Propietarios, lock-in | **FIWARE** (open source) |
| **Interoperabilidad** | Cerrada | **Data Spaces** (GAIA-X) |
| **Licencia** | Comercial | **EUPL** |
| **Compliance** | Adaptación posterior | **Nativo NIS2, CER, AI Act, DORA** |

### El argumento geopolítico (para el pitch)

> "Musk quiere romper la UE. Putin quiere una UE débil. China quiere dividir la UE. Trump quiere una UE de extrema derecha.
>
> **La infraestructura crítica de Europa no puede depender de Big Tech americana.**
>
> PRISMA es **Powered by FIWARE**, tecnología europea, open source, preparado para Data Spaces. Soberanía tecnológica desde el día 1."

### Contexto regulatorio favorable

| Regulación | Fecha | Afecta a | Oportunidad |
|------------|-------|----------|-------------|
| **NIS2** | Oct 2024 | Infraestructuras críticas | Utilities, energía, agua |
| **CER** | Oct 2024 | Entidades críticas | Mismo target |
| **AI Act** | Ago 2024 | IA en emergencias = alto riesgo | Compliance by design |
| **DORA** | Ene 2025 | Sector financiero | Bancos, aseguradoras, fondos |

**DORA (Digital Operational Resilience Act):** Nueva oportunidad que Everbridge ya vende. Aplica a todo el sector financiero europeo. PRISMA podría expandir aquí post-MVP.

### ROI: Cómo lo vende Everbridge

Everbridge cita Forrester: **358% ROI**, $8.5M en 3 años:
- $3M efficiency gains
- $2M reduced IT downtime
- $1.5M security team productivity

**Para PRISMA (caso Ola Calor + San Fermín):**
- Cancelación San Fermín evitada: **100M€+**
- Vidas salvadas: **incalculable**
- Crisis reputacional evitada: **decenas de M€**
- Coste PRISMA: **<<1% del impacto evitado**

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

### Por qué no solo B2G

| Aspecto | B2G (Gobierno) | B2B (Privado) |
|---------|----------------|---------------|
| Ciclo de venta | 6-18 meses (licitaciones) | 1-3 meses |
| Dependencia | Presupuestos públicos, política | Decisión empresarial |
| Escalabilidad | Limitada (una CCAA cada vez) | Alta (muchas empresas) |
| **Atractivo inversor** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

> **Para inversores:** B2G es el piloto que da credibilidad. B2B es donde está la escalabilidad y el retorno.

### El mercado B2B: Quién paga por inteligencia de riesgos

**Empresas con activos, operaciones o personal expuestos a cascadas:**

| Sector | Dolor específico | Qué compran hoy |
|--------|------------------|-----------------|
| **Utilities (agua, energía)** | Infraestructura expuesta, obligación NIS2 | Alertas rayos, SCADA monitoring |
| **Energía renovable** | Parques eólicos/solares | Heat stress, tormentas, irradiancia |
| **Seguros** | Pricing de riesgo, gestión claims | Modelos climáticos, early warning |
| **Inmobiliarias/Construcción** | Activos expuestos, obras paradas | Alertas inundación, viento |
| **Eventos/Turismo** | Decisiones cancelación, seguridad | Meteo + riesgos combinados |
| **Logística/Transporte** | Rutas afectadas, flotas | Alertas carreteras, puertos |
| **Agricultura** | Cosechas, riego, heladas | Agro-meteo, plagas |
| **Industria** | Continuidad operaciones | Heat stress laboral, calidad aire |

### Referencia: Empresas DRR/Early Warning que ya venden B2B

Empresas que ya monetizan inteligencia de riesgos al sector privado:

- **Tomorrow.io** / **Climavision** → Alertas meteo hiperlocales
- **DTN** → Riesgos para energía, agricultura, transporte
- **One Concern** → Resiliencia para seguros e inmobiliarias
- **Previsico** → Alertas inundación para utilities
- **Tesicnor/RRD** (Navarra) → Heat stress, riesgos industriales

### Target B2B especial: Empresas de Gemelos Digitales

**Insight clave:** Empresas que desarrollan gemelos digitales tienen datos y visualización, pero les falta inteligencia predictiva. PRISMA puede ser el **módulo de inteligencia** que integran en sus soluciones.

| Empresa | Qué tienen | Qué les falta | PRISMA aporta |
|---------|------------|---------------|---------------|
| **Tracasa** | Gemelo urbano Pamplona | Solo visualización | Predicción cascadas |
| **iris360** | Plataforma IoT + gemelo 3D | Dashboards reactivos | Razonamiento IA |
| **Integradores Smart City** | Datos + capas GIS | Inteligencia situacional | El cerebro |
| **Consultoras digitales** | Proyectos gemelos para clientes | Diferenciación | IA como servicio |

**Modelo:** PRISMA como módulo/API que se integra en gemelos de terceros → escalabilidad sin fuerza de ventas masiva.

### Modelo dual: B2G como ancla, B2B como escala

```
┌─────────────────────────────────────────────────────────────────┐
│                         PRISMA                                   │
│              (Inteligencia de riesgos en cascada)               │
└─────────────────────────────────────────────────────────────────┘
                    │                           │
         ┌──────────┴──────────┐     ┌─────────┴──────────┐
         ▼                      ▼     ▼                    ▼
┌─────────────────┐    ┌─────────────────────────────────────────┐
│     B2G         │    │                B2B                       │
│  (Ancla/Piloto) │    │           (Escalabilidad)                │
├─────────────────┤    ├─────────────────────────────────────────┤
│ • 112 Navarra   │    │ • Utilities (agua, energía)             │
│ • Ayuntamientos │    │ • Seguros (pricing, claims)             │
│ • Protección    │    │ • Inmobiliarias (activos)               │
│   Civil         │    │ • Eventos (San Fermín, festivales)      │
│                 │    │ • Industria (heat stress, continuidad)  │
│ Valor: piloto,  │    │ • Logística (rutas, flotas)             │
│ credibilidad,   │    │                                         │
│ caso de uso     │    │ Valor: escalabilidad, recurrencia,      │
│                 │    │ ciclos cortos, atractivo inversor       │
└─────────────────┘    └─────────────────────────────────────────┘
```

### Data Spaces como canal de monetización B2B

```
PRISMA (productor de inteligencia)
        │
        ▼
Data Space (marketplace europeo)
        │
        ├── Suscripción "Alertas zona industrial Pamplona"
        ├── Suscripción "Riesgos eventos masivos Navarra"  
        ├── Suscripción "Heat stress laboral tiempo real"
        ├── API "Predicción cascada por coordenadas"
        │
        ▼
Consumidores B2B pagan por alertas relevantes
```

**Ventaja Data Spaces:** No vendes a cada empresa individualmente → publicas en el marketplace y las empresas se suscriben. Escalabilidad sin fuerza de ventas masiva.

### Resumen para inversores

| Fase | Canal | Cliente | Valor |
|------|-------|---------|-------|
| **MVP** | Directo | 112 Navarra | Piloto, credibilidad, caso de uso |
| **v1** | Directo | Utilities Navarra | Primeros ingresos B2B |
| **v2** | Data Space | Multi-sector | Escalabilidad, recurrencia |
| **v3** | Multi-región | España + UE | Expansión geográfica |

---

## 🌍 Valor Expandido

- Tesicnor/RRD como integrador industrial (ya venden al sector privado)
- Modelo replicable a otras CCAA (el 112 existe en todas)
- Potencial de estandarización nacional/europea

---

## 🔗 Data Space Ready

### PRISMA: FIWARE-native desde día 1

- **Powered by FIWARE** → Certificación objetivo Q4 2026
- **NGSI-v2/NGSI-LD** → Interoperabilidad nativa con cualquier sistema FIWARE
- **Smart Data Models** → Entidades estandarizadas (WeatherObserved, AirQualityObserved, Alert...)
- **Context Broker** → Orion-LD como fuente de verdad
- **MCP FIWARE** → Model Context Protocol desarrollado para integrar LLMs con FIWARE (activo propio, ya operativo)

### Data Spaces: El futuro de los datos en Europa

PRISMA está preparado para conectar con:
- **GAIA-X** → Infraestructura de datos federada europea
- **IDSA** → International Data Spaces Association
- **Data Spaces sectoriales** → Energía, Movilidad, Salud, Smart Cities

### Modelo de negocio futuro (post-MVP)

```
PRISMA genera alertas contextualizadas
        ↓
Data Space (marketplace de datos)
        ↓
Suscriptores pagan por alertas relevantes:
  • Empresas zona industrial
  • Organizadores eventos (San Fermín)
  • Sanidad privada
  • Aseguradoras
  • Medios de comunicación
```

> **Mensaje para inversores:** PRISMA no es solo un producto, es un **nodo en el ecosistema europeo de datos**. Preparado para el futuro de la interoperabilidad.

---

## 📋 Decisiones Pendientes

### Técnicas
- [x] ¿Qué LLM usar? → **GPT-4o** (Mistral en fase posterior)
- [ ] ¿SMS real o simulado para demo? → Simulado
- [x] ¿Integración real con AEMET o datos sintéticos? → **Sintéticos**, entidades FIWARE reales

### Demo
- [x] ¿Cuántos escenarios de fecha preparar? → **3** (15 Jun, 1 Jul, 1 Ago)
- [ ] ¿Mostrar mapa o solo chat?

### Narrativa
- [ ] ¿Empezar por DANA o por ola calor 2023?
- [ ] ¿Mencionar San Fermín explícitamente?

### Gestión de latencia LLM (riesgo en demo)
GPT-4o puede tardar 3-8 segundos. Mitigaciones:
- **Streaming**: `st.write_stream` para mostrar respuesta mientras se genera
- **Spinner con contexto**: "PRISMA analizando 7 fuentes de datos..."
- **Respuestas cacheadas**: Para preguntas frecuentes ("¿cuál es la situación?")

### Plan B para la demo (si algo falla el 19 dic)
- **Video pregrabado** de la demo funcionando
- **Modo offline**: Datos hardcodeados que no dependan de FIWARE en vivo
- **Script de respuestas**: Si LLM no responde, leer de guion preparado

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

## 🎤 El Meta-Argumento del Pitch

### La historia detrás de la demo

> "Esto que veis es el resultado de dos meses de trabajo con herramientas modernas: Cursor, LLMs, MCPs, n8n, FIWARE.
>
> **Esto demuestra la velocidad de iteración que permiten las herramientas de nueva generación.**
>
> Con un equipo de 3-4 personas, podríamos tener v1 en producción en 6 meses."

### Por qué esto importa

Las empresas de software tradicionales necesitan:
- Equipos de 10-20 personas
- 12-18 meses de desarrollo
- Millones en inversión inicial

PRISMA demuestra que con:
- **Low-code** (n8n, Streamlit)
- **AI-assisted development** (Cursor + LLMs)
- **Estándares abiertos** (FIWARE, MCP)
- **Infraestructura cloud moderna**

...un equipo pequeño puede iterar a velocidades antes imposibles.

### El mensaje para inversores

> "No estáis invirtiendo solo en un producto. Estáis invirtiendo en un equipo que domina las herramientas de nueva generación.
>
> Donde otros necesitan 18 meses y 2M€, nosotros entregamos en 6 meses con 250k€.
>
> **Esa es la ventaja competitiva real.**"

### Activos diferenciadores ya operativos

| Activo | Estado | Diferencial |
|--------|--------|-------------|
| **MCP FIWARE** | ✅ Operativo | Integración LLM ↔ Context Broker |
| **Sandbox FIWARE** | ✅ Operativo | Entidades, suscripciones |
| **n8n workflows** | 🔄 En desarrollo | Orquestación, agente |
| **Conocimiento dominio** | ✅ Sólido | 112 Navarra, emergencias, CECOPI |

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

