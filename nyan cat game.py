import pygame
import random

pygame.init()

window_height = 800
window_width = 1200
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

print("press SPACE to jump")
print("press r to restart")
print("press q to quit")


slika_macke = pygame.image.load('Nyan_cat_slika.png').convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (200, 100))
macka = slika_macke.get_rect()
macka.x = 200
macka.y = 300


velocity_y = 0
gravity = 1
jump_strength = -20
velocity_x = -5

platform_list = []
for i in range(4):
    platform = pygame.Rect(random.randrange(300, 1200), random.randrange(50, 700), 500, 50)
    platform_list.append(platform)


def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y


def platforme_premik():
    for rect in platform_list:
        rect.x += velocity_x


def jump():
    global velocity_y
    velocity_y = jump_strength


def collisions():
    global velocity_y

    if macka.bottom > window_height:
        macka.bottom = window_height
        velocity_y = 0

    for platform in platform_list:
        if macka.colliderect(platform) and velocity_y > 0:
            macka.bottom = platform.top
            velocity_y = 0

    for platform in platform_list:
        if platform.x < -500:
            platform.x = 1200
            platform.y = random.randrange(50, 700)


def draw_every_platform():
    for rect in platform_list:
        pygame.draw.rect(screen, "black", rect)


def game_loop():
    global velocity_y

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

        gravitacija()
        collisions()
        platforme_premik()

        screen.blit(slika_macke, macka)
        draw_every_platform()

        pygame.display.update()
        clock.tick(60)


while True:
    game_loop()