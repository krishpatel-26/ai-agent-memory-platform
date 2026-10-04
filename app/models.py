from datetime import datetime, timezone
from pydantic import BaseModel, Field

class MemoryCreate(BaseModel):
    agent_id: str = Field(min_length=1, max_length=100)
    user_id: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=3, max_length=5000)
    importance: float = Field(default=.5, ge=0, le=1)
    confidence: float = Field(default=.7, ge=0, le=1)
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Memory(MemoryCreate):
    id: str
    created_at: datetime
    access_count: int = 0

class SearchResult(BaseModel):
    memory: Memory
    score: float
    reasons: list[str]
