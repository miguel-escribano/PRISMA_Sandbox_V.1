# PRISMA - Resumen Ejecutivo

## 🎯 Información básica

**Nombre proyecto**: **PRISMA** (Pamplona Resilient & Intelligent Situational Multirisk Agent)  
**Nombre empresa futura**: **RESILIA**  
**Fundador**: Miguel Escribano  
**Estado**: MVP a desarrollar en TwIN Lab  
**Programa TwIN Lab**: 2 o 3 (Desarrollo de prototipo/Validación técnica en entornos reales)

---

## 🚨 El problema

Las ciudades enfrentan **riesgos en cascada sistémicos** donde un evento inicial (ola de calor, inundación, apagón) provoca fallos encadenados en múltiples sectores en efecto dominó:

- Ola de calor → cortes eléctricos → aglomeraciones → colapsos hospitalarios
- En Navarra: 80M€ en pérdidas por desastres en dos décadas (Consorcio de Seguros)
- **Puntos ciegos** en interpretación y comunicación de emergencias retrasan decisiones vitales
- Contradicen Directriz de resiliencia (UE) y Marco Sendai (ONU)

**Necesidad**: Soluciones de inteligencia situacional que fusionen alertas tempranas, datos abiertos, streams en tiempo real (IoT, RRSS, 112) para evaluar impacto en cascada y coordinar respuestas rápidas.

---

## 💡 La solución

**PRISMA** es una **aplicación vertical FIWARE-compliant** basada en microservicios y **agentes IA híbridos (GenAI + Agentic AI)** para orquestar Inteligencia Situacional (detectar-comprender-actuar).

### Proceso

1. **Ingesta de datos**: IoT, Copernicus, IDENA, RRSS, 112
2. **Transformación**: Semántico-espacial en modelos geovectoriales interoperables (Geo 3D, ArcGIS, Thinking City)
3. **Analítica de riesgos**: Tiempo real, probabilidades y cascadas de impacto, dashboards
4. **Acción**: Sugerencia y activación (PAMRI, avisos push/SMS, control semafórico)
5. **Comunicación multimodal**: Texto, voz, imagen adaptada al usuario vía context broker
6. **Auditoría completa**: Cumplimiento AI Act

### Principios de los agentes

- **Lifecycle Aware & Role Aligned**: Adaptación a fases DRR y roles
- **Empathy by Design**: Interfaces claros, lógica explicable
- **Human in the Loop & Trust**: Usuario modifica recomendaciones con trazabilidad

### Alineación

- Marco de Sendai y UNDRR "Early Warnings for All"
- Interoperabilidad multirriesgo

### MVP

Enfoque en riesgos **hidro-meteorológicos** (inundaciones, tormentas) o **tecnológicos**, según datos del Gemelo Digital de Pamplona.

---

## 🔥 Caso de uso: Apagón prolongado

1. **🚨 Detección**: Picos en APIs Red Eléctrica, reportes RRSS, caída nodos críticos
2. **🧭 Confirmación**: Fusiona datos urbanos, topográficos (LiDAR), meteo, población vulnerable
3. **🧠 Inteligencia situacional**: Capas interactivas de hospitales sin luz, gasolineras cerradas, tráfico irregular, riesgo incendios
4. **🧩 Recomendación y acción (Human-in-the-loop)**:
   - Fortalecer rutas acceso centros sanitarios
   - Regular tráfico
   - Activar generadores en nodos críticos
   - Difundir alertas segmentadas (SMS, app, radio)
   - Operador humano valida cada recomendación
5. **📈 Aprendizaje situacional**: Registra, audita (AI Act), genera informe postevento, almacena en memoria vectorial

---

## 🚀 Innovación disruptiva

1. **Enfoque DRR integral**: Todo el ciclo de gestión del riesgo (análisis, planificación, respuesta, reconstrucción) y cadena de valor del dato
2. **IA activa y multicapas**: Agentes cognitivos + simulación + flujos IoT (Niveles 4-5, no solo reactivo-contextual 1-2)
3. **Interoperabilidad abierta**: Estándares CAP y NGSI-LD, integración fluida con sensores, redes europeas alerta, ecosistema FIWARE
4. **Coordinación automática**: Respuestas ante riesgos compuestos (tormenta → apagón → fallo hospitalario) - pasa de herramienta analítica a actor operativo
5. **AI-as-a-Service**: Capacidad avanzada en nube, elimina barreras económicas/técnicas, viable para ciudades medianas

---

## 🛠️ Tecnologías clave

1. **IA distribuida**: LLM (GPT, Mistral) orquestan agentes con roles (alerta, análisis, comunicación) + supervisión humana + trazabilidad
2. **Automatización**: Processing Engines (Flink/Spark/LangChain/TensorFlow), CEP (Perseo), grafo de prompts/agentes
3. **Interoperabilidad**: FIWARE, NGSI-LD, CAP
4. **Datos externos**: CH Ebro, AEMET, Copernicus → contextos activos de riesgo
5. **Visualización**: Dashboards y mapas interactivos (perfiles técnico, operativo, analítico)
6. **Comunicación multicanal**: Protección Civil, población general, RRSS (tono, urgencia, formato adaptados)
7. **Seguridad**: AI Act, ENS, GDPR (cifrado, control accesos, registro decisiones)
8. **Memoria y resiliencia**: Memoria vectorial (ChromaDB), aprendizaje continuo, recuperación ante fallos

---

## 🎯 Mercado objetivo

### B2G (GovTech y Territorios Resilientes)
- CCAA, municipios (estrategias EDIL), Protección Civil
- Confederaciones Hidrográficas, Defensa, FSE
- Infraestructuras críticas, sanidad, transporte, educación, servicios sociales
- Buscan: Resiliencia multirriesgo, cumplimiento NIS2, CER 2022/2557, Sendai

### B2B/B2B2G
- Energía, ciclo integral del agua, ESCO
- Industria/alimentación, sanidad, finanzas, turismo, comercio
- Aseguradoras
- Protección de activos frente a riesgos climáticos, ciberataques, operativos

### R+D/Innovación
- Organizaciones internacionales, centros investigación, universidades
- Soluciones GDTs, acceso a financiación R+D

### Tamaño de mercado
- **Mercado español ciudades inteligentes**: 1B€/año (200+ ciudades Agenda2030 + Plan EDIL)

---

## 💰 Modelo de negocio

- **Tipo**: SaaS cloud-native (FIWARE, NGSI-LD, CAP)
- **Pricing**: Pay-as-you-grow adaptado a presupuestos municipales y fondos europeos
- **Licencia**: EUPL (código abierto) → fomenta innovación abierta, auditorías AI Act
- **Certificación**: FIWARE "Powered by" → entrada mercados europeos (Italia, Portugal)

### Proyección 3 años (RESILIA)
- **15 ciudades + 10 utilities**
- **750k€/año**
- **6-10 empleos técnicos**

---

## 👥 Equipo

### Fundador: Miguel Escribano

**Experiencia (20 años)**: Integración tecnologías y servicios sector público/privado (ciudades e industrias)

**Últimos 10 años**: Especialización IoT, liderando soluciones con:
- SAP, Intel, Suez, US EPA, WHO, UNEP, Acciona, World Athletics

**Financiación asegurada**: €4.5M+ para inversión y desarrollo sistemas IoT/SaaS

**Premios**: Airlab 2023, US EPA 2019 (precisión sensores)

**Publicaciones**: Co-autor en sensores eventos deportivos, mapas calidad del aire, gemelos digitales Smart City/Smart Port

**Otros**:
- Miembro CEN/TC 264 (estándares técnicos europeos)
- Experiencia en gestión propuestas, consorcios, pilotos con administraciones
- Plan de negocio Early Warnings con requisitos SaaS alineados NGSI-LD
- Director RevOps: Ingresos multiplicados x15, facturando >10M€ en SaaS/IoT
- Presentaciones: COP25, Asamblea UNEP, Smart City Expo World Congress, +15 conferencias

### Experiencia documentada (8 proyectos TRL 6-8)

**Track record demostrable** con nivel de madurez tecnológica alto:

1. **Red híbrida calidad del aire** (España) - TRL 7
   - Mapeo urbano con sensores y estaciones oficiales

2. **World Athletics Clean Air Project** - TRL 8
   - Despliegue ambiental en maratones y estadios con interfaz digital, visualizaciones 3D
   - Cliente: World Athletics (organismo internacional)

3. **SOCIO-BEE** (H2020) - TRL 6
   - Plataforma ciudadana para mapear calidad del aire con sensores móviles
   - Proyecto Horizon 2020 (financiación europea)

4. **Puerto de Palma** (APB) - TRL 8
   - Gestión integrada de activos portuarios con visor geoespacial
   - Cliente: Autoridad Portuaria de Baleares

5. **Monitorización ambiental Albacete** - TRL 8
   - Red de sensores y pantallas LED informativas en vía pública
   - Cliente: Administración municipal

6. **SCADA municipal Rivas Vaciamadrid** - TRL 8
   - Integración de datos ambientales en SCADA municipal
   - Cliente: Ayuntamiento

7. **Ortelium** - TRL 7
   - Integración de sensores y observaciones ciudadanas para respuesta ambiental

8. **Tesicnor** (en desarrollo) - TRL 7
   - Redacción de SRD para SaaS de alertas tempranas ante riesgos climáticos

**Resumen**: 5 proyectos en producción (TRL 8), experiencia con administraciones públicas, organismos internacionales y proyectos H2020.

### Estado actual del proyecto
- **Proyecto personal de inteligencia situacional** (PRISMA - aún sin empresa constituida)
- **Fundador trabajando como consultor independiente**
- **Participación individual en TwIN Lab** (20-30h semanales, autofinanciado)
- **Objetivo**: Validar MVP funcional + decidir si crear empresa RESILIA o buscar socios
- **3 colaboradores "shadow"** (potenciales co-fundadores si se constituye empresa):
  - Experto en comunicación de emergencias
  - Experto en interfaces de usuario IA
  - Experto en sistemas Early Warning Climáticas

### Capacidades actuales
- **Criterio de producto**: SRD de SaaS ambiental y sistema multiriesgos agentico
- **Gobernanza de datos**
- **Experiencia operativa**: >1,000 estaciones IoT "FIWARE ready" alimentando GDTs (puertos, minería, smart cities)
- **Kit no-code**: Notion, Zapier, n8n, CrewAI, LLMs habituales (prototipar flujos, dashboards, agentes conversacionales)
- **Herramientas de uso diario**: CRM/ERP (gestión de relaciones con clientes y recursos)
- **Herramientas de uso ocasional**: Canva/Figma (diseño), Mailing (campañas email), RRSS, SEO
- **Capacidades técnicas**: Python (MLOps - Machine Learning Operations), IoT (despliegue y gestión)

### Necesidades
- **Ayuda técnica intensiva**
- **Recursos para inferencia y posible entrenamiento/afinar modelos**
- **Partners técnicos**: Python + microservicios, DevOps, CesiumJS
- **GPU cloud o cluster local**

---

## 🤝 Partners y colaboraciones (propuestas)

### 1. Núcleo técnico
- **TRACASA Instrumental**: Sandbox TwIN, broker Orion-LD, IDENA
- **112 Navarra / SOS Navarra**: Validación operativa CECOPI, protocolos reales
- **FIWARE Foundation**: Certificación, Marketplace, eventos
- **JAKALA o similar**: Consultoría IA, UX

### 2. Validación sectorial
- **Complejo Hospitalario de Navarra**: Piloto blackout, brotes sanitarios
- **Subestación Tajonar (Iberdrola)**: Escenarios apagón, ciber-intrusión
- **NASERTIC / CPD Gobierno**: Telemetría TIC crítica, riesgos ciber-operacionales
- **EDAR Arazuri y ETAP Eguíllor**: Incidentes agua y saneamiento
- **Mercairuña**: Seguridad alimentaria crisis prolongadas

### 3. Escalado y proyección
- **Professor Octopus AI Lab**: Módulos LLM, visualización 3D avanzada
- **UNDRR Europe**: Alineación "Early Warnings for All"
- **TESICNOR**: Patrones multirriesgo listos para despliegue

### 4. Adopción social y continuidad
- **Cruz Roja, DYA, Voluntarios Protección Civil**: Logística humanitaria, ejercicios campo
- **Navarra Televisión**: Difusión masiva alertas, refuerzo marca

---

## 🌍 Impacto y sostenibilidad

### Ambiental
- Resiliencia climática: Pronósticos hidrometeorológicos + datos satelitales + sensores locales
- Anticipar: Inundaciones, olas de calor, episodios mala calidad del aire
- Alineación: Directiva 2024/2881, "Early Warnings for All"
- Optimización dinámica tráfico → movilidad baja en carbono, reduce emisiones
- Despliegue: Nube con energía renovable, algoritmos eficiencia energética

### Social
- Protege servicios esenciales y población vulnerable (riesgos tecnológicos, ciber-operacionales, seguridad pública + climáticos)
- Alertas: WCAG 2.2, lenguaje claro, canales multilingües
- Prioriza colectivos sensibles: Mayores, infancia, turistas
- GDT → transparencia, participación ciudadana, confianza

### Económica y gobernanza
- Modelo SaaS pay-as-you-grow: Sin inversiones iniciales elevadas, adaptado a cualquier tamaño de ciudad
- Código abierto (EUPL): Ecosistema local innovación, auditorías AI Act, CER 2022/2557, NIS2
- Estrategia datos/procesos: ENS Alto, ISO 22301 (continuidad operativa, trazabilidad, gobernanza responsable)

### Valor público
- Dota al GDT de Pamplona de capa de inteligencia situacional
- Cubre 4 escenarios críticos: Inundación, calor extremo, black-out eléctrico, ciberataque OT
- Pasa de datos dispersos a órdenes CAP verificables
- MVP funcional en 6 meses (con ayuda adecuada)
- Métricas: Tiempo de alerta, reducción de daños, aceptación social
- Referencia para otros territorios

---

## 💼 Recursos comprometidos

### Fundador
- **Dedicación**: 20-30h semanales (autofinanciado)
- **No necesita**: Apoyo en estrategia
- **Supervisión**: Desarrollo producto, PoCs (formación datos/IA)

### Externalizaciones
- **Tareas técnicas**: Compatibilidad, normativas, ciberseguridad (proveedores homologados SCD)

### Próximos pasos inmediatos
- **Ronda de inversión**: Red de VCs GovTech y GreenTech
- **Pruebas pagadas**: Utilities y ambientales (algunas usuarias FIWARE)
- **Contrataciones**: Post Demo Day
- **Participación**: CEIN Navarra (ya ha participado antes)
- **Herramientas**: Notion, Zapier, n8n, CrewAI
- **Verano**: Pruebas con datos locales

---

## 📅 Objetivos temporales

### 6 meses (en TwIN Lab)
- MVP funcional fusionando IoT, Copernicus, RRSS, ciencia ciudadana
- Validación con técnicos municipales
- Métricas de impacto documentadas

### 1 año
- Validado en GDT de Pamplona
- Primeras réplicas en proceso
- Certificación FIWARE "Powered by"
- Primeros clientes piloto

### 18 meses
- Replicación a otros municipios y regiones RETECH

### 2-3 años (RESILIA)
- 15 ciudades + 10 utilities
- 750k€/año
- 6-10 empleos técnicos
- Federaciones con GDTs para soluciones transfronterizas

---

## 🎓 Relación con TwIN Lab

### Lo que aporta TwIN Lab
- Broker FIWARE
- Sandbox de datos (tráfico, emisiones, LiDAR, Copernicus)
- Acompañamiento metodológico
- Acceso a plataforma GDT Pamplona
- Partners técnicos locales
- Demo Day (inversores, socios FIWARE)

### Lo que PRISMA aporta al programa
- Caso de éxito FIWARE de alto impacto (inteligencia situacional multirriesgo)
- Demostrador replicable para otros territorios
- Palanca de emprendimiento (de consultoría ad-hoc a producto SaaS validado)
- Contribución al ecosistema RETECH con solución exportable
- Alineación con objetivos UE: Resiliencia, seguridad, soberanía digital

---

**Última actualización**: 2025-11-09 (añadido análisis EIC 2026)  
**Fuente**: Propuesta aceptada TwIN Lab - PRISMA, EIC Work Programme 2026

---

## EIC 2026 — Recomendación Ejecutiva

**Programa EIC más relevante**: **Ruta dual: EIC Transition (corto plazo 2025-2026) → EIC Accelerator Challenge V.2.5 "Deep Tech for Climate Adaptation" (medio plazo 2026-2027)**

**Justificación**: PRISMA representa **encaje perfecto con EIC** por múltiples factores convergentes: (1) **TRL 4-5** (MVP en desarrollo en TwIN Lab, objetivo TRL 6 en 6 meses) ideal para EIC Transition que financia validación y demo en entorno relevante, (2) **GovTech/Climate deep tech** con inteligencia situacional multirriesgo usando **agentes IA híbridos (GenAI + Agentic AI) + FIWARE Context Broker** = innovación más allá estado del arte que EIC busca, (3) **Challenge V.2.5 Climate Adaptation** menciona explícitamente "flood and coastal protection, predictive systems, early warning systems" — exactamente lo que hace PRISMA con coordinación automática riesgos compuestos alineado con **UNDRR "Early Warnings for All"**, (4) **Track record fundador verificado** (Miguel Escribano: 8 proyectos TRL 6-8, €4.5M+ funding asegurado, experiencia SAP/Intel/Suez/WHO/UNEP, premios Airlab 2023, US EPA 2019) reduce significativamente riesgo percibido por evaluadores EIC, (5) **FIWARE-native desde diseño** (certificación Powered by planificada 2026) habilita ruta Fast Track EIC Accelerator sin Short Application. **Alineación estratégica adicional**: EIC busca conectar startups con **Mission on Climate Adaptation** (400+ regiones EU) via Business Acceleration Services — PRISMA ya diseñado para B2G (ciudades, utilities, protección civil) con pilotos GDT Pamplona confirmados.

**Prioridad de acción**: **Máxima** (proyecto FIWARE-compliant con fundador experimentado + mercado validado B2G + tecnología diferenciada IA agéntica). **Bloqueos críticos inmediatos**: (1) ⚠️ **Constituir empresa RESILIA Q1 2025** — EIC requiere SME establecida (consultor independiente no elegible), (2) **EIC Transition requiere proyecto previo elegible** (EIC Pathfinder, H2020 relevante) que PRISMA no tiene → **Solución: Fast Track desde FIWARE** (proyectos TwIN Lab son FIWARE-based, elegibles para Fast Track si Open Call exitosa). **Timeline recomendado óptimo**: (1) **Q1 2025** → Constituir RESILIA (SL recomendado), completar MVP TRL 4-5 en TwIN Lab, (2) **Q2-Q3 2025** → Solicitar **FIWARE Open Call** (€50-200k equity-free, Smart Cities/IoT), desarrollar pilotos GDT Pamplona + 112 Navarra, (3) **Q4 2025-Q1 2026** → Obtener **certificación FIWARE Powered by**, validación CECOPI operativa, 3-5 cartas intención ayuntamientos/utilities, (4) **Q2-Q3 2026** → Aplicar **EIC Accelerator Challenge V.2.5 vía Fast Track** (salta Short Application), pitch panel expertos con demo funcional. **Cut-offs EIC Accelerator 2026**: 7 ene, 4 mar, 6 may, 8 jul, 2 sep, 4 nov → objetivo batch Q2-Q3 2026 (may/jul). **Grant potential total**: €50-200k (FIWARE) + €2.5M (EIC grant) + €1-10M (EIC equity opcional, evaluar dilución). **Business Acceleration Services EIC**: Acceso automático (1) coaching intensivo 12+ días/año, (2) €60k co-funding servicios ecosystem partners, (3) €60k support pilotos con compradores públicos/privados, (4) network 400+ regiones Mission Climate Adaptation para scaling, (5) corporate matchmaking utilities/ciudades EU. **Documentación crítica preparar**: Business plan robusto internacional, lifecycle assessment solución, regulatory compliance strategy (AI Act, ENS Alto, GDPR, NIS2), IP protection strategy (código EUPL ya definido), evidencias tracción B2G (cartas ayuntamientos críticas).

