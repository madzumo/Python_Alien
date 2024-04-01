import pygame.mixer
from pygame import mixer, mixer_music


class GameSounds:
    def __init__(self, ai_game):
        pepa = True

    def play_main_song(self):
        pygame.mixer.music.load('images/aliens_attack.mp3')
        pygame.mixer.music.play(-1)
