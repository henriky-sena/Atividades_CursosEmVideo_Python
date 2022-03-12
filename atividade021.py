'''mp3'''
# a aula está desatuializada  :/

import pygame

# iniciando o mixer
pygame.mixer.init()

# iniciando o pygame
pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# é isso, ele não vai  :(
