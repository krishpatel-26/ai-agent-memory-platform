# Memory Retrieval & Consolidation

The platform now separates persistence from retrieval and consolidation.

1. **Write** memories through the existing service/store layer.
2. **Retrieve** with `MemoryRetriever`, using lightweight lexical matching plus confidence weighting. This deterministic implementation is intentionally local and can later be replaced by an embedding index without changing the service contract.
3. **Consolidate** related memories by type, retaining the highest-confidence metadata while combining distinct content.

The design avoids external model dependencies, making local testing deterministic. A future vector adapter can implement the same retrieval boundary for semantic search.
