# Test Plan

- Verify that memories from one agent/user scope never appear in another scope.
- Verify lexical matches outrank unrelated memories.
- Verify older memories receive lower recency weight.
- Verify repeated high-confidence memories are eligible for consolidation.
- Verify invalid payloads are rejected at the API boundary.
- Verify the health endpoint reports an operational service.

The suite should remain deterministic and runnable without external model providers.
