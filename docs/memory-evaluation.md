# Memory evaluation plan

## Retrieval metrics
- Recall@k on a curated query-to-memory set.
- Precision@k to measure irrelevant memories returned.
- MRR for the rank of the first useful memory.
- Tenant isolation: zero cross-tenant retrievals in adversarial tests.

## Lifecycle metrics
- Expiration-decision agreement against a labeled policy set.
- Percentage of records with source and timestamp metadata.
- Number of unresolved conflicting memories.
- Deletion-job retries and failures (for a future deletion worker).

## Test set design
Include paraphrased queries, stale facts, explicit user corrections, conflicting memories, empty stores, and users with overlapping terminology. Keep evaluation data synthetic or consented.
