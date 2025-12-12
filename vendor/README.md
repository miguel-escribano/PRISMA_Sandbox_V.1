# PRISMA - Vendor Integrations

This directory contains configurations and documentation for third-party service integrations.

## 📁 Structure

```
vendor/
├── postman/                      # API testing & development
│   ├── collections/              # Postman request collections
│   ├── environments/             # Environment configurations
│   └── README.md                 # Setup instructions
│
└── mcp/                          # Model Context Protocol servers
    └── README.md                 # MCP setup & usage
```

## 🚀 Quick Links

### Postman (API Testing)
📁 **Source:** MCP Server directories
- `C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\`
- `C:\Users\migue\FIWARE-MCP-Server-Auth-Miguel\`

**Purpose:** Test and interact with FIWARE Sandbox APIs
- 50+ FIWARE operations (tested and proven)
- OAuth2 authentication
- Two subservices (dev/prod)

**Get Started:** See [postman/README.md](postman/README.md)

### MCP Servers (Cursor Integration)
📁 **Location:** `vendor/mcp/`

**Purpose:** Access FIWARE Sandbox directly from Cursor chat
- Query entities in conversation
- Create/update entities via AI
- Two configured servers (environment/miguel)

**Get Started:** See [mcp/README.md](mcp/README.md)

---

## 🔌 Integration Overview

### FIWARE Sandbox (Telefónica Cloud)
**Service:** `sc_pamplona_sandbox`

**Two Subservices:**
1. `/02_Escribano` - Development workspace (read/write)
2. `/sdmenvironment` - Production sensors (86 real sensors, read-only)

**Access Methods:**
- 🔧 **Postman** - Manual API testing and exploration
- 🤖 **MCP Servers** - Cursor chat integration
- 💻 **Python/Code** - Direct API calls (see Documentation/)

### External Data APIs (Future)
Additional integrations planned:
- **AEMET** - Spanish meteorological agency
- **Red Eléctrica de España** - National electricity grid
- **IDENA** - Navarra geographic information
- **OpenAI/Mistral** - LLM services

---

## 🔒 Security Notes

### Credentials Management
- ⚠️ **Never commit API keys or passwords**
- Use environment variables for sensitive data
- Tokens expire every 24 hours (sandbox)
- Keep Postman environments in `.gitignore`

### OAuth2 Tokens
- Obtained via Postman "Get Token" request
- Valid for 24 hours
- Must be refreshed daily
- Used by both Postman and MCP servers

---

## 📚 Additional Resources

### FIWARE Platform
- **NGSI-v2 Spec:** https://fiware.github.io/specifications/ngsiv2/stable/
- **Swagger Explorer:** https://swagger.lab.fiware.org/
- **FIWARE Catalogue:** https://github.com/FIWARE/catalogue

### Development Tools
- **Postman Docs:** https://learning.postman.com
- **MCP Protocol:** https://modelcontextprotocol.io
- **Cursor MCP:** https://docs.cursor.com/mcp

### Data Models
- **Smart Data Models:** https://github.com/smart-data-models
- **Data Model Search:** https://smartdatamodels.org/

---

**Last updated:** December 5, 2025  
**Maintainer:** Miguel Escribano
