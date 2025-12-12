# STH Command

## Quick Reference
- **Postman**: Lines 1124-1290 (STH section)
- **Endpoint**: GET /STH/v1/contextEntities/type/{type}/id/{id}/attributes/{attr}

## Query Parameters
- `dateFrom`, `dateTo` - ISO format dates
- `lastN` - Last N values
- `aggrMethod` - max, min, sum
- `aggrPeriod` - hour, day, month

## Example
```
/STH/v1/contextEntities/type/Sensor/id/Sensor:001/attributes/temperature?lastN=20
```

