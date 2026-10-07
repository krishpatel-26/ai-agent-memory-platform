import logging

from fastapi import FastAPI, HTTPException, Query

from .config import Settings
from .models import MemoryCreate
from .store import MemoryStore
from .service import MemoryService

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
settings = Settings()
store = MemoryStore(settings.db_path)
service = MemoryService(store)
app = FastAPI(title='AI Agent Memory Platform', version='1.1.0')


@app.get('/health')
def health():
    return {'status': 'ok', 'service': 'memory-platform'}


@app.post('/v1/memories')
def create(memory: MemoryCreate):
    try:
        return service.remember(memory)
    except Exception as exc:
        logging.exception('memory_write_failed')
        raise HTTPException(500, 'memory write failed') from exc


@app.get('/v1/memories/search')
def search(user_id: str, agent_id: str, q: str = Query(min_length=1), limit: int = 10):
    limit = max(1, min(limit, settings.max_results))
    return {'items': service.recall(user_id, agent_id, q, limit)}


@app.get('/v1/memories')
def list_memories(user_id: str, agent_id: str):
    return {'items': store.list(user_id, agent_id)}


@app.post('/v1/memories/consolidate')
def consolidate_memories(user_id: str, agent_id: str):
    try:
        items, source_count = service.consolidate(user_id, agent_id)
        return {'source_count': source_count, 'result_count': len(items), 'items': items}
    except Exception as exc:
        logging.exception('memory_consolidation_failed')
        raise HTTPException(500, 'memory consolidation failed') from exc
