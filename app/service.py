import logging
from .store import MemoryStore
from .scoring import rank_memories
log=logging.getLogger(__name__)
class MemoryService:
    def __init__(self,store:MemoryStore): self.store=store
    def remember(self,memory):
        row=self.store.add(memory); log.info('memory_stored id=%s agent=%s',row['id'],row['agent_id']); return row
    def recall(self,user_id,agent_id,query,limit=10):
        rows=self.store.list(user_id,agent_id); ranked=rank_memories(rows,query)
        return ranked[:limit]
