from app.models import MemoryCreate
from app.store import MemoryStore
from app.retrieval import MemoryRetriever

def test_retriever_ranks_matching_memory(tmp_path):
    s=MemoryStore(tmp_path/'memory.db')
    s.add(MemoryCreate(agent_id='a',user_id='u',content='prefers Python and FastAPI',confidence=.9))
    s.add(MemoryCreate(agent_id='a',user_id='u',content='studies robotics',confidence=.8))
    hits=MemoryRetriever(s).retrieve('u','a','Python',limit=1)
    assert len(hits)==1 and 'Python' in hits[0]['content']
