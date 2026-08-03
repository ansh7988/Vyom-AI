import asyncio
import tempfile
import os
from voice_engine.language import detect_language
from voice_engine.edge_backend import generate_audio
from voice_engine.player import AudioPlayer
from voice_engine.profiles import get_profile

from voice_engine.speech_request import SpeechRequest
from voice_engine.queue_manager import SpeechQueue
from voice_engine.worker import SpeechWorker
player = AudioPlayer()


class VoiceEngine:

    def __init__(self):
        self.gender = "male"
        self.queue = SpeechQueue()
        self.worker = SpeechWorker(self.queue)
        self.worker.start()

    def set_voice(self, gender):
        self.gender = gender

    def speak(self, text):

        language = detect_language(text)

        profile = get_profile(language, self.gender)

        request = SpeechRequest(
            text=text,
            profile=profile
        )

        self.queue.add(request)
        # Delete the file after playback

    def stop(self):
        self.worker.stop()

    def is_speaking(self):
        return self.worker.is_speaking()


voice = VoiceEngine()