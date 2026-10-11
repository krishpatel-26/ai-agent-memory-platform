# Memory service incident response

1. Identify whether the incident concerns unauthorized retrieval, incorrect memory, retention, or availability.
2. Disable the affected write/retrieval path if cross-user exposure is suspected.
3. Preserve minimal audit metadata and avoid copying raw personal content into tickets.
4. Determine affected tenants and time window.
5. Correct or remove impacted records using the approved operational process.
6. Verify tenant isolation and retention behavior with regression tests.
7. Record root cause, impact, mitigation, and follow-up owner.

Do not run destructive cleanup solely because a retention evaluation returns expired; require the authorized deletion workflow.
