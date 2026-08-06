import asyncio
import os
import tempfile
from voice_engine.language import detect_language
from voice_engine.edge_backend import generate_audio
from voice_engine.player import player
from voice_engine.profiles import get_profile
from voice_engine.speech_request import SpeechRequest
from voice_engine.queue_manager import SpeechQueue
from voice_engine.worker import SpeechWorker
import os


class VoiceEngine:

    def __init__(self):
        self.gender = "male"
        self.on_start = None
        self.on_finish = None
        self.on_interrupt = None
        self.queue = SpeechQueue()
        self.worker = SpeechWorker(self.queue)
        self.worker.on_finish = lambda: (self.on_finish() if self.on_finish else None)
        self.worker.start()

    def set_voice(self, gender):
        self.gender = gender

    def speak(
        self,
        text,
        priority=2,
        emotion="normal",
        interrupt=False,
    ):
        if not text or not text.strip():
            return  # Ignore empty or whitespace-only text
        language = detect_language(text)

        profile = get_profile(language, self.gender, emotion)

        if interrupt:
            player.stop()
            self.queue.clear()

        if self.on_start:
            self.on_start()

        request = SpeechRequest(
            text=text,
            profile=profile,
            priority=priority,
            emotion=emotion,
            interrupt=interrupt,
        )

        self.queue.add(request)
        # Delete the file after playback

    def stop(self):
        if self.on_interrupt:
            self.on_interrupt()

        player.stop()
        self.queue.clear()

    def is_speaking(self):
        return self.worker.is_speaking()


voice = VoiceEngine()
