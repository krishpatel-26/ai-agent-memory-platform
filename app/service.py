import logging
from datetime import datetime

from .consolidation import consolidate
from .models import Memory, MemoryCreate
from .scoring import rank_memories
from .store import MemoryStore

log = logging.getLogger(__name__)


class MemoryService:
    def __init__(self, store: MemoryStore):
        self.store = store

    def remember(self, memory: MemoryCreate):
        row = self.store.add(memory)
        log.info('memory_stored id=%s agent=%s kind=%s', row['id'], row['agent_id'], row['kind'])
        return row

    def recall(self, user_id, agent_id, query, limit=10):
        rows = self.store.list(user_id, agent_id)
        ranked = rank_memories(rows, query)[:limit]
        self.store.record_access([row['id'] for row in ranked])
        for row in ranked:
            row['access_count'] = int(row.get('access_count', 0)) + 1
        return ranked

    def consolidate(self, user_id, agent_id):
        rows = self.store.list(user_id, agent_id)
        memories = [self._to_memory(row) for row in rows]
        consolidated = consolidate(memories)
        log.info('memory_consolidated agent=%s user=%s source_count=%d result_count=%d',
                 agent_id, user_id, len(memories), len(consolidated))
        return consolidated, len(memories)

    @staticmethod
    def _to_memory(row):
        occurred_at = datetime.fromisoformat(row['created_at'])
        return Memory(
            id=row['id'], agent_id=row['agent_id'], user_id=row['user_id'], content=row['content'],
            kind=row['kind'], importance=row['importance'], confidence=row['confidence'],
            occurred_at=occurred_at, created_at=occurred_at, access_count=row['access_count'],
            last_accessed_at=(datetime.fromisoformat(row['last_accessed_at'])
                              if row['last_accessed_at'] else None),
        )
