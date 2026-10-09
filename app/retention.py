from datetime import datetime, timezone

DEFAULT_RETENTION_DAYS = 180
PINNED_KINDS = {"preference", "goal"}

def is_expired(memory: dict, now: datetime | None = None, retention_days: int = DEFAULT_RETENTION_DAYS) -> bool:
    """Return whether a memory is beyond retention; durable user preferences/goals are exempt."""
    if str(memory.get("kind", "fact")).lower() in PINNED_KINDS:
        return False
    if retention_days < 0:
        raise ValueError("retention_days must be non-negative")
    created = datetime.fromisoformat(str(memory["created_at"]))
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    reference = now or datetime.now(timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)
    return (reference - created).total_seconds() >= retention_days * 86400
