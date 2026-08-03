import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import asyncio
import tempfile
import time

from voice_engine.language import detect_language
from voice_engine.profiles import get_profile
from voice_engine.edge_backend import generate_audio
from voice_engine.player import AudioPlayer

player = AudioPlayer()

text = "Hello, I am Vyom."

# Language Detection
t1 = time.perf_counter()
language = detect_language(text)
t2 = time.perf_counter()

# Profile Selection
profile = get_profile(language, "male")
t3 = time.perf_counter()

# Temporary File
with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp:
    path = temp.name

# Generate Audio
t4 = time.perf_counter()
asyncio.run(generate_audio(text, profile, path))
t5 = time.perf_counter()

# Playback
player.play(path)
t6 = time.perf_counter()

os.remove(path)

print(f"Language Detection : {(t2-t1)*1000:.2f} ms")
print(f"Profile Selection  : {(t3-t2)*1000:.2f} ms")
print(f"TTS Generation     : {(t5-t4)*1000:.2f} ms")
print(f"Playback           : {(t6-t5)*1000:.2f} ms")
print(f"Total              : {(t6-t1)*1000:.2f} ms")