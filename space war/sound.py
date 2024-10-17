import pygame

def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('space war\sound for game\cruising-down-8bit-lane-159615.mp3')
    pygame.mixer.music.play(-1)
