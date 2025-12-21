# PRISMA Database Schema

**Version:** v1.0-pitch  
**Database:** Supabase (PostgreSQL)  
**Last Updated:** 2025-12-21

---

## Overview

PRISMA uses three core tables to implement the OODA cycle:

| Table | Purpose | Rows (v1.0) | Size |
|-------|---------|-------------|------|
| `prisma_events` | Immutable event log | 160 | 1.3 MB |
| `prisma_latest_state` | Current entity state | 21 | 176 KB |
| `prisma_decisions` | Agent decisions | 8 | 304 KB |

---

## Table Descriptions

### 1. prisma_events

**Purpose:** Append-only event log. All sensor data and entity updates are stored here.

**Schema:**
```sql
event_id TEXT PRIMARY KEY
entity_id TEXT NOT NULL
entity_type TEXT NOT NULL
ts TIMESTAMPTZ NOT NULL
source TEXT
attributes JSONB NOT NULL
meta JSONB NOT NULL
raw JSONB
run_id BIGINT UNIQUE
```

**Key Concepts:**
- **Immutable:** Events are never updated or deleted
- **run_id:** Groups events from the same execution cycle (enables snapshot consistency)
- **attributes:** Sensor readings (temperature, PM2.5, wind speed, etc.)
- **meta:** Metadata (units, location, attribute types)

**Indexes:**
- `prisma_events_entity_idx` — Fast lookup by entity + time
- `prisma_events_ts_idx` — Fast time-based queries
- `prisma_events_run_id_idx` — Snapshot consistency

**Example Row:**
```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "entity_id": "WeatherObserved:AEMET_API_Pamplona_Noain",
  "entity_type": "WeatherObserved",
  "ts": "2025-07-06T13:00:00+00:00",
  "source": "fiware_subscription",
  "attributes": {
    "temperature": 36,
    "relativeHumidity": 38,
    "windSpeed": 5,
    "windDirection": "S"
  },
  "meta": {
    "location": {"type": "Point", "coordinates": [-1.6442, 42.8184]},
    "units": {"temperature": "°C", "windSpeed": "km/h"}
  },
  "run_id": 1734800400000
}
```

---

### 2. prisma_latest_state

**Purpose:** Current state snapshot. One row per entity with latest known values.

**Schema:**
```sql
entity_id TEXT PRIMARY KEY
entity_type TEXT NOT NULL
ts TIMESTAMPTZ NOT NULL
source TEXT
attributes JSONB NOT NULL
meta JSONB NOT NULL
```

**Key Concepts:**
- **Upserted:** Each new event updates this table (replaces old value)
- **Fast queries:** Used by ORIENT phase to build snapshots
- **21 entities:** All active FIWARE entities in the system

**Example Row:**
```json
{
  "entity_id": "AirQualityObserved:Kunak_Rochapea",
  "entity_type": "AirQualityObserved",
  "ts": "2025-07-06T13:15:00+00:00",
  "source": "fiware_subscription",
  "attributes": {
    "PM2_5": 62,
    "CO": 0.8,
    "NO2": 45,
    "qualityIndex": 3
  },
  "meta": {
    "location": {"type": "Point", "coordinates": [-1.6398, 42.8256]}
  }
}
```

---

### 3. prisma_decisions

**Purpose:** Agent decisions and risk assessments (OODA DECIDE phase).

**Schema:**
```sql
id UUID PRIMARY KEY DEFAULT gen_random_uuid()
snapshot_ts BIGINT NOT NULL
alert_level TEXT NOT NULL
summary TEXT
key_factors JSONB
recommended_actions JSONB
decision_ts TIMESTAMPTZ NOT NULL DEFAULT now()
scenario_ts TIMESTAMPTZ
```

**Key Concepts:**
- **snapshot_ts:** Logical evaluation time (Unix milliseconds) — the "cognitive boundary"
- **alert_level:** LOW, MEDIUM, HIGH, CRITICAL
- **key_factors:** Array of 3 factors that influenced the decision
- **recommended_actions:** Array of 3 actions with responsible parties
- **scenario_ts:** Synthetic timestamp (only for demo scenarios)

**Indexes:**
- `prisma_decisions_snapshot_ts_idx` — Fast lookup by snapshot time

**Example Row:**
```json
{
  "id": "97c02e1a-6af3-43b7-ae8c-7be7dab37a9f",
  "snapshot_ts": 1766096716840,
  "alert_level": "CRITICAL",
  "summary": "Incendios activos cercanos con alto riesgo de propagación y humo afectando Pamplona. Calidad del aire degradada y hospital con alta ocupación.",
  "key_factors": [
    "Incendio en Ultzama (17 km) activo, alta intensidad y propagación extrema",
    "PM2.5 norte 62 vs sur 24 - gradiente confirma avance",
    "1M personas San Fermín expuestas - decisión eventos crítica"
  ],
  "recommended_actions": [
    "Activar SMS alerta llegada humo inminente - 112 Navarra",
    "Abrir refugios climatizados filtración HEPA - Ayuntamiento Pamplona",
    "Decidir suspensión eventos tarde San Fermín - CECOPI"
  ],
  "decision_ts": "2025-12-18T22:35:47.845853+00:00",
  "scenario_ts": "2025-07-06T17:00:00+00:00"
}
```

---

## Data Flow

```
1. OBSERVE
   ├─ FIWARE subscription → n8n webhook
   ├─ Parse event
   ├─ INSERT INTO prisma_events (append)
   └─ UPSERT INTO prisma_latest_state (replace)

2. ORIENT
   ├─ SELECT * FROM prisma_latest_state
   ├─ Build coherent snapshot
   └─ Pass to DECIDE agent

3. DECIDE
   ├─ AI agent evaluates risk
   ├─ INSERT INTO prisma_decisions
   └─ Send alert to Telegram
```

---

## Temporal Model

PRISMA uses **snapshot-based reasoning**, not real-time "now":

- **snapshot_ts** (BIGINT) — Logical evaluation time (Unix milliseconds)
- A snapshot represents a **coherent worldview**, not an instantaneous state
- Events inside a snapshot may have different timestamps
- Temporal coherence is achieved at the **decision level**, not the event level

> **Core principle:** The snapshot is the cognitive boundary of the agent.

---

## Run-Based Execution

**Problem:** Supabase node in n8n doesn't support ORDER BY  
**Solution:** Run-based execution model

- Each OBSERVE execution generates unique `run_id`
- All events in that execution share `run_id`
- Snapshots built using: `run_id DESC LIMIT 1`
- Guarantees internal consistency despite async event arrival

---

## Schema Evolution

### Future Tables (Planned)

- `prisma_snapshots` — Formal snapshot storage with run_id
- `prisma_actions` — Executed actions and operator confirmations
- `prisma_conversations` — Chat history with agent
- `prisma_cascade_patterns` — Learned cascade patterns (ML)

### Migration Strategy

- JSONB columns allow flexible schema evolution
- No foreign key constraints (FIWARE entities are dynamic)
- Backward-compatible changes only
- Use Supabase migrations for DDL changes

---

## Backup & Restore

**Backup:**
```bash
# Full schema + data
pg_dump -h db.xxx.supabase.co -U postgres -d postgres > backup.sql

# Schema only
pg_dump -h db.xxx.supabase.co -U postgres -d postgres --schema-only > schema.sql
```

**Restore:**
```bash
psql -h db.xxx.supabase.co -U postgres -d postgres < backup.sql
```

---

## Performance Notes

- **prisma_events** grows indefinitely (append-only). Consider partitioning by month in production.
- **prisma_latest_state** is small (21 rows) and fast.
- **prisma_decisions** grows slowly (one per ORIENT cycle, ~2 min intervals).

---

## Security

- **RLS:** Disabled in MVP (private repo, trusted environment)
- **API Keys:** Stored in n8n credentials (not in database)
- **Production:** Enable RLS, add service roles, audit logging

---

For questions: miguel.escribano@gmail.com

