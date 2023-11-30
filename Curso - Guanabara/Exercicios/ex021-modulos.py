import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer_music.load('skibidi.mp3')
pygame.mixer_music.play(start=0.0)
input()
pygame.event.wait()

