from collections import defaultdict
from .models import Memory

def consolidate(memories: list[Memory]) -> list[Memory]:
    groups=defaultdict(list)
    for m in memories: groups[m.memory_type].append(m)
    result=[]
    for kind, items in groups.items():
        best=max(items,key=lambda x:x.confidence)
        if len(items)==1: result.append(best); continue
        combined='; '.join(dict.fromkeys(x.content for x in items))
        result.append(best.model_copy(update={'content':combined[:2000]}))
    return result
