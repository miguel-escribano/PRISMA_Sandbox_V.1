# IoT Agent - Telefónica Sandbox

## 📡 Endpoints disponibles

### IoT Agent JSON
- **Host**: `iota-json.iotplatform.telefonica.com`
- **Puerto datos**: `8185` (HTTP)
- **Puerto gestión**: `8088` (HTTPS) - usar `iota.iotplatform.telefonica.com`
- **URL envío datos**: `http://iota-json.iotplatform.telefonica.com:8185/iot/json`
- **URL gestión**: `https://iota.iotplatform.telefonica.com:8088`

### IoT Agent Ultralight
- **Host**: `iota-ul.iotplatform.telefonica.com`
- **Puerto**: `8085`

### IoT Agent Manager
- **Host**: `iota.iotplatform.telefonica.com`
- **Puerto**: `8088`

## 🔐 Autenticación

Usa las mismas credenciales que el Context Broker:
- **Service**: `sc_pamplona_sandbox`
- **Subservice**: `/02_Escribano` o `/sdmenvironment`
- **Headers**: `X-Auth-Token` (obtener de Keystone)

## 🔍 Descubrir Endpoints

**Antes de provisionar, consulta los endpoints disponibles:**

1. Usa el recurso MCP FIWARE: `fiware://examples`
2. Contiene la colección Postman con todos los endpoints
3. Busca ejemplos de IoT Agent JSON en la sección "IoTAs"

## 📋 Provisionar dispositivo IoT Agent JSON

### Patrón Autoprovision (Recomendado)

**Ventajas:**
- ✅ No necesitas registrar devices manualmente
- ✅ Los devices se crean automáticamente al enviar datos
- ✅ Device ID = Entity ID (más simple)
- ✅ Mismo patrón que `/sdmenvironment`

**Pasos:**

1. Crear Service Group con autoprovision
2. Enviar datos (el device se crea automáticamente)

**Service Group con Autoprovision:**
```json
{
  "services": [{
    "apikey": "tu_api_key",
    "entity_type": "TuTipoEntidad",
    "resource": "/iot/json",
    "protocol": "IoTA-JSON",
    "transport": "HTTP",
    "autoprovision": true,
    "entityNameExp": "id",
    "payloadType": "ngsiv2"
  }]
}
```

**Campos clave:**
- `autoprovision: true` - Crea devices automáticamente
- `entityNameExp: "id"` - Usa device_id como entity_id
- `payloadType: "ngsiv2"` - Formato de datos NGSI-v2

**Enviar datos (formato NGSI-v2):**
```json
{
  "atributo1": {
    "value": valor1,
    "type": "Number"
  },
  "atributo2": {
    "value": "valor2",
    "type": "Text"
  }
}
```

**Ejemplo completo:** Ver sección "Ejemplo completo: REE Navarra" más abajo.

---

### Patrón Manual (Alternativo)

Si necesitas control total sobre el device:

### 1. Crear Service Group

**Endpoint**: `POST https://iota.iotplatform.telefonica.com:8088/iot/services`

**Headers**:
```
Fiware-Service: sc_pamplona_sandbox
Fiware-ServicePath: /02_Escribano
X-Auth-Token: <TOKEN>
Content-Type: application/json
```

**Body**:
```json
{
  "services": [{
    "apikey": "tu_api_key",
    "cbroker": "https://cb.iotplatform.telefonica.com:10027",
    "entity_type": "TuTipoEntidad",
    "resource": "/iot/json"
  }]
}
```

### 2. Registrar dispositivo

**Endpoint**: `POST https://iota.iotplatform.telefonica.com:8088/iot/devices`

**Headers**: (igual que arriba)

**Body**:
```json
{
  "devices": [{
    "device_id": "tu_device_id",
    "entity_name": "TuEntidad:ID",
    "entity_type": "TuTipoEntidad",
    "protocol": "IoTA-JSON",
    "transport": "HTTP",
    "attributes": [
      {"object_id": "t", "name": "temperature", "type": "Number"}
    ],
    "static_attributes": [
      {"name": "location", "type": "geo:json", "value": {"type": "Point", "coordinates": [-1.7125, 42.8367]}}
    ]
  }]
}
```

### 3. Enviar datos al IoT Agent

**Endpoint**: `POST http://iota-json.iotplatform.telefonica.com:8185/iot/json?k=<API_KEY>&i=<DEVICE_ID>`

**Headers**:
```
Fiware-Service: sc_pamplona_sandbox
Fiware-ServicePath: /02_Escribano
Content-Type: application/json
```

**Body**:
```json
{
  "atributo1": valor1,
  "atributo2": valor2
}
```

**Nota**: NO necesitas `X-Auth-Token` para enviar datos (puerto 8185).

## 🔍 Consultar configuración

### Listar devices registrados
```
GET https://iota.iotplatform.telefonica.com:8088/iot/devices
Headers: Fiware-Service, Fiware-ServicePath, X-Auth-Token
```

### Listar service groups
```
GET https://iota.iotplatform.telefonica.com:8088/iot/services
Headers: Fiware-Service, Fiware-ServicePath, X-Auth-Token
```

### Ver device específico
```
GET https://iota.iotplatform.telefonica.com:8088/iot/devices/{device_id}?protocol=IoTA-JSON
Headers: Fiware-Service, Fiware-ServicePath, X-Auth-Token
```

## 🗑️ Eliminar configuración

### Eliminar device
```
DELETE https://iota.iotplatform.telefonica.com:8088/iot/devices/{device_id}?protocol=IoTA-JSON
Headers: Fiware-Service, Fiware-ServicePath, X-Auth-Token
```

### Eliminar service group
```
DELETE https://iota.iotplatform.telefonica.com:8088/iot/services?apikey={API_KEY}&resource=/iot/json
Headers: Fiware-Service, Fiware-ServicePath, X-Auth-Token
```

## 📊 Ejemplo completo: REE Navarra (Patrón Autoprovision)

**Configuración:**
- **Device ID**: `EnergyDemand:Navarra:REE` (mismo que Entity ID)
- **Entity**: `EnergyDemand:Navarra:REE`  
- **API Key**: `ree_navarra_api_key`  
- **Subservice**: `/02_Escribano`

**1. Crear Service Group:**
```bash
POST https://iota.iotplatform.telefonica.com:8088/iot/services
Headers:
  - Fiware-Service: sc_pamplona_sandbox
  - Fiware-ServicePath: /02_Escribano
  - X-Auth-Token: <TOKEN>
  - Content-Type: application/json

Body:
{
  "services": [{
    "apikey": "ree_navarra_api_key",
    "entity_type": "EnergyDemandObserved",
    "resource": "/iot/json",
    "protocol": "IoTA-JSON",
    "transport": "HTTP",
    "autoprovision": true,
    "entityNameExp": "id",
    "payloadType": "ngsiv2"
  }]
}
```

**2. Enviar datos (formato NGSI-v2):**
```bash
POST http://iota-json.iotplatform.telefonica.com:8185/iot/json?k=ree_navarra_api_key&i=EnergyDemand:Navarra:REE
Headers:
  - Fiware-Service: sc_pamplona_sandbox
  - Fiware-ServicePath: /02_Escribano
  - Content-Type: application/json

Body:
{
  "demand": {
    "value": 450.5,
    "type": "Number"
  },
  "dateObserved": {
    "value": "2025-01-06T10:30:00Z",
    "type": "DateTime"
  },
  "location": {
    "value": {
      "type": "Point",
      "coordinates": [-1.7125, 42.8367]
    },
    "type": "geo:json"
  }
}
```

**Resultado:**
- ✅ Device `EnergyDemand:Navarra:REE` se crea automáticamente
- ✅ Entity `EnergyDemand:Navarra:REE` se actualiza en Context Broker
- ✅ Device ID = Entity ID (patrón `/sdmenvironment`)

## 📚 Referencias

- Config completa: `config.py` (líneas 53-67)
- Postman examples: `C:\Users\migue\FIWARE-MCP-Server-02_Escribano\postman\fiware-ngsi-v2-examples.json`
- Documentación FIWARE: https://fiware-iotagent-json.readthedocs.io/

## ⚠️ Notas importantes

1. **Puerto 8185 (datos)**: HTTP, NO requiere auth token
2. **Puerto 8088 (gestión)**: HTTPS, SÍ requiere auth token
3. **Service Group**: Debe existir ANTES de enviar datos
4. **Device**: Debe estar registrado ANTES de enviar datos
5. **API Key**: Debe coincidir entre Service Group y petición de datos
