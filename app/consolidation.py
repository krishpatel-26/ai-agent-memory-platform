from collections import defaultdict

from .models import Memory


def consolidate(memories: list[Memory]) -> list[Memory]:
    """Create deterministic, confidence-aware summaries without an LLM call."""
    groups = defaultdict(list)
    for memory in memories:
        groups[memory.kind].append(memory)

    result = []
    for kind, items in groups.items():
        best = max(items, key=lambda item: (item.confidence, item.importance, item.occurred_at))
        if len(items) == 1:
            result.append(best)
            continue
        combined = '; '.join(dict.fromkeys(item.content.strip() for item in items if item.content.strip()))
        result.append(best.model_copy(update={
            'content': combined[:2000],
            'importance': max(item.importance for item in items),
            'confidence': max(item.confidence for item in items),
            'occurred_at': max(item.occurred_at for item in items),
            'created_at': best.created_at,
            'access_count': sum(item.access_count for item in items),
            'last_accessed_at': max((item.last_accessed_at for item in items if item.last_accessed_at), default=None),
        }))
    return sorted(result, key=lambda item: (item.kind, -item.confidence, -item.importance))
