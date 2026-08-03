import threading
import time
from voice_engine.queue_manager import SpeechQueue
import asyncio
import tempfile
import os

from voice_engine.edge_backend import generate_audio
from voice_engine.player import AudioPlayer
player = AudioPlayer()
class SpeechWorker:

    def __init__(self, queue):

        self.queue = queue

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )
            
    def run(self):

        while self.running:

            with self.queue.condition:

                while self.queue.is_empty() and self.running:
                    self.queue.condition.wait()

                if not self.running:
                    break

                request = self.queue.get_next()

            with tempfile.NamedTemporaryFile(
                suffix=".mp3",
                delete=False,
            ) as temp:

                path = temp.name

            asyncio.run(
                generate_audio(
                    text=request.text,
                    profile=request.profile,
                    output_file=path,
                )
            )

            player.play(path)

            os.remove(path)


    def start(self):
        self.thread.start()


    def stop(self):

        self.running = False

        with self.queue.condition:
            self.queue.condition.notify_all()

        self.thread.join()