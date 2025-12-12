# PRISMA — Mapa de Exploración de Mercado

**Territorio, Patrones, Hipótesis (Fase Pre-MVP)**

---

## Resumen Ejecutivo

### Contexto

Este documento es un **mapa exploratorio**, no un plan estratégico definitivo. PRISMA se encuentra en fase pre-MVP (TRL 4-5), sin empresa constituida, fundador solo, participando en TwIN Lab 2025 para validar propuesta de valor y modelo de negocio.

**Objetivo**: Mapear el territorio de mercado, identificar patrones invariantes, white spaces competitivos, y generar hipótesis a validar mediante conversaciones con clientes potenciales y mentores TwIN Lab.

### Hallazgos Clave

**1. Mercado fragmentado entre infraestructura IoT y gestión de emergencias**

El ecosistema de gemelos digitales urbanos y resiliencia se divide claramente en dos mundos que NO se hablan:

- **Mundo 1 — Plataformas IoT/Data Space** (Siemens, Azure, AWS, iris360): Dashboards, sensores, gemelos 3D estáticos, monitorización reactiva. Excelentes en visibilidad operacional, débiles en respuesta autónoma a emergencias.

- **Mundo 2 — Critical Event Management** (Everbridge, One Concern, Palantir): Alertas masivas, coordinación manual, análisis post-evento. Excelentes en notificación, débiles en detección autónoma y comprensión semántica de eventos complejos.

**PRISMA propone un puente**: Computer Vision autónoma + LLMs multimodales + Agentic AI coordinación → Sistema nervioso autónomo (no solo sensorial) para emergencias.

**2. Timing crítico: Ventana tecnológica 12-18 meses**

Los competidores actuales construyeron sus plataformas en era pre-GenAI (2015-2022). LSTM, RNN, dashboards reactivos, alertas basadas en umbrales. Retrofitting GenAI a estas arquitecturas requiere 12-18 meses mínimo.

PRISMA puede arrancar con arquitectura **nativa GenAI** (LLMs multimodales, Agentic AI, CV state-of-the-art) desde día 1. Primera verdad fundamental: **la velocidad de innovación IA supera la capacidad de adoption de infraestructuras legacy**.

**3. Regulación europea empuja inversión obligatoria (NIS2, CER, AI Act)**

Directivas NIS2 (ciberseguridad infraestructuras críticas) y CER (resiliencia entidades críticas) obligan a energía, transporte, farma, agua a invertir en resiliencia 2024-2026. AI Act clasifica sistemas IA en emergencias como "alto riesgo" → compliance by design es ventaja competitiva.

**Insight estratégico**: Sectores críticos NO compran "tech cool", compran **compliance + mitigación riesgo regulatorio**. PRISMA by design para NIS2/CER/AI Act = puerta de entrada.

**4. Dual B2G/B2B es obligatorio (no opcional)**

GovTech puro sufre:
- Ciclos venta 12-18 meses
- CAC alto (licitaciones, certificaciones, competencia desleal grandes integradores)
- Cash burn peligroso para fundador solo sin financiación

**Quick-wins B2B críticos**: Utilities privadas, hospitales privados, recintos eventos, aeropuertos, seguridad privada. Pricing 50-150k €, ciclos 3-6 meses, validación rápida.

**5. Modelo de negocio: Arquetipo híbrido projects-to-product es el más viable**

Fundador solo año 1 → Servicios AIOps / proyectos custom (cash flow 0-3 meses)  
Fundador + 1-2 devs año 2 → Extraer módulos reutilizables (Detección CV, Respuesta Agentic AI)  
Fundador + equipo año 3 → Producto SaaS modular

**NO** plataforma SaaS monolítica día 1 (imposible sin funding 500k-1M).  
**NO** open-source day 1 (sin co-founder técnico, complejidad excesiva).

### Hipótesis Prioritarias a Validar en TwIN Lab

1. **¿Sectores críticos pagarían por "autonomous response" vs "better dashboards"?** (energía, farma, transporte)
2. **¿Canal indirecto vía partners tipo Tesicnor acelera acceso a clientes públicos?**
3. **¿Hay demanda proyectos custom AIOps 50-100k € en privado antes que plataforma SaaS?**
4. **¿Compliance NIS2/CER by design resuena como diferencial vs "mejor IA"?**
5. **¿Casos uso "personas en riesgo" (hospitales, estadios, transporte) tienen mayor urgencia que infraestructura pura (utilities, agua)?**

---

## 1. Ecosistema de Actores — Mapeo Competitivo

### 1.1 Metodología

**Principio**: SIEMPRE producto específico, NUNCA empresa genérica.  
Ejemplo: "Siemens" → ❌  |  "**Siemens City Digital Twin**" → ✅

Investigamos **30+ actores** agrupados en 5 tiers. Este NO es un análisis exhaustivo, es un **mapa de territorio** para identificar patrones.

---

### 1.2 TIER 1 — Gigantes Globales (Infraestructura IoT + Gemelos Digitales)

**¿Por qué importan?**: Definen estándares, capturan presupuestos grandes, tienen credibilidad institucional. Son el "establishment" contra el que PRISMA compite o con el que potencialmente colabora.

| **Empresa** | **Producto Específico** | **Propósito** | **Sectores Target** | **Tech Stack** | **Modelo Negocio** | **URLs** |
|-------------|-------------------------|---------------|---------------------|----------------|-------------------|----------|
| **Siemens** | **City Digital Twin** | Gemelos urbanos para sostenibilidad, simulación escenarios, movilidad | Smart Cities, energía, infraestructura urbana | Open urban IoT platform, DTDL (Digital Twins Definition Language), simulación integrada | Proyectos B2G grandes (3-10M €), plataforma licenciada | `https://www.siemens.com/global/en/company/insights/digital-twins-powering-sustainable-urbanization.html` |
| **Microsoft** | **Azure Digital Twins** | Plataforma cloud para réplicas digitales de espacios/infraestructuras | Smart Cities, edificios inteligentes, utilities | Azure IoT Hub, DTDL, integración Azure Maps, AI integrado | PaaS (pago por uso), típico B2B enterprise | `https://azure.microsoft.com/en-us/blog/connecting-urban-environments-with-iot-and-digital-twins/` |
| **AWS** | **Smart Cities IoT + Digital Twins** | Infraestructura cloud para gemelos digitales, optimización procesos | Ciudades, utilities, transporte | AWS IoT Core, Amplify, Cognito, Lambda | PaaS/IaaS pago por uso, proyectos custom con partners | `https://aws.amazon.com/blogs/publicsector/building-smart-infrastructure-using-aws-services-digital-twins/` |
| **IBM** | **Maximo Asset Monitor + Digital Twin** | Gestión activos industriales/urbanos con gemelos predictivos | Smart Cities, utilities, transporte, industria | Watson IoT, Maximo, AI/ML predictivo | SaaS + servicios profesionales, proyectos B2B/B2G | `https://www.ibm.com/think/topics/digital-twin` |
| **Oracle** | **IoT Digital Twin Cloud** | Gemelos industriales integrados con ERP/CX, analytics | Industria, supply chain, utilities | OCI (Oracle Cloud Infrastructure), IoT Cloud Service, integración ERP/CX nativa | PaaS + licencias, típico enterprise B2B | `https://docs.oracle.com/en/cloud/paas/iot-cloud/iotgs/oracle-iot-digital-twin-implementation.html` |
| **GE Vernova** | **GridOS Digital Grid** | Software operación redes eléctricas, DERMS, gestión DER | Energía (utilities, grid operators) | GridOS DERMS, ADMS, AI grid management | SaaS + proyectos, típico utilities B2B | `https://www.gevernova.com/software/industry/grid` |
| **Cisco** | **Smart Connected Communities** | Red IoT multi-servicio para ciudades (sensores, cámaras, kiosks, Wi-Fi) | Smart Cities, transporte, seguridad pública | IoT Intent-based Network, sensores, video surveillance | Hardware + software + servicios, B2G | `https://www.cisco.com/c/en/us/solutions/industries/smart-connected-communities.html` |
| **Emerson** | **Digital Twin Automation** | Gemelos para plantas industriales, simulación procesos | Industria (química, oil & gas, pharma, minería) | Mimic Simulation Software, DeltaV Simulation Cloud | SaaS + licencias + servicios profesionales, B2B industrial | `https://www.emerson.com/en-us/automation/operations-business-management/dynamic-simulation/digital-twin-solutions` |

**Patrón observado #1**: Todos son **plataformas de infraestructura** (IoT, sensores, dashboards, simulación) pero **NO sistemas de respuesta autónoma**. Detectan, monitorizan, alertan → **humano decide y actúa**.

**Insight estratégico**: Inversores financian estos gigantes porque venden a **CIOs/CTOs** (presupuesto infraestructura IT). PRISMA debe vender a **CISO/responsables emergencias/operaciones** (presupuesto resiliencia/riesgo).

---

### 1.3 TIER 2 — Plataformas DT Especializadas (Nicho Vertical)

**¿Por qué importan?**: Estos actores demuestran que especialización vertical funciona. NO intentan ser "todo para todos", se enfocan en AEC (Architecture/Engineering/Construction), planificación urbana, GIS.

| **Empresa** | **Producto Específico** | **Propósito** | **Diferencial** | **URLs** |
|-------------|-------------------------|---------------|-----------------|----------|
| **Bentley Systems** | **iTwin Platform** | Gemelos digitales infraestructuras (puentes, carreteras, túneles, edificios) | Open APIs, federación datos ingeniería (CAD, BIM, GIS), ciclo vida completo asset | `https://www.bentley.com/software/itwin-platform/` |
| **Dassault Systèmes** | **3DEXPERIENCE Cities** | Planificación urbana colaborativa, sostenibilidad, participación ciudadana | Simulación 3D avanzada, conecta stakeholders públicos-privados-ciudadanos | `https://www.3ds.com/progress-is-human/cities` |
| **Esri** | **ArcGIS Urban** | Digital twins enfocados GIS, planificación urbana, análisis espacial | Líder GIS mundial, integración spatial data masiva, análisis escenarios zoning | `https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview` |
| **PTC** | **ThingWorx** | Gemelos industriales IoT, realidad aumentada (AR) para mantenimiento | AR para field service, fuerte en manufactura/industria | `https://www.ptc.com/en/products/thingworx` |
| **Autodesk** | **InfraWorks** | Modelado 3D infraestructura civil (carreteras, puentes), planificación | Integración con Autodesk ecosystem (AutoCAD, Revit), diseño ingeniería | `https://www.autodesk.com/products/infraworks/overview` |
| **Hexagon AB** | **M.App Enterprise** | Gemelos para seguridad pública, operaciones emergencias, respuesta | Enfoque seguridad pública, CAD para 911/emergencias, geospatial analytics | `https://hexagon.com/products/m-app-enterprise` |

**Patrón observado #2**: Especialización paga. Bentley domina infraestructura civil, Esri domina GIS. NO intentan hacer "todo". PRISMA podría especializarse en **resiliencia/emergencias/situational awareness**.

**Insight capital**: Bentley $5B valuation, Hexagon $20B+. Inversores pagan múltiplos altos por **liderazgo vertical** vs "otro dashboard genérico".

---

### 1.4 TIER 3 — Startups/Scale-ups (Emergencias, Resiliencia, Urban Analytics)

**¿Por qué CRÍTICOS para PRISMA?**: Aquí están los competidores directos en **gestión emergencias** y los arquetipos de modelo de negocio. También ejemplos de cómo escapar de "infraestructura IoT" hacia "respuesta activa".

#### 3A. Critical Event Management & Disaster Resilience

| **Empresa** | **Producto Específico** | **Propósito** | **Tech Stack** | **Tracción** | **URLs** |
|-------------|-------------------------|---------------|----------------|--------------|----------|
| **Everbridge** | **Critical Event Management Platform** | Alertas masivas, notificaciones multi-canal, coordinación emergencias | Alerting engine, integración 100+ canales (SMS, email, voz, app), dashboard gestión crisis | Público (NASDAQ: EVBG), ~500M $ revenue, 6,000+ clientes (gobiernos, enterprises) | `https://www.everbridge.com/platform/critical-event-management/` |
| **One Concern** | **Resilience-as-a-Service** | Predicción impacto desastres (terremotos, inundaciones) con AI/ML, preparación pre-evento | AI/ML hazard models, geospatial analytics, simulación block-by-block | Series C $45M (2021), clientes: SF, LA, Cupertino, Japón municipalities | `https://www.oneconcern.com/en/` |
| **Palantir** | **Gotham / Foundry + AIP** | Plataforma analytics operaciones críticas (defensa, emergencias, cities) | Ontology-based integration, AI Platform (AIP) con LLMs, data fusion multi-source | Público (NYSE: PLTR), $2B+ revenue, clientes: defense, cities (controversial: predictive policing) | `https://www.palantir.com/platforms/gotham/` |

**ANÁLISIS CRÍTICO — ¿Qué hacen bien? ¿Qué NO hacen?**

**Everbridge**:
- ✅ **Qué hace bien**: Coordinación manual excelente, alerts masivos, multi-canal, integrado con 911/112.
- ❌ **Qué NO hace**: Detección autónoma eventos. Alguien tiene que pulsar botón "enviar alerta". NO tiene CV autónoma, NO interpreta eventos complejos con LLM.
- 🎯 **White space PRISMA**: CV detecta evento → LLM interpreta gravedad → **ENTONCES** Everbridge envía alerts. PRISMA sería "cerebro", Everbridge "brazos".

**One Concern**:
- ✅ **Qué hace bien**: Predicción PRE-desastre (terremotos, inundaciones) con modelos científicos validados. Análisis vulnerabilidad infraestructura.
- ❌ **Qué NO hace**: Respuesta DURANTE emergencia. Es preparación/prevención, NO detección real-time ni coordinación respuesta.
- 🎯 **White space PRISMA**: One Concern predice "¿qué pasaría si terremoto 7.5?". PRISMA detecta "terremoto AHORA, edificio X colapsando, 50 personas atrapadas, coordinar bomberos + hospitales".

**Palantir**:
- ✅ **Qué hace bien**: Fusión datos masiva (multi-source integration), analytics sofisticados, ontología flexible. AIP añade LLMs (2023-2024).
- ❌ **Qué NO hace**: Venta mid-market Europa (solo mega-contratos defense/gobierno USA). CAC altísimo. NO tiene módulos CV autónoma ni Agentic AI coordinación (aún).
- 🎯 **White space PRISMA**: Palantir vende a Pentágono/FBI ($20M+ contratos). PRISMA podría vender a utilities/hospitals/airports europeos (50-200k € proyectos). Diferente buyer, diferente GTM.

**Patrón observado #3**: Ninguno combina **CV autónoma + LLM interpretación + Agentic AI coordinación** en un solo sistema. Everbridge es "notificador", One Concern es "predictor", Palantir es "integrador de datos".

**Insight sistémico**: ¿Por qué nadie lo ha construido? **NO es tech (todo existe open-source)**. Es **timing** (LLMs multimodales + Agentic AI maduros solo desde 2023-2024) + **GTM** (vendedores emergency management vendían "alertas", no "autonomía").

---

#### 3B. Urban Digital Twin Startups/Scale-ups

| **Empresa** | **Producto Específico** | **Propósito** | **Diferencial** | **Tracción** | **URLs** |
|-------------|-------------------------|---------------|-----------------|--------------|----------|
| **Cityzenith** | **SmartWorldOS** | Gemelo digital ciudades enfocado descarbonización, eficiencia energética edificios | "Clean Cities" initiative, donó plataforma a 100 ciudades, foco net-zero | Proyectos: LA, Phoenix, Las Vegas, Amaravati (India $6.5B capital), iniciativa filantropía tech | `https://cityzenith.com/` |
| **Aretian** | **Barcelona City Digital Twin** | Analytics urbano, planificación económica, modelado escenarios | Especialización Barcelona/Europa, integración datos socioeconómicos + urbanos | Proyecto Barcelona Metropolitan Region, stakeholders: Barcelona Global, IESE, fundaciones | `https://www.aretian.com/aretian-cdt` |
| **Urbanetic** | **TwinWorks** | Gemelos digitales operacionales ciudades, análisis flujos, movilidad | Enfoque operaciones ciudad día-a-día vs solo planificación | Scale-up europea, múltiples proyectos municipales | `https://urbanetic.io/twinworks` |
| **iris360** | **Platform (IoT + Data Space + Digital Twins)** | Plataforma modular IoT FIWARE, Data Space (GAIA-X, IDSA), gemelos 3D | Compliance total (FIWARE, UNE 178104, GAIA-X), certificaciones ENS Alto, ISO 27001, española | Casos éxito: Algeciras (puerto), Medellín, Cartagena. Empresa madura (~50-100 empleados estimado) | `https://www.iris360iot.com/` |

**CASO DE ESTUDIO PROFUNDO: iris360 vs PRISMA**

**¿Por qué iris360 es el competidor MÁS relevante para entender?**

Es una empresa española madura, técnicamente excelente, con casos de éxito reales, compliance impecable... pero tiene **límites arquitecturales claros** que definen el white space de PRISMA.

**Lo que iris360 HACE EXCELENTE**:
- Plataforma IoT robusta (sensores Libelium + terceros, dashboards customizables)
- Data Space compliant (GAIA-X, IDSA, FIWARE, BDVA) → interoperabilidad europea
- Gemelos digitales 3D (simulación escenarios, VR/AR, visualización inmersiva)
- Certificaciones (ENS Alto, ISO 27001, ISO 17025)
- Casos de éxito B2G (Ayuntamientos, puertos)

**Lo que iris360 NO HACE (White Space PRISMA)**:

1. **Situational Awareness Autónoma**
   - iris360: Sensor puerta aeropuerto detecta 500 personas (umbral 300) → Dashboard rojo → **Operador humano ve alerta → Operador decide enviar seguridad**
   - PRISMA: CV autónoma analiza cámaras → LLM interpreta "aglomeración peligrosa, personas empujando, riesgo avalancha" → Agentic AI redistribuye 3 agentes desde otra puerta + alerta médicos + cierra acceso → **TODO en 30 segundos, autónomo**

2. **Fusión Multimodal Real-Time**
   - iris360: Centrado en **sensores IoT** (dispositivos, APIs, bases de datos estructuradas)
   - PRISMA: Social media (Twitter pánico) + 112 transcrito (llamadas emergencia) + bases socioeconómicas (vulnerabilidad poblacional) + sensores + CV cámaras → **Fusión multimodal heterogénea**

3. **Fase RESPUESTA del Ciclo de Vida del Riesgo**
   - iris360: Prevención ✅ (simulación), Preparación ✅ (dashboards), Detección ✅ (alertas), Respuesta ⚠️ (humano decide viendo dashboard)
   - PRISMA: Respuesta **Autónoma** → Agentic AI coordina multi-agencia sin intervención humana (redistribución recursos, triaje, comunicación)

4. **GenAI Interpretación (no Deep Learning Clásico)**
   - iris360: IA predictiva LSTM/RNN para series temporales (excelente para "predecir tráfico mañana")
   - PRISMA: LLMs multimodales para interpretación semántica ("se ha caído árbol encima coche, persona atrapada, llamar ambulancia")

5. **Compliance NIS2 + CER + AI Act by Design**
   - iris360: ENS Alto (España), ISO 27001. **NO menciona NIS2** (Directiva UE 2022), CER, AI Act
   - PRISMA: Diseñado desde día 1 para NIS2/CER/AI Act → ventana oportunidad sectores críticos obligados cumplir 2024-2026

**Conclusión iris360 vs PRISMA**:
- iris360 es "sistema nervioso sensorial" (ve, siente, informa)
- PRISMA es "sistema nervioso autónomo" (detecta, interpreta, actúa sin decisión consciente humana)

**¿Hay mercado si iris360 ya existe?** SÍ, porque:
- Categorías diferentes: iris360 = Infraestructura IoT | PRISMA = Respuesta Autónoma Emergencias
- Buyers diferentes: iris360 vende a CIO/CDO (IT budget) | PRISMA vende a CISO/Emergencias (risk/resilience budget)
- Timing: iris360 arquitectura pre-GenAI (2015-2022), PRISMA nativa GenAI (ventana 12-18 meses)
- Posible complementariedad: iris360 infraestructura + PRISMA capa inteligencia autónoma (partnership potential)

---

### 1.5 TIER 4 — Integradores (Acceso Indirecto Mercado)

**¿Por qué importan?**: Tienen contratos marco con gobiernos, acceso a licitaciones, credibilidad institucional. PRISMA solo NO puede competir en licitaciones GovTech, pero **vía partners integr adores sí**.

| **Empresa** | **Relevancia** | **Potencial Rol PRISMA** |
|-------------|----------------|--------------------------|
| **Indra Sistemas** | Integrador líder España (defense, transporte, Smart Cities) | Partner tech: Indra vende proyecto, PRISMA entrega módulo CV+Agentic AI (revenue share 70/30) |
| **Atos / Eviden** | Integrador europeo, foco ciberseguridad, defense | Similar Indra, posible integración módulos PRISMA en proyectos grandes |
| **Telefónica Tech** | Operator telecom + integrador Smart Cities España/LATAM | Canal distribución, especialmente LATAM donde tiene presencia fuerte |
| **Capgemini / Accenture** | Consultoras globales, proyectos transformación digital ciudades | Partners potenciales para proyectos internacionales (fuera España) |
| **Jacobs Engineering** | Ingeniería infraestructuras críticas (USA/global) | Acceso mercado USA/UK si PRISMA escala internacionalmente |
| **Tesicnor** | **CRÍTICO**: Ingeniería especializada DRR (Disaster Risk Reduction), proyectos Navarra/Euskadi/Europa | **Partnership prioritario**: Tienen DRR Platform, acceso clientes públicos, conocen ciclo vida riesgo. Revenue share + co-desarrollo |

**Patrón observado #4**: Integradores NO construyen tech core, la compran/integran. Buscan diferenciadores técnicos para ganar licitaciones. PRISMA podría ser ese diferenciador ("única solución con CV autónoma + compliance NIS2 by design").

**Modelo partnership típico**:
- Revenue share: 70% integrador, 30% PRISMA (si integrador vende)
- o inverso: 70% PRISMA, 30% integrador (si PRISMA vende con introducción integrador)
- Integrador aporta: Acceso clientes, credibilidad, gestión proyecto, certificaciones
- PRISMA aporta: Tech core, especialización emergencias, diferenciación licitación

---

### 1.6 TIER 5 — Ecosistemas y Estándares (Enabling Infrastructure)

**¿Por qué importan?**: NO venden productos, pero definen estándares, canales de financiación (grants, open calls), y credibilidad institucional. Participar en estos ecosistemas = señal de calidad + acceso a funding + visibilidad europea.

| **Ecosistema** | **Propósito** | **Relevancia PRISMA** | **URLs** |
|----------------|---------------|----------------------|----------|
| **FIWARE Foundation** | Estándar europeo open-source plataformas Smart Cities (NGSI-LD, context brokers, data models) | Certificación "Powered by FIWARE" = credibilidad B2G Europa. Open Calls cascade funding (10-170k € típico). Marketplace visibilidad. | `https://www.fiware.org/` |
| **GAIA-X** | Federación infraestructura datos europea (soberanía digital, interoperabilidad clouds) | Compliance GAIA-X = argumento venta "datos no salen UE", especialmente sectores críticos preocupados por soberanía (energía, farma, defense) | `https://www.data-infrastructure.eu/` |
| **IDSA** | International Data Spaces Association (estándares compartición datos segura B2B) | Connector IDS integrado en PRISMA = interoperabilidad con otros sistemas europeos (utilities, transporté, hospitales que adopten IDS) | `https://internationaldataspaces.org/` |
| **BDVA** | Big Data Value Association (lobby industry + research agenda EU) | Participación BDVA = acceso early a H2020/Horizon Europe calls, networking con grandes (Siemens, SAP, etc.) | `https://www.big-data-value.eu/` |
| **PANTHEON** | Proyecto H2020 European Digital Twin platform | Partnership potencial: PANTHEON busca casos uso verticales. PRISMA podría ser caso uso "emergencias/resiliencia". Credibilidad académica + acceso co-funding. | TODO: Buscar URL proyecto activo |
| **DestinE** | Destination Earth (EU): Gemelo digital Tierra para cambio climático, desastres naturales | Acceso datos clima/desastres gratis. Posible integración PRISMA con predicciones DestinE (inundaciones, olas calor) → early warning. | `https://destination-earth.eu/` |
| **Tesicnor DRR Platform** | **CRÍTICO**: Plataforma Disaster Risk Reduction de Tesicnor (Navarra). Ingeniería especializada renovables + riesgos ambientales. | **Partnership prioritario #1**: Tienen arquitectura DRR, acceso clientes públicos Navarra/Euskadi, experiencia ciclo vida riesgo. Posible co-desarrollo módulos PRISMA para su plataforma. | TODO: Analizar SRD Tesicnor en profundidad |

**Patrón observado #5**: Ecosistemas europeos buscan **casos de éxito replicables** para justificar inversión pública. PRISMA podría ser showcase "European GenAI for resilience" → grants, visibilidad, partnerships.

**Insight capital**: Estar en FIWARE Marketplace + GAIA-X compliant + partnership PANTHEON = señal para inversores "esto es serio, no solo vaporware".

---

### 1.7 Síntesis — Patrones Emergentes del Ecosistema

Después de mapear 30+ actores, emergen **5 verdades fundamentales** sobre cómo funciona este mercado:

#### PATRÓN 1: Fragmentación Infraestructura vs Respuesta

**Observación**: Nadie integra "sensores → análisis → acción" en un solo sistema autónomo.

- **Mundo Infra** (Siemens, Azure, AWS, iris360): Sensores → Dashboard → Humano decide
- **Mundo Emergencias** (Everbridge, One Concern): Alguien pulsa botón → Alert masivo → Humano coordina

**Implicación**: El mercado asume que "respuesta siempre es manual". Esto es un **supuesto heredado de era pre-IA** (cuando no existía CV autónoma ni Agentic AI).

**Oportunidad PRISMA**: Ser el primer actor que cierra el loop **detección → interpretación → acción autónoma**.

---

#### PATRÓN 2: Innovación IA más rápida que Adoption Legacy

**Observación**: Competidores construyeron plataformas 2015-2022 (pre-GenAI). Arquitecturas basadas en:
- Deep learning clásico (LSTM, RNN)
- Dashboards reactivos
- Alertas basadas en umbrales (if sensor > X → alert)

GenAI multimodal (GPT-4V, Gemini) + Agentic AI (AutoGen, LangChain) maduró **2023-2024**. Retrofitting estas capacidades a arquitecturas legacy requiere **12-18 meses mínimo** (reescribir core, migrar datos, reentrenar equipos).

**Implicación temporal**: Ventana oportunidad **12-18 meses** donde PRISMA puede construir nativo GenAI mientras competidores retrofittean.

**Riesgo**: Palantir, Everbridge tienen capital para acelerar. One Concern ya tiene AI/ML team fuerte. Ventana NO es permanente.

---

#### PATRÓN 3: Compliance Regulatoria como Forcing Function

**Observación**: NIS2 (ciberseguridad infraestructuras críticas) y CER (resiliencia entidades críticas) obligan a energía, transporte, farma, agua a invertir en resiliencia **2024-2026**. NO es opcional, es mandato legal.

AI Act (2024) clasifica sistemas IA en emergencias/críticas como **"alto riesgo"** → requisitos documentación, auditoría, transparencia.

**Implicación buyer psychology**: Sectores críticos NO compran "tech cool", compran **mitigación riesgo regulatorio**. Decision maker es CISO/Legal/Compliance, NO CTO.

**Oportunidad PRISMA**: Posicionarse como "compliance by design" (NIS2/CER/AI Act desde día 1) vs competidores que retrofittean compliance.

**Messaging**: "PRISMA le ayuda a cumplir NIS2 mientras mejora su resiliencia" > "PRISMA tiene mejor IA".

---

#### PATRÓN 4: Especialización Vertical paga múltiplos 2-3x

**Observación**: Comparativa valuations (aproximadas, fuentes públicas/estimates):

| **Tipo** | **Ejemplos** | **Valuation típica** | **Revenue multiple** |
|----------|-------------|---------------------|---------------------|
| Infra genérica | Azure IoT (dentro MSFT), AWS IoT | - | Valorado como cloud general ~5-8x revenue |
| Vertical líderes | Bentley (infra civil), Hexagon (seguridad), Palantir (defense/gov) | $3-20B | 10-15x revenue |
| SaaS vertical | Everbridge (CEM) | $2-3B (aprox, fluctúa) | 8-10x revenue |
| Servicios/consulting | Integradores, ingenierías | - | 0.5-2x revenue (EBITDA multiples) |

**Implicación strategic**: Inversores pagan **2-3x más por liderazgo vertical** que por "otro dashboard IoT genérico".

**Oportunidad PRISMA**: Especializarse en **"Autonomous Situational Awareness for Critical Emergencies"** (vertical) vs "Smart Cities platform" (horizontal).

---

#### PATRÓN 5: Canal Indirecto acelera B2G, Dual B2G/B2B reduce riesgo

**Observación**: Startups que intentaron GovTech directo sin tractión B2B previa:
- Ciclos venta 12-18 meses
- CAC altísimo (licitaciones, certificaciones, lobbying)
- Cash burn peligroso sin funding fuerte
- Competencia desleal integradores grandes (Indra, Atos lobby político)

**Contraejemplo éxito**: Everbridge primero vendió a **enterprises privadas** (bancos, utilities, pharmas) → casos éxito → después gobiernos.

**Implicación GTM**: Dual B2G/B2B NO es opcional, es **obligatorio para sobrevivir**.

**Secuencia recomendada PRISMA**:
1. Año 1: Quick-wins B2B privado (utilities, hospitales privados, recintos eventos) → Cash flow + casos éxito
2. Año 2: B2B + canal indirecto vía Tesicnor/integradores → Acceso B2G sin competir directo
3. Año 3: B2G directo con track record sólido

---

## 2. Sectores Críticos — Opportunity Maps

### 2.1 Criterios de Selección

PRISMA no puede ser "para todos". La especialización vertical paga múltiplos 2-3x superiores vs plataformas horizontales genéricas. Seleccionamos 7 sectores basados en tres criterios:

1. **Tensión Geopolítica**: Autonomía estratégica Europa vs dependencia Asia (energía, farma, defense)
2. **Situational Awareness Crítica**: Personas en riesgo inmediato, decisiones tiempo real, eventos multimodales
3. **Regulación Forcing Function**: NIS2, CER, AI Act obligan inversión 2024-2026 (no opcional)

**Tier A (análisis profundo)**: Energía, Farma/Salud, Transporte Crítico, Espacios Públicos/Eventos, Agua  
**Tier B (análisis medio)**: Defensa, Alimentación

---

### 2.2 TIER A — Sectores Análisis Profundo

#### 2.2.1 Energía (Utilities, Grid Operators)

**Tensión fundamental**: Dependencia gas ruso (pre-2022 ~40% UE) + transición renovables (intermitencia) + ciberataques OT crecientes (Colonial Pipeline USA 2021, grid attacks Ucrania) = tormenta perfecta resiliencia.

**Regulación obligatoria**:
- **NIS2** (Directiva UE 2022, transposición octubre 2024): Energía es "sector alta criticidad" Annex I. Obligatorio: risk assessments regulares, gestión incidentes 24h, supervisión cadena suministro, auditorías no anunciadas, multas diarias por incumplimiento.
- **CER** (2022/2557): Utilities deben planes resiliencia multi-riesgo (ciber + físico + cascada).

**Players B2B prioritarios**:
- Iberdrola (España ~40GW capacidad), EDP (Portugal/España), Naturgy, Endesa → Utilities grandes con presupuestos IT/resiliencia 50-200M € anuales
- REE (Red Eléctrica España): Grid operator, responsable estabilidad red, presión regulatoria máxima NIS2

**Casos uso PRISMA específicos**:
1. **Detección autónoma ciberataques OT**: CV analiza dashboards SCADA → LLM detecta patrones anómalos (ransomware, DDoS) → Agentic AI aísla zonas, activa redundancias, coordina CERT
2. **Coordinación apagones cascada**: Social media early warning (tendencias "apagón barrio X") + sensores grid + 112 transcrito (llamadas "sin luz hospitales") → LLM prioriza restauración (hospitales > industria > residencial)
3. **Respuesta emergencias físicas subestaciones**: CV detecta incendio/intrusión → Agentic AI coordina bomberos + seguridad + redirige carga eléctrica a subestación backup

**Pricing orientativo** (basado en benchmarking Everbridge, Palantir utilities):
- PoC/Pilot: 50-80k € (6 meses, 1 subestación crítica)
- Despliegue regional: 150-300k € anual (ARR modelo o proyecto 12 meses)
- Decision maker: CISO + Director Operaciones Grid + Compliance Officer (triple approval NIS2)

**Cycle venta**:
- B2B privado (Iberdrola, Naturgy): 6-9 meses típico (PoC rápido 3 meses, después contrato)
- B2G (REE): 12-18 meses (licitación pública)

---

#### 2.2.2 Farma/Salud (Hospitales, Pharma Manufacturing)

**Tensión fundamental**: Dependencia APIs China/India 80%+ (principios activos farmacéuticos) + reshoring post-COVID + pandemias futuras (OMS predice cada 5-10 años) = soberanía sanitaria crítica.

**Regulación obligatoria**:
- **CER**: Hospitales grandes y pharma manufacturers esenciales → planes resiliencia multi-amenaza
- **AI Act**: Sistemas IA en triaje emergencias/coordinación médica = **"alto riesgo"** Annex III → Documentación, auditoría, transparencia obligatoria. PRISMA debe diseñarse compliance AI Act desde día 1.

**Players B2B prioritarios**:
- Hospitales públicos grandes: Osakidetza (Euskadi), Sermas (Madrid), Hospital Vall d'Hebron → presupuestos IT/emergencias ~10-30M € anuales
- Hospitales privados: Quirónsalud (red 50+ hospitales España), HM Hospitales → ciclos compra más rápidos que público
- Pharma manufacturers: Rovi (vacunas, biosimilares), Almirall, Esteve → resilliencia cadena producción crítica
- Distribuidoras: Cofares, Alliance Healthcare → continuidad suministro farmacias

**Casos uso PRISMA específicos**:
1. **Early warning brotes epidémicos**: Social media (trending "fiebre hospital X") + 112 transcrito (llamadas síntomas) + datos epidemiológicos públicos → LLM detecta patrón brote 24-48h antes que métodos tradicionales → Agentic AI pre-alerta hospitales, activa protocolos
2. **Coordinación saturación UCI multi-hospital**: CV detecta ocupación UCI Hospital A 95% → LLM analiza gravedad pacientes → Agentic AI coordina derivaciones Hospital B/C + ambulancias + camas disponibles → triaje autónomo
3. **Gestión crisis pharma (rotura stock medicamento crítico)**: Integración bases datos distribuidoras + social media alarma desabastecimiento → LLM prioriza hospitales críticos (UCI, oncología) → Agentic AI redirige stock, coordina transporte urgente

**Pricing orientativo**:
- PoC hospital: 40-60k € (3 meses, módulo early warning brotes)
- Despliegue red hospitalaria: 100-200k € anual (red 5-10 hospitales)
- Decision maker: Director TI + Director Médico + Comité Emergencias (hospitales públicos lenta burocracia, privados más rápido)

**Cycle venta**:
- B2B privado (Quirónsalud): 4-6 meses
- B2G (hospitales públicos): 9-15 meses

**Insight crítico**: Hospitales son sector con **máxima urgencia situational awareness personas en riesgo**. COVID demostró fragilidad sistemas coordinación manual. Willingness-to-pay alta si PRISMA demuestra "salva vidas".

---

#### 2.2.3 Transporte/Movilidad Crítica (Aeropuertos, Puertos, Renfe)

**Tensión fundamental**: Puertos estratégicos Asia-Europa (Valencia 1º EU contenedores, Algeciras) + aeropuertos hub (Madrid-Barajas 60M pasajeros) + terrorismo soft targets + accidentes masivos (Germanwings 2015, train crashes) = alta exposición riesgo.

**Regulación obligatoria**:
- **NIS2**: Transporte es sector crítico Annex I
- **CER**: Infraestructuras transporte deben planes resiliencia multi-riesgo

**Players B2B prioritarios**:
- Aena (aeropuertos España): Monopolio, presupuesto IT ~100M €, necesitan soluciones escalables 50+ aeropuertos
- Puertos del Estado: Autoridades portuarias (Valencia, Algeciras, Barcelona) → proyectos individuales o coordinados
- Renfe: Operador ferroviario, preocupación seguridad pasajeros (accidentes, terrorismo)
- TMB/Metro Madrid: Transporte urbano masivo, riesgo aglomeraciones, emergencias túneles

**Casos uso PRISMA específicos**:
1. **Detección aglomeraciones peligrosas aeropuerto**: CV autónoma en puertas embarque/llegada → LLM detecta "densidad crítica + movimiento bloqueado + posible pánico" → Agentic AI redistribuye seguridad, cierra accesos, alerta megafonía, coordina servicios médicos
2. **Coordinación accidente ferroviario**: CV detecta anomalía vía (descarrilamiento) + 112 masivo (llamadas emergencia) → LLM evalúa gravedad (heridos, fuego, químicos) → Agentic AI coordina bomberos + hospitales + evacuación pasajeros otros trenes + corte eléctrico catenaria
3. **Seguridad portuaria multi-amenaza**: CV detecta contenedor sospechoso + Integración listas negras aduana + LLM análisis riesgo → Agentic AI activa protocolos inspección, coordina policía/aduanas

**Pricing orientativo**:
- PoC aeropuerto medio (Bilbao, Valencia): 60-100k € (6 meses, 1 terminal)
- Despliegue aeropuerto grande (Madrid, Barcelona): 200-400k € anual
- Decision maker: Director Seguridad + Director Operaciones + IT

**Cycle venta**:
- Aena (público): 12-18 meses (licitación)
- Puertos (mixto público-privado): 9-12 meses

---

#### 2.2.4 Espacios Públicos / Eventos Masivos (Estadios, Recintos, Ayuntamientos)

**Tensión fundamental**: Terrorismo soft targets (Bataclan París 2015, Manchester Arena 2017) + aglomeraciones masivas (Love Parade Alemania 2010: 21 muertos aplastamiento) + eventos internacionales (Mundial, Eurovisión) = máxima exposición mediática.

**Regulación obligatoria**:
- Menos regulación directa NIS2/CER (no son "infraestructuras críticas" formalmente), PERO presión pública/mediática altísima tras incidentes

**Players B2B prioritarios**:
- Recintos privados grandes: Camp Nou (FC Barcelona), Wanda Metropolitano (Atlético Madrid), IFEMA (ferias), WiZink Center → Presión aseguradoras + reputación
- Ayuntamientos (policía municipal): Madrid, Barcelona, Valencia → Coordinación eventos públicos (conciertos, manifestaciones)
- Organizadores eventos: Live Nation, Primavera Sound, festivales → Responsabilidad seguridad miles/decenas miles personas
- Seguridad privada: Prosegur, Securitas → Buscan diferenciación tech para contratos

**Casos uso PRISMA específicos**:
1. **Prevención avalanchas estadio/concierto**: CV detecta densidad crítica sector + análisis flujo personas (bloqueo salidas) → LLM interpreta gravedad inminente → Agentic AI cierra accesos nuevos visitantes, abre salidas emergencia, redistribuye seguridad, megafonía dispersión
2. **Detección amenazas terroristas**: CV detecta comportamiento sospechoso (paquete abandonado, persona nervios) + Análisis social media (amenazas previas evento) → LLM evalúa riesgo → Agentic AI alerta seguridad, activa protocolo evacuación discreto
3. **Coordinación emergencia médica masiva**: CV detecta persona caída + multitud rodeando → LLM identifica "emergencia médica + riesgo aplastamiento" → Agentic AI coordina médicos in-situ + ambulancia + dispersión multitud + pausa evento si necesario

**Pricing orientativo**:
- PoC recinto (1 evento grande, ej: concierto 50k personas): 30-50k €
- Contrato anual recinto (Wanda, IFEMA): 80-150k € (múltiples eventos)
- Decision maker: Director Seguridad + Director Operaciones

**Cycle venta**:
- B2B privado (recintos, organizadores): **3-6 meses** (RÁPIDO, urgencia pre-evento grande)
- B2G (Ayuntamientos): 9-12 meses

**Insight crítico**: Este es el sector **quick-win más claro para PRISMA**. Ciclos cortos, urgencia real, willingness-to-pay (aseguradoras presionan), casos uso muy visibles ("salvamos vidas en Camp Nou" = PR brutal).

---

#### 2.2.5 Agua (Utilities Hídricas, Confederaciones)

**Tensión fundamental**: Escasez hídrica cambio climático (España mediterránea sequías recurrentes) + inundaciones extremas (DANA Valencia oct 2024: 200+ muertos) + contaminación industrial/agrícola = estrés hídrico creciente.

**Regulación obligatoria**:
- **NIS2**: Utilities agua = sector crítico
- **CER**: Gestión crisis sequía/inundación

**Players B2B prioritarios**: Canal Isabel II (Madrid), Agbar (Grupo Veolia, múltiples ciudades), EMASESA (Sevilla), Confederaciones Hidrográficas

**Casos uso PRISMA**: Coordinación crisis sequía (priorización sectores), early warning inundaciones (social media + pluviómetros + CV cauces), detección contaminación (análisis patrones consumo anómalos)

**Pricing**: 60-120k € PoC, 150-250k € anual despliegue  
**Cycle**: B2B 6-9m, B2G 12-15m

---

### 2.3 TIER B — Análisis Medio

#### Defensa (Bases Militares, Navantia, Indra Sistemas)

**Tensión**: Máxima (geopolítica global), pero **difícil acceso directo** para startup sin credenciales security clearance. Requiere canal indirecto vía Indra/Navantia.

**Casos uso**: Protección infraestructuras críticas, coordinación multi-amenaza (ciber + físico), análisis threat intelligence

**Estrategia PRISMA**: NO atacar directo año 1-2. Partnership Indra cuando haya tracción B2B otros sectores. Indra necesita diferenciadores tech para ganar licitaciones defense.

#### Alimentación (Mercadona, Mercasa, Cooperativas)

**Tensión**: Continuidad cadena frío, brotes sanitarios (listeria, e-coli), trazabilidad. Menos urgencia inmediata que otros sectores.

**Casos uso**: Early warning brotes (social media "intoxicación restaurante X" + datos sanitarios) → LLM identifica lote contaminado → Agentic AI coordina retirada retail

**Estrategia PRISMA**: Prioridad media-baja año 1. Explorar si hay quick-win evidente, sino postponer.

---

## 3. Marco Conceptual — Ciclo de Vida del Riesgo

### 3.1 Framework Mental (inspirado Tesicnor DRR + Sendai Framework)

El **Ciclo de Vida del Riesgo** estructura cómo organizaciones gestionan amenazas, desde anticipación hasta recuperación. PRISMA puede posicionarse en TODAS las fases (vs competidores focalizados en 1-2):

```
PREVENCIÓN → PREPARACIÓN → DETECCIÓN → RESPUESTA → RECUPERACIÓN
   ↑_____________________________________________________________↓
              (Ciclo continuo: aprendizaje de cada crisis)
```

**Fase 1 - PREVENCIÓN/MITIGACIÓN**:
- Qué: Reducir probabilidad evento (ej: simulación escenarios, identificación vulnerabilidades)
- Herramientas actuales: Simuladores (Siemens, Dassault), análisis vulnerabilidad (One Concern)
- PRISMA diferencial: **LLM analiza históricos incidentes + social media patterns → identifica riesgos emergentes NO obvios** (ej: tendencia quejas Twitter sobre "aglomeraciones puerta 12 aeropuerto" → predice avalancha futura si no se actúa)

**Fase 2 - PREPARACIÓN**:
- Qué: Planes, protocolos, entrenamientos, recursos pre-posicionados
- Herramientas actuales: Dashboards operacionales (iris360, Azure DT), manuales procedimientos
- PRISMA diferencial: **Gemelo digital predictivo entrenado con LLM → simula crisis específicas ("¿qué pasa si huelga ambulancias + gripe masiva?") → recomienda pre-posicionamiento recursos**

**Fase 3 - DETECCIÓN/EARLY WARNING**:
- Qué: Identificar evento ANTES o inicio (minutos/horas ventaja crítica)
- Herramientas actuales: Sensores + alertas umbrales, monitorización manual
- PRISMA diferencial: ✅ **CORE VALUE PROPOSITION** → **CV autónoma + fusión multimodal (social media + 112 + sensores) + LLM interpretación semántica → detección 10-100x más rápida que humano viendo dashboards**

**Fase 4 - RESPUESTA**:
- Qué: Acción inmediata (evacuación, rescate, contención daños)
- Herramientas actuales: Coordinación manual vía radio/calls, Everbridge alertas masivas
- PRISMA diferencial: ✅ **CORE VALUE PROPOSITION #2** → **Agentic AI coordina multi-agencia AUTÓNOMAMENTE** (redistribuye recursos, prioriza acciones, comunica stakeholders) **sin esperar decisión humana consciente** (supervisión sí, operación no)

**Fase 5 - RECUPERACIÓN**:
- Qué: Vuelta a normalidad, reparación daños, análisis lecciones aprendidas
- Herramientas actuales: Project management manual, dashboards reporting
- PRISMA diferencial: **LLM analiza logs completos crisis → genera informe automático lecciones + recomendaciones mejora protocolos → alimenta Fase 1 (ciclo)**

---

### 3.2 Aplicabilidad Arquitectura Modular PRISMA

El ciclo vida del riesgo permite **venta modular** (NO forzar plataforma monolítica):

**Módulo 1 - "PRISMA Detect"** (Detección Fase 3):
- CV autónoma + LLM interpretación
- Venta rápida (PoC 3 meses, 40-60k €)
- Cliente compra SOLO detección, integra con sus sistemas respuesta actuales

**Módulo 2 - "PRISMA Respond"** (Respuesta Fase 4):
- Agentic AI coordinación
- Vende DESPUÉS que Módulo 1 (upsell)
- Precio 80-120k € adicional

**Módulo 3 - "PRISMA Predict"** (Prevención/Preparación Fases 1-2):
- Gemelo predictivo LLM
- Venta enterprise madura (>200k €)

**Ventaja modular**:
1. Cliente paga menos upfront (reduce riesgo percibido)
2. PRISMA demuestra valor rápido (PoC Módulo 1 → resultados 3 meses → upsell Módulo 2)
3. Arquitectura NO monolítica = menos riesgo obsolescencia (si LLM cambia, solo actualizar componente, no reescribir todo)

---

## 4. Arquetipos de Modelo de Negocio — Contextos de Aplicación

**Premisa**: NO decidir modelo ahora. Explorar **cuándo tiene sentido cada arquetipo** basado en contexto (funding, equipo, tracción mercado).

### 4.1 Arquetipo A — Plataforma SaaS Monolítica

**Descripción**: PaaS completa cobertura ciclo vida riesgo (Prevención → Recuperación), multi-tenant cloud, ARR modelo.

**Cuándo tiene sentido**:
- Conseguido funding 500k-1M € (Series A/grants grandes)
- Equipo 5-7 personas (2-3 devs, 1 PM, 1 sales, founder)
- Dispuesto esperar 18-24m time-to-market sin revenue significativo
- Mercado SaaS maduro con willingness-to-pay ARR confirmada

**Qué asumimos**:
- Clientes prefieren plataforma completa vs módulos
- Diferenciación sostenible 3-5 años (no obsolescencia rápida IA)
- Competencia directa Palantir/Everbridge justifica apuesta grande

**Qué validar primero**: ¿Hay willingness-to-pay 50-100k € ARR? ¿O prefieren proyectos custom?

**Riesgos**:
- Obsolescencia IA rápida (LLMs mejoran 6-12 meses, arquitectura legacy tras 2 años)
- Capital intensivo (burn rate 50-80k €/mes con equipo 7 personas)
- Time-to-market largo (competidores retrofittean GenAI antes que PRISMA lanza)

**Ejemplos**: Everbridge, One Concern

**Fit fundador solo**: ❌ Imposible bootstrappear

---

### 4.2 Arquetipo B — Servicios AIOps / Ingeniería Custom

**Descripción**: Consultoría especializada soluciones resiliencia IA a medida. Cliente paga por proyecto (50-150k €), NO hay producto propio reutilizable inmediato. "Time-for-money".

**Cuándo tiene sentido**:
- Fundador solo año 1, necesita cash flow 0-3 meses (supervivencia)
- Sin financiación secured, bootstrapping puro
- Mercado prefiere custom vs plataforma estándar
- Aprender mercado "haciendo" (validar casos uso, pricing, pain points reales)

**Qué asumimos**:
- Hay demanda proyectos custom 50-100k €
- Cliente OK externalizar ejecución (fundador + freelancers)
- Fundador puede vender + entregar (dual role)

**Qué validar primero**: ¿Hay 2-3 clientes dispuestos pagar 50k € por proyecto custom 3-6 meses?

**Riesgos**:
- NO escalable (lineal: más proyectos = más tiempo fundador)
- Valoración baja exit (3-5x EBITDA típico servicios vs 8-12x ARR SaaS)
- Dependencia fundador (si fundador se va, negocio muere)
- Trampa "quedarse en consulting" (difícil transición a producto después)

**Ejemplos**: Consultoras boutique (Thoughtworks, ThoughtMachine fase inicial)

**Fit fundador solo**: ✅ Viable año 1

---

### 4.3 Arquetipo C — Híbrido Projects-to-Product (Módulos Reutilizables)

**Descripción**: Arrancar con proyectos custom (cash flow año 1), extraer módulos comunes progresivamente hacia producto SaaS (año 2-3). "Databricks model".

Inspirado ciclo vida riesgo: Vender primero **"PRISMA Detect"** (Módulo CV+LLM detección), después **"PRISMA Respond"** (Agentic AI), luego **"PRISMA Predict"** (gemelo predictivo).

**Cuándo tiene sentido**:
- Fundador solo año 1, puede conseguir 1-2 devs año 2 (grants TwIN Lab, primeros clientes funding)
- Hay tracción proyectos B2B (2-3 clientes año 1)
- Proyectos tienen patrones comunes (80% código reutilizable entre clientes)
- Fundador puede gestionar complejidad dual (servicios + producto simultáneo año 2)

**Qué asumimos**:
- Mercado acepta módulos estándar (NO necesita 100% custom)
- Puedes productizar 80% código mientras entregas nuevos proyectos
- Equipo crece orgánicamente (revenue proyectos funda devs producto)

**Qué validar primero**: ¿Proyectos cliente A y B comparten 60-80% lógica común? ¿Aceptarían módulo estándar si es 40% más barato?

**Riesgos**:
- Complejidad gestión dual (proyectos custom tiran tiempo, producto requiere foco)
- Riesgo quedarse solo en proyectos si no se disciplina tiempo producto
- Requiere habilidad "decir NO proyectos no-estratégicos" (difícil cuando necesitas cash)

**Ejemplos**: Databricks (Spark consulting → Unified Analytics Platform), Confluent (Kafka → Confluent Cloud)

**Fit fundador solo**: ✅ Viable año 1, necesita equipo año 2

---

### 4.4 Arquetipo D — Stack Modular Open-Core + Servicios

**Descripción**: Core open-source (building blocks reutilizables: connector FIWARE, módulo CV, Agentic AI framework), monetización vía **servicios profesionales** + **módulos premium** + **marketplace partners**.

Estructura capas ciclo vida:
- Capa "Detección" (open): CV básica, conectores sensores
- Capa "Respuesta" (premium): Agentic AI avanzado, integración multi-agencia
- Capa "Análisis" (premium): LLM interpretación custom, gemelo predictivo

**Cuándo tiene sentido**:
- Encuentras co-founder técnico (crítico, fundador solo NO puede mantener open-source + community)
- Puedes invertir 6-9 meses sin revenue construyendo core (grants, savings)
- Quieres ecosistema partners (FIWARE, integradores adoptan tu stack)
- Visión largo plazo (5-7 años) construir estándar europeo

**Qué asumimos**:
- Open-source atrae comunidad (devs, partners, evangelists)
- Servicios profesionales generan revenue suficiente (típico: 60-70% revenue open-core companies año 1-3)
- Puedes gestionar complejidad arquitectura modular + documentación extensa

**Qué validar primero**: ¿Ecosistema FIWARE/GAIA-X interesado en adoptar stack? ¿Partners (Tesicnor, integradores) dispuestos integrar?

**Riesgos**:
- Complejidad arquitectura inicial (módulos intercambiables requieren diseño sofisticado)
- Necesita documentación extensa + developer relations (coste oculto alto)
- Revenue año 1-2 bajo (open-source gratis, servicios tardan)
- Requiere comunidad (si NO hay adopción, fallas)

**Ejemplos**: Red Hat (RHEL), GitLab, Elastic, Confluent (Kafka open → Cloud)

**Fit fundador solo**: ⚠️ Difícil, factible con outsourcing dev PERO arriesgado (comunidad requiere credibilidad técnica founder)

---

### 4.5 Tabla Comparativa Arquetipos

| **Dimensión** | **A-SaaS** | **B-Servicios** | **C-Híbrido** | **D-Modular** |
|---------------|------------|-----------------|---------------|---------------|
| **Time to revenue** | 12-18m | 0-3m ✅ | 0-6m ✅ | 6-12m |
| **Capital necesario** | Alto (500k-1M) | Bajo (20-50k) ✅ | Medio (100-300k) | Medio-Alto (200-500k) |
| **Riesgo obsolescencia IA** | Alto ⚠️ | Bajo ✅ | Medio | Bajo ✅ |
| **Escalabilidad** | Alta (ARR) | Baja (lineal) ⚠️ | Media | Alta (ecosistema) |
| **Fit fundador solo año 1** | No ❌ | Sí ✅ | Sí ✅ | Difícil ⚠️ |
| **Valoración exit** | Alta (8-12x ARR) | Baja (3-5x EBITDA) ⚠️ | Media-Alta (6-10x) | Alta (8-12x) |
| **Alineación ciclo riesgo** | Monolítico | Custom por proyecto | Modular progresivo ✅ | Modular componentes ✅ |
| **Complejidad gestión** | Media-Alta | Baja ✅ | Alta ⚠️ | Muy Alta ⚠️ |

**Insight estratégico**: Para fundador solo sin funding, **Arquetipo C (Híbrido)** es sweet spot. Combina:
- Cash flow rápido (proyectos)
- Escalabilidad futura (productizar módulos)
- Fit ciclo vida riesgo (venta modular)
- Transición orgánica servicios → producto (Databricks model probado)

---

## 5. Análisis SWOT — Reflexión Estratégica

**(NO decisiones, SÍ mapeo fuerzas/debilidades/oportunidades/amenazas)**

### 5.1 FORTALEZAS (Internas, Controlables)

**F1. Tech Stack Único Nativo GenAI**
- PRISMA arranca 2025 con LLMs multimodales (GPT-4V, Gemini, Grok) + Agentic AI (AutoGen, LangChain) + CV state-of-the-art (YOLO, SAM) desde día 1
- Competidores (iris360, Everbridge) arquitecturas pre-GenAI (2015-2022) → retrofitting 12-18 meses
- **Ventana oportunidad** 12-18 meses construir nativo mientras otros migran

**F2. Compliance by Design (NIS2/CER/AI Act)**
- Diseño desde día 1 para compliance → auditoría, transparencia, documentación
- Competidores retrofittean compliance (coste alto, tiempo largo)
- **Messaging diferencial**: "PRISMA le ayuda cumplir NIS2" > "PRISMA tiene mejor IA"

**F3. Track Record Fundador (8 Proyectos TRL 6-8)**
- Credibilidad técnica demostrada (según memoria TwIN Lab)
- Reduce riesgo percibido buyer ("¿puede ejecutar?")
- Facilita conversaciones B2B (vs startup sin track record)

**F4. Open-Source EUPL (Auditable Sector Público)**
- Código auditable = requisito licitaciones públicas sensibles
- Competidores propietarios (Palantir, Everbridge) = caja negra
- **Argumento B2G**: "EUPL = soberanía digital europea, NO depende vendor USA"

**F5. Timing Mercado (Regulación + GenAI Madurez)**
- NIS2/CER obligan inversión 2024-2026 (forcing function)
- LLMs multimodales + Agentic AI maduros 2023-2024 (tech ready)
- Confluencia timing regulatorio + tecnológico = ventana perfecta

---

### 5.2 DEBILIDADES (Internas, Mitigables)

**D1. Fundador Solo, Sin Equipo**
- Limitación ejecución (1 persona NO escala)
- Riesgo percibido buyer ("¿y si se va/enferma?")
- **Mitigación**: Outsourcing devs freelancers + TwIN Lab network + partnerships (Tesicnor entrega, PRISMA tech core)

**D2. Sin Empresa Constituida, Sin Marca**
- Credibilidad institucional baja vs Siemens, Everbridge
- Dificulta licitaciones públicas (requisitos legales)
- **Mitigación**: Leverage TwIN Lab (marca paraguas), casos éxito rápidos B2B (credibilidad por resultados), partnership integradores (Indra vende, PRISMA entrega)

**D3. Sin Financiación Secured**
- Cash flow crítico meses 0-6
- NO puede esperar 18m time-to-market SaaS
- **Mitigación**: Bootstrappear proyectos B2B 50-100k €, grants TwIN Lab/FIWARE, modelo híbrido (cash flow proyectos → financia desarrollo producto)

**D4. Necesidad Externalizar Desarrollo**
- Calidad código riesgo (freelancers vs equipo estable)
- Dependencia terceros (disponibilidad, commitment)
- **Mitigación**: Selección rigurosa freelancers (portfolio verificado), contratos milestones claros, co-founder técnico futuro (búsqueda activa TwIN Lab network)

---

### 5.3 OPORTUNIDADES (Externas, Aprovechables)

**O1. NIS2 + CER + Sendai (Mandatos Regulatorios)**
- Energía, transporte, farma, agua OBLIGADOS invertir resiliencia 2024-2026
- Presupuestos aprobados (NO discrecionales)
- **Acción**: Messaging compliance-first, partnerships consultoras compliance (deloitte, EY auditan NIS2 → recomiendan PRISMA)

**O2. Fondos Next Generation EU (Grants 2024-2026)**
- FIWARE Open Calls: 10-170k € cascade funding
- H2020/Horizon Europe: 200k-2M € proyectos colaborativos
- TwIN Lab grants (TODO: cuantificar)
- **Acción**: Aplicar sistemáticamente Q1-Q2 2025, ¿prioridad FIWARE Powered by?

**O3. FIWARE Marketplace (Canal Europeo)**
- Visibilidad 50+ iHubs, 1000+ empresas ecosistema
- Certificación "Powered by" = señal calidad B2G
- **Acción**: Roadmap certificación 2025 (requiere conformidad NGSI-LD, tiempo estimado 3-6 meses)

**O4. PANTHEON/H2020 Partnerships (Credibilidad)**
- PANTHEON busca casos uso verticales disaster resilience
- Co-desarrollo = funding + credibilidad académica + acceso consortium
- **Acción**: Contactar PANTHEON Q1 2025, proponer caso uso "autonomous response emergencies"

**O5. Palantir/Everbridge NO Mid-Market Europa (Ventana)**
- Palantir vende mega-contratos defense/gobierno USA (5-20M €)
- Everbridge enfoque anglo (USA/UK), España mercado secundario
- **PRISMA puede dominar mid-market europeo** (50-200k € utilities/hospitals/airports) antes que bajen
- **Ventana**: 3-5 años estimado antes Palantir ataque mid-market Europa agresivamente

---

### 5.4 AMENAZAS (Externas, Monitorizables)

**A1. Palantir Bajando a Smart Cities (Horizonte 3-5 años)**
- Palantir tiene capital ilimitado, puede atacar cualquier mercado
- Señales monitorizar: Partnerships Smart Cities Europa, contratos <5M €, hiring sales Europa
- **Defensa**: Especialización vertical + velocidad (ganar 20-30 clientes antes que lleguen) + diferenciación "European, EUPL, compliance by design" vs "USA, caja negra, controversial"

**A2. Everbridge Añadiendo GenAI (12-18 meses)**
- Everbridge tiene revenue $500M, puede invertir 20-50M $ I+D GenAI
- Probable roadmap 2025-2026: LLMs interpretación alerts, Agentic AI beta
- **Defensa**: Ventana 12-18m construir nativo + ganar clientes (switching cost después)

**A3. Integradores Marca Blanca (Indra, Atos Copian)**
- Integradores podrían ver PRISMA → copiar → marca blanca licitaciones
- Riesgo especialmente si NO hay partnership formal
- **Defensa**: Partnership formal Tesicnor/Indra (revenue share, clausulas no-competencia), open-source EUPL (si copian, al menos comunidad crece), patentes clave (si viables, TODO: evaluar)

**A4. Ciclos Venta Públicos Largos (Riesgo Cash Burn)**
- B2G 12-18 meses típico → cash burn peligroso sin B2B paralelo
- Competencia desleal licitaciones (Indra/Atos lobby político)
- **Defensa**: Dual B2G/B2B OBLIGATORIO (70/30 B2B/B2G año 1-2), quick-wins B2B (estadios, hospitales privados)

**A5. Obsolescencia Rápida LLMs (Riesgo Técnico)**
- LLMs mejoran 6-12 meses (GPT-5, Gemini 2.0, modelos open-source)
- Arquitectura monolítica riesgo legacy tras 2 años
- **Defensa**: Arquitectura modular intercambiable (LLM = componente reemplazable, NO core system), tracking activo state-of-the-art (papers, benchmarks)

---

## 6. Estrategia Dual B2G/B2B — Por Qué Es Obligatorio (No Opcional)

### 6.1 Primera Verdad: GovTech Puro Es Suicidio para Startup Sin Funding

**Anatomía fracaso GovTech startup**:

```
Mes 0-6:   Desarrollo producto, certificaciones (ENS, ISO 27001) → Burn 30-50k € sin revenue
Mes 6-12:  Identificar licitación, preparar oferta técnica → Burn 30-50k € sin revenue
Mes 12-18: Licitación, evaluación, impugnaciones, adjudicación → Burn 30-50k € sin revenue
Mes 18-24: Cobro primer hito (si ganas) → Revenue FINALMENTE

Total burn: 90-150k € antes primer euro. Si NO ganas licitación (competencia Indra/Atos) → Quiebra.
```

**Por qué NO funciona**:
- CAC altísimo (150k € / cliente ganado estimado)
- Ciclos 12-18 meses (cash flow negativo imposible sin funding)
- Win rate bajo startups (Indra/Atos lobby político, pricing predatorio)
- Timing impredecible (licitación aplazada 6 meses → muerte startup)

**Excepción histórica**: Palantir tuvo 200M $ CIA antes vender comercial. No es replicable.

---

### 6.2 Segunda Verdad: B2B Privado = Validación + Cash Flow + Credibilidad

**Anatomía éxito B2B privado**:

```
Mes 0-1:   LinkedIn outreach, intro partner, reunión decision maker
Mes 1-3:   PoC 40-60k € (detección autónoma 1 caso uso)
Mes 3:     Cobro PoC → Cash flow POSITIVO
Mes 4-6:   Demostración valor PoC → Upsell proyecto completo 100-150k €
Mes 6:     Cobro proyecto → Cash flow POSITIVO acumulado 150-200k €

Total burn: 10-20k € antes primer euro. Win rate alto (50-70% si PoC funciona).
```

**Por qué SÍ funciona**:
- Ciclos cortos (3-6 meses PoC → contrato)
- Decision maker único (Director Seguridad/Operaciones vs comité licitación público)
- Willingness-to-pay alta (aseguradoras presionan, compliance NIS2, reputación)
- Casos éxito replicables (Quirónsalud → HM Hospitales → Osakidetza)

---

### 6.3 Modelo Recomendado: 70/30 B2B/B2G Año 1-2 → 50/50 Año 3+

**Año 1 (TwIN Lab) - 100% B2B Privado**:
- Target: 3-5 PoCs (40-60k € cada) = 150-250k € revenue
- Sectores quick-win: Espacios Públicos (Camp Nou, Wanda), Hospitales privados (Quirónsalud), Utilities (Iberdrola, Naturgy)
- Objetivo: Cash flow + casos éxito + aprendizaje mercado

**Año 2 - 70% B2B / 30% B2G (Indirecto vía Partners)**:
- B2B: Escalar a 8-12 clientes (100-200k € medio) = 1-1.5M € revenue
- B2G indirecto: Partnership Tesicnor/Indra → 2-3 proyectos públicos (revenue share 70/30 integrador/PRISMA) = 300-500k € revenue adicional
- Total: ~1.5M € revenue, equipo 5-7 personas

**Año 3+ - 50% B2B / 50% B2G (Directo + Indirecto)**:
- B2G directo: Track record permite licitaciones directas (credibilidad demostrada)
- Equilibrio estable

---

### 6.4 Canales de Acceso Mercado (Específicos)

#### Canal 1: Directo B2B (LinkedIn + Eventos + FIWARE Network)

**Táctica LinkedIn** (Month 1-3):
- Identificar 30 decision makers: Director Seguridad/CISO utilities, hospitales, aeropuertos, recintos
- Outreach: "Compliance NIS2 + CV autónoma emergencias → PoC 3 meses sin compromiso"
- Conversion rate esperado: 10-15% (3-5 reuniones de 30 outreach)

**Táctica Eventos** (Month 3-6):
- Smart City Expo World Congress (Barcelona, nov 2025)
- Greencities (Málaga)
- Networking TwIN Lab (empresas programa + mentores)

**Táctica FIWARE** (Month 6-12):
- Certificación "Powered by FIWARE" (credibilidad B2G)
- Listado Marketplace FIWARE (visibilidad 50+ iHubs)

#### Canal 2: Indirecto vía Partners (Tesicnor Prioritario)

**Modelo partnership Tesicnor**:
- **Revenue share**: 70% Tesicnor / 30% PRISMA (si Tesicnor vende) o inverso si PRISMA vende con intro Tesicnor
- **Qué aporta Tesicnor**: Acceso clientes públicos Navarra/Euskadi/Europa, credibilidad ingeniería, gestión proyecto, certificaciones
- **Qué aporta PRISMA**: Tech core diferenciador (CV+LLM+Agentic AI), compliance NIS2/CER by design
- **Win-win**: Tesicnor gana licitaciones con tech único, PRISMA accede B2G sin competir directo
- **Acción**: Reunión Q1 2025 presentar propuesta partnership formal

#### Canal 3: Ecosistemas FIWARE/GAIA-X (Visibilidad Europa)

**FIWARE Marketplace**:
- Certificación H1 2025 (6 meses estimado)
- Listado solución "Autonomous Situational Awareness for Critical Emergencies"
- Tracción esperada: 5-10 leads Europa/año (conversión 20-30%)

**GAIA-X Compliance**:
- Argumento venta "datos NO salen UE" (vs AWS/Azure/Palantir USA)
- Especialmente potente sectores críticos (energía, defense, farma) preocupados soberanía

---

## 7. Hipótesis Prioritarias a Validar en TwIN Lab

**Filosofía**: Este documento mapea territorio, PERO necesitamos validar asunciones con datos reales. TwIN Lab = laboratorio validación. 

### 7.1 Hipótesis Comerciales (Mes 1-3 TwIN Lab)

**H1. Sectores críticos priorizan compliance > features IA**  
✅ Validar: Conversaciones 5-8 decision makers (CISO utilities, Director emergencias hospital, Director seguridad aeropuerto)  
❓ Pregunta clave: "¿Qué es más urgente: cumplir NIS2 o tener 'mejor IA'?"  
🎯 Señal éxito: 60%+ mencionan compliance como driver #1 compra

**H2. Willingness-to-pay 40-60k € PoC 3 meses**  
✅ Validar: Presentar pricing específico en conversaciones  
❓ Pregunta clave: "¿Pagarían 50k € PoC 3 meses módulo detección autónoma?"  
🎯 Señal éxito: 40%+ dicen "sí, si demuestra ROI" o "budget disponible"

**H3. B2B privado ciclos 3-6 meses vs B2G 12-18 meses**  
✅ Validar: Preguntar timing decisión compra típico  
❓ Pregunta clave: "¿Cuánto tarda decisión PoC/contrato en su organización?"  
🎯 Señal éxito: B2B confirma 3-6m, B2G confirma >12m

---

### 7.2 Hipótesis Técnicas (Mes 3-5 TwIN Lab)

**H4. CV autónoma detecta eventos 10-100x más rápido que humano viendo dashboards**  
✅ Validar: PoC técnico con dataset real (vídeos aeropuerto/estadio + logs emergencias)  
❓ Métrica: Tiempo detección evento CV vs humano  
🎯 Señal éxito: CV detecta en <30 segundos vs humano 5-15 minutos

**H5. LLM interpreta eventos complejos mejor que alerts basados umbrales**  
✅ Validar: Comparar LLM vs sistema actual en 20-30 casos reales  
❓ Métrica: False positives, false negatives, gravedad correcta  
🎯 Señal éxito: LLM reduce false positives 50%+ vs sistema actual

---

### 7.3 Hipótesis Estratégicas (Mes 4-6 TwIN Lab)

**H6. Partnership Tesicnor acelera acceso B2G**  
✅ Validar: Reunión Tesicnor, proponer partnership, evaluar interés  
❓ Pregunta clave: "¿Integrarían tech PRISMA en proyectos? ¿Revenue share aceptable?"  
🎯 Señal éxito: Tesicnor propone 1-2 proyectos concretos donde incluir PRISMA

**H7. FIWARE Marketplace genera 5-10 leads Europa/año**  
✅ Validar: Hablar con empresas certificadas FIWARE sobre tracción real  
❓ Pregunta clave: "¿Cuántos leads genera Marketplace anualmente? ¿Conversión?"  
🎯 Señal éxito: Confirmación 5-10 leads/año, conversión 20-30%

---

### 7.4 Criterios de Pivote (Señales Ajuste Estrategia)

**Si validamos tracción proyectos B2B rápidos (H1+H2+H3)** → Explorar más **Arquetipo C (Híbrido Projects-to-Product)**  
**Si validamos interés plataforma pero NO willingness-to-pay** → Replantear pricing o pivote servicios primero (Arquetipo B)  
**Si validamos sector específico con urgencia extrema (ej: hospitales post-pandemia)** → Especializar verticalmente (solo Farma/Salud)  
**Si validamos canal indirecto fuerte (H6)** → Priorizar partnerships sobre venta directa  
**Si NO validamos nada (0/7 hipótesis)** → Replantear propuesta valor o sector target

---

## 8. Estado del Arte Tecnológico y Gaps I+D

### 8.1 Introducción: Por qué importa el "reasoning no lineal"

La promesa de PRISMA—detectar y responder a situaciones emergentes NO programadas—descansa sobre una pregunta técnica fundamental: **¿puede un sistema de IA razonar autónomamente sobre qué hacer cuando enfrenta una combinación de riesgos que nunca vio antes?**

Esta sección explora el estado del arte de las cinco tecnologías críticas necesarias, identifica dónde la tecnología actual es suficiente, y dónde necesitamos investigación adicional.

#### El Problema del Reasoning No Lineal

Los sistemas de gestión de emergencias actuales operan con **lógica programada lineal**:

```
IF sensor_temperatura > 40°C AND zona = hospital
THEN activar_protocolo_calor_extremo
```

Este enfoque funciona para situaciones **predefinidas**. Pero falla ante:

1. **Combinaciones impredecibles**: Tormenta + ciberataque SCADA + evento masivo simultáneos
2. **Patrones sutiles multimodales**: Datos RRSS + sensores + 112 que juntos revelan riesgo que individualmente no se ve
3. **Cascadas emergentes**: Efectos dominó entre dominios (clima → energía → ciber → sanitario) sin modelo previo

**PRISMA necesita "reasoning situacional no lineal"**: observar, interpretar contexto complejo, razonar sobre acciones sin workflow predefinido.

**Pregunta I+D**: ¿Existe la tecnología hoy para lograrlo? ¿Dónde están los gaps?

---

### 8.2 Componente 1: Computer Vision Autónoma para Detección sin Reglas Predefinidas

#### 8.2.1 Estado del Arte (2024)

**Tecnologías clave**:

**1. Zero-Shot Object Detection**
- **CLIP** (OpenAI, 2021): Vision-language model que entiende objetos sin training específico. Accuracy ~40-60% objetos nuevos.
- **OWL-ViT** (Google, 2022): Open-World Localization with Vision Transformers. Detecta objetos por descripción texto. Benchmark COCO: 25-35% mAP zero-shot.
- **Grounding DINO** (IDEA-Research, 2023): State-of-the-art zero-shot detection. COCO zero-shot: 52.5% AP, superior a CLIP/OWL-ViT.

**2. Vision-Language Models (VLMs) para Scene Understanding**
- **GPT-4V** (OpenAI, 2023): Multimodal GPT-4 con vision. Comprende escenas complejas, genera descripciones contextuales.
- **Gemini 1.5 Pro** (Google, 2024): Contexto 1M tokens, procesa video largo, spatial reasoning mejorado.
- **Claude 3.5 Sonnet** (Anthropic, 2024): Vision capabilities, análisis documentos/imágenes, menor alucinación que GPT-4V en benchmarks.
- **LLaVA** (Microsoft, 2023): Open-source VLM, 13B parameters, performance comparable GPT-4V en tareas específicas.

**3. Anomaly Detection en Video Streams**
- **ST-GCN** (Spatial-Temporal Graph Convolutional Networks): Detecta comportamientos anómalos en multitudes.
- **Real-time Violence Detection**: Modelos CNN+LSTM para detectar violencia/pánico en videos vigilancia (Accuracy ~85-90% benchmarks públicos).
- **Crowd Density Estimation**: CSRNet, MCNN (Multi-Column Neural Network) para estimar densidad multitudes (MAE <10 personas en videos test).

**4. Event Detection en Datos Urbanos**
- **UrbanEye** (research): Framework detección eventos urbanos integrando múltiples cámaras.
- **CitySim benchmarks**: Datasets sintéticos ciudades para entrenar detección accidentes, aglomeraciones.

#### 8.2.2 Aplicaciones Urbanas Existentes

| **Sistema** | **Organización** | **Capacidad** | **Limitaciones** |
|-------------|------------------|---------------|------------------|
| **Hikvision Smart City** | China (comercial) | Detección facial, conteo personas, análisis tráfico | Rule-based triggers, NO interpretación semántica contextual |
| **Amazon Rekognition Video** | AWS (comercial) | Detección objetos, personas, actividades en video | Requiere labels predefinidos, NO zero-shot verdadero |
| **Verkada Command** | Verkada (startup USA) | Búsqueda personas/vehículos por descripción natural | Cloud-only, limitado a búsqueda post-evento |

#### 8.2.3 Gap Analysis PRISMA

| **Capacidad Requerida** | **Estado Actual** | **TRL** | **Gap** |
|-------------------------|-------------------|---------|---------|
| Detección zero-shot objetos urbanos | Grounding DINO 52% AP | TRL 7 | ✅ Maduro |
| Scene understanding multimodal (video+audio+texto) | GPT-4V, Gemini 1.5 | TRL 7 | ✅ Maduro |
| Anomaly detection tiempo real (<5s latency) | ST-GCN, CNN+LSTM | TRL 6 | ⚠️ Latencia límite |
| Interpretación semántica "pánico incipiente" sin labels | VLMs + prompt engineering | TRL 5 | ⚠️ Requiere validación dominio |
| Fusión multi-cámara coherencia espacial | UrbanEye (research) | TRL 4 | ❌ Gap I+D |

**Conclusión CV**: Tecnología base **existe y es madura** (TRL 6-7) para detección zero-shot y scene understanding. **Gaps**:
1. **Latencia**: VLMs lentos (GPT-4V ~10-30s por imagen). Necesario: modelos edge optimizados o hybrid edge-cloud.
2. **Fusión multi-cámara**: Tracking coherente persona entre cámaras sin ID facial (RGPD). Research abierto.
3. **Validación dominio**: VLMs entrenados datos generales, NO específicos emergencias urbanas. Fine-tuning necesario.

---

### 8.3 Componente 2: LLM Multimodal para Fusión de Datos Heterogéneos

#### 8.3.1 Estado del Arte (2024)

**Multimodal LLMs**:

| **Modelo** | **Modalidades** | **Contexto** | **Spatial Reasoning** | **Coste** |
|-----------|-----------------|--------------|----------------------|-----------|
| **GPT-4o** (OpenAI) | Texto, imagen, audio | 128k tokens | Bueno (describe layouts, mapas) | $5/$15 por 1M tokens |
| **Gemini 1.5 Pro** (Google) | Texto, imagen, video, audio | 1M tokens | Excelente (procesa videos largos, analiza trayectorias) | $1.25/$5 por 1M tokens |
| **Claude 3.5 Sonnet** (Anthropic) | Texto, imagen | 200k tokens | Bueno (análisis documentos técnicos, diagramas) | $3/$15 por 1M tokens |
| **Grok 2** (xAI) | Texto, imagen | 128k tokens | Medio (menos probado spatial) | Sin pricing público |

**Spatial-Temporal Reasoning Específico**:
- **GeoLLM** (research 2024): LLM fine-tuned con datos geoespaciales, comprende coordenadas, distancias, topología.
- **UrbanGPT** (research 2024): GPT fine-tuned datos urbanos (tráfico, eventos, población). Performance 15-20% mejor que GPT-4 base en tareas urban planning.
- **CityBench** (benchmark): Dataset para evaluar LLMs en tareas urban analytics (predicción tráfico, recomendación rutas, análisis eventos).

**RAG con Datos Geoespaciales**:
- **LangChain + Vector DB (ChromaDB, Pinecone, Weaviate)**: Framework maduro para RAG. Embeddings geoespaciales via fine-tuned models.
- **PostGIS + Pgvector**: PostgreSQL extension para queries geoespaciales + vector similarity. Integración LLM+GIS.

#### 8.3.2 Límites Actuales

**1. Precisión Geoespacial**:
- LLMs generalistas (GPT-4, Gemini) cometen errores en cálculos distancia/área (~20-30% error en benchmarks GeoLLM).
- Fine-tuning con datos GIS mejora, pero requiere dataset específico (no existe público para emergencias urbanas).

**2. Latencia Fusión**:
- Fusionar sensores (100+ streams) + GIS (layers complejos) + RRSS (millones tweets) + 112 (audio transcrito) en contexto LLM = **query time 30-60s con GPT-4**.
- Gemini 1.5 Pro (1M context) permite batch completo, pero latencia similar.

**3. Alucinación en Datos Críticos**:
- LLMs inventan datos cuando no tienen info (ej: "Hospital X tiene 50 camas UCI" cuando no conoce dato real).
- Solución parcial: RAG + validation layer, pero añade complejidad.

#### 8.3.3 Gap Analysis PRISMA

| **Capacidad Requerida** | **Estado Actual** | **TRL** | **Gap** |
|-------------------------|-------------------|---------|---------|
| Fusión texto + imagen + structured data | GPT-4o, Gemini multimodal | TRL 7 | ✅ Maduro |
| Comprensión contexto urban semántico | UrbanGPT (research) | TRL 5 | ⚠️ Necesita fine-tuning |
| Spatial reasoning preciso (distancias, áreas, topología) | GeoLLM (research) | TRL 4 | ❌ Gap I+D |
| Latencia <10s fusión 100+ fuentes datos | Ninguno actual | TRL 3 | ❌ Gap I+D arquitectura |
| Validación automática facts críticos (camas UCI, capacidad) | Ninguno robusto | TRL 3 | ❌ Gap I+D |

**Conclusión LLM**: Tecnología base multimodal **madura** (TRL 7). **Gaps críticos**:
1. **Spatial reasoning preciso**: Necesita fine-tuning GeoLLM para dominio emergencias.
2. **Latencia**: Arquitectura híbrida necesaria (filtrado pre-LLM, solo queries críticos a LLM).
3. **Validación facts**: Capa intermedia RAG + knowledge graphs para evitar alucinaciones en datos críticos (capacidades hospitales, inventarios).

---

### 8.4 Componente 3: Agentic AI para Reasoning en Situaciones Emergentes NO Programadas

#### 8.4.1 Estado del Arte (2024)

**Agentic AI Frameworks**:

| **Framework** | **Mantenedor** | **Arquitectura** | **Madurez** | **Crisis Management Cases** |
|---------------|----------------|------------------|-------------|---------------------------|
| **LangChain** | LangChain Inc | Chains, agents, tools, memory | Producción (TRL 8) | Ninguno público crisis management |
| **CrewAI** | CrewAI | Multi-agent collaboration, roles, tasks | Beta (TRL 6) | Ninguno público |
| **AutoGen** (Microsoft) | Microsoft Research | Multi-agent conversations, code execution | Research (TRL 5) | Paper simulation disaster response |
| **Semantic Kernel** | Microsoft | Integration LLM+apps, plugins | Producción (TRL 7) | Uso enterprise general, NO crisis específico |
| **LangGraph** | LangChain | Graph-based agent orchestration | Beta (TRL 6) | Ninguno público |

**Multi-Agent Systems para Crisis Management (Research)**:
- **DEFACTO** (Distributed Emergency Framework): Sistema multi-agente coordinación emergencias (paper 2022). Simulaciones terremotos. TRL 4.
- **RoboCup Rescue Simulation**: Benchmark multi-agent rescue operations. Agents coordinan búsqueda, rescate, extinción fuegos. TRL 5 (simulación).

**Planning Under Uncertainty**:
- **POMDP** (Partially Observable Markov Decision Processes): Framework teórico planning con incertidumbre. Computacionalmente costoso, NO escala tiempo real.
- **Monte Carlo Tree Search (MCTS)**: Usado AlphaGo. Aplicable planning emergencias, pero requiere modelo mundo (no existe para emergencias urbanas).
- **LLM-based Planning**: Papers 2023-2024 muestran GPT-4 puede generar planes complejos via Chain-of-Thought. Accuracy ~60-70% planes válidos (benchmark HotPotQA).

**Explainable AI para Decisiones Críticas**:
- **LIME** (Local Interpretable Model-agnostic Explanations): Explica predictions modelos black-box. Aplicable post-hoc.
- **SHAP** (SHapley Additive exPlanations): Similar LIME, base teoría juegos. Más robusto.
- **Attention Maps** (Transformers): Visualiza qué tokens influyeron decisión LLM. Útil debug, menos útil explicación no-técnicos.
- **Constitutional AI** (Anthropic): LLMs entrenados con principios éticos explicables. Claude usa, mejora explicabilidad vs GPT-4.

#### 8.4.2 ¿Puede Agentic AI Actual Manejar Decisiones Vida/Muerte?

**Evidencia Positiva**:
1. **Medicina**: IBM Watson Oncology recomendaba tratamientos cáncer (descontinuado 2022 por problemas accuracy, PERO demostró viabilidad técnica).
2. **Aviación**: Autopilots toman decisiones críticas (emergency landings) bajo supervisión humana. Precedente regulatorio HITL.
3. **Military**: Sistemas autónomos defensa (CIWS Phalanx) toman decisiones letales en milisegundos. Controversial pero operativo.

**Evidencia Negativa**:
1. **Tes la FSD**: Crashes fatales autonomous driving. Muestra límites decisiones vida/muerte sin supervisión perfecta.
2. **Chatbot médicos**: Google Med-PaLM 2 accuracy ~85% diagnósticos (bueno, pero NO suficiente vida/muerte).
3. **Falta de casos uso producción**: NO existe sistema Agentic AI deployed en gestión emergencias reales (solo simulaciones/research).

**Consenso Research 2024**: Agentic AI **puede sugerir** decisiones críticas con accuracy 70-85% (comparable humano promedio en dominios acotados). **NO debe decidir solo** sin HITL. Human-in-the-Loop obligatorio sistemas alto riesgo (AI Act).

#### 8.4.3 Gap Analysis PRISMA

| **Capacidad Requerida** | **Estado Actual** | **TRL** | **Gap** |
|-------------------------|-------------------|---------|---------|
| Framework agentic AI multi-agent | LangChain, CrewAI production-ready | TRL 7-8 | ✅ Maduro |
| Reasoning LLM sin workflow predefinido | GPT-4, Claude CoT | TRL 7 | ✅ Maduro (con HITL) |
| Planning under uncertainty tiempo real | POMDP, MCTS, LLM-planning | TRL 4-5 | ⚠️ Latencia problema |
| Explicabilidad decisiones para operadores NO técnicos | LIME, SHAP, Constitutional AI | TRL 6 | ⚠️ Necesita UX adaptado |
| Casos uso producción crisis management real | Ninguno (solo simulaciones) | TRL 4 | ❌ Gap validación |
| Garantías safety decisiones vida/muerte sin HITL | Ninguno aceptable | TRL 2 | ❌ Gap fundamental (requiere HITL siempre) |

**Conclusión Agentic AI**: Frameworks **maduros** (TRL 7-8) para orquestación. Reasoning LLM **suficiente** para sugerir acciones (TRL 7) PERO **Human-in-the-Loop obligatorio**. **Gaps**:
1. **Validación dominio**: Cero casos uso producción emergencias reales. PRISMA sería pionero → necesita validación extensiva.
2. **Safety guarantees**: NO existe método formal para garantizar Agentic AI nunca sugiere acción catastrófica. HITL mitiga, pero requiere operador entrenado.
3. **Explicabilidad operadores**: LIME/SHAP técnicos. Necesita capa UX "por qué sistema recomienda X" en lenguaje no-técnico.

---

### 8.5 Componente 4: Non-Linear Cascade Modeling (Riesgos Compuestos)

#### 8.5.1 Estado del Arte (2024)

**Complex Systems Modeling**:

**1. Network Analysis para Infraestructuras**
- **CIPRNet** (Critical Infrastructure Preparedness and Resilience Research Network, EU): Framework modelado interdependencias infraestructuras críticas. Usado proyectos H2020.
- **CASCADES toolkit** (research): Simula cascadas fallos entre redes (energía → agua → transporte).

**2. Agent-Based Models (ABM)**
- **NetLogo**: Platform open-source ABM. Usado research epidemias, evacuaciones, tráfico.
- **MASON** (Multi-Agent Simulator Of Neighborhoods): Java-based ABM, escalable millones agentes.
- **Modelos epidemiológicos**: SIR, SEIR extendidos con networks (papers COVID-19 2020-2021). Predicen cascadas sanitarias.

**3. Causal Inference en Sistemas Dinámicos**
- **Granger Causality**: Tests estadísticos causalidad temporal series (X causa Y si pasado X mejora predicción Y). Limitado: asume linealidad.
- **Do-Calculus** (Pearl): Framework formal causal inference. Computacionalmente costoso, requiere grafo causal conocido a priori.
- **Neural Granger Causality** (2023): Redes neuronales detectan causalidad no-lineal. Papers muestran mejora 20-30% vs Granger clásico.

**4. Digital Twin + Physics-Informed Neural Networks (PINNs)**
- **PINNs**: Redes neuronales incorporan leyes físicas (ecuaciones diferenciales) en training. Mejoran accuracy predicción fluidos, estructuras.
- **Urban Digital Twins con PINNs**: Research 2023-2024 modela flujos tráfico, dispersión contaminantes. TRL 4-5.

**5. Risk Propagation en Infraestructuras Críticas**
- **CASCADE toolkit**: Open-source tool simula cascadas sector energía.
- **InfraRisk** (EPFL research): Framework probabilistic risk propagation. Input: grafo infraestructuras + probabilidades fallo → Output: distribución probabilidad colapso cascada.

#### 8.5.2 ¿Modelos Actuales Capturan Emergencia?

**Definición Emergencia (Complexity Theory)**: Comportamiento sistema NO predecible de propiedades componentes individuales (ej: tráfico grid-lock emerge de decisiones individuales conductores, NO predecible de reglas individuales).

**Limitaciones Modelos Actuales**:
1. **ABM capturan emergencia local** (comportamientos colectivos agentes), PERO requieren **reglas agentes definidas a priori**. Si evento nuevo (ej: ciberataque nuevo tipo), reglas NO existen.
2. **Network analysis predice cascadas conocidas** (energía → agua), PERO **NO emergencia cross-domain** (cambio climático → migración → disturbios sociales → ciberataques oportunistas). Demasiados grados libertad.
3. **PINNs mejoran accuracy física**, PERO **NO socio-técnico** (comportamiento humano bajo pánico NO sigue leyes físicas).

**Consenso Research**: Modelado cascadas **funciona dominios acotados** (energía, agua, epidemias individuales). **NO existe modelo general** cascadas multi-dominio (clima + ciber + sanitario + social) con capacidad predictiva útil.

#### 8.5.3 Gap Analysis PRISMA

| **Capacidad Requerida** | **Estado Actual** | **TRL** | **Gap** |
|-------------------------|-------------------|---------|---------|
| Modelado cascadas single-domain (energía, agua, salud individual) | CIPRNet, CASCADES, SIR/SEIR | TRL 6-7 | ✅ Maduro |
| Detección causalidad no-lineal datos temporales | Neural Granger Causality | TRL 5 | ⚠️ Necesita validación |
| Simulación ABM comportamiento multitudes | NetLogo, MASON production-ready | TRL 7 | ✅ Maduro |
| Modelado cascadas cross-domain (clima → ciber → sanitario) | Ninguno validado | TRL 3 | ❌ Gap I+D fundamental |
| Predicción emergencia (comportamientos NO programados) | Ninguno robusto | TRL 2 | ❌ Gap teoría complexity |
| Integración Digital Twin + cascade models tiempo real | Urban DT research | TRL 4 | ❌ Gap I+D |

**Conclusión Cascade Modeling**: Herramientas **maduras** para single-domain (TRL 6-7). **Gap fundamental**: modelado cross-domain multi-riesgo NO existe con accuracy útil (TRL 2-3).

**Implicación PRISMA**: NO puede **predecir** cascadas impredecibles (nobody can). PERO puede:
1. **Detectar patrones early** (LLM analiza múltiples señales correlacionadas antes cascada visible).
2. **Simular escenarios "qué pasaría si"** (ABM + known cascade models para riesgos conocidos).
3. **Aprender de eventos pasados** (memory vectorial casos históricos cascadas, pattern matching).

---

### 8.6 Componente 5: Human-in-the-Loop en Sistemas Autónomos Críticos

#### 8.6.1 Estado del Arte (2024)

**HITL Design Patterns**:

| **Patrón** | **Descripción** | **Ejemplo** | **Madurez** |
|------------|-----------------|-------------|-------------|
| **Approval Workflow** | Sistema sugiere, humano aprueba antes ejecución | Tesla FSD (humano supervisa), IBM Watson (médico aprueba) | TRL 8 |
| **Active Learning** | Sistema pide feedback cuando inseguro | reCAPTCHA, Gmail spam filter | TRL 9 |
| **Audit Trail** | Sistema ejecuta, humano audita post-hoc | Sistemas trading algorítmico | TRL 9 |
| **Confidence Threshold** | Solo ejecuta auto si confidence >X%, sino pregunta humano | Autonomous warehouse robots (Amazon) | TRL 8 |
| **Human Override** | Humano puede detener/modificar acción en curso | Emergency stop industrial robots | TRL 9 |

**Explainability for Crisis Operators (No Técnicos)**:

**Buenas prácticas UX**:
1. **Lenguaje natural**: "Sistema recomienda evacuar Sector A porque detectó aglomeración peligrosa (densidad 8 personas/m², umbral seguro 4) + reportes RRSS pánico + 3 llamadas 112 últimos 5min."
2. **Visualización contextual**: Mapa calor cámaras + overlay alertas 112 + timeline eventos últimos 30min.
3. **Niveles confianza claros**: "Confianza Alta (85%)" vs "Confianza Baja (40%) - Revisar manualmente".
4. **Acción sugerida + alternativas**: "Recomendado: Evacuar Sector A. Alternativas: (1) Redirigir flujo vía Salida B, (2) Aumentar seguridad Sector A + monitorizar."

**Ejemplos Comerciales**:
- **Palantir Gotham**: Dashboards analistas inteligencia. Visualización graphs complejos, explica por qué entidad X relacionada Y.
- **Everbridge CEM**: Alertas con contexto (mapa + afectados + recursos disponibles). Operador aprueba envío alerta.

**Trust Calibration (Cuando Confiar AI)**:

**Research (Cognitive Science + HCI)**:
- **Overtrust**: Humanos confían demasiado AI → NO supervisan → fallos peligrosos (ej: Tesla crashes FSD).
- **Undertrust**: Humanos desconfían AI correcta → ignoran sugerencias → pierden beneficio.
- **Calibrated trust**: Confiar AI cuando accuracy alto + explicabilidad clara + humano verifica.

**Métricas Trust**:
- **Reliability (%) historia**: "Sistema acertó 87% recomendaciones últimos 30 días."
- **Transparency**: Mostrar siempre razones decisión.
- **Consistency**: Decisiones similares situaciones similares (NO random).

#### 8.6.2 AI Act Compliance (Arts. 13-16)

**Requisitos AI Act Sistemas Alto Riesgo** (emergencias = Annex III alto riesgo):

| **Artículo** | **Requisito** | **Implicación PRISMA** | **Tecnología Disponible** |
|--------------|---------------|------------------------|--------------------------|
| **Art. 13** | **Transparency**: Usuarios informados que interactúan con IA | UI debe decir "Recomendación generada por IA PRISMA" | ✅ Trivial (UI label) |
| **Art. 14** | **Human oversight**: Medidas supervisión humana efectiva | Approval workflow obligatorio decisiones críticas | ✅ Design pattern maduro |
| **Art. 15** | **Accuracy, robustness, cybersecurity**: Niveles apropiados | Testing extensivo + Red Team cyber | ⚠️ Testing costoso |
| **Art. 16** | **Record-keeping**: Logs automáticos decisiones, datos input, razonamiento | Database audit trail: timestamp + input data + LLM reasoning + decisión + operador approved/rejected | ✅ Tecnología madura (PostgreSQL + logging) |

**Arquitectura Compliance PRISMA**:

```
1. Evento detectado (CV)
   ↓
2. LLM analiza → genera recomendación
   ↓
3. Sistema LOG: timestamp, input data (sensores, RRSS, 112), LLM reasoning (prompt + response), confidence score
   ↓
4. UI muestra operador: Recomendación + explicación + confidence + alternativas
   ↓
5. Operador: APROBAR / RECHAZAR / MODIFICAR
   ↓
6. Sistema LOG: decisión operador (quién, cuándo, qué), razón si rechazó
   ↓
7. Ejecución acción
   ↓
8. Sistema LOG: resultado acción, métricas impacto
```

**Auditoría Post-Evento**:
- Logs permiten reconstruir completamente decisión.
- Reguladores pueden verificar: ¿Sistema sugirió correcto? ¿Operador supervisó apropiadamente?

#### 8.6.3 Gap Analysis PRISMA

| **Capacidad Requerida** | **Estado Actual** | **TRL** | **Gap** |
|-------------------------|-------------------|---------|---------|
| Approval workflow HITL | Patrón design maduro (Tesla, IBM Watson) | TRL 8 | ✅ Maduro |
| Explicabilidad lenguaje natural decisiones | LLM-generated explanations + UX | TRL 7 | ✅ Maduro |
| Audit trail compliance AI Act | Database logging standard | TRL 9 | ✅ Trivial |
| Trust calibration (mostrar reliability histórica) | Metrics + UX design | TRL 7 | ✅ Maduro |
| UX operadores crisis (estrés alto, decisiones rápidas) | Palantir, Everbridge ejemplos | TRL 7 | ⚠️ Requiere user testing dominio |
| Training operadores uso sistema IA | Ninguno específico crisis + IA | TRL 5 | ⚠️ Gap pedagógico |

**Conclusión HITL**: Tecnología y design patterns **completamente maduros** (TRL 7-9). Compliance AI Act **arquitecturalmente trivial** (logging + approval workflow).

**Gap real**: **Cultural + training**. Operadores emergencias NO entrenados supervisar IA. Necesita:
1. **Change management**: "IA es asistente, NO reemplazo" messaging.
2. **Training program**: Simulations con sistema IA, enseñar cuándo confiar/desconfiar.
3. **User testing**: Iteración UX con operadores reales 112, bomberos, policía.

---

### 8.7 Gap Analysis Consolidado

| **Tecnología** | **TRL** | **Viabilidad PRISMA MVP** | **Gaps Críticos** | **Alternativas/Mitigación** |
|----------------|---------|---------------------------|-------------------|----------------------------|
| **CV Autónoma** | 6-7 | ✅ Alta | Latencia VLMs (10-30s), fusión multi-cámara | Hybrid edge-cloud, tracking simple sin facial recognition |
| **LLM Multimodal** | 7 | ✅ Alta | Spatial reasoning preciso, validación facts | Fine-tuning GeoLLM, RAG + knowledge graphs |
| **Agentic AI** | 7-8 | ✅ Alta (con HITL) | Validación dominio (cero casos producción crisis reales) | PoC extensivo TwIN Lab, validación operadores 112 |
| **Cascade Modeling** | 3-6 | ⚠️ Media | NO predicción cross-domain | Limitarse single-domain conocido + pattern matching histórico |
| **Human-in-the-Loop** | 8-9 | ✅ Muy alta | Cultural/training operadores | Change management, training simulations |

**Conclusión General**: **4 de 5 componentes maduros (TRL 6-9)**. Cascade modeling cross-domain es **Gap I+D fundamental**, PERO PRISMA puede funcionar **sin predicción perfecta** (detectar early, pattern matching, simular escenarios).

**Recomendación**: MVP PRISMA **técnicamente viable HOY** con tecnología existente. Riesgos principales son **validación dominio** (operadores aceptarán?) y **cultural** (cambio workflow).

---

### 8.8 Roadmap Técnico de Viabilidad

#### 8.8.1 MVP TwIN Lab (6 meses, TRL 6-7)

**Qué usar (tecnología madura)**:

| **Componente** | **Tecnología Específica** | **Justificación** |
|----------------|---------------------------|-------------------|
| **CV Autónoma** | Grounding DINO (zero-shot detection) + GPT-4V (scene understanding) | State-of-the-art, APIs disponibles, NO requiere training custom |
| **LLM Multimodal** | Gemini 1.5 Pro (1M context, mejor coste/performance) | Fusiona múltiples fuentes datos, spatial reasoning aceptable |
| **Agentic AI** | LangChain + CrewAI (multi-agent) | Production-ready, comunidad activa, ejemplos código abundantes |
| **Cascade Modeling** | **NO incluir MVP** (Gap I+D) | Limitarse detección + pattern matching casos históricos (RAG) |
| **HITL** | Approval workflow (Streamlit UI) + PostgreSQL audit logs | Rápido implementar, cumple AI Act básico |

**Arquitectura MVP**:

```
Cámaras/Sensores → Grounding DINO (detección objetos/personas)
                         ↓
                    GPT-4V (scene understanding: "¿qué pasa?")
                         ↓
                    Gemini 1.5 Pro (fusión: sensores + RRSS + 112 + GIS)
                         ↓
                    CrewAI Agent (reasoning: "¿qué hacer?")
                         ↓
                    UI Streamlit (operador aprueba/rechaza)
                         ↓
                    PostgreSQL (audit log)
                         ↓
                    Acción (mock: email, SMS via API)
```

**Scope MVP**:
- **1-2 escenarios**: Aglomeración peligrosa (estadio/aeropuerto) + Apagón eléctrico
- **Datos**: Pamplona TwIN Lab (IoT municipal + Copernicus + IDENA + mock RRSS + mock 112)
- **Validación**: Técnicos municipales + 112 Navarra (feedback cualitativo, NO despliegue producción)

**Coste Estimado MVP**:
- APIs LLM (Gemini, GPT-4V): ~€5-10k (6 meses testing)
- Desarrollo (externalized o fundador): ~€40-50k
- **Total**: €50-60k

#### 8.8.2 Versión Comercial (12-18 meses, TRL 7-8)

**Qué necesita madurar**:

1. **Latencia**: Reducir 30s → <10s
   - **Solución**: Hybrid edge-cloud (filtrado local, LLM cloud solo queries críticos)
   - **Riesgo técnico**: Medio (requiere edge devices + optimization)
   - **Alternativa**: Aceptar latencia 20-30s si clientes OK (validar MVP)

2. **Spatial reasoning preciso**:
   - **Solución**: Fine-tune GeoLLM con datos emergencias (crear dataset)
   - **Riesgo técnico**: Alto (requiere dataset etiquetado, costoso)
   - **Alternativa**: RAG con knowledge graphs infraestructuras (capacidades hospitales, rutas, etc.)

3. **Fusión multi-cámara**:
   - **Solución**: Tracking sin facial recognition (siluetas, trayectorias)
   - **Riesgo técnico**: Medio (research activo, pero soluciones parciales existen)
   - **Alternativa**: Limitarse análisis cámara individual (suficiente muchos casos uso)

4. **Validación dominio**:
   - **Solución**: PoCs pagados con 3-5 clientes early adopters (hospitales, recintos eventos)
   - **Riesgo técnico**: Bajo (técnico), Alto (comercial: encontrar early adopters)

**Arquitectura Comercial**:
- Multi-tenant SaaS (Kubernetes + PostgreSQL + Redis cache)
- Edge devices opcionales (NVIDIA Jetson para latencia <10s)
- Integraciones: APIs Everbridge, SCADA utilities, CAD policial (custom por cliente)
- Certificaciones: ISO 27001 (año 2), ENS Alto (año 2, España B2G)

#### 8.8.3 Visión I+D (24-36 meses, TRL 4-6)

**Qué requiere investigación fundamental**:

1. **Cascade Modeling Cross-Domain**:
   - **Línea I+D**: Modelar emergencia cascadas clima → ciber → sanitario con accuracy >70%
   - **Approach**: Digital twin urbano + ABM + causal inference neural networks
   - **Partnership**: Universidad (UPNA, UNAV Navarra) + H2020 consortium
   - **Output**: Paper academic + dataset público + prototipo TRL 5

2. **Garantías Safety Formal Verification**:
   - **Línea I+D**: Métodos formales verificar Agentic AI nunca sugiere acción catastrófica
   - **Approach**: Formal verification (SMT solvers) + adversarial testing red team
   - **Partnership**: Research labs AI safety (Anthropic, OpenAI, DeepMind colaboran H2020)
   - **Output**: Framework safety auditable reguladores

3. **Explicabilidad Avanzada No-Técnicos**:
   - **Línea I+D**: UX explicabilidad operadores crisis (estrés, tiempo real)
   - **Approach**: Cognitive science + HCI + user testing extensivo
   - **Partnership**: HCI labs universidades + operadores 112 multiple countries
   - **Output**: Guidelines UX sistemas IA emergencias

**Funding I+D**:
- **Horizon Europe**: Cluster 3 (Civil Security) + Cluster 4 (Digital/Industry). Typical grant: €3-5M, 15-20 partners, 36 meses.
- **CDTI**: Proyectos I+D individual empresa (TRL 4-6). Subvención 50-70% (€200-500k).
- **Partnerships académicos**: Co-funding PhD students (UNAV, UPNA). Cost: €50-80k/año per PhD (3 años típico).

---

### 8.9 Validaciones Propuestas (Boceto Experimental)

**Nota**: SIN diseño experimental completo, SOLO identificar validaciones críticas.

#### Validación 1: CV Detección Anomalías Sin Reglas Predefinidas

**Objetivo**: ¿Grounding DINO + GPT-4V detectan eventos críticos NO programados?

**Setup**:
- Dataset: 100 videos simulados/reales estadio, aeropuerto, hospital (50 con eventos críticos, 50 normales)
- Eventos críticos: Aglomeración peligrosa, persona caída, humo/fuego, comportamiento errático
- Baseline: Sistema rule-based (thresholds densidad, motion detection clásico)
- Test: PRISMA CV (Grounding DINO + GPT-4V zero-shot)

**Métrica Éxito**:
- **Recall eventos críticos**: >85% (detecta 85%+ eventos reales)
- **Precision**: >70% (70%+ alertas son eventos reales, NO false positives)
- **Latencia**: <30s por video frame

**Validación**: Operadores 112 Navarra revisan outputs, confirman utilidad.

#### Validación 2: LLM Fusión Multimodal Contexto Real Pamplona

**Objetivo**: ¿Gemini 1.5 Pro fusiona correctamente sensores + GIS + mock RRSS + mock 112?

**Setup**:
- Scenario: Tormenta intensa Pamplona (datos reales AEMET + IoT TwIN Lab)
- Input: Pluviómetros (datos reales) + nivel río Arga (mock alert) + tweets simulados pánico + transcripción 112 (simulada)
- Expected output: "Riesgo inundación zona baja ciudad (barrios X, Y) próximos 60min. Prioridad: Cerrar pasos subterráneos A, B. Alertar hospitales C, D."
- Test: LLM genera output, expertos emergencias evalúan accuracy + utilidad

**Métrica Éxito**:
- **Accuracy spatial**: 100% identifica zonas riesgo correctas (validado mapa topográfico)
- **Utilidad decisional**: >4/5 rating expertos ("recomendación útil")
- **Latencia**: <60s fusión completa

#### Validación 3: Agentic AI Recomendaciones Escenarios Sintéticos

**Objetivo**: ¿CrewAI agents generan recomendaciones sensatas SIN workflow predefinido?

**Setup**:
- 20 escenarios sintéticos multi-riesgo (combinar clima, ciber, sanitario, eventos)
- Ej: "Apagón hospital durante ola calor + evento concierto 10k personas nearby"
- Agentic AI (CrewAI + GPT-4) genera plan acción
- Panel expertos (bomberos, 112, técnicos municipales, CISO utility) evalúan cada plan

**Métrica Éxito**:
- **Expert agreement**: >70% expertos aprueban plan (rating >3/5)
- **Safety**: 0% planes con acciones peligrosas (verified manual)
- **Novelty**: >50% planes incluyen acciones NO estándar (demuestra reasoning beyond programado)

**Validación**: Iteración prompts + agents config hasta alcanzar métricas.

---

### 8.10 Referencias y Recursos Técnicos

#### Papers Clave (Estado del Arte 2023-2024)

**Computer Vision**:
1. Liu et al., "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection", *ECCV 2023*
2. Minderer et al., "Simple Open-Vocabulary Object Detection with Vision Transformers" (OWL-ViT), *ECCV 2022*
3. Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (CLIP), *ICML 2021*

**Multimodal LLMs**:
4. OpenAI, "GPT-4V(ision) System Card", 2023
5. Google, "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context", 2024
6. Liu et al., "LLaVA: Visual Instruction Tuning", *NeurIPS 2023*

**Agentic AI & Multi-Agent Systems**:
7. Wuet al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", *Microsoft Research* 2023
8. Chase Harrison, "LangChain: Building applications with LLMs through composability", 2022
9. Nair et al., "DEFACTO: A Multi-Agent Framework for Distributed Emergency Response", *IEEE Systems Journal* 2022

**Cascade Modeling & Complex Systems**:
10. Setola et al., "Managing the Complexity of Critical Infrastructures: A Modelling and Simulation Approach" (CIPRNet), *Springer* 2016
11. Eusgeld et al., "System-of-systems approach for interdependent critical infrastructures", *Reliability Engineering* 2011
12. Raissi et al., "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations", *JCP* 2019

**Human-in-the-Loop & Explainable AI**:
13. Ribeiro et al., "Why Should I Trust You?: Explaining the Predictions of Any Classifier" (LIME), *KDD* 2016
14. Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions" (SHAP), *NeurIPS* 2017
15. Amershi et al., "Guidelines for Human-AI Interaction", *CHI* 2019

**AI Act & Regulatory**:
16. European Commission, "Regulation (EU) 2024/1689 on Artificial Intelligence (AI Act)", Official Journal EU, 2024

#### Recursos Open-Source

**CV & VLMs**:
- Grounding DINO: `https://github.com/IDEA-Research/GroundingDINO`
- OWL-ViT: `https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit`
- LLaVA: `https://github.com/haotian-liu/LLaVA`

**Agentic AI Frameworks**:
- LangChain: `https://github.com/langchain-ai/langchain`
- CrewAI: `https://github.com/joaomdmoura/crewAI`
- AutoGen: `https://github.com/microsoft/autogen`
- LangGraph: `https://github.com/langchain-ai/langgraph`

**Complex Systems & ABM**:
- NetLogo: `https://ccl.northwestern.edu/netlogo/`
- MASON: `https://cs.gmu.edu/~eclab/projects/mason/`
- CASCADE toolkit: `https://github.com/CASCADE-Tools` (si disponible)

**HITL & Explainability**:
- LIME: `https://github.com/marcotcr/lime`
- SHAP: `https://github.com/slundberg/shap`

#### Benchmarks & Datasets

- **COCO** (object detection): `https://cocodataset.org/`
- **CityBench** (urban analytics LLMs): Research dataset, buscar papers recientes
- **RoboCup Rescue Simulation**: `https://rescuesim.robocup.org/`

#### APIs Comerciales (Pricing 2024)

| **Servicio** | **Provider** | **Pricing** | **Use Case PRISMA** |
|--------------|--------------|-------------|---------------------|
| GPT-4V | OpenAI | $10/$30 por 1M tokens | Scene understanding imágenes |
| Gemini 1.5 Pro | Google | $1.25/$5 por 1M tokens | Fusión multimodal (mejor coste/performance) |
| Claude 3.5 Sonnet | Anthropic | $3/$15 por 1M tokens | Reasoning + explicabilidad |
| Grounding DINO | Self-hosted (GPU) | ~$100-200/mes GPU cloud | Zero-shot object detection |

---

## 9. Preguntas Sin Respuesta (Guía Descubrimiento)

**(Honestidad intelectual: Lo que NO sabemos aún)**

### 9.1 Sobre Mercado

- ❓ ¿Utilities españolas tienen presupuesto NIS2 específico aprobado 2025? ¿Cuánto?
- ❓ ¿Hospitales privados compran tech resiliencia directamente o via consultoras IT (Everis, Accenture)?
- ❓ ¿Aena centraliza decisiones IT en Madrid o cada aeropuerto decide?
- ❓ ¿Recintos eventos (Camp Nou, Wanda) renuevan contratos seguridad anualmente o multi-año?
- ❓ ¿Hay más startups europeas (FR, DE, UK) atacando mismo white space que NO hemos identificado?

### 9.2 Sobre Tech

- ❓ ¿Qué LLM multimodal tiene mejor ratio costo/rendimiento emergencias? (GPT-4V vs Gemini vs Grok vs Claude)
- ❓ ¿Framework Agentic AI más maduro? (LangChain vs AutoGen vs Custom)
- ❓ ¿Latencia aceptable respuesta autónoma? (clientes OK con 30 segundos? o necesitan <10s?)
- ❓ ¿Integración sistemas legacy (SCADA, 112, CAD policial) complejidad técnica alta? ¿Quién hace integración (PRISMA o cliente)?

### 9.3 Sobre GTM

- ❓ ¿Revenue share típico partnerships integradores? (70/30? 60/40? Depende quién vende?)
- ❓ ¿Certificaciones críticas para B2G España? (ENS Alto suficiente? Necesitan más?)
- ❓ ¿Tesicnor tiene pipeline proyectos Q1-Q2 2025 donde incluir PRISMA ya?
- ❓ ¿Cuánto cuesta certificación FIWARE "Powered by"? (time + money)

---

## 10. Conclusión — Recomendaciones Accionables TwIN Lab

### 10.1 Modelo Negocio Recomendado (Basado en Análisis)

**Arquetipo C (Híbrido Projects-to-Product)** es sweet spot para fundador solo fase actual:

- **Año 1 (TwIN Lab)**: 3-5 proyectos B2B custom (40-60k € PoCs) → 150-250k € revenue → Cash flow + casos éxito
- **Año 2**: Productizar módulos comunes ("PRISMA Detect", "PRISMA Respond") + continuar proyectos (70% tiempo producto, 30% proyectos) → 1-1.5M € revenue → Contratar 2-3 devs
- **Año 3**: Producto SaaS modular + proyectos enterprise → 2-3M € revenue → Equipo 5-7 personas

**Rationale**:
- Minimiza riesgo (cash flow mes 3-6, NO esperar 18m)
- Maximiza aprendizaje (proyectos custom enseñan pain points reales)
- Path escalabilidad (productizar módulos probados en proyectos)
- Fit ciclo vida riesgo (venta modular alineada con framework)

---

### 10.2 Sectores Target Prioridad (Q1-Q2 2025)

**Tier 1 (ataque inmediato)**:
1. **Espacios Públicos/Eventos** (ciclo 3-6m, willingness-to-pay alta, quick-win)
2. **Farma/Salud privado** (Quirónsalud, HM → ciclo 4-6m, urgencia alta)

**Tier 2 (explorar paralelo)**:
3. **Energía utilities** (ciclo 6-9m, regulación NIS2 empuja)
4. **Transporte** (aeropuertos medios → ciclo 6-9m)

**Postponer año 1**:
- Defensa (requiere credenciales + integradores)
- Alimentación (menos urgencia)
- B2G directo (requiere track record)

---

### 10.3 Acciones Concretas Mes 1-3 TwIN Lab

**Semana 1-2: Refinamiento propuesta valor**
- Presentar 3-4 value propositions variantes a mentores TwIN Lab
- Iterar messaging (compliance-first vs tech-first)
- Definir propuesta valor final

**Semana 3-6: Conversaciones descubrimiento (5-8 targets)**
- Energía: 2 conversaciones (Iberdrola, Naturgy contacts via LinkedIn/TwIN Lab)
- Farma: 2 conversaciones (Quirónsalud, hospital público via TwIN Lab network)
- Eventos: 1 conversación (recinto IFEMA, organizador eventos)
- Transporte: 1 conversación (aeropuerto medio, contact vía?)
- Agua: 1 conversación (Canal Isabel II)

**Semana 7-12: PoC técnico demo**
- Dataset: Vídeos aeropuerto/estadio (público o generado)
- Demo: CV detecta aglomeración → LLM interpreta → Alerta mock Agentic AI
- Output: Video demo 3-5 min para mostrar conversaciones

**Mes 3: Decisión pivote o persevere**
- Evaluarsist hipótesis validadas (¿4/7+?)
- Si SÍ → Continuar Arquetipo C, buscar primeros 2 PoCs pagados
- Si NO → Pivotar propuesta valor o sector

---

### 10.4 KPIs Cualitativos TwIN Lab (NO rigidos, SÍ orientativos)

- ✅ **5-8 conversaciones discovery** con decision makers reales
- ✅ **2-3 "quiero probar esto"** señales interés real (no solo cortesía)
- ✅ **1 partner potential** (Tesicnor o similar) conversación avanzada
- ✅ **Demo técnica funcional** (video 3-5 min)
- ✅ **1-2 PoCs pipeline** (50%+ probabilidad cerrar Q2 2025)

---

## 11. Epílogo — Verdades Fundamentales (Chamath Mode)

Este análisis reveló **5 verdades invariantes** sobre el mercado resiliencia/emergencias:

**1. Innovación IA > Velocidad Adoption Legacy**  
→ Los que construyen nativo GenAI 2024-2025 tienen ventana 12-18 meses antes retrofitting competidores. NO es permanente, PERO es real.

**2. Regulación = Forcing Function > Product-Market Fit**  
→ NIS2/CER obligan inversión. Sectores críticos compran "mitigación riesgo legal" disfrazado de "tech". Compliance messaging > Features IA.

**3. Especialización Vertical paga 2-3x > Plataforma Horizontal**  
→ Inversores financian Bentley ($5B infra civil), Everbridge ($3B emergencias), NO "otro IoT dashboard". PRISMA debe especializarse "Autonomous Response Emergencies" vs "Smart Cities genérico".

**4. Dual B2G/B2B NO opcional, ES supervivencia**  
→ GovTech puro = suicidio cash flow sin funding. B2B privado = validación + cash flow + credibilidad → ENTONCES B2G. Secuencia importa.

**5. Efectos Sistémicos: Si IA autónoma escala emergencias, ¿qué cambia?**  
→ Coordinadores emergencias actuales (112, CISO, directores seguridad) pasan de **operadores a supervisores**. Agentic AI decide, humano audita. Resistencia cultural previsible ("IA NO puede decidir evacuar edificio"). PRISMA debe gestionar change management, NO solo tech.

---

**Fin del Mapa de Exploración. Siguiente paso: Validar hipótesis en campo.**

