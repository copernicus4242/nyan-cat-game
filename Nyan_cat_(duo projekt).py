import pygame
pygame.init()

window_height = 800
window_width = 800
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Nyan Cat')
exit = False

slika_macke = pygame.image.load('Nyan_cat_slika.png').convert_alpha()

macka  = slika_macke.get_rect()
macka.center = (200, 300)

while not exit:
    screen.fill((0, 0, 0))

    screen.blit(slika_macke, macka)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()

pygame.quit()
