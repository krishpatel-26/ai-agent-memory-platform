# API Contract

## Write memory

`POST /v1/memories`

Request fields: `agent_id`, `user_id`, `content`, `importance`, `confidence`, and optional `occurred_at`.

## Search

`GET /v1/memories/search`

Required query fields: `agent_id`, `user_id`, and `q`. The response contains the memory, numeric relevance score, and human-readable ranking reasons.

## Consolidate

`POST /v1/memories/consolidate`

Consolidation is scoped to one agent and user. Repeated high-confidence memories are candidates for durable fact promotion.

## Health

`GET /health` returns a small readiness payload suitable for container probes.
