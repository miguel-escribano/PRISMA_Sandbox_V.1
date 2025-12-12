# Subscriptions Command

## Quick Reference
- **Postman**: Lines 887-1121 (Subscriptions section)
- **Endpoint**: POST /v2/subscriptions

## Basic Structure
```json
{
  "description": "Description",
  "subject": {
    "entities": [{ "id": "EntityID", "type": "EntityType" }],
    "condition": { "attrs": [] }
  },
  "notification": {
    "http": { "url": "https://webhook-url" },
    "attrs": []
  }
}
```

## Key Points
- Empty `attrs` = all attributes
- Use for n8n webhooks, alerts, STH
- Variables: `${id}`, `${type}`, `${attributeName}`

