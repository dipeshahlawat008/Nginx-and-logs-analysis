from collections import deque, Counter
import time

class SimpleAnomalyDetector:
    def __init__(self, window_seconds=60):
        self.window = window_seconds
        self.events = deque()

    def add_event(self, timestamp, status):
        now = time.time()
        self.events.append((now, status))
        self._evict(now)

    def _evict(self, now):
        while self.events and (now - self.events[0][0]) > self.window:
            self.events.popleft()

    def status_summary(self):
        return Counter(status for _, status in self.events)
