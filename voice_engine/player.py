import pygame
import threading
import time

pygame.mixer.init()


class AudioPlayer:

    def __init__(self):
        self.is_playing = False
        self.lock = threading.Lock()

    def play(self, audio_file):

        with self.lock:

            self.is_playing = True

            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            while True:

                if not pygame.mixer.music.get_busy():
                    break

                if not self.is_playing:
                    break

                time.sleep(0.02)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

            self.is_playing = False

    def stop(self):

        with self.lock:

            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()

            self.is_playing = False

    def speaking(self):
        with self.lock:
            return self.is_playing

player = AudioPlayer()