# AI Agent Memory Platform

Production-oriented memory infrastructure for autonomous agents. The platform provides scoped long-term memory, idempotent persistence, relevance ranking, recency decay and a provider-independent API layer.

## Architecture
`API -> MemoryService -> MemoryStore -> SQLite` with ranking isolated as a replaceable retrieval component.

## Features
- Agent/user namespace isolation
- Persistent SQLite storage
- Importance + confidence aware retrieval
- Lexical relevance with recency decay
- Validation through Pydantic
- Structured application logging
- Environment-driven configuration
- Deterministic local execution; no API key required

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Tests: `pytest -q`

## Next evolution
The retrieval interface is intentionally provider-independent so embedding search, hybrid retrieval, memory consolidation and vector stores can be added without changing the API contract.