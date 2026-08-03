from voice_engine.speech_request import SpeechRequest
from collections import deque
import threading

class SpeechQueue:

    def __init__(self):
        self.queue = deque()
        self.condition = threading.Condition()

    def add(self, request:SpeechRequest):
        with self.condition:
            self.queue.append(request)
            self.condition.notify()

    def get_next(self):
        with self.condition:
            if self.queue:
                return self.queue.popleft()
            return None

    def clear(self):
        with self.condition:
            self.queue.clear()

    def is_empty(self):
        with self.condition:
            return len(self.queue) == 0

    def size(self):
        with self.condition:
            return len(self.queue)