import sqlite3
import uuid
from datetime import datetime, timezone

class MemoryStore:
    def __init__(self, path='memory.db'):
        self.path = str(path)
        with sqlite3.connect(self.path) as db:
            db.execute('CREATE TABLE IF NOT EXISTS memories (id TEXT PRIMARY KEY, agent TEXT, user TEXT, content TEXT, importance REAL, confidence REAL, created_at TEXT)')

    def add(self, memory):
        row = {
            'id': str(uuid.uuid4()), 'agent_id': memory.agent_id, 'user_id': memory.user_id,
            'content': memory.content, 'importance': memory.importance,
            'confidence': memory.confidence, 'created_at': memory.occurred_at.isoformat()
        }
        with sqlite3.connect(self.path) as db:
            db.execute('INSERT INTO memories VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (row['id'], row['agent_id'], row['user_id'], row['content'], row['importance'], row['confidence'], row['created_at']))
            db.commit()
        return row

    def list(self, user_id, agent_id):
        with sqlite3.connect(self.path) as db:
            rows=db.execute('SELECT id,agent,user,content,importance,confidence,created_at FROM memories WHERE user=? AND agent=?', (user_id,agent_id)).fetchall()
        return [dict(zip(['id','agent_id','user_id','content','importance','confidence','created_at'], r)) for r in rows]
