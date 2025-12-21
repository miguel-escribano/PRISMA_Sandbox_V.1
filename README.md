# PRISMA Sandbox V.1

**Situational Intelligence for Critical Infrastructures and Cities**

*Multi-Source Risks. Single Point of Foresight.*

**Version:** v1.0-pitch (December 2025)  
**Status:** Stable — First pitch completed

PRISMA implements a modern, human-in-the-loop **OODA (Observe–Orient–Decide–Act)** decision cycle that enables proactive agents to observe asynchronous environments, reason coherently, propose actions, and interact with humans without temporal ambiguity.

**MVP Demo:** Heat Wave + Forest Fire scenario in Pamplona/Navarra.

---

## What is PRISMA?

PRISMA is European situational intelligence built for critical infrastructure and cities. It's **Intelligence-as-a-Service** that plugs into your existing infrastructure (FIWARE, IoT, APIs) and makes it intelligent.

**Three core outputs:**
1. **Prioritized Alerts** — No noise, only what matters now
2. **Traceable Explanation** — Every decision references concrete data (AI Act compliant)
3. **Recommended Actions** — Specific suggestions. Human always decides.

---

## Quick Start

```bash
# 1. Setup
cp .env.example .env  # Add your FIWARE credentials

# 2. Initialize FIWARE entities
python src/fiware_init_mvp.py

# 3. Run the app
streamlit run streamlit/app.py
```

App runs at http://localhost:8501

---

## How PRISMA Works

PRISMA is not a simulation or a dashboard. It's a **decision system** that:

1. **Observes** asynchronous data streams (FIWARE, APIs, IoT, social media)
2. **Orients** by building coherent logical snapshots of the world
3. **Decides** by assessing risks and recommending cascade impacts
4. **Acts** through human confirmation — the operator always has final say

The key innovation: **decisions are made against frozen snapshots**, not a moving present. This makes PRISMA explainable, auditable, and safe for real operations.

---

## Conceptual Model (OODA Mapping)

PRISMA is an explicit implementation of Boyd's OODA loop adapted for complex, multi-source environments:

| OODA Phase | PRISMA Component | Description |
|------------|------------------|-------------|
| **Observe** | `PRISMA:OBSERVE` | Ingests events from FIWARE Context Broker, external APIs, IoT sensors |
| **Orient** | Logical Snapshot | Aggregates context into a coherent worldview at `snapshot_ts` |
| **Decide** | `PRISMA:ORIENT_DECIDE` | Evaluates risk levels, cascade patterns, recommends actions |
| **Act** | Human Confirmation | Operator reviews, modifies, confirms or rejects proposals |

**Key distinction:** Orient and Decide are explicitly separated, and the Act phase is **conversational and human-mediated**.

---

## Temporal Model

PRISMA does **not** use real-time "now". Instead, it introduces a **logical snapshot**:

```
┌─────────────────────────────────────────────────────────────────┐
│                     TEMPORAL COHERENCE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Events arrive asynchronously:                                 │
│   ───●────●──●─────●────●───●──────●────> time                 │
│      │    │  │     │    │   │      │                           │
│      ▼    ▼  ▼     ▼    ▼   ▼      ▼                           │
│   ┌──────────────────────────────────┐                         │
│   │     LOGICAL SNAPSHOT             │                         │
│   │     snapshot_ts = T              │                         │
│   │     ─────────────────────────    │                         │
│   │     Coherent worldview at T      │                         │
│   │     All decisions reference T    │                         │
│   └──────────────────────────────────┘                         │
│                                                                 │
│   → Decisions are always made with respect to a frozen         │
│     snapshot, never a moving present.                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

- `snapshot_ts` (BIGINT): logical evaluation time
- A snapshot represents a **coherent worldview**, not an instantaneous state
- Events inside a snapshot may have different timestamps
- Temporal coherence is achieved at the **decision level**, not the event level

> **Core principle:** The snapshot is the cognitive boundary of the agent.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PRISMA OODA CYCLE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────┐│
│  │   OBSERVE    │    │    ORIENT    │    │    DECIDE    │    │  ACT   ││
│  │              │    │              │    │              │    │        ││
│  │ FIWARE CB    │───▶│ Snapshot     │───▶│ Risk         │───▶│ Human  ││
│  │ External APIs│    │ Builder      │    │ Assessment   │    │ Review ││
│  │ IoT Sensors  │    │              │    │              │    │        ││
│  │ Social Media │    │ Context      │    │ Cascade      │    │Confirm/││
│  │ 112 Calls    │    │ Aggregation  │    │ Detection    │    │ Reject ││
│  └──────────────┘    └──────────────┘    └──────────────┘    └────────┘│
│         │                   │                   │                │     │
│         ▼                   ▼                   ▼                ▼     │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                      DATA LAYER (Supabase)                      │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │  │
│  │  │  prisma_events  │  │  prisma_latest  │  │   snapshots     │  │  │
│  │  │   (immutable)   │  │ (current state) │  │  (run-based)    │  │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘  │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Component Flow

```
Streamlit App (localhost:8501)
       │
       ├── ScenarioRunner (subprocess)
       │         │
       │         ▼
       │   CSV Timelines (17 datapoints, 13:00-17:00)
       │         │
       ▼         ▼
    FIWARE Context Broker (Telefónica Cloud)
       │
       ▼
    n8n Webhooks (subscriptions) ──▶ Supabase (prisma_events)
       │
       ▼
    PRISMA Agent (OODA cycle)
       │
       ▼
    Human-in-the-Loop (conversation)
```

---

## Data Architecture

### Storage (Supabase)

| Table | Purpose | Characteristics |
|-------|---------|-----------------|
| `prisma_events` | Historical events | Immutable, append-only |
| `prisma_latest` | Current state per entity | Latest known values |
| `snapshots` | Decision snapshots | Run-based, coherent worldviews |

### Snapshot Content

Each snapshot aggregates entities with:
- `latest_ts` — timestamp of most recent data
- `recent_activity` — count + time range of events
- `attributes` — decision-relevant state values

### Run-Based Execution

```
Problem:  Supabase node in n8n doesn't support ORDER BY
          → Can't safely read "latest state" during concurrent writes

Solution: Run-based execution model
          → Each OBSERVE execution generates unique run_id
          → All events in that execution share run_id
          → Snapshots built using: run_id DESC LIMIT 1

Result:   Snapshots are run-based, not time-based
          → Guarantees internal consistency
```

---

## Agent Behavior

The PRISMA agent is **proactive and conversational**. It continuously performs:

1. **Observe** (cron-based) — Ingest new events
2. **Orient** (build snapshot) — Aggregate into coherent context
3. **Decide** (assess risk) — Evaluate situation, recommend actions
4. **Act (via conversation)** — Initiate dialogue when decision emerges

### Conversation Model

- One active conversation per relevant snapshot
- Conversation is bound to `snapshot_ts`
- The snapshot **never changes during conversation**
- If world changes → new snapshot → new conversation

The human can:
- Confirm actions
- Ask for explanations
- Request details
- Modify or reject proposals

The agent responds **only using the active snapshot**, ensuring temporal coherence.

---

## Why PRISMA: Dynamic Digital Twin Management

Traditional FIWARE deployments are **static by design**. Configuring IoT Agents, entities, subscriptions, and CEP rules requires developers to write and execute scripts. The digital twin is frozen at deployment time.

PRISMA changes this paradigm through **MCP (Model Context Protocol) + AI Agent integration**:

| Traditional FIWARE | PRISMA |
|--------------------|--------|
| Static entity model defined at design time | Dynamic model that evolves with the incident |
| Developer writes scripts to add entities | AI agent creates entities via natural language |
| Subscriptions hardcoded | Agent configures subscriptions based on situational needs |
| Rigid, pre-planned scenarios | Adaptive to unexpected resources and events |
| Reactive dashboards | Proactive decision support |

**Example:** During a forest fire, a neighboring region loans a fire truck. In traditional FIWARE, this resource wouldn't exist in the model—or a developer would need to manually create the entity. With PRISMA, the AI agent semi-automatically models the new `FireTruck:Prestamo_LaRioja_001` entity, sets up tracking subscriptions, and integrates it into the incident lifecycle—all through the MCP interface.

The digital twin becomes a **living model** that adapts in real-time to the chaos of emergency management.

---

## MCP Servers — First FIWARE MCP with NGSI-v2

PRISMA implements the **first Model Context Protocol server native to FIWARE** with full NGSI-v2 support.

This means AI agents can directly:
- Read entity state from Context Broker
- Write/update entities
- Configure subscriptions
- Reason over Smart Data Models

| MCP Server | Subservice | Purpose |
|------------|------------|---------|
| `FIWARE-MCP-Server-02_Escribano` | `/02_Escribano` | Dev sandbox |
| `FIWARE-MCP-Server-sdmenvironment` | `/sdmenvironment` | Prod (86 sensors) |

The MCP interface transforms the Context Broker from a passive data store into an **active participant in the decision cycle**.

---

## Demo Scenarios

| Scenario | Description | Duration |
|----------|-------------|----------|
| **6 julio** | Extreme crisis - heat wave + uncontrolled fires | 4h → 15min @x16 |
| **15 junio** | Training - situation gets controlled | 4h → 15min @x16 |
| **1 agosto** | Rain saves the day - escalation then relief | 4h → 15min @x16 |

---

## FIWARE Entities

| Entity Type | Source | Instances |
|-------------|--------|-----------|
| WeatherObserved | AEMET API | 1 (Pamplona) |
| AirQualityObserved | Kunak IoT (TwIN Lab) + GobNavarra | 3 (Kunak BajaNavarra, Kunak Rochapea, Iturrama) |
| IndoorAirQuality | inBiot MICA_WELL (TwIN Lab) | 3 (HUN, inBiot offices, CC Itaroa) |
| ForestFire | EFFIS API | 3 (Baztán, Ultzama, Roncal) |
| FireForecast | TESICNOR RRD (TwIN Lab) | 3 (Baztán, Ultzama, Roncal) |
| Drone | Bravodrones (TwIN Lab) | 2 (Fire inspector, Crowd monitor) |
| EmergencyCalls | SOS 112 Navarra | 1 |
| HospitalStatus | SNS-Osasunbidea | 1 (HUN Urgencias) |
| SocialMediaAlert | Commercial API | 1 |
| TrafficAlert | DGT API | 3 (N-121-A, NA-411, NA-137) |

**TwIN Lab Ecosystem Integration:** PRISMA integrates data from multiple TwIN Lab companies:
- **Kunak** - High-precision outdoor air quality sensors
- **inBiot** - Indoor air quality monitoring (MICA_WELL) for healthy buildings
- **Bravodrones** - Drones with computer vision for fire inspection and crowd monitoring
- **TESICNOR RRD** - Predictive models for fire propagation forecasting

---

## Project Structure

```
├── data/
│   └── ola_calor_incendio/       # Scenario timelines
│       ├── timeline_6_julio.csv
│       ├── timeline_15_junio.csv
│       └── timeline_1_agosto.csv
│
├── streamlit/
│   ├── app.py                    # Main Streamlit UI
│   └── app_config/
│       ├── scenarios.py          # Entity definitions & streams
│       └── knowledge_base.py     # Agent knowledge base
│
├── src/
│   ├── fiware_client.py          # FIWARE API client
│   ├── fiware_init_mvp.py        # Initialize FIWARE entities
│   ├── scenario_runner.py        # Injects CSV data to FIWARE
│   └── config.py                 # Configuration loader
│
├── n8n/                          # Workflow definitions
├── business/                     # GTM, pitch, business docs
└── vendor/                       # Smart Data Models, GeoJSON
```

---

## Configuration

Edit `.env`:
- `FIWARE_USERNAME` / `FIWARE_PASSWORD` - Telefónica credentials
- `SERVICE` - `sc_pamplona_sandbox`
- `SUBSERVICE` - `/02_Escribano`

---

## Core Design Principles

1. **The snapshot is the cognitive boundary of the agent** — All reasoning happens within a frozen worldview
2. **Human-in-the-loop by design** — Act phase is always conversational
3. **Temporal coherence at decision level** — Not at event level
4. **Explainable and auditable** — Every decision traces to a specific snapshot
5. **Demo-safe and production-ready** — Same architecture for both

---

## One-Sentence Summary

> PRISMA is European **Intelligence-as-a-Service** for critical infrastructure: it connects multi-source data in real-time, predicts cascade impacts, and recommends prioritized actions—with the human always in control.

---

## Current Status (v1.0-pitch)

### ✅ What's Working
- **OODA Cycle:** Full implementation (OBSERVE, ORIENT, DECIDE)
- **FIWARE Integration:** 21 entities across 10 types
- **n8n Workflows:** 3 stable workflows (OBSERVE 1.0, ORIENT 2.0, DECIDE 2.0)
- **Supabase Persistence:** 3 tables (events, latest_state, decisions)
- **Telegram Integration:** Alerts + conversational chat
- **Streamlit UI:** Scenario runner with 3 demo scenarios
- **Agent Context:** Full system prompt with thresholds, cascades, actions
- **FIWARE MCP:** First NGSI-v2 MCP server (open source)

### 📋 Next Steps (Q1 2026)
- Self-hosted FIWARE
- Real API integrations (AEMET, EFFIS, 112)
- Enhanced RAG architecture
- Production deployment preparation

### 📚 Documentation
- **Pitch Deck:** `business/Pitch/PRISMA_PITCH_DECK.md`
- **n8n Workflows:** `n8n/PRISMA 1.0/README.md`
- **Database Schema:** `database/README.md`
- **Changelog:** `CHANGELOG.md`
- **Architecture:** See sections above on OODA, Snapshots, and MCP

### 📞 Contact
miguel.escribano@gmail.com | +34 605 977 027

---

TwIN Lab 2025 | Miguel Escribano
