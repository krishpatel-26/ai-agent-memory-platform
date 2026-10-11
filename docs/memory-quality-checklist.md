# Memory quality checklist

Before writing a memory:
- Normalize whitespace and avoid duplicate facts.
- Record the source and observed time where available.
- Separate stable preferences from temporary events.
- Preserve uncertainty instead of converting guesses into facts.
- Avoid storing secrets or unnecessary sensitive details.

Before retrieval:
- Apply tenant/user scope.
- Rank by relevance and recency.
- Exclude expired items according to policy.
- Return provenance with retrieved items.
- Test that a query cannot access another user's records.

Before consolidation:
- Keep conflicting source facts visible.
- Prefer newer explicit corrections over older inferred values.
- Do not merge items solely because they share a few words.
