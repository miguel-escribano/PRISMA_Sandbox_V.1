# Perseo Command

## Quick Reference
- **Postman**: Lines 1292-1477 (Perseo CEP section)
- **Endpoint**: /rules

## Rule Structure
```json
{
    "name": "RuleName",
    "text": "EPL query",
    "action": { "type": "email|update|post", "parameters": {...} }
}
```

## Action Types
- `email` - Send email alerts
- `update` - Update another entity
- `post` - HTTP webhook

## EPL Pattern
```sql
select *,"RuleName" as ruleName from pattern [every ev=iotEvent((cast(`type`?, String) = "EntityType") AND (cast(cast(`attr`?, String), float) > THRESHOLD))]
```

