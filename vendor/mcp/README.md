# MCP Server Configurations

Model Context Protocol (MCP) servers enable Cursor to interact directly with the FIWARE Sandbox from this chat interface.

## 📍 Configuration Location

MCP servers are configured in Cursor's settings, **not in this repository**.

**Configuration files location:**
```
Windows: %APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
macOS: ~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

## 🔧 Available MCP Servers

### 1. FIWARE Context Broker - Environment (Production)
**Service:** `sc_pamplona_sandbox`  
**Subservice:** `/sdmenvironment`

**Capabilities:**
- Query real sensor entities (86 sensors)
- Read air quality, weather, noise data
- Check entity status
- Time-series data access

**Usage in chat:**
```
"Show me all AirQualityObserved entities"
"Query weather data from /sdmenvironment"
```

### 2. FIWARE Context Broker - Miguel (Development)
**Service:** `sc_pamplona_sandbox`  
**Subservice:** `/02_Escribano`

**Capabilities:**
- Create test entities
- Update entity attributes
- Delete entities
- Manage subscriptions
- Full read/write access

**Usage in chat:**
```
"Create a test Hospital entity in /02_Escribano"
"Delete entity urn:ngsi-ld:Test:001"
```

## 🚀 Setup Instructions

### Prerequisites
- Cursor IDE installed
- MCP servers extension enabled
- Valid Telefónica sandbox credentials

### Configuration Steps

1. **Open Cursor Settings**
   - Press `Ctrl+,` (Windows) or `Cmd+,` (Mac)
   - Search for "MCP"

2. **Add FIWARE MCP Server** (if not already configured)
   ```json
   {
     "mcpServers": {
       "fiware-environment": {
         "command": "node",
         "args": ["/path/to/fiware-mcp-server"],
         "env": {
           "FIWARE_SERVICE": "sc_pamplona_sandbox",
           "FIWARE_SUBSERVICE": "/sdmenvironment",
           "FIWARE_CB_URL": "https://cb.iotplatform.telefonica.com:10027",
           "OAUTH_TOKEN": "your-token-here"
         }
       },
       "fiware-miguel": {
         "command": "node",
         "args": ["/path/to/fiware-mcp-server"],
         "env": {
           "FIWARE_SERVICE": "sc_pamplona_sandbox",
           "FIWARE_SUBSERVICE": "/02_Escribano",
           "FIWARE_CB_URL": "https://cb.iotplatform.telefonica.com:10027",
           "OAUTH_TOKEN": "your-token-here"
         }
       }
     }
   }
   ```

3. **Restart Cursor** to load configurations

4. **Verify Connection**
   - Open a chat
   - Try: "Query version from FIWARE Context Broker"

## 🔑 Authentication

MCP servers use the **same OAuth2 tokens** as Postman.

**Token Management:**
- Tokens expire every 24 hours
- Refresh by running Postman "Get Token" request
- Update MCP config with new token
- Or configure automatic token refresh (advanced)

## 💡 Usage Tips

### Query Production Data
```
"Show me all entities in /sdmenvironment"
"Get AirQualityObserved data from last hour"
"List all WeatherObserved sensors"
```

### Development/Testing
```
"Create a Hospital entity in /02_Escribano"
"Update temperature attribute to 25.5"
"Subscribe to changes on WeatherObserved entities"
```

### Architecture Queries
```
"What entities exist in the sandbox?"
"Show me the schema of AirQualityObserved"
"List all subscriptions"
```

## 🛠️ Troubleshooting

### "Failed to connect to Context Broker"
- Check token expiration
- Verify service/subservice values
- Confirm network connectivity

### "Permission denied"
- Production (`/sdmenvironment`) may be read-only
- Use dev subservice (`/02_Escribano`) for write operations

### "MCP server not responding"
- Restart Cursor
- Check MCP server logs
- Verify configuration syntax

## 📚 Additional Resources

- **MCP Protocol:** https://modelcontextprotocol.io
- **FIWARE APIs:** https://fiware.github.io/specifications/ngsiv2/stable/
- **Cursor MCP Docs:** https://docs.cursor.com/mcp

---

**Note:** MCP configurations are **per-user, per-machine**. Each developer needs their own setup.

**Last updated:** December 5, 2025
