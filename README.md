# PRISMA Sandbox V.1

Situational intelligence system for emergency management using AI agents + FIWARE.

**MVP Demo:** Heat Wave + Forest Fire scenario in Pamplona/Navarra.

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

## Demo Scenarios

| Scenario | Description | Duration |
|----------|-------------|----------|
| **6 julio** | Extreme crisis - heat wave + uncontrolled fires | 4h → 15min @x16 |
| **15 junio** | Training - situation gets controlled | 4h → 15min @x16 |
| **1 agosto** | Rain saves the day - escalation then relief | 4h → 15min @x16 |

## Architecture

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
    n8n Webhooks (subscriptions)
       │
       ▼
    LLM Agent (reasoning)
```

## Why PRISMA: Dynamic Digital Twin Management

Traditional FIWARE deployments are **static by design**. Configuring IoT Agents, entities, subscriptions, and CEP rules requires developers to write and execute scripts. The digital twin is frozen at deployment time.

PRISMA changes this paradigm through **MCP (Model Context Protocol) + AI Agent integration**:

| Traditional FIWARE | PRISMA |
|--------------------|--------|
| Static entity model defined at design time | Dynamic model that evolves with the incident |
| Developer writes scripts to add entities | AI agent creates entities via natural language |
| Subscriptions hardcoded | Agent configures subscriptions based on situational needs |
| Rigid, pre-planned scenarios | Adaptive to unexpected resources and events |

**Example:** During a forest fire, a neighboring region loans a fire truck. In traditional FIWARE, this resource wouldn't exist in the model—or a developer would need to manually create the entity. With PRISMA, the AI agent semi-automatically models the new `FireTruck:Prestamo_LaRioja_001` entity, sets up tracking subscriptions, and integrates it into the incident lifecycle—all through the MCP interface.

The digital twin becomes a **living model** that adapts in real-time to the chaos of emergency management.

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
└── vendor/                       # Smart Data Models, GeoJSON
```

## FIWARE Entities

| Entity Type | Source | Instances |
|-------------|--------|-----------|
| WeatherObserved | AEMET API | 1 (Pamplona) |
| AirQualityObserved | ThinkingCities IoT | 3 (Rochapea, FelisaMunarriz, Iturrama) |
| ForestFire | EFFIS API | 3 (Baztán, Ultzama, Roncal) |
| EmergencyCalls | SOS 112 Navarra | 1 |
| HospitalStatus | SNS-Osasunbidea | 1 (HUN Urgencias) |
| SocialMediaAlert | Commercial API | 1 |
| TrafficAlert | DGT API | 3 (N-121-A, NA-411, NA-137) |

## Configuration

Edit `.env`:
- `FIWARE_USERNAME` / `FIWARE_PASSWORD` - Telefónica credentials
- `SERVICE` - `sc_pamplona_sandbox`
- `SUBSERVICE` - `/02_Escribano`

## MCP Servers

Two FIWARE MCP servers available:

| MCP Server | Subservice |
|------------|------------|
| `FIWARE-MCP-Server-02_Escribano` | `/02_Escribano` (dev sandbox) |
| `FIWARE-MCP-Server-sdmenvironment` | `/sdmenvironment` (prod - 86 sensors) |

---

TwIN Lab 2025 | Miguel Escribano
