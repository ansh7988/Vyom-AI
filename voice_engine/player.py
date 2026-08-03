import pygame
import time

pygame.mixer.init()

class AudioPlayer:

    def __init__(self):
        self.is_playing = False

    def play(self, audio_file):

        self.is_playing = True

        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.05)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()      # <-- VERY IMPORTANT

        self.is_playing = False

    def stop(self):

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        self.is_playing = False

    def speaking(self):
        return self.is_playing