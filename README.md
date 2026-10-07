Production-oriented memory infrastructure for autonomous agents with scoped persistence, deterministic retrieval, access telemetry, and confidence-aware consolidation.

Architecture: API -> MemoryService -> MemoryStore -> SQLite.

Features:
- Agent/user namespace isolation
- SQLite persistence with lightweight schema migration
- Importance, confidence, recency, and capped access-frequency ranking
- Typed memory kinds for deterministic consolidation
- Read-only consolidation endpoint
- Pydantic validation and structured logging
- Deterministic local execution with no API key required

Run with `pip install -r requirements.txt` and `uvicorn app.main:app --reload`.

Consolidation: POST /v1/memories/consolidate?user_id=<user>&agent_id=<agent> returns one candidate per memory kind. The highest-confidence memory anchors metadata while distinct content is merged with a 2,000-character cap.
