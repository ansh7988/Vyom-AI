import sys
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from voice_engine.engine import voice

print("Testing Voice Engine...")

voice.speak("Hello AnshDeep! This is a test of the voice engine.")

voice.speak("How are you today?")

voice.speak("This is the third sentence.")

# Wait so the worker thread can finish speaking
time.sleep(10)