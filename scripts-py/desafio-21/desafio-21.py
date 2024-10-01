# importar a biblioteca pygame
import pygame 

# uma forma de implementar o código
pygame.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar...')