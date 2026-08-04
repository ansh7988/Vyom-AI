import threading
import time
from voice_engine.queue_manager import SpeechQueue
import asyncio
import tempfile
import os
from voice_engine import cache
from voice_engine.edge_backend import generate_audio
from voice_engine.player import player
class SpeechWorker:

    def __init__(self, queue):

        self.queue = queue
        self.running = True
        self.on_finish = None

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
                
                path = cache.get(text=request.text, profile=request.profile)

        
            if cache.exists(request.text, request.profile):

                temp_path = path + ".tmp.mp3"

                asyncio.run(
                    generate_audio(
                        text=request.text,
                        profile=request.profile,
                        output_file=temp_path,
                    )
                )

                os.replace(temp_path, path)
                print(f"[CACHE STORE] Audio stored at {path}")
            player.play(path)

            if self.on_finish:
                self.on_finish()


    def start(self):
        self.thread.start()


    def stop(self):

        self.running = False

        with self.queue.condition:
            self.queue.condition.notify_all()

        self.thread.join()