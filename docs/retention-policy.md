# Memory Retention Policy

The retention helper in `app/retention.py` separates expiration policy from storage mutation.

- Facts and events expire after the configured retention window (180 days by default).
- Preferences and goals are retained because they represent durable context.
- Naive timestamps are interpreted as UTC.
- Negative retention windows are rejected.
- The helper only evaluates expiration; it does not delete data. A caller must apply deletion through the storage layer and its authorization boundary.

This separation makes retention testable and prevents a policy check from silently mutating persisted memories.
