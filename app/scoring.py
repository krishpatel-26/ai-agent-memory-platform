import math

def lexical(query, text):
    q=set(query.lower().split())
    t=set(text.lower().split())
    return len(q & t) / max(len(q), 1)

def score(content, query, age_days, importance, confidence):
    relevance=lexical(query, content)
    recency=math.exp(-max(age_days, 0) / 30)
    return round(.45*relevance + .25*recency + .20*importance + .10*confidence, 4)
