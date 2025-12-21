# PRISMA Pitch Deck

**Tagline:** Multi-Source Risks. Single Point of Foresight.  
**Duration:** 7 minutes (5 min pitch + 2 min demo)  
**Last updated:** 2025-12-21

---

## Slide 1: The Pattern That Repeats

**Visual:** Cascade events amplify risks

### Same pattern:
- **Valencia 2024:** Rain. Late Alert. 220 dead.
- **Maui 2023:** Wildfire. Sirens silent. 101 dead.
- **Texas 2021:** Heatwave. Grid collapse. 700 dead.
- **Colonial 2021:** One hack. Pipeline paralysed.

### Same problem:
- **Data existed.**
- **Connection didn't.**
- **Intelligence didn't.**

### Narrative (30 seconds)

Valencia, October 2024. AEMET issued a red alert. Eight hours later, 220 people were dead. The data existed. The connection didn't.

The pattern repeats everywhere: Maui's sirens never sounded. Texas froze while the grid collapsed. Colonial Pipeline showed how one cyberattack paralyzes half a country's fuel.

These aren't isolated failures. They're **cascade events**—where one trigger amplifies through interconnected systems.

**The problem isn't the lack of data. It's that no one connects it in time.**

---

## Slide 2: We Can Do Better

**Subtitle:** NIS2 and CER will be mandatory for critical infrastructure in 18 months

### Current process vs With Situational Intelligence

| | Data Setup | Data Transformation | Resolution | Result |
|---|---|---|---|---|
| **Good luck using current process** | Data Silos | No cascade prediction | Improvisation under pressure | Losses. Delays. Lives at risk. |
| **With Situational Intelligence** | Real-time fusion. | Coherent snapshots. OODA framework. | AI + human early coordination. | Time advantage. Any data manegeable. Any city scalable. |

### Narrative

In 18 months, NIS2 and CER will be mandatory for critical infrastructure. Those without anticipation capability will be out of compliance.

But the real cost isn't the fines. It's arriving late when it matters.

**"Doing nothing" is no longer the safe option.**

---

## Slide 3: And Now, ReArming Europe

**Visual:** US-EU tension, geopolitical shift

### Context:
- Trump and MAGA tech are launching a cold war with Europe.
- EU's critical infrastructure data is at US clouds.
- NIS2, CER, AI Act, ReArm Europe are shaping our capacities and markets.

### The question:

> When we need security intel, do we rent it from Palantir, AWS, Everbridge...?  
> **Or shall we build?**

### Narrative

Palantir. Microsoft. AWS. Google.

These are the options today. Excellent technology. But when Musk calls for abolishing the EU after a €140M fine... when geopolitics shift overnight... do we want our emergency response dependent on decisions made in Palo Alto?

NIS2, CER, AI Act, ReArm Europe—these aren't bureaucracy. They're Europe saying: **we need our own capability.**

The question isn't whether we need situational intelligence. It's whether we build it ourselves or rent it from someone else.

---

## Slide 4: The Utopia

**Subtitle:** Situational Intelligence for Critical Infrastructures and Cities

### Six pillars:

- **European** | EU data residency. No foreign dependencies.
- **Interoperable** | FIWARE native. Connects to what you already have.
- **Intelligent** | Anticipates cascades, doesn't just alert.
- **AI Safe** | Human-in-the-loop. AI Act compliant.
- **Multirisk** | Any threat. Snapshot & Parallel detection. No silos.
- **Evolving** | Agile development. Speed of iteration.

### Narrative

This is the vision: European situational intelligence. Interoperable, intelligent, safe, multirisk, and evolving at the speed we need.

**IMPORTANT:** PRISMA is NOT mentioned in this slide yet.

---

## Slide 5: PRISMA — Intelligence-as-a-Service

**Visual:** Three core outputs

```
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│   PRIORITIZED       │  │   TRACEABLE         │  │   RECOMMENDED       │
│   ALERT             │  │   EXPLANATION       │  │   ACTIONS           │
│                     │  │                     │  │                     │
│ "Traffic Cascade    │  │ "Based on these     │  │ "We suggest         │
│  risk detected.     │  │  5 indicators,      │  │  activating         │
│  Probability: 87%"  │  │  snapshot 14:32"    │  │  protocol X,        │
│                     │  │                     │  │  alerting Y"        │
│ No noise.           │  │ Auditable.          │  │ Human decides.      │
│ Only what matters.  │  │ AI Act awareness.   │  │ Always.             │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
```

### Narrative

PRISMA doesn't replace what you already have. It's an intelligence layer that plugs into your infrastructure.

If you have a FIWARE digital twin, PRISMA makes it intelligent.  
If you have IoT sensors, PRISMA gives them context.  
If you have emergency protocols, PRISMA executes them with judgment.

**Your infrastructure + our brain.**

PRISMA delivers three things:

- **Prioritized alerts** — No noise, only what matters now.
- **Traceable explanation** — Every decision references concrete data. Auditable, AI Act compliant.
- **Recommended actions** — Specific suggestions. The human always decides.

---

## Slide 6: How It Started

**Visual:** GovTech Air Quality Challenge + Air Quality Expert Agent

### Left panel:
- **Mejor puntuación en el Concurso de Ideas GovTech Reto Calidad del Aire 1 – 95/100**
- Partners: Suez, Kunak, inBiot, Science for Change
- **TwIN Govtech: Calidad del aire**
- ARNASTU-RESPIRA 2030: Un Gemelo Digital de Calidad del Aire y Clima para una Pamplona-Iruña resiliente, justa y saludable.

### Right panel:
- **Agente experto en Calidad del Aire**
- Anne - AAQ & IAQ & WELL AP Consultant
- Expert agent that interprets indoor and outdoor air quality data and weather conditions to assess wellness WELL AP and Thermal Comfort standards.

### Narrative

PRISMA started as a GovTech challenge for air quality in Pamplona. The idea was simple: connect sensors, weather, and health data to anticipate respiratory crises.

But the real insight came from building an expert agent that could reason across multiple data sources. That's when we realized: **this isn't just about air quality. It's about any cascade.**

---

## Slide 7: First Win — FIWARE MCP

**Subtitle:** AI Talks Directly to the City

**Visual:** Architecture diagram + GitHub repo

### What we built:
- **(First?) NGSI-v2 Model Context Protocol (MCP) server native to FIWARE with full Smart Data Models support.**
- 4 Tools
- 3 Prompts
- Auth, autorefresh

### Impact:
FIWARE MCP allows AI agents (like Claude in Cursor) to interact directly with FIWARE Context Brokers using natural language, with full Smart Data Models support.

### Narrative

We built the first MCP server that lets AI talk directly to FIWARE. No custom APIs. No middleware. Just natural language.

This is open source. Anyone can use it. But we're the ones who know how to make it intelligent.

---

## Slide 8: The MVP

**Visual:** Streamlit app screenshot + architecture diagram

### What's implemented TODAY:

```
┌─────────────────────────────────────────────────────────────┐
│                    MVP ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Streamlit UI ◄──── AI Agent (LLM) ◄──── Knowledge Base    │
│       │                   │                                 │
│       ▼                   ▼                                 │
│  FIWARE Context Broker (Telefónica Cloud)                  │
│       │                                                     │
│       ▼                                                     │
│  n8n Workflows (subscriptions, webhooks)                   │
│       │                                                     │
│       ▼                                                     │
│  CSV Timelines (synthetic scenario data)                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Design principle: OODA Snapshot-Oriented

> **"The snapshot is the cognitive boundary of the agent."**
>
> All decisions are made against a frozen context (snapshot).
> That's why it's explainable, auditable, and AI Act compliant.

### What the demo shows:
- FIWARE Context Broker with 21 real entities (weather, air quality, fires, hospitals, traffic, drones, social media)
- n8n orchestrating data flows with 3 AI agents (OBSERVE, ORIENT, DECIDE)
- Streamlit as visualization interface
- AI agent interpreting context and suggesting actions
- Timelines with synthetic data (in production would be real APIs)
- Telegram integration for alerts and conversational interaction

### Transparency note
The data in this demo is synthetic. The architecture is real. With one hour of API access, it would be real data.

---

## Slide 9: What's Next

**Subtitle:** Roadmap

### Two business models:
1. **Custom integrations** (first model)
2. **IaaS** (second model)

| Phase | Timeline | Deliverables |
|-------|----------|--------------|
| **MVP 2.0** | Q1-2026 | Self host Fiware, all modules in the app, new RAG |
| **1st Pilot** | Q2-2026 | Communication, real data, secure AI |
| **Fund & Grow** | Q3-2026 | Set up company, raise, hire, grow |

---

## Slide 10: We're Looking For

| | What | Detail |
|---|-----|--------|
| 🎯 | **Early Adopters** | Cities and utilities willing to co-create |
| 🧠 | **Talent** | Python/FIWARE, ML engineers |
| 💰 | **Investors** | Defense + Climate tech + GovTech |
| 🤝 | **Partners** | FIWARE Enablers & integrators |

---

## Slide 11: The Team

**Visual:** Photo + credentials

### Miguel Escribano
*Sustainability & Business Development Specialist*

Air quality monitoring, green tech, and climate solutions with municipalities, industries, and investors.

Trained in Product Development and AI Architecture.

Passionate about integrating AI and IoT into meaningful sustainability projects.

### Track Record

| Credential | Detail |
|------------|--------|
| **Funding** | €4.5M+ in IoT/SaaS projects |
| **Organizations** | WHO, UNEP, US EPA, World Athletics, SAP, Intel, Suez |
| **Track record** | 8 projects TRL 6-8 |
| **Revenue** | RevOps Director: revenue x15, >€10M |
| **Recognition** | Airlab 2023, US EPA 2019, COP25 |

### Experience with coding:
- First ChatGPT account 2022
- First Google Collab, 2023
- First Github account, August 2025
- First Cursor account, September 2025
- ...

### Shadow team:
- **Anticipa360** — Emergency communications expert
- **Larraby** — AI interfaces expert
- **MB3** — Early Warning Systems expert
- **GOBE** — Strategic communications
- **CEIN** — AI and data science research center

---

## Slide 12: Would You Like to Build European Situational Intelligence?

**PRISMA**  
Multi-Source Risks. Single Point of Foresight.

**Contact:**  
+34 605 977 027 | miguel.escribano@gmail.com | @migoch

---

## OPTIONAL TECHNICAL SLIDE — Architecture Deep Dive

**Use with:** Technical audiences, tech-savvy investors

### Technical roadmap (architectural direction)

| Phase | Component | Status |
|-------|-----------|--------|
| **MVP (today)** | FIWARE CB + n8n + Streamlit + Agent | ✅ Implemented |
| **Q1 2026** | Real API integration (AEMET, EFFIS, 112) | 🔜 Next |
| **Q2 2026** | Event persistence (Supabase/PostgreSQL) | 📋 Designed |
| **Q2 2026** | Formal snapshots with run_id | 📋 Designed |
| **Q3 2026** | Specialized multi-agent | 📋 Conceptual |

### Important note
The OODA model with snapshots and run_id is the **design principle** guiding the architecture. The current MVP demonstrates the concept with a simplified implementation. Formal persistence in Supabase is the next technical step.

---

## EXECUTION NOTES

### Timing (7 minutes total)

| Section | Slides | Time |
|---------|--------|------|
| The problem + context | 1-3 | 2 min |
| The vision + PRISMA | 4-5 | 1.5 min |
| Journey + Demo | 6-8 | 2.5 min |
| Roadmap + Team + CTA | 9-11 | 1 min |

### Pre-pitch checklist

- [ ] Demo running locally
- [ ] Backup video recorded (in case of failure)
- [ ] Screenshots ready
- [ ] Technical slide prepared (in case they ask)

### Plan B for Demo

1. Recorded backup video (2 min)
2. Screenshots with narration
3. "The demo is running on my machine, I'll show you after"

### Frequently Asked Questions

**"How is it different from Everbridge?"**
> Everbridge notifies known crises with predefined workflows. PRISMA detects emerging situations that were never programmed.

**"Why FIWARE?"**
> European standard for smart cities. Interoperable, open source, marketplace of 200+ cities.

**"How much does it cost?"**
> SaaS pay-as-you-grow. From €12k/year for small cities to €150k/year for utilities. PoC: €30-60k.

**"What if the AI is wrong?"**
> Human-in-the-loop always. The system suggests, the operator decides.

**"Can't anyone build this?"**
> Yes, the technical barrier has lowered. The domain knowledge barrier hasn't. 20 years can't be learned from a prompt.

**"Where is the snapshot model?"**
> It's the design principle. The MVP demonstrates the concept. Formal implementation with persistence is the next technical step.

---

*Born in TwinLab*  
*Contact: Miguel Escribano — miguel.escribano@gmail.com*
