from app.models import MemoryCreate
from app.store import MemoryStore
from app.service import MemoryService


def test_memory_is_scoped_and_ranked(tmp_path):
    s = MemoryService(MemoryStore(str(tmp_path / 'm.db')))
    s.remember(MemoryCreate(user_id='u1', agent_id='a1', content='User prefers Python APIs', kind='preference', importance=.9, confidence=.95))
    s.remember(MemoryCreate(user_id='u1', agent_id='a2', content='User prefers Python APIs'))
    hits = s.recall('u1', 'a1', 'Python', 5)
    assert len(hits) == 1 and hits[0]['agent_id'] == 'a1'
    assert hits[0]['access_count'] == 1


def test_consolidation_merges_same_kind_and_keeps_best_metadata(tmp_path):
    s = MemoryService(MemoryStore(str(tmp_path / 'm.db')))
    s.remember(MemoryCreate(user_id='u', agent_id='a', content='Uses Python', kind='preference', confidence=.7, importance=.6))
    s.remember(MemoryCreate(user_id='u', agent_id='a', content='Uses FastAPI', kind='preference', confidence=.95, importance=.8))
    items, source_count = s.consolidate('u', 'a')
    assert source_count == 2
    assert len(items) == 1
    assert items[0].kind == 'preference'
    assert items[0].confidence == .95
    assert 'Uses Python' in items[0].content and 'Uses FastAPI' in items[0].content
