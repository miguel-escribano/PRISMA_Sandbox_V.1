# Vendor Setup Checklist

Quick reference for setting up all vendor integrations.

## ✅ Completed

- [x] Directory structure created
- [x] README documentation written
- [x] MCP server documentation

## 📍 Postman Collections Location

### MCP Server Directories (Source of Truth)

**Postman collections are maintained in the MCP server directories:**

```
C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\
└── ThinkingCities APIs sdmenvironment.postman_collection.json

C:\Users\migue\FIWARE-MCP-Server-Auth-Miguel\
└── ThinkingCities APIs sdmenvironment.postman_collection.json
```

**These collections contain 50+ operations:**
- Orion Context Broker (26 ops)
- STH Historical Data (3 ops)
- Perseo CEP (5 ops)
- IoT Agent (15 ops)

## 🔧 Setup Options

### Option A: Use Directly from MCP Folders (Recommended)
**Pros:** Always up-to-date, single source of truth
**Cons:** Per-developer setup

1. Open Postman
2. Import from: `C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\ThinkingCities APIs sdmenvironment.postman_collection.json`
3. Create environment variables (see below)

### Option B: Copy to Repo (Optional)
Only if you need version control or team sharing:

```bash
# Copy collection (optional)
copy "C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\ThinkingCities APIs sdmenvironment.postman_collection.json" vendor\postman\collections\

# Create environments
# (manually in Postman, export to vendor/postman/environments/)
```

## 🔑 Environment Configuration

Create two Postman environments manually:

### Environment 1: Escribano_Dev (`/02_Escribano`)
```json
{
  "name": "PRISMA Sandbox - Dev",
  "values": [
    {"key": "service", "value": "sc_pamplona_sandbox"},
    {"key": "subservice", "value": "/02_Escribano"},
    {"key": "user", "value": "MiguelEscribano"},
    {"key": "password", "value": "YOUR_PASSWORD"},
    {"key": "auth_host", "value": "auth.iotplatform.telefonica.com"},
    {"key": "auth_port", "value": "15001"},
    {"key": "cb_host", "value": "cb.iotplatform.telefonica.com"},
    {"key": "cb_port", "value": "10027"},
    {"key": "token", "value": ""}
  ]
}
```

### Environment 2: SDM_Prod (`/sdmenvironment`)
```json
{
  "name": "PRISMA Sandbox - Prod",
  "values": [
    {"key": "service", "value": "sc_pamplona_sandbox"},
    {"key": "subservice", "value": "/sdmenvironment"},
    {"key": "user", "value": "MiguelEscribano"},
    {"key": "password", "value": "YOUR_PASSWORD"},
    {"key": "auth_host", "value": "auth.iotplatform.telefonica.com"},
    {"key": "auth_port", "value": "15001"},
    {"key": "cb_host", "value": "cb.iotplatform.telefonica.com"},
    {"key": "cb_port", "value": "10027"},
    {"key": "token", "value": ""}
  ]
}
```

## 🔧 MCP Server Setup

### MCP Servers Already Configured

**Locations:**
```
C:\Users\migue\FIWARE-MCP-Server-Auth-Environment\
C:\Users\migue\FIWARE-MCP-Server-Auth-Miguel\
```

**Configuration in Cursor:**
- Already set up in Cursor settings
- Reference: `vendor/mcp/README.md`

### Verify MCP Connection
1. Open Cursor chat
2. Test: "Query version from Context Broker"
3. Should connect to sandbox

## 📝 Next Steps

### Immediate (Before Development)
- [ ] Import Postman collection from MCP folder
- [ ] Create two environments in Postman
- [ ] Test "Get auth token" request
- [ ] Verify entity queries work in both subservices

### Short-term
- [ ] Test MCP server integration in Cursor chat
- [ ] Document common query patterns
- [ ] Create example entity templates
- [ ] Test subscription workflows

### Optional
- [ ] Copy collection to repo for version control
- [ ] Set up automated token refresh
- [ ] Create Postman tests
- [ ] Add monitoring

---

## 🎯 Key Points

1. **Postman collections live in MCP folders** - not archived versions
2. **Two subservices** - dev (`/02_Escribano`) and prod (`/sdmenvironment`)
3. **MCP servers already configured** - just need Postman environments
4. **50+ proven operations** - tested and working

---

**Priority:** Import collection from MCP folder, create environments

**Last updated:** December 5, 2025
