# Memory privacy boundaries

## Data minimization
Store only information needed for a defined user-facing purpose. Prefer a short, typed fact over a raw conversation transcript.

## Sensitivity
Do not persist credentials, authentication tokens, payment details, government identifiers, or other secrets in long-term memory. Sensitive personal data should require a separately reviewed product policy and explicit purpose.

## Retention
Retention evaluation is advisory. The current retention decision helper reports whether an item is past its policy window; it does not delete records. A production deletion job must be separately authorized, auditable, and retry-safe.

## Access
- Scope memory reads to the requesting user or tenant.
- Enforce authorization before retrieval, not only after retrieval.
- Log identifiers and decisions, not raw memory contents.
- Provide a correction and deletion path.

## Review checklist
- Is the memory necessary?
- Is the source and timestamp known?
- Is the item user-correctable?
- Is the retention rule explicit?
- Can access and deletion be audited?
