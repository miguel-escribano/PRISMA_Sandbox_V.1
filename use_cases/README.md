# Casos de Uso PRISMA MVP

Documentación de casos de uso para el MVP de PRISMA.

**Pitch 19 diciembre 2025:** Dos casos demostrativos — mismo motor de inteligencia situacional, diferente dominio inyectado.

## Casos Activos

| Caso | Dominio | Duración demo | Descripción |
|------|---------|---------------|-------------|
| [Ola de Calor + Incendio](./CASO_USO_MVP_Ola_Calor_Incendio.md) | 🌡️ Ambiental | ~3 min | Cascada: calor + humo → colapso sanitario |
| [Ciberataque Infraestructura Agua](./CASO_USO_MVP_Ciberataque_Depuradora.md) | 🔐 Cyber | ~2 min | Cascada: ransomware → crisis hídrica pre-San Fermín |

## Estructura de la demo (7 min)

| Minuto | Contenido |
|--------|-----------|
| 0-1 | El problema (cascadas, silos, DANA Valencia) |
| 1-4 | **Caso 1:** Ola Calor + Incendio |
| 4-6 | **Caso 2:** Ciberataque Depuradora |
| 6-7 | Diferencial + Roadmap + Ask |

> **Mensaje clave:** "Mismo motor. Diferente cascada."

---

## Principio arquitectónico

| Capa | Qué es | ¿Cambia por caso? |
|------|--------|-------------------|
| **Inteligencia Situacional** | Motor de razonamiento: interpreta, predice, recomienda | **NO** (agnóstico) |
| **Dominio** | Conocimiento específico: entidades, umbrales, protocolos | **SÍ** (inyectado) |

Ambos casos demuestran que el **mismo motor** puede razonar sobre dominios completamente diferentes (ambiental vs cyber) si se le inyecta el conocimiento de dominio correcto.

---

## Criterios de selección de casos de uso

1. **Fácil de modelar** (datos disponibles)
2. **Dolor real y actual** (no hipotético)
3. **Presupuesto asignado** (obligación legal o política)
4. **Integración con ecosistema existente** (SOS Navarra 112, Tracasa)
5. **Cascada multi-sistema** (no evento aislado)

