from app.models import MemoryCreate
from app.store import MemoryStore
from app.retrieval import MemoryRetriever

def test_retriever_ranks_matching_memory(tmp_path):
    s=MemoryStore(tmp_path/'memory.jsonl')
    s.add(MemoryCreate(agent_id='a',memory_type='preference',content='prefers Python and FastAPI',confidence=.9))
    s.add(MemoryCreate(agent_id='a',memory_type='fact',content='studies robotics',confidence=.8))
    hits=MemoryRetriever(s).retrieve('Python',limit=1)
    assert len(hits)==1 and 'Python' in hits[0].content
