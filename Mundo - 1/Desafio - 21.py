import pygame
pygame.init()
pygame.mixer.music.load('Ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#atem o script rodando enquanto a musica toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)





