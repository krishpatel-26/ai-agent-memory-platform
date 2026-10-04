# Service Design

The memory service exposes three core operations: write, search, and consolidate.

Write creates a unique memory identifier and records creation and occurrence timestamps.

Search retrieves only memories belonging to the requested agent and user, then ranks them using a weighted score: 45% lexical relevance, 25% recency decay, 20% importance, and 10% confidence.

Consolidation detects repeated high-confidence content and promotes it to a durable fact. The operation is deterministic, idempotent for an existing fact, and can later be replaced by an LLM-backed summarizer behind the same service boundary.

This design keeps the default implementation local and deterministic while leaving clear seams for embeddings, reranking, vector storage, and model-based consolidation.
