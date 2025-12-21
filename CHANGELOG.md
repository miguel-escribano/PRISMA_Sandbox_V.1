# CHANGELOG

All notable changes to PRISMA will be documented in this file.

## [v1.0-pitch] - 2025-12-21

### Added
- **First stable pitch version**
- Complete OODA cycle implementation (OBSERVE, ORIENT, DECIDE)
- FIWARE MCP Server integration (first NGSI-v2 MCP)
- Streamlit UI with scenario runner
- n8n workflows for agent orchestration
- Supabase persistence (prisma_events, prisma_decisions)
- Telegram integration (alerts + conversational chat)
- 21 FIWARE entities across 10 entity types
- 3 demo scenarios (6 julio, 15 junio, 1 agosto)
- Agent system prompt with full context (thresholds, cascades, actions)
- Bidirectional chat with agent (PRISMA_CHAT 1.0)
- **Staggered injection** — Realistic data arrival simulation in scenario_runner.py
  - Distributes entity updates across each time window (not burst)
  - Weather (0-5%), Air Quality (5-25%), Fires (25-55%), Emergencies (55-70%), Traffic (70-80%), Drones (80-90%), Social (90-100%)
  - Deterministic (seed=42) for reproducible demos
  - Retrocompatible: disable with `--no-stagger`

### Technical Stack
- FIWARE Context Broker (Telefónica Cloud)
- n8n (3 workflows: OBSERVE, ORIENT_DECIDE, CHAT)
- Streamlit + Python
- Supabase (PostgreSQL)
- Claude Sonnet 4.5 / GPT-4o
- Telegram Bot API

### Documentation
- Pitch deck finalized (business/Pitch/PRISMA_PITCH_DECK.md)
- README updated with IaaS positioning
- Architecture diagrams and OODA mapping

---

## Future Versions

### [v2.0] - Q1 2026 (Planned)
- Self-hosted FIWARE
- All modules integrated in app
- New RAG architecture
- Real API integrations (AEMET, EFFIS, 112)

### [Pilot] - Q2 2026 (Planned)
- Production deployment
- Real-time data feeds
- Secure AI infrastructure
- Communication protocols

