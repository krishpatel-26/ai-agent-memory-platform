import sqlite3

class MemoryStore:
    def __init__(self, path='memory.db'):
        self.path = path
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE IF NOT EXISTS memories (id TEXT PRIMARY KEY, agent TEXT, user TEXT, content TEXT, importance REAL, confidence REAL)')

    def add(self, memory):
        with sqlite3.connect(self.path) as db:
            db.execute('INSERT INTO memories VALUES (?, ?, ?, ?, ?, ?)', memory)
            db.commit()

    def by_scope(self, agent, user):
        with sqlite3.connect(self.path) as db:
            return db.execute('SELECT * FROM memories WHERE agent=? AND user=?', (agent, user)).fetchall()
