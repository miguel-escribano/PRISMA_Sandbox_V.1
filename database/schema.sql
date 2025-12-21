-- PRISMA Database Schema
-- Version: v1.0-pitch
-- Date: 2025-12-21
-- Database: Supabase (PostgreSQL)

-- ============================================================================
-- TABLE: prisma_events
-- Purpose: Immutable event log - all sensor data and entity updates
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.prisma_events (
    event_id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    source TEXT,
    attributes JSONB NOT NULL,
    meta JSONB NOT NULL,
    raw JSONB,
    run_id BIGINT UNIQUE
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS prisma_events_entity_idx ON public.prisma_events (entity_id, ts DESC);
CREATE INDEX IF NOT EXISTS prisma_events_ts_idx ON public.prisma_events (ts DESC);
CREATE INDEX IF NOT EXISTS prisma_events_run_id_idx ON public.prisma_events (run_id);

COMMENT ON TABLE public.prisma_events IS 'Immutable event log - append-only storage for all entity updates';
COMMENT ON COLUMN public.prisma_events.event_id IS 'Unique event identifier (UUID)';
COMMENT ON COLUMN public.prisma_events.entity_id IS 'FIWARE entity ID (e.g., WeatherObserved:AEMET_API_Pamplona_Noain)';
COMMENT ON COLUMN public.prisma_events.entity_type IS 'FIWARE entity type (e.g., WeatherObserved, AirQualityObserved)';
COMMENT ON COLUMN public.prisma_events.ts IS 'Event timestamp (from sensor or synthetic scenario)';
COMMENT ON COLUMN public.prisma_events.source IS 'Data source (e.g., fiware_subscription, api_poll)';
COMMENT ON COLUMN public.prisma_events.attributes IS 'Entity attributes (sensor readings, metadata)';
COMMENT ON COLUMN public.prisma_events.meta IS 'Metadata (units, location, attribute types)';
COMMENT ON COLUMN public.prisma_events.raw IS 'Raw FIWARE payload (optional, for debugging)';
COMMENT ON COLUMN public.prisma_events.run_id IS 'Execution run identifier (for snapshot consistency)';

-- ============================================================================
-- TABLE: prisma_latest_state
-- Purpose: Current state snapshot - latest known value per entity
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.prisma_latest_state (
    entity_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    source TEXT,
    attributes JSONB NOT NULL,
    meta JSONB NOT NULL
);

COMMENT ON TABLE public.prisma_latest_state IS 'Current state snapshot - latest known value per entity';
COMMENT ON COLUMN public.prisma_latest_state.entity_id IS 'FIWARE entity ID (primary key)';
COMMENT ON COLUMN public.prisma_latest_state.entity_type IS 'FIWARE entity type';
COMMENT ON COLUMN public.prisma_latest_state.ts IS 'Timestamp of latest update';
COMMENT ON COLUMN public.prisma_latest_state.source IS 'Data source';
COMMENT ON COLUMN public.prisma_latest_state.attributes IS 'Latest entity attributes';
COMMENT ON COLUMN public.prisma_latest_state.meta IS 'Latest metadata';

-- ============================================================================
-- TABLE: prisma_decisions
-- Purpose: Agent decisions and risk assessments
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.prisma_decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    snapshot_ts BIGINT NOT NULL,
    alert_level TEXT NOT NULL,
    summary TEXT,
    key_factors JSONB,
    recommended_actions JSONB,
    decision_ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    scenario_ts TIMESTAMPTZ
);

-- Index for querying by snapshot
CREATE INDEX IF NOT EXISTS prisma_decisions_snapshot_ts_idx ON public.prisma_decisions (snapshot_ts);

COMMENT ON TABLE public.prisma_decisions IS 'Agent decisions and risk assessments (OODA DECIDE phase)';
COMMENT ON COLUMN public.prisma_decisions.id IS 'Unique decision identifier (UUID)';
COMMENT ON COLUMN public.prisma_decisions.snapshot_ts IS 'Snapshot timestamp (Unix milliseconds) - logical evaluation time';
COMMENT ON COLUMN public.prisma_decisions.alert_level IS 'Risk level: LOW, MEDIUM, HIGH, CRITICAL';
COMMENT ON COLUMN public.prisma_decisions.summary IS 'Human-readable situation summary (max 2 sentences)';
COMMENT ON COLUMN public.prisma_decisions.key_factors IS 'Array of key factors influencing the decision';
COMMENT ON COLUMN public.prisma_decisions.recommended_actions IS 'Array of recommended actions with responsible parties';
COMMENT ON COLUMN public.prisma_decisions.decision_ts IS 'Real-time timestamp when decision was made';
COMMENT ON COLUMN public.prisma_decisions.scenario_ts IS 'Synthetic scenario timestamp (for demo scenarios only)';

-- ============================================================================
-- STATISTICS (as of v1.0-pitch)
-- ============================================================================

-- Table sizes:
-- prisma_events: 1328 kB (160 rows)
-- prisma_decisions: 304 kB (8 rows)
-- prisma_latest_state: 176 kB (21 rows)

-- ============================================================================
-- NOTES
-- ============================================================================

-- 1. Row-Level Security (RLS) is disabled on all tables for MVP
-- 2. No foreign key constraints (FIWARE entities are dynamic)
-- 3. JSONB columns allow flexible schema evolution
-- 4. run_id enables snapshot consistency despite async event arrival
-- 5. scenario_ts is only used in demo scenarios (synthetic data)

