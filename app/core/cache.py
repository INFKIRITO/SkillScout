import time
from typing import Any, Dict, Tuple


class InMemoryCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._store: Dict[str, Tuple[float, Any]] = {}

    def get(self, key: str):
        entry = self._store.get(key)
        if not entry:
            return None

        timestamp, value = entry
        if time.time() - timestamp > self.ttl:
            del self._store[key]
            return None

        return value

    def set(self, key: str, value: Any):
        self._store[key] = (time.time(), value)
