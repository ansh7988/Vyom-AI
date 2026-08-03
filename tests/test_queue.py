import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from voice_engine.queue_manager import SpeechQueue

queue = SpeechQueue()

queue.add("Hello")
queue.add("Opening Chrome")
queue.add("Done")

print(queue.get_next())
print(queue.get_next())
print(queue.get_next())

print(queue.is_empty())
print(queue.size())