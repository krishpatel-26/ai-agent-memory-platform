import math
from datetime import datetime, timezone


def rank_memories(rows, query):
    terms = {x.lower() for x in query.split() if len(x) > 1}
    now = datetime.now(timezone.utc)

    def score(row):
        text = row['content'].lower()
        lexical = sum(1 for term in terms if term in text)
        importance = float(row.get('importance', .5))
        confidence = float(row.get('confidence', .5))
        age = max((now - datetime.fromisoformat(row['created_at'])).total_seconds() / 86400, 0)
        recency = math.exp(-age / 30)
        access = min(int(row.get('access_count', 0)), 10) / 10
        return lexical * 4 + importance * 2 + confidence + recency + access * .5

    return sorted(rows, key=score, reverse=True)
