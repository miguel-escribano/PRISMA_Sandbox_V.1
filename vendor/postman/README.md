# Postman Collections & Environments

Postman configurations for testing and interacting with the Telefónica IoT Platform (FIWARE Sandbox).

## 📍 Collection Source

**Primary Source:** MCP Server directories
```
C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\
└── ThinkingCities APIs sdmenvironment.postman_collection.json (50+ operations)

C:\Users\migue\FIWARE-MCP-Server-Auth-Miguel\
└── ThinkingCities APIs sdmenvironment.postman_collection.json (50+ operations)
```

**These are the authoritative, tested collections** - use these instead of archived versions.

## 📁 Structure

```
postman/
├── collections/                        # Optional: Copy from MCP folders
│   └── (Import directly from MCP folders - see below)
│
└── environments/                       # Create manually in Postman
    ├── Escribano_Dev.postman_environment.json      (/02_Escribano)
    └── SDM_Prod.postman_environment.json           (/sdmenvironment)
```

## 🚀 Quick Start

### 1. Import Collection from MCP Folder

**Method 1: Direct Import (Recommended)**
1. Open Postman
2. Click "Import"
3. Browse to: `C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\ThinkingCities APIs sdmenvironment.postman_collection.json`
4. Import

**Method 2: Copy to Repo (Optional)**
```bash
# Only if you need version control
copy "C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\ThinkingCities APIs sdmenvironment.postman_collection.json" collections\
```

### 2. Create Environments

**Create manually in Postman (2 environments needed):**

#### Environment 1: `PRISMA Sandbox - Dev`
```json
{
  "name": "PRISMA Sandbox - Dev",
  "values": [
    {"key": "service", "value": "sc_pamplona_sandbox", "enabled": true},
    {"key": "subservice", "value": "/02_Escribano", "enabled": true},
    {"key": "user", "value": "MiguelEscribano", "enabled": true},
    {"key": "password", "value": "YOUR_PASSWORD", "enabled": true},
    {"key": "auth_host", "value": "auth.iotplatform.telefonica.com", "enabled": true},
    {"key": "auth_port", "value": "15001", "enabled": true},
    {"key": "cb_host", "value": "cb.iotplatform.telefonica.com", "enabled": true},
    {"key": "cb_port", "value": "10027", "enabled": true},
    {"key": "sth_host", "value": "sth.iotplatform.telefonica.com", "enabled": true},
    {"key": "sth_port", "value": "18666", "enabled": true},
    {"key": "cep_host", "value": "cep.iotplatform.telefonica.com", "enabled": true},
    {"key": "cep_port", "value": "18090", "enabled": true},
    {"key": "token", "value": "", "enabled": true}
  ]
}
```

#### Environment 2: `PRISMA Sandbox - Prod`
```json
{
  "name": "PRISMA Sandbox - Prod",
  "values": [
    {"key": "service", "value": "sc_pamplona_sandbox", "enabled": true},
    {"key": "subservice", "value": "/sdmenvironment", "enabled": true},
    {"key": "user", "value": "MiguelEscribano", "enabled": true},
    {"key": "password", "value": "YOUR_PASSWORD", "enabled": true},
    {"key": "auth_host", "value": "auth.iotplatform.telefonica.com", "enabled": true},
    {"key": "auth_port", "value": "15001", "enabled": true},
    {"key": "cb_host", "value": "cb.iotplatform.telefonica.com", "enabled": true},
    {"key": "cb_port", "value": "10027", "enabled": true},
    {"key": "sth_host", "value": "sth.iotplatform.telefonica.com", "enabled": true},
    {"key": "sth_port", "value": "18666", "enabled": true},
    {"key": "cep_host", "value": "cep.iotplatform.telefonica.com", "enabled": true},
    {"key": "cep_port", "value": "18090", "enabled": true},
    {"key": "token", "value": "", "enabled": true}
  ]
}
```

### 3. Get OAuth Token

**First request to run:**
```
Collection → IDM & Auth → Get auth token
```

This will:
1. Authenticate with Telefónica platform
2. Automatically save token to `{{token}}` variable
3. Token is used in all subsequent requests

**Token expires after 24 hours** - re-run when needed.

### 4. Test Connection

**Run these to verify setup:**
```
1. Context Broker → Get Orion version
2. Context Broker → List all entities
```

## 📚 Collection Contents (50+ Operations)

### IDM & Auth (1 op)
- `Get auth token` - OAuth authentication

### Context Broker - Orion (26 ops)
**Basic Operations:**
- Get Orion version
- List all entities
- Get entity by ID
- Create entity
- Update entity attributes
- Delete entity

**Advanced Operations:**
- Batch entity creation
- Batch entity update
- Pagination queries
- Attribute queries
- Geo-queries (near, within)
- Subscriptions (create, list, update, delete)
- Registration discovery

### STH-Comet - Historical Data (3 ops)
- Get historical data
- Query time range
- Aggregations

### Perseo CEP - Rules Engine (5 ops)
- Create rule
- List rules
- Get rule by name
- Update rule
- Delete rule

### IoT Agent (15 ops)
- Device provisioning
- Service group management
- Measurement sending
- Device queries
- UltraLight & JSON protocols

## 🎯 Two Subservices Strategy

### `/02_Escribano` (Development)
**Purpose:** Safe testing and experimentation
- Full read/write access
- Create test entities
- Try subscriptions
- Experiment with rules
- No impact on production

**Use:** `PRISMA Sandbox - Dev` environment

### `/sdmenvironment` (Production)
**Purpose:** Real sensor monitoring
- **86 real sensors** across Pamplona
- AirQualityObserved (14 sensors)
- WeatherObserved (23 sensors)
- NoiseLevelObserved (10 sensors)
- **Read-only recommended**
- Be careful with modifications

**Use:** `PRISMA Sandbox - Prod` environment

## 🔒 Security Notes

- ⚠️ **Never commit credentials** to git
- Store passwords in Postman vault or environment variables
- Tokens expire every 24 hours
- Keep `.env` files out of version control

## 📖 Additional Resources

- **NGSI-v2 Spec:** https://fiware.github.io/specifications/ngsiv2/stable/
- **Swagger Explorer:** https://swagger.lab.fiware.org/
- **Smart Data Models:** https://github.com/smart-data-models
- **FIWARE Catalogue:** https://github.com/FIWARE/catalogue

---

**Source:** `C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\`  
**Collection:** ThinkingCities APIs sdmenvironment (50+ operations)  
**Last updated:** December 5, 2025
