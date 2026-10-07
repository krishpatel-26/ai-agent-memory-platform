from __future__ import annotations

import sqlite3
import uuid
from datetime import datetime, timezone


class MemoryStore:
    def __init__(self, path='memory.db'):
        self.path = str(path)
        with sqlite3.connect(self.path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                agent TEXT NOT NULL,
                user TEXT NOT NULL,
                content TEXT NOT NULL,
                kind TEXT NOT NULL DEFAULT 'fact',
                importance REAL NOT NULL,
                confidence REAL NOT NULL,
                created_at TEXT NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed_at TEXT
            )''')
            self._migrate(db)

    @staticmethod
    def _migrate(db):
        columns = {row[1] for row in db.execute('PRAGMA table_info(memories)').fetchall()}
        migrations = {
            'kind': "ALTER TABLE memories ADD COLUMN kind TEXT NOT NULL DEFAULT 'fact'",
            'access_count': "ALTER TABLE memories ADD COLUMN access_count INTEGER NOT NULL DEFAULT 0",
            'last_accessed_at': "ALTER TABLE memories ADD COLUMN last_accessed_at TEXT",
        }
        for name, statement in migrations.items():
            if name not in columns:
                db.execute(statement)
        db.commit()

    def add(self, memory):
        row = {
            'id': str(uuid.uuid4()), 'agent_id': memory.agent_id, 'user_id': memory.user_id,
            'content': memory.content, 'kind': memory.kind, 'importance': memory.importance,
            'confidence': memory.confidence, 'created_at': memory.occurred_at.isoformat(),
            'access_count': 0, 'last_accessed_at': None,
        }
        with sqlite3.connect(self.path) as db:
            db.execute('''INSERT INTO memories
                (id, agent, user, content, kind, importance, confidence, created_at, access_count, last_accessed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                tuple(row.values()))
            db.commit()
        return row

    def list(self, user_id, agent_id):
        with sqlite3.connect(self.path) as db:
            rows = db.execute('''SELECT id,agent,user,content,kind,importance,confidence,
                created_at,access_count,last_accessed_at
                FROM memories WHERE user=? AND agent=? ORDER BY created_at DESC''',
                (user_id, agent_id)).fetchall()
        keys = ['id', 'agent_id', 'user_id', 'content', 'kind', 'importance', 'confidence',
                'created_at', 'access_count', 'last_accessed_at']
        return [dict(zip(keys, r)) for r in rows]

    def record_access(self, memory_ids: list[str]) -> None:
        if not memory_ids:
            return
        now = datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(self.path) as db:
            db.executemany('''UPDATE memories
                SET access_count = access_count + 1, last_accessed_at = ?
                WHERE id = ?''', [(now, memory_id) for memory_id in memory_ids])
            db.commit()
