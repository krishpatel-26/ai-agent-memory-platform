from datetime import datetime, timezone

DEFAULT_RETENTION_DAYS = 180
PINNED_KINDS = {"preference", "goal"}


def retention_decision(
    memory: dict,
    now: datetime | None = None,
    retention_days: int = DEFAULT_RETENTION_DAYS,
) -> dict:
    """Explain retention eligibility without deleting or mutating stored memory."""
    if retention_days < 0:
        raise ValueError("retention_days must be non-negative")

    kind = str(memory.get("kind", "fact")).lower()
    if kind in PINNED_KINDS:
        return {"expired": False, "reason": "pinned_kind", "retention_days": None}

    created = datetime.fromisoformat(str(memory["created_at"]))
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    reference = now or datetime.now(timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)

    age_seconds = max(0.0, (reference - created).total_seconds())
    expired = age_seconds >= retention_days * 86400
    return {
        "expired": expired,
        "reason": "retention_elapsed" if expired else "within_retention",
        "age_days": round(age_seconds / 86400, 3),
        "retention_days": retention_days,
    }


def is_expired(memory: dict, now: datetime | None = None, retention_days: int = DEFAULT_RETENTION_DAYS) -> bool:
    """Compatibility helper: evaluate expiration; never delete memory."""
    return retention_decision(memory, now, retention_days)["expired"]
