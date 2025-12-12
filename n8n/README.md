# PRISMA - n8n Workflows

This directory contains n8n workflow definitions for data collection, processing, and automation.

## Contents

*To be populated*

## Purpose

n8n serves as the orchestration layer connecting:
- Telefónica IoT Platform (FIWARE)
- External APIs (AEMET, Red Eléctrica, IDENA)
- AI agents for cascade analysis
- Alert generation and notifications

## Workflow Categories

### Data Collection
- Real sensor data queries from `/sdmenvironment`
- External API integrations (weather, energy, geographic)
- Social media monitoring

### Data Processing
- NGSI-v2 entity transformation
- Data validation and enrichment
- Anomaly detection

### AI Agents
- Cascade risk analysis
- Decision engine
- Learning loops

### Response
- Alert generation
- Resource coordination
- Notification distribution

## Planned Workflows

- `sandbox-sensor-collector.json` - Query real sensors
- `aemet-weather-collector.json` - AEMET integration
- `cascade-analyzer.json` - AI cascade analysis
- `alert-generator.json` - Alert management

---

*Last updated: December 5, 2025*
