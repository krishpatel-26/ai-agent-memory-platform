from app.models import MemoryCreate
from app.store import MemoryStore
from app.service import MemoryService

def test_memory_is_scoped_and_ranked(tmp_path):
 s=MemoryService(MemoryStore(str(tmp_path/'m.db')))
 s.remember(MemoryCreate(user_id='u1',agent_id='a1',content='User prefers Python APIs',kind='preference',importance=.9,confidence=.95))
 s.remember(MemoryCreate(user_id='u1',agent_id='a2',content='User prefers Python APIs'))
 hits=s.recall('u1','a1','Python',5)
 assert len(hits)==1 and hits[0]['agent_id']=='a1'
