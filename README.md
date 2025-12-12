# PRISMA Sandbox V.1

Situational intelligence system for emergency management using AI agents + FIWARE.

## Quick Start

```bash
# 1. Setup
cp .env.example .env  # Add your credentials

# 2. Start MCP Server
python start.py

# 3. Use FIWARE
python test_fiware_connection.py
```

## Architecture

```
Cursor / Your App
       │
       ▼
MCP Server (localhost:5002)
       │
       ▼
Telefónica FIWARE (cloud)
```

## Configuration

Edit `.env`:
- `FIWARE_USERNAME` / `FIWARE_PASSWORD` - Telefónica credentials
- `SERVICE` - `sc_pamplona_sandbox`
- `SUBSERVICE` - `/02_Escribano` (dev) or `/sdmenvironment` (prod)

**Note:** Use `FIWARE_USERNAME` (not `USERNAME`) to avoid Windows environment variable conflicts.

## Subservices

| Subservice | Purpose |
|------------|---------|
| `/02_Escribano` | Development sandbox |
| `/sdmenvironment` | Production - 86 sensors in Pamplona |

## Project Structure

```
├── start.py              # Start MCP server
├── config.py             # Configuration loader
├── src/fiware_client.py  # Direct FIWARE client
├── .env                  # Your credentials (gitignored)
├── vendor/               # Smart Data Models, GeoJSON refs
└── .cursor/commands/     # FIWARE command reference
```

## MCP Servers

This project uses **2 FIWARE MCP servers** for different subservices:

| MCP Server | Subservice | Location |
|------------|------------|----------|
| `FIWARE-MCP-Server-02_Escribano` | `/02_Escribano` | `C:\Users\migue\FIWARE-MCP-Server-02_Escribano` |
| `FIWARE-MCP-Server-sdmenvironment` | `/sdmenvironment` | `C:\Users\migue\FIWARE-MCP-Server-sdmenvironment` |

**Configuration:**
- Each MCP has its own `.env` file with credentials
- Configured in `~/.cursor/mcp.json`
- Use `FIWARE_USERNAME` and `FIWARE_PASSWORD` (not `USERNAME`/`PASSWORD`)
- Each MCP has a unique `FastMCP` instance name

**Available Tools:**
- `CB_version` - Check Context Broker version
- `fiware_request` - Execute NGSI-v2 API requests
- `list_smart_data_model_domains` - List available Smart Data Models
- `get_smart_data_model` - Get Smart Data Model schema

**Resources:**
- `fiware://examples` - Postman collection with API examples

See `.cursor/commands/` for detailed usage guides.

---

TwIN Lab 2025 | Miguel Escribano
