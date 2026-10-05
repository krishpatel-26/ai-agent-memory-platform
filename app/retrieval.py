from .store import MemoryStore

class MemoryRetriever:
    def __init__(self, store: MemoryStore): self.store=store

    def retrieve(self, user_id: str, agent_id: str, query: str, limit: int = 5) -> list[dict]:
        terms={x.lower() for x in query.split() if len(x)>2}
        rows=self.store.list(user_id, agent_id)
        scored=[]
        for row in rows:
            lexical=sum(1 for term in terms if term in row['content'].lower())
            score=lexical + float(row['confidence'])*0.25 + float(row['importance'])*0.1
            if score > 0: scored.append((score,row))
        scored.sort(key=lambda x:x[0], reverse=True)
        return [row for _,row in scored[:limit]]
