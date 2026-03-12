import pygame
pygame.init()

window_height = 800
window_width = 800
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Nyan Cat')
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
