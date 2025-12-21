# PRISMA 1.0 — n8n Workflows

**Version:** v1.0-pitch (December 2025)  
**Status:** Stable — Used in first pitch

This folder contains the production n8n workflows that implement PRISMA's OODA cycle.

---

## Workflows

### 1. PRISMA_OBSERVE 1.0
**Purpose:** Ingest and store incoming sensor data

**Trigger:** FIWARE subscription webhook (POST)

**Flow:**
1. Receives entity updates from FIWARE Context Broker
2. Extracts entity_id, entity_type, timestamp, attributes
3. Parses `agentContext` field for LLM interpretation
4. Stores raw event in Supabase (`prisma_events`)
5. Calls AI agent to generate human-readable summary
6. Sends formatted message to Telegram (data brain)

**Output:** Telegram message with icon, timestamp, entity info, facts, and summary

**Agent Model:** Claude Sonnet 4.5

**Key Features:**
- Pure JSON output from agent (no markdown)
- Unicode icons by entity_type
- Coordinates included when available
- Separator lines for readability

---

### 2. PRISMA_ORIENT 2.0
**Purpose:** Build coherent snapshots and assess risk (ORIENT + DECIDE phases)

**Trigger:** Cron (every 2 minutes) or manual

**Flow:**
1. **Freeze Snapshot:** Query latest state of all entities from Supabase
2. **Build Context:** Aggregate recent events, entity states, and metadata
3. **AI Agent (DECIDE):** Evaluate risk level and recommend actions
4. **Store Decision:** Save to Supabase (`prisma_decisions`)
5. **Send Alert:** Format and send decision to Telegram

**Output:** Telegram message with alert level, summary, key factors, and recommended actions

**Agent Model:** Claude Sonnet 4.5 (with full system prompt context)

**Key Features:**
- Snapshot-based reasoning (temporal coherence)
- Includes synthetic timestamp (`scenario_ts`) for demo scenarios
- Structured output: alert_level, summary, key_factors, recommended_actions
- Separator lines between sections

---

### 3. PRISMA_DECIDE 2.0
**Note:** This workflow is now integrated into PRISMA_ORIENT 2.0. The separate file exists for historical reference but is not actively used in v1.0-pitch.

---

## Importing Workflows

1. Open n8n
2. Go to **Workflows** → **Import from File**
3. Select the JSON file
4. Configure credentials:
   - Supabase (API key)
   - Telegram Bot (token)
   - Anthropic/OpenAI (API key)
5. Update webhook URLs if needed
6. Activate workflow

---

## Telegram Bots

| Bot | Purpose | Workflow |
|-----|---------|----------|
| `PRISMA_112_Comms` | Data brain (OBSERVE) | PRISMA_OBSERVE 1.0 |
| `PRISMA_112_ORIENT_DECIDE` | Decision alerts (ORIENT) | PRISMA_ORIENT 2.0 |

---

## Supabase Tables

| Table | Used By | Purpose |
|-------|---------|---------|
| `prisma_events` | OBSERVE | Raw sensor data (append-only) |
| `prisma_decisions` | ORIENT | Agent decisions with snapshots |

---

## Agent Prompts

### OBSERVE Agent
- **System Prompt:** Embedded in workflow
- **Context:** Uses `agentContext` field from each entity
- **Output:** JSON with icon, entity_id, entity_type, ts, location, facts, summary

### DECIDE Agent
- **System Prompt:** Full context from `streamlit/app_config/AGENT_SYSTEM_PROMPT_CONTEXT.md`
- **Context:** Snapshot of all entities + recent events
- **Output:** JSON with alert_level, summary, key_factors, recommended_actions

---

## Known Issues / Limitations

- **Rate Limits:** Anthropic has 30k tokens/min limit. Large snapshots can hit this. Workaround: Use GPT-4o or reduce context size.
- **Telegram Parsing:** Special characters in entity_id (`:`, `_`) must be escaped or replaced.
- **Synthetic Timestamps:** Demo scenarios use `scenario_ts` field. Production would use real timestamps.

---

## Version History

- **v1.0-pitch (2025-12-21):** First stable version used in pitch
- **v0.x (2025-12):** Development iterations

---

For questions or issues: miguel.escribano@gmail.com

