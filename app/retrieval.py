from .store import MemoryStore
from .models import Memory

class MemoryRetriever:
    def __init__(self, store: MemoryStore): self.store=store
    def retrieve(self, query: str, limit: int = 5) -> list[Memory]:
        terms={x.lower() for x in query.split() if len(x)>2}
        memories=self.store.list_memories()
        scored=[]
        for m in memories:
            text=f'{m.content} {m.memory_type}'.lower()
            score=sum(1 for t in terms if t in text) + m.confidence * 0.25
            if score: scored.append((score,m))
        scored.sort(key=lambda x:x[0], reverse=True)
        return [m for _,m in scored[:limit]]
