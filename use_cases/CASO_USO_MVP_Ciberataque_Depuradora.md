# CASO DE USO MVP: Ciberataque a Infraestructura del Agua

**Inspirado en:** Everbridge Critical Event Management  
**Diferencial PRISMA:** No solo notificamos crisis, **prevenimos cascadas sistémicas**  
**Fecha objetivo demo:** 19 diciembre 2025 (Elevator Pitch TwIN Lab)

> 📋 **Estrategia dual:** Este caso se presenta junto con [Ola de Calor + Incendio](./CASO_USO_MVP_Ola_Calor_Incendio.md) para demostrar que **el mismo motor de inteligencia situacional** funciona en dominios completamente diferentes (ambiental vs cyber).

---

## 🎯 Resumen Ejecutivo

### Por qué este caso de uso

**Ventajas estratégicas:**
- ✅ **NIS2 obligatorio 2024** → Utilities deben invertir (mercado cautivo)
- ✅ **Cascada no-obvia** → Agua → Hospitales → Colegios → Economía
- ✅ **Referencia conocida** → Colonial Pipeline (mayo 2021, USD 4.4M rescate)
- ✅ **No climático** → Foco en coordinación multi-actor, no en meteorología
- ✅ **Diferencial claro** → Everbridge notifica, PRISMA predice cascada
- ✅ **Fusión multi-fuente heterogénea** → Demuestra el verdadero valor de PRISMA:
  - 🌡️ **Datos ambientales** (temperatura, calidad aire) → Contexto estacional
  - 📞 **112 transcrito** (llamadas masivas "no sale agua", "agua sucia")
  - 🐦 **RRSS** (Twitter/X hashtags #AguaPamplona, #SinAgua)
  - 🏭 **SCADA industrial** (telemetría depuradora)
  - 🗺️ **Geoespacial** (IDENA: hospitales, colegios, población)
  - 📊 **Datos abiertos** (consumo histórico, eventos programados)

### Mensaje clave

> **"No gestionamos eventos. Prevenimos cascadas."**
> 
> - Detectamos el trigger (ciberataque)
> - Predecimos la cascada (qué fallará después)
> - Coordinamos la respuesta (quién hace qué, cuándo)

---

## 📋 Ficha Técnica del Escenario

### Infraestructura del Agua de Pamplona

**Agua potable (entrada):**
- **ETAP Urtasun** ← Embalse de Eugui
- **ETAP Egillor** ← Manantial de Arteta  
- **ETAP Tiebas** ← Embalse de Itoiz
- Suministran agua potable a 250.000 habitantes

**Aguas residuales (salida):**
- **EDAR Arazuri** → Depura antes de verter al río Arga
- 95% aguas residuales Comarca Pamplona
- 1.753 km de colectores

**Sistemas SCADA vulnerables:**
- Control bombeo, cloración, filtros
- Telemetría presión red distribución
- Compuertas embalses

### Escenario: Ataque coordinado ransomware a red hídrica

**Contexto temporal crítico:**
- 📅 **3 de julio 2026** (3 días antes de San Fermín)
- 🎉 **San Fermín:** 6-14 julio, +1 millón visitantes esperados
- 🌡️ **Temperatura:** 35°C, principio ola calor
- 👥 **Población:** De 250k a 700k+ (turistas llegando)
- 🏃 **Preparativos:** Encierros, conciertos, seguridad reforzada

**Vector de ataque:**
- Ransomware entra por proveedor de mantenimiento SCADA (supply chain)
- Se propaga a toda la red hídrica de Mancomunidad de la Comarca de Pamplona
- Afecta sistemas de control de ETAPs, EDAR y red de distribución

**Impacto cascada múltiple:**

| Infraestructura | Impacto inmediato | Cascada |
|-----------------|-------------------|---------|
| **ETAPs** (Urtasun, Egillor, Tiebas) | Potabilización detenida | Sin agua potable para 700k personas |
| **EDAR Arazuri** | Depuración detenida | Vertido sin tratar al río Arga |
| **Red distribución** | Bombeo paralizado | Presión cae, grifos secos en horas |

**Consecuencias si no se detecta a tiempo:**
- 🚫 **Cancelación San Fermín** (pérdidas 100M€+)
- 📺 **Crisis reputacional internacional** (CNN, BBC ya en Pamplona)
- 🏥 **Colapso sanitario** (calor 35°C + 700k personas + sin agua)
- 💀 **Riesgo vidas** (golpes calor, deshidratación masiva)
- 🌊 **Desastre medioambiental** (vertido sin tratar al Arga)
- ⚖️ **Multas UE** (incumplimiento directiva aguas residuales)

### Dependencias críticas

**Agua potable (ETAPs):**
- 🏥 **3 hospitales** (quirófanos, UCI, diálisis) + servicios emergencia San Fermín
- 🏨 **Hoteles** (capacidad x3 por fiestas, turistas internacionales)
- 🍺 **Hostelería** (bares, restaurantes, peñas - corazón de la fiesta)
- 👴 **12 residencias mayores** (población vulnerable + calor)
- 🎪 **Infraestructura fiestas** (escenarios, carpas, fuentes públicas)

**Aguas residuales (EDAR):**
- 🌊 **Río Arga** (ecosistema, pesca, regadío)
- 🏘️ **Poblaciones aguas abajo** (Huarte, Villava, Burlada ya pasadas; Zizur, Barañáin aguas arriba)
- 🌾 **Agricultura** (regadío Ribera del Arga)
- ⚖️ **Normativa UE** (Directiva 91/271/CEE aguas residuales)

### Referencias reales de ciberataques

**Colonial Pipeline (Mayo 2021):**
- Ransomware DarkSide cerró 5.500 millas de oleoducto
- 45% combustible costa Este USA afectado
- Rescate pagado: USD 4.4M
- **Problema real:** No sabían qué fallaría después (gasolineras, aeropuertos, hospitales)

**Oldsmar Water Treatment (Febrero 2021):**
- Hacker accedió a sistema SCADA
- Intentó aumentar soda cáustica x100 (envenenar agua)
- Detectado por operador humano (suerte)

**Lección aprendida:** Los datos existían en silos separados. Nadie fusionó la información para ver la cascada.

### Por qué el contexto ambiental importa

**El mismo ciberataque tiene impacto diferente según contexto:**

**Verano (38°C, ola calor):** Ventana 2-3h → Crisis sanitaria  
**Invierno (2°C):** Ventana 12-24h → Molestia gestionable  
**San Fermín (1M turistas):** Crisis reputacional internacional

**Diferencial PRISMA:**
```
Sistema tradicional:
"Alerta SCADA" → Respuesta estándar

PRISMA:
"Alerta SCADA" + 38°C + Twitter trending + 112 saturado
→ "CRÍTICO: 2h, no 12h"
```

---

## 🎬 ESTRUCTURA DEMO

> **En presentación dual (ambiental + cyber):** Este caso ocupa ~2 minutos. Se muestra como "segundo escenario" para demostrar versatilidad del motor. Ver estructura condensada al final de esta sección.

### VERSIÓN COMPLETA (7 minutos) — Si se presenta solo

### ACTO 1: El Problema (1 minuto)

**Slide + Narración:**

> "Colonial Pipeline, mayo 2021. Un ransomware cerró el oleoducto más grande de Estados Unidos.
> 
> El problema NO fue el hack. Fue que nadie sabía **qué fallaría después**:
> - Gasolineras sin combustible
> - Aeropuertos cancelando vuelos  
> - Hospitales sin suministros
> 
> Los datos existían. Pero estaban en **silos separados**.
> 
> En Pamplona, si hackean la depuradora Arazuri, ¿sabrías en tiempo real qué hospitales se quedan sin agua? ¿Qué colegios cerrar? ¿Dónde enviar cisternas primero?"

**Visual sugerido:**
- Foto Colonial Pipeline
- Mapa Pamplona con EDAR Arazuri marcada
- Iconos hospitales, colegios, industria (sin conexiones visibles)

---

### ACTO 2: La Demo PRISMA (4 minutos)

#### Pantalla 1: Detección Automática (30 segundos)

**Dashboard PRISMA mostrando:**

```
🚨 ALERTA CRÍTICA - 09:47h
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Infraestructura Agua Pamplona - Ataque coordinado
⚠️  ETAP Urtasun: Acceso no autorizado, bombas OFFLINE
⚠️  ETAP Egillor: Comunicación perdida
⚠️  EDAR Arazuri: Sistema cloración desactivado
⚠️  Red distribución: Presión cayendo

FUENTES CONFIRMADAS:
✓ SCADA múltiple: Alertas ETAPs + EDAR (09:45h)
✓ Twitter: 23 menciones "sin agua" / "agua rara" (09:46h)  
✓ 112: 8 llamadas zonas dispersas (09:47h)
✓ Meteo: 37°C - Ola calor día 4

CASCADA DETECTADA:
• Sin agua potable → Hospitales, colegios, industria
• Vertido sin tratar → Contaminación río Arga
• Verano + ola calor = Ventana 2-3h

PROBABILIDAD CIBERATAQUE COORDINADO: 97%
```

**Narración:**
> "Son las 9:47 de la mañana. Hace 37 grados, ola de calor día 4.
> 
> PRISMA fusiona en **2 minutos**:
> - SCADA (acceso no autorizado)
> - Twitter (12 tweets "agua huele raro")
> - 112 (2 llamadas agua turbia)
> - Meteo (37°C, ola calor)
> 
> **Esto es clave**: El contexto ambiental cambia TODO.
> 
> En enero tendríamos 12 horas. En julio con 37°C, tenemos 2-3 horas."

**Elementos técnicos clave:**
- Fusión multi-fuente (SCADA + RRSS + 112 + meteo)
- Contexto ambiental (cambia priorización)
- Confirmación cruzada (reduce falsos positivos)

---

#### Pantalla 2: Predicción de Cascada (1 minuto)

**Mapa interactivo Pamplona mostrando:**

```
🧠 ANÁLISIS DE IMPACTO EN CASCADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INFRAESTRUCTURAS EN RIESGO:

🏥 CRÍTICO - Hospitales (4 horas)
   • Hospital A: 3 quirófanos activos
   • Hospital B: UCI 18 pacientes
   • Clínica C: Diálisis 24 pacientes
   ⚠️  Sin agua → Cancelación cirugías urgentes

🏫 ALTO - Centros educativos (6 horas)  
   • 47 colegios (12.000 alumnos)
   ⚠️  Protocolo sanitario → Cierre obligatorio

🏢 MEDIO - Industria alimentaria (8 horas)
   • Mercairuña: Cadena frío
   ⚠️  Sin agua → Pérdidas 2M€/día

🎉 CRÍTICO - San Fermín (INMEDIATO)
   • 700.000+ personas (turistas + locales)
   • 3 días para chupinazo
   ⚠️  Sin agua → CANCELACIÓN FIESTAS

🏘️ ALTO - Población general (6 horas)
   • Hoteles 100% ocupación
   • 2.500 corredores/día encierros
   ⚠️  Golpes calor sin hidratación

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 POBLACIÓN AFECTADA: 700.000+ personas
🗓️  CONTEXTO: 3 días antes San Fermín
🌡️  TEMPERATURA: 35°C (ola calor)
⏱️  VENTANA DE ACTUACIÓN: 2 horas
💰 IMPACTO ECONÓMICO SIN ACCIÓN: 50-100M€
```

**Narración:**
> "Aquí está el diferencial de PRISMA.
> 
> No solo detecta el ataque. **Predice la cascada**:
> - **San Fermín en 3 días**. 700.000 personas. Medios internacionales.
> - En 2 horas, turistas sin agua en hoteles a 35°C
> - En 4 horas, 3 hospitales sin agua para cirugías
> - En 6 horas, decisión crítica: ¿Se cancela San Fermín?
> 
> **Sin PRISMA**, el alcalde se entera por Twitter. Con PRISMA, tiene 2 horas de ventaja.
> 
> Esto es lo que faltó en Colonial Pipeline. **Visibilidad de dependencias en tiempo real**."

**Elementos técnicos clave:**
- Mapeo de dependencias (grafo de infraestructuras)
- Priorización automática (criticidad + tiempo)
- Impacto económico estimado (ROI claro)

---

#### Pantalla 3: Recomendaciones IA + Human-in-the-Loop (1.5 minutos)

**Panel de decisión mostrando:**

```
🎯 ACCIONES RECOMENDADAS (Prioridad IA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SUMINISTRO ALTERNATIVO [CRÍTICO]
   ✓ Activar cisternas → 3 hospitales
   ✓ Ruta optimizada: 47 min llegada
   ✓ Capacidad: 72h autonomía
   ✓ Coste estimado: 15k€
   
2. COORDINACIÓN SANITARIA [ALTO]
   ✓ Cancelar cirugías no urgentes (12 programadas)
   ✓ Derivar diálisis → Hospital D (fuera zona)
   ✓ Alertar UCI: Protocolo agua embotellada
   ✓ Notificar Salud Pública Navarra
   
3. EDUCACIÓN [MEDIO]
   ✓ Notificar 47 directores colegios
   ✓ SMS padres: "Recogida anticipada 14h"
   ✓ Protocolo cierre ordenado
   
4. COMUNICACIÓN PÚBLICA [MEDIO]
   ✓ Nota prensa: "Incidente controlado"
   ✓ RRSS: "Agua embotellada disponible"
   ✓ Evitar pánico compras
   ✓ Hotline ciudadana: 948 XXX XXX

5. CIBERSEGURIDAD [ALTO]
   ✓ Alertar CERT Navarra
   ✓ Aislar sistema SCADA infectado
   ✓ Activar modo manual depuradora
   ✓ Análisis forense (preservar evidencias)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️  TIEMPO PARA APROBAR: 2 minutos
👤 OPERADOR 112: Validar acciones ↓

[APROBAR TODO] [REVISAR] [RECHAZAR]
```

**Interacción en vivo (demo):**
1. Operador (tú) revisa recomendaciones en pantalla
2. Hace clic en "APROBAR TODO"
3. Sistema muestra confirmación: "Plan activado - 5 acciones en ejecución"

**Narración:**
> "PRISMA no decide solo. **Human-in-the-Loop**.
> 
> La IA sugiere 5 acciones priorizadas. El operador valida en **30 segundos**.
> 
> Una vez aprobado, PRISMA ejecuta automáticamente:
> - APIs a empresa cisternas (pedido automático)
> - SMS a directores colegios
> - Alertas hospitales
> - Comunicación pública coordinada
> - Notificación CERT
> 
> Todo trazable. Todo auditable. **AI Act compliant desde día 1**."

**Elementos técnicos clave:**
- Supervisión humana (no autónomo 100%)
- Priorización inteligente (no todas las acciones son iguales)
- Ejecución automática post-aprobación (velocidad)
- Trazabilidad completa (compliance)

---

#### Pantalla 4: Timeline y Trazabilidad (1 minuto)

**Dashboard final mostrando:**

```
📊 INCIDENTE RESUELTO - Timeline Completa
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 3 de julio 2026 - 3 días antes San Fermín
🌡️ 35°C - Ola de calor

09:45h → Detección anomalía SCADA
09:47h → Confirmación ciberataque (3 fuentes)
09:50h → Análisis cascada: "SAN FERMÍN EN RIESGO"
09:52h → Operador aprueba plan respuesta
09:53h → Cisternas activadas (llegada 10:40h)
10:00h → Alcaldía notificada (2h ventaja vs Twitter)
10:15h → Hospitales + Hoteles principales notificados
10:30h → Plan contingencia agua turistas
10:45h → Nota prensa: "Incidente controlado"
11:20h → CERT Navarra aísla sistema infectado
13:45h → Depuradora operativa (modo manual)
16:30h → Cisternas en puntos críticos

06 julio → 🎉 CHUPINAZO A LAS 12:00h

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ RESULTADO:
   • San Fermín 2026: CELEBRADO normalmente
   • 0 turistas hospitalizados por deshidratación
   • 0 cancelaciones hoteles
   • Tiempo respuesta: 8 minutos (vs 2-4 horas manual)
   • Pérdidas evitadas: ~100M€
   • Cumplimiento NIS2: 100% trazabilidad

💾 Informe auditoría generado automáticamente
🧠 Memoria vectorial actualizada (próxima vez -40% tiempo)

MÉTRICAS CLAVE:
• Detección → Acción: 8 minutos
• Población protegida: 250.000 habitantes
• Pérdidas evitadas: 5-8M€
• Actores coordinados: 12 (hospitales, colegios, CERT, prensa)
```

**Narración:**
> "De detección a acción: **8 minutos**.
> 
> Sin PRISMA, este proceso toma 2-4 horas. Y sin coordinación:
> - Cirugías canceladas
> - Pánico en supermercados
> - Pérdidas millonarias
> - Posibles intoxicaciones
> 
> Con PRISMA:
> - Timeline completa auditable (NIS2)
> - Aprendizaje automático (próxima vez más rápido)
> - **0 vidas en riesgo**
> - **5-8M€ pérdidas evitadas**"

**Elementos técnicos clave:**
- Auditoría completa (NIS2, AI Act)
- Aprendizaje continuo (memoria vectorial)
- Métricas de impacto (ROI demostrable)

---

### ACTO 3: El Diferencial (1 minuto)

**Slide comparativa:**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│         EVERBRIDGE              vs              PRISMA          │
│                                                                 │
│  ✓ Notifica el ataque       →      ✓ Detecta el ataque        │
│  ✓ Envía alertas masivas    →      ✓ Predice la cascada       │
│  ✗ No mapea dependencias    →      ✓ Mapea dependencias       │
│  ✗ Respuesta manual         →      ✓ Coordina automático      │
│  ✗ Sin aprendizaje          →      ✓ Mejora continua          │
│  ✗ Reglas predefinidas      →      ✓ Razonamiento LLM         │
│                                                                 │
│  "Te avisa del problema"    →      "Te dice qué hacer"         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

COMPLEMENTARIOS, NO COMPETIDORES:
• Everbridge ejecuta lo conocido (workflows predefinidos)
• PRISMA razona sobre lo desconocido (situaciones emergentes)
```

**Narración:**
> "Everbridge es excelente notificando crisis **conocidas**.
> 
> PRISMA razona sobre crisis **desconocidas**:
> - ¿Qué fallará después?
> - ¿Quién debe actuar primero?
> - ¿Cómo coordinamos 12 actores en paralelo?
> 
> No competimos con Everbridge. **Los complementamos**.
> 
> Ellos son el sistema de notificación. Nosotros somos el cerebro que decide qué notificar, a quién, y cuándo."

---

### ACTO 4: Roadmap (1 minuto)

**Slide timeline:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOY (Dic 2025) - MVP DEMO
├─ Detección + Predicción cascada
├─ 2 casos de uso: Ambiental (calor+incendio) + Cyber (ransomware agua)
└─ Demo funcional (datos simulados + APIs reales)

Q1 2026 (Si decisión GO empresa)
├─ Piloto real EDAR Arazuri + 112 Navarra
├─ Integración FIWARE (Orion-LD, Perseo CEP)
└─ Validación técnica con operadores reales

Q2 2026
├─ Módulo Energía (apagones, subestaciones)
├─ Módulo Salud (brotes, saturación UCI)
└─ 2-3 pilotos pagados (utilities + hospitales)

Q4 2026
├─ Multi-infraestructura (agua + energía + salud)
├─ Predicción 48h (no solo reactivo)
└─ Certificación FIWARE "Powered by"

2027
├─ 5-8 clientes activos (B2G + B2B)
├─ ARR objetivo: 200k€
└─ Expansión geográfica (Euskadi, Aragón)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MERCADO OBJETIVO:
• 50+ Utilities España (NIS2 obligatorio 2024)
• 30+ Hospitales grandes (CER + AI Act)
• 200+ Ciudades (Sendai Framework, Plan EDIL)

VENTANA COMPETITIVA: 12-18 meses antes que competidores retrofitteen GenAI

PRICING ORIENTATIVO:
• PoC utilities: 60-100k€ (6 meses)
• Despliegue anual: 80-150k€ (SaaS recurrente)
```

---

### VERSIÓN CONDENSADA (2 minutos) — Para presentación dual

**Contexto:** Se presenta después del caso ambiental. El público ya entiende qué es PRISMA.

**Minuto 4-5: Transición + Detección**

> "Mismo motor. Diferente cascada.
>
> Ahora, 3 de julio. 3 días antes de San Fermín. Ransomware entra por proveedor SCADA.
>
> PRISMA fusiona en 2 minutos: anomalía SCADA + 12 tweets 'agua rara' + 2 llamadas 112.
>
> Contexto: 35°C. En enero tendríamos 12 horas. Hoy tenemos 2."

**Minuto 5-6: Cascada + Acción**

> [Mostrar mapa con hospitales, hoteles, San Fermín]
>
> "San Fermín en 3 días. 700.000 personas. Sin agua.
>
> PRISMA ya tiene el plan: cisternas a hospitales, notificar CERT, cancelar cirugías no urgentes.
>
> El operador aprueba en 30 segundos. [Click APROBAR - Telegram suena]
>
> 8 minutos de detección a acción. Sin PRISMA, 2-4 horas."

**Cierre (transición a diferencial):**

> "Dos dominios. Dos cascadas. Un solo motor de inteligencia situacional."

---

## 🏗️ Arquitectura Técnica MVP

### Decisión: Chat Conversacional + FIWARE Event-Driven

**Por qué:**
- ✅ Narrativa natural para demo
- ✅ FIWARE real con suscripciones (no mock)
- ✅ Event-driven (no polling)
- ✅ Demuestra arquitectura profesional

---

## 📐 Arquitectura de Componentes

```
┌─────────────────────────────────────────────────────┐
│           STREAMLIT (Chat UI)                       │
│  [Botón: Iniciar Escenario] → Dispara Workflow 1   │
│  [Chat] → Consulta estado actual                   │
└────────────────┬────────────────────────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
    ↓                         ↓
┌─────────────┐         ┌──────────────────────────┐
│ n8n WF1     │         │ n8n WF2                  │
│ Generator   │         │ Agent PRISMA             │
│             │         │                          │
│ Escribe en  │         │ Recibe notificaciones    │
│ FIWARE      │         │ desde FIWARE             │
└──────┬──────┘         └────────┬─────────────────┘
       │                         │
       │ PUT/PATCH               │ POST (notification)
       │                         │
       └────→ ┌─────────────────┴────────┐
              │  FIWARE Context Broker   │
              │  (Orion-LD)              │
              │                          │
              │  Entidades:              │
              │  - EDAR_Arazuri          │
              │  - TwitterMentions       │
              │  - Calls112              │
              │  - WeatherObserved       │
              │                          │
              │  [Subscriptions]         │
              │  → Notifica a WF2        │
              └──────────────────────────┘
```

---

## 🔄 Flujo de Información

### FASE 1: Iniciar Escenario (Botón en Streamlit)

```
Usuario clica [Iniciar Escenario]
    ↓
Streamlit → POST /webhook/start-scenario
    ↓
n8n WF1 (Event Generator):
    ↓
T+0s:  PUT FIWARE /v2/entities/EDAR_Arazuri
       {status: "anomaly", chlorinePumps: "offline"}
    ↓
T+30s: PUT FIWARE /v2/entities/TwitterMentions
       {count: 12, hashtag: "#AguaSuciaPamplona"}
    ↓
T+60s: PUT FIWARE /v2/entities/Calls112
       {count: 2, topic: "agua_turbia"}
    ↓
FIWARE (automático):
    → Detecta cambios
    → POST /webhook/fiware-notification (a n8n WF2)
    → Notifica 3 veces (una por cada entidad)
    ↓
n8n WF2 (Agent PRISMA):
    → Recibe 3 notificaciones
    → Guarda en memoria interna
    → Actualiza alert_level = "critical"
    ↓
Streamlit muestra:
    "✅ Escenario listo - PRISMA recibió 3 notificaciones"
```

---

### FASE 2: Usuario Consulta (Chat)

```
Usuario escribe: "¿Qué está pasando?"
    ↓
Streamlit → POST /webhook/chat
    ↓
n8n WF2 (Agent PRISMA):
    ↓
    Identifica intención: "detect"
    ↓
    Lee memoria interna:
    - SCADA: anomaly (notificado hace 2 min)
    - Twitter: 12 menciones (notificado hace 1 min)
    - 112: 2 llamadas (notificado hace 30 seg)
    ↓
    Query FIWARE (confirmar estado actual):
    GET /v2/entities/EDAR_Arazuri
    GET /v2/entities/WeatherObserved
    ↓
    LLM fusiona + analiza
    ↓
    Responde: "🚨 He recibido 3 notificaciones..."
    ↓
Streamlit muestra respuesta bot
```

---

### FASE 3: Aprobar y Ejecutar

```
Usuario escribe: "Aprobar"
    ↓
n8n WF2:
    ↓
    Identifica intención: "execute"
    ↓
    Telegram: Envía alerta Hospital A
    Telegram: Envía alerta Colegios
    ↓
    Responde: "✅ Plan activado"
    ↓
Usuario ve Telegram (teléfono suena)
```

---

## 🎯 Componentes a Construir

### 1. FIWARE (Entidades + Suscripción)

**Entidades en Sandbox TwIN Lab:**

```json
// 1. Infraestructura Agua (simplificado para MVP)
{
  "id": "WaterInfra_Pamplona",
  "type": "WaterNetwork",
  "etap_status": {"value": "normal"},
  "edar_status": {"value": "normal"},
  "distribution_pressure": {"value": "normal"}
}

// 2. TwitterMentions_Pamplona
{
  "id": "TwitterMentions_Pamplona",
  "type": "TwitterMentions",
  "count": {"value": 0},
  "hashtag": {"value": ""}
}

// 3. Calls112_Pamplona
{
  "id": "Calls112_Pamplona",
  "type": "Calls112",
  "count": {"value": 0},
  "topic": {"value": ""}
}

// 4. WeatherObserved_Pamplona
{
  "id": "WeatherObserved_Pamplona",
  "type": "WeatherObserved",
  "temperature": {"value": 25},
  "alert": {"value": "none"}
}
```

**Suscripción FIWARE:**
```json
POST /v2/subscriptions
{
  "subject": {
    "entities": [
      {"idPattern": ".*", "type": "WaterTreatmentPlant"},
      {"idPattern": ".*", "type": "TwitterMentions"},
      {"idPattern": ".*", "type": "Calls112"}
    ]
  },
  "notification": {
    "http": {
      "url": "http://n8n:5678/webhook/fiware-notification"
    }
  }
}
```

**Esto hace que FIWARE notifique automáticamente a n8n WF2 cuando cualquier entidad cambia.**

---

### 2. n8n Workflows (2 separados)

**Workflow 1: Event Generator**
```
[Webhook] /start-scenario
    ↓
[HTTP PUT] FIWARE EDAR_Arazuri {status: "anomaly"}
[Wait 30s]
[HTTP PUT] FIWARE TwitterMentions {count: 12}
[Wait 30s]
[HTTP PUT] FIWARE Calls112 {count: 2}
    ↓
[Respond] "Scenario ready"
```

**Workflow 2: Agent PRISMA**
```
[Webhook A] /fiware-notification
    → Guarda en memoria (variables n8n)

[Webhook B] /chat
    ↓
[Switch] Identifica intención
    ├─ "qué está pasando" → Lee memoria + Query FIWARE + LLM
    ├─ "qué hacer" → LLM genera plan
    └─ "aprobar" → Telegram + Mocks
    ↓
[Respond] JSON respuesta
```

---

### 3. Streamlit (Chat UI + Botón)

**Pantalla inicial:**
- Botón: "Iniciar Escenario Ciberataque"
- Progress bar (90 segundos)
- Habilita chat cuando listo

**Chat:**
- Input usuario
- Historial conversación
- Llamadas a n8n WF2 /chat

---

### 4. Knowledge Base (n8n variable)

**Archivo:** `knowledge_base.json`

```json
{
  "infraestructura": {
    "hospitales": [
      {"nombre": "Hospital A", "quirofanos": 3, "autonomia_agua": "4h"},
      {"nombre": "Hospital B", "uci_camas": 18, "autonomia_agua": "6h"},
      {"nombre": "Clínica C", "diálisis": 24, "autonomia_agua": "3h"}
    ],
    "colegios": 47,
    "población": 250000,
    "edar": "Arazuri"
  },
  "protocolos": {
    "ciberataque": {
      "acciones": [
        "1. Alertar CERT Navarra",
        "2. Activar cisternas hospitales",
        "3. Notificar Protección Civil",
        "4. Comunicación pública"
      ]
    }
  },
  "umbrales": {
    "twitter_critico": 10,
    "temperatura_critica": 37,
    "scada_anomalia": 0.9
  }
}
```

**Uso en n8n:**
```
Variable global: knowledge_base = {{content de archivo}}

OpenAI Prompt incluye:
"Infraestructura: {{$vars.knowledge_base.infraestructura}}
 Protocolos: {{$vars.knowledge_base.protocolos}}"
```

---

## 🎬 Demo Flow (Pitch)

**Minuto 3 del pitch:**

**Tú:** "Voy a iniciar un escenario de ciberataque. Observen cómo PRISMA detecta cambios en tiempo real..."

**[Proyectas Streamlit - clicas botón]**

```
⏳ Generando eventos en FIWARE Context Broker...

✓ 09:45h - SCADA Arazuri actualizado
  → FIWARE notificó a PRISMA automáticamente

✓ 09:46h - Twitter mentions actualizado  
  → FIWARE notificó a PRISMA automáticamente

✓ 09:47h - Llamadas 112 actualizadas
  → FIWARE notificó a PRISMA automáticamente

✅ Escenario listo - PRISMA recibió 3 notificaciones
```

**Tú (mientras esperas 90 seg):** "No estoy consultando manualmente. FIWARE está notificando a PRISMA cada vez que algo cambia. Esto es **event-driven architecture** real."

**[Chat habilitado - escribes]:** "¿Qué está pasando?"

**Bot responde:**
```
🚨 He recibido 3 notificaciones en los últimos 2 minutos:

1. 09:45h - SCADA Arazuri reportó anomalía
2. 09:46h - Twitter: 12 menciones negativas
3. 09:47h - 112: 2 llamadas agua turbia

He fusionado estas fuentes y confirmo:
Ciberataque con 94% probabilidad...
```

**[Escribes]:** "¿Qué debemos hacer?"

**Bot:** "Recomiendo: 1. Cisternas hospitales, 2. Cancelar cirugías..."

**[Escribes]:** "Aprobar"

**Bot:** "✅ Plan activado. Revisa tu Telegram..."

**[Tu teléfono suena - proyectas Telegram]**

```
PRISMA Bot:
🚨 ALERTA CRÍTICA
Activar cisternas Hospital A
```

**[Vuelves a slides]:** "Esto es lo que faltó en Colonial Pipeline."

**Tiempo total:** 3-4 minutos

---

## ⚡ Plan de Ejecución (1 Semana)

### Lunes: FIWARE + Workflows Base
- [ ] Crear 4 entidades FIWARE (EDAR, Twitter, 112, Weather)
- [ ] Crear suscripción FIWARE → n8n
- [ ] n8n WF1: Event Generator básico
- [ ] n8n WF2: Webhook recibir notificaciones

### Martes: Generador de Escenarios
- [ ] n8n WF1: Completar timeline (PUT entidades con delays)
- [ ] Test: Verificar que FIWARE notifica a WF2
- [ ] n8n WF2: Guardar notificaciones en memoria

### Miércoles: Agente Conversacional
- [ ] n8n WF2: Switch intenciones (detect, recommend, execute)
- [ ] n8n WF2: Integrar LLM (OpenAI node)
- [ ] Test: Consultar memoria + FIWARE

### Jueves: Streamlit + Telegram
- [ ] Streamlit: Botón iniciar escenario + progress bar
- [ ] Streamlit: Chat básico
- [ ] n8n WF2: Telegram alertas
- [ ] Test: Flujo completo

### Viernes: Pulir y Ensayar
- [ ] Refinar respuestas LLM
- [ ] Timing demo (3-4 min exactos)
- [ ] Ensayo completo x3

---

## 📋 Decisiones Pendientes

### Técnicas
- [ ] **LLM**: ¿GPT-4 (mejor calidad) o Mistral (open source)?
- [ ] **Timing delays**: ¿30s entre eventos o más rápido/lento?
- [ ] **Suscripción FIWARE**: ¿Notificar todos los atributos o solo cambios?

### Demo
- [ ] **Telegram**: ¿Canal privado o grupo? (privado más simple)
- [ ] **Proyección**: ¿2 pantallas o alternar? (2 pantallas más fluido)
- [ ] **Plan B**: Video grabado backup por si falla conexión

### Narrativa
- [ ] **Tono bot**: Conversacional pero profesional
- [ ] **Longitud respuestas**: Concisas (3-4 líneas max por punto)
- [ ] **Mencionar FIWARE**: Sí, enfatizar "notificación automática vía FIWARE"

---

## 🎯 Diferencial Clave a Comunicar

**No es solo un chatbot. Es:**
1. **Event-driven** (FIWARE notifica, no polling)
2. **Fusión multi-fuente** (SCADA + Twitter + 112 + Meteo)
3. **Contexto ambiental** (37°C cambia priorización)
4. **Ejecución real** (Telegram suena de verdad)

---

## 📋 Cumplimiento NIS2 (Diferencial Regulatorio)

**El MVP demuestra cumplimiento NIS2 porque:**
- ✅ **Detección ciberataques** (SCADA anomalía)
- ✅ **Coordinación respuesta** (plan priorizado)
- ✅ **Supervisión humana** (Human-in-the-Loop)
- ✅ **Auditoría completa** (timeline trazable)

**Mensaje para utilities:** "No solo proteges activos, cumples NIS2 automáticamente"

---

## 💰 ROI Específico del Caso de Uso

**Sin PRISMA (escenario pre-San Fermín):**
- Detección ataque coordinado: 2-4 horas (cada planta reporta por separado)
- No se detecta patrón coordinado
- 700k personas sin agua potable
- **Pérdidas potenciales:**
  - Cancelación/suspensión San Fermín: **50-100M€**
  - Daño reputacional internacional: **incalculable**
  - Crisis sanitaria: Hospitalizaciones masivas
  - Multas medioambientales: **1-5M€**

**Con PRISMA:**
- Detección: 8 minutos (correlación automática multi-planta)
- Alerta: "Ataque coordinado, patrón ransomware"
- Cisternas activas antes de impacto crítico
- EDAR en modo manual antes de vertido
- San Fermín: Continúa con plan contingencia
- **Pérdidas: <500k€** (costes operativos + contingencia)

**ROI:** "Por 100-150k€/año, evitas crisis de 50-100M€"

**Mensaje para inversores:** "¿Cuánto vale evitar la cancelación de San Fermín?"

---

## ⚠️ El antipatrón: DANA Valencia (octubre 2024)

**229 fallecidos.** ¿Qué falló?

| Factor humano | Lo que pasó |
|---------------|-------------|
| **Información fragmentada** | AEMET alertó, CHJ alertó, pero cada uno por su canal |
| **Luchas políticas** | Gobierno central vs Generalitat vs ayuntamientos |
| **Elusión responsabilidad** | "Eso lo decide X", "Yo no tenía esa información" |
| **Desconocimiento técnico** | Decisores sin entender qué significaban los datos |
| **Parálisis por comité** | Reuniones mientras el agua subía |
| **Alerta tardía** | 20:12h, cuando ya había fallecidos |

**La jueza:** *"Grosera negligencia"* y *"manifiesta pasividad"* de la Generalitat.

**Amnistía Internacional:** Vulneración del derecho a la vida por no proporcionar información adecuada y oportuna.

---

### 🎯 Lo que PRISMA habría cambiado:

| Sin sistema | Con PRISMA |
|-------------|------------|
| Cada fuente reporta por separado | **Fusión automática** de todas las fuentes |
| "¿Quién tiene que decidir?" | **Recomendación clara** con responsable asignado |
| "No sabía que era tan grave" | **Visualización de cascada** en tiempo real |
| Reunión de 2 horas para decidir | **Decisión en 2 minutos** (human-in-the-loop) |
| Alerta cuando ya hay muertos | **Alerta en T+8 minutos** |
| "Nadie me avisó" | **Trazabilidad completa**: quién sabía qué, cuándo |

---

### 💡 La propuesta de valor en una frase:

> **"PRISMA no sustituye a los humanos. Les da la información correcta, en el momento correcto, con las opciones claras. Para que no haya excusas."**

O más directo para inversores:

> **"PRISMA es el sistema que Valencia no tenía el 29 de octubre."**

---

## 🆚 Diferencial vs Everbridge (Simplificado)

| | Everbridge | PRISMA |
|---|---|---|
| **Cuándo actúa** | Después del evento | Antes del evento |
| **Cómo funciona** | Reglas predefinidas | Razonamiento IA |
| **Qué hace** | Notifica lo conocido | Detecta lo desconocido |

**Mensaje:** "Everbridge te avisa que hubo apagón. PRISMA te avisa que VA A HABER apagón en 30 min."

---

## 🎯 Target del MVP y Modelo de Valor

### Cliente Primario
**Utility con departamento innovación** (ej: Veolia, Suez, utilities públicas con fondos I+D)
- Obligada NIS2
- Presupuesto innovación
- Interés en FIWARE/data spaces

### Valor Expandido (Data Spaces FIWARE)
PRISMA no solo protege a la utility, **genera valor para terceros:**

```
Utility (EDAR Arazuri)
    ↓ genera alertas
PRISMA (microservicios en data space)
    ↓ redistribuye a
┌─────────────────────────────────────┐
│ Suscriptores de alertas:           │
│ • Empresas zona industrial         │
│ • Eventos deportivos (San Fermín)  │
│ • Sanidad privada (Quirónsalud)    │
│ • Comercios (Mercairuña)           │
│ • Aseguradoras                     │
└─────────────────────────────────────┘
```

**Modelo de monetización:**
- Utility paga por protección propia
- PRISMA revende microservicios de alerta a terceros interesados
- Data space FIWARE habilita interoperabilidad

### Early Adopter Potencial
- **Mancomunidad Comarca Pamplona** (gestiona ciclo integral agua)
- **EDAR Arazuri / ETAPs** (socios potenciales TwIN Lab)
- **Estado conversaciones:** Pendiente validar post-pitch

---

## 🔗 Data Space Ready (Visión Futura)

### Qué es
PRISMA está diseñado para participar en **Data Spaces europeos** (ecosistemas federados de intercambio de datos con soberanía).

### Por qué importa
- Proyectos EU como DS4SSCC, SIMPL están creando data spaces para ciudades
- TwIN Lab/FIWARE evoluciona hacia data spaces
- Quien esté preparado, entra primero

### PRISMA: FIWARE-native desde día 1
- ✅ **NGSI-LD nativo** (no retrofit, diseñado así desde inception)
- ✅ **FIWARE Context Broker** (infraestructura data spaces)
- ✅ **APIs abiertas** (publicables en catálogos)
- ✅ **Smart Data Models** (interoperabilidad europea)
- 🎯 **Powered by FIWARE** (certificación objetivo 2026)

**Diferencial:** Competidores deben adaptar sistemas legacy. PRISMA nace compatible.
**Beneficio certificación:** Acceso a FIWARE Marketplace + credibilidad B2G europea.

### Modelo de monetización futuro

```
PRISMA publica en Data Space:
    ↓
"Servicio de Alertas Multirriesgo"
    ↓
Suscriptores pagan por acceso:
• Empresas zona industrial
• Eventos (San Fermín)
• Sanidad privada
• Aseguradoras
• Comercios
```

### Para MVP
- **No implementamos** data space propio (complejo)
- **Sí diseñamos** compatible desde día 1
- **Referencia:** [iris360 Data Space](https://www.iris360iot.com/data-space/) (Libelium)

---

## 📊 Métricas de Éxito

### Para el pitch (19 dic)

**Técnicas:**
- ✅ Demo funciona sin errores críticos
- ✅ Flujo completo en 7 minutos
- ✅ Interacción en vivo (aprobar plan)

**Narrativa:**
- ✅ Problema claro (Colonial Pipeline)
- ✅ Diferencial evidente (vs Everbridge)
- ✅ Roadmap creíble

**Validación mercado:**
- ✅ 3-5 conversaciones clientes potenciales
- ✅ Feedback positivo mentores TwIN Lab

### Post-pitch (decisión go/no-go)

**Criterios para GO empresa:**
- ✅ Feedback inversores/mentores positivo
- ✅ Interés real co-fundadores shadow
- ✅ Viabilidad técnica validada
- ✅ Ruta funding clara (50-100k€ año 1)

**Criterios para PIVOT:**
- ⚠️ Feedback tibio o negativo
- ⚠️ Complejidad técnica subestimada
- ⚠️ Sin co-fundadores comprometidos
- ⚠️ Funding incierto

---

## 💰 Modelo de Negocio (Post-MVP)

### Mercado objetivo

**Segmento 1: Utilities (NIS2 obligatorio)**
- 50+ empresas agua/energía España
- Ciclo venta: 6-9 meses
- Pricing: 60-100k€ PoC, 80-150k€ anual

**Segmento 2: Hospitales (CER + AI Act)**
- 30+ hospitales grandes España
- Ciclo venta: 4-6 meses (privado), 9-15 meses (público)
- Pricing: 40-60k€ PoC, 60-100k€ anual

**Segmento 3: Ciudades (Sendai Framework)**
- 200+ ciudades Agenda 2030
- Ciclo venta: 9-18 meses (licitación)
- Pricing: 30-60k€ anual (según habitantes)

### Propuesta de valor

**Para utilities:**
> "Cumple NIS2 + protege activos críticos + reduce pérdidas operativas"

**Para hospitales:**
> "Protege vidas + cumple CER + mejora coordinación emergencias"

**Para ciudades:**
> "Cumple Sendai + protege ciudadanos + reduce daños económicos"

### Diferenciadores

1. **Compliance by design** (NIS2, CER, AI Act desde día 1)
2. **Mapeo dependencias en tiempo real** (nadie más lo hace)
3. **Razonamiento LLM** (no solo reglas predefinidas)
4. **FIWARE-native** (interoperabilidad europea)
5. **Track record fundador** (€4.5M+ funding histórico)

---

## 🚀 Plan de Ejecución Final (Semana 12-19 dic)

### Lunes-Martes: FIWARE + Base
- [ ] Crear entidades FIWARE (WaterInfra, Twitter, 112, Weather)
- [ ] Configurar suscripción FIWARE → n8n
- [ ] n8n WF1: Event Generator con delays

### Miércoles: Agente + LLM
- [ ] n8n WF2: Integrar consulta FIWARE + LLM
- [ ] Knowledge base en prompts (hospitales, protocolos)
- [ ] Test flujo completo

### Jueves: UI + Alertas
- [ ] Streamlit: Botón escenario + chat
- [ ] Telegram alertas reales
- [ ] Sincronizar con caso ambiental

### Viernes: Ensayo
- [ ] Demo completa 2 min (este caso)
- [ ] Integrar con demo ambiental (7 min total)
- [ ] Plan B preparado

---

## 📝 Notas y Decisiones Pendientes

### Decisiones técnicas

- [ ] **LLM**: ¿GPT-4 (mejor calidad) o Mistral (open source, EUPL)?
- [ ] **Frontend**: ¿Streamlit (rápido) o Gradio (más visual)?
- [ ] **SCADA mock**: ¿Datos sintéticos o históricos reales?

### Decisiones narrativa

- [ ] **Tono pitch**: ¿Técnico o emocional? (probablemente híbrido)
- [ ] **Demo en vivo**: ¿Riesgo o imprescindible? (imprescindible, con plan B)
- [ ] **Comparativa Everbridge**: ¿Mencionar explícitamente o implícito?

### Validaciones pendientes

- [ ] Conversación EDAR Arazuri (¿datos reales SCADA?)
- [ ] Conversación 112 Navarra (¿protocolos reales?)
- [ ] Conversación utilities (¿interés real NIS2?)

---

## 💡 Principios de Trabajo

**Keep it simple:**
- Documento vivo, no biblia
- Iterar según aprendizaje real
- No overengineer antes de validar
- MVP primero, complejidad después

**Próximos pasos:**
1. Validar narrativa con 2-3 personas
2. Empezar desarrollo técnico mínimo
3. Iterar según feedback

---

**Última actualización:** 12 diciembre 2025  
**Próxima revisión:** Post-pitch (20 dic)  
**Owner:** Miguel Escribano

