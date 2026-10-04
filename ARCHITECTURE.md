# Architecture

## Memory lifecycle

1. Validate agent and user scope.
2. Persist an immutable memory event.
3. Compute retrieval features from lexical overlap, recency, importance and confidence.
4. Rank candidates within the tenant scope.
5. Increment access counters for selected memories.
6. Consolidate repeated high-confidence memories into durable facts.

## Production boundaries

The API, memory policy, persistence adapter, ranking engine and optional model providers are separate modules. SQLite is the local reference store; a Postgres adapter can implement the same repository contract for deployment.

## Safety

Memory retrieval is always scoped by agent and user identifiers. Secrets belong in environment variables and are never stored in memory content by the platform itself.
