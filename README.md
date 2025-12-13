# PRISMA Sandbox V.1

Situational intelligence system for emergency management using AI agents + FIWARE.

**MVP Demo:** Heat Wave + Forest Fire scenario in Pamplona/Navarra.

## Quick Start

```bash
# 1. Setup
cp .env.example .env  # Add your FIWARE credentials

# 2. Initialize FIWARE entities
cd streamlit
python fiware_init_mvp.py

# 3. Run the app
streamlit run app.py
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

## Project Structure

```
├── streamlit/
│   ├── app.py                    # Main Streamlit UI
│   ├── scenario_runner.py        # Injects CSV data to FIWARE
│   ├── fiware_init_mvp.py        # Initialize FIWARE entities
│   ├── app_config/
│   │   ├── scenarios.py          # Entity definitions & streams
│   │   └── knowledge_base.py     # Agent knowledge base
│   └── data/
│       ├── timeline_6_julio.csv
│       ├── timeline_15_junio.csv
│       └── timeline_1_agosto.csv
│
├── src/
│   ├── fiware_client.py          # FIWARE API client
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
