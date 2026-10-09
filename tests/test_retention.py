from datetime import datetime, timedelta, timezone
import pytest
from app.retention import is_expired

def test_old_fact_expires():
    now = datetime.now(timezone.utc)
    memory = {"kind": "fact", "created_at": (now - timedelta(days=181)).isoformat()}
    assert is_expired(memory, now=now)

def test_goal_is_retained_even_when_old():
    now = datetime.now(timezone.utc)
    memory = {"kind": "goal", "created_at": (now - timedelta(days=500)).isoformat()}
    assert not is_expired(memory, now=now)

def test_negative_retention_is_rejected():
    with pytest.raises(ValueError):
        is_expired({"kind": "fact", "created_at": datetime.now(timezone.utc).isoformat()}, retention_days=-1)
