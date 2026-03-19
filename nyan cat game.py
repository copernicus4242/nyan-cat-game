import pygame
pygame.init()

window_height = 500
window_width = 800
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

slika_macke = pygame.image.load("nyan-cat-slika.png").convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (100, 75))

bg = pygame.image.load("Background.jpg").convert()

print("press SPACE to jump")
print("press r to restart")
print("press q to quit")


macka = slika_macke.get_rect()
velocity_y = 0
gravity = 1
jump_strength = -20

def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y

def jump():
    global velocity_y
    velocity_y = jump_strength

def screen_collision():
    if macka.bottom > window_height:
        macka.bottom = window_height


def game_loop():
    macka.center = (200, 300)
    bg_x = 0
    velocity_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    return

        screen.fill((255, 255, 255))
        bg_x -= 2

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + bg.get_width(), 0))
        if bg_x <= -bg.get_width():
            bg_x = 0


        gravitacija()
        screen_collision()

        screen.blit(slika_macke, macka)

        pygame.display.update()
        clock.tick(60)

while True:
    game_loop()