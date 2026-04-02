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


slika_macke = pygame.image.load('Nyan-cat-slika.png').convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (150, 100))
macka = slika_macke.get_rect()
macka.x = 200
macka.y = 300

velocity_y = 0
gravity = 0.2
jump_strength = -10
velocity_x = -2


platform_list = [
    pygame.Rect(300, 400, 300, 50),
    pygame.Rect(600, 400, 300, 50),
    pygame.Rect(900, 400, 300, 50),
    pygame.Rect(1200, 400, 300, 50),
    pygame.Rect(1500, 400, 300, 50)
]

platforme_y_list = [600, 500, 400, 300, 200, 100]


platform = pygame.image.load("Klobasa.png").convert_alpha()
platform = pygame.transform.scale(platform, (300, 50))


bg = pygame.image.load("Background.jpg").convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y

def platforme_premik():
    global velocity_y

    for platform in platform_list:
        platform.x += velocity_x


        if macka.colliderect(platform):
            if macka.bottom <= platform.top:
                macka.bottom = platform.top
                velocity_y = 0

def jump():
    global velocity_y
    velocity_y = jump_strength

def collisions(prev_y):
    global velocity_y

    for platform in platform_list:
        platform.x += velocity_x

        if macka.colliderect(platform):
            if velocity_y > 0 and prev_y + macka.height <= platform.top:
                macka.bottom = platform.top
                velocity_y = 0


    for platform in platform_list:
        if platform.x < -300:
            platform.x = window_width
            platform.y = random.choice(platforme_y_list)

def draw_every_platform():
    for rect in platform_list:
        screen.blit(platform, rect)

def game_loop():
    global velocity_y
    velocity_y = 0

    while True:
        prev_y = macka.y
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


        screen.blit(bg, (0, 0))

        gravitacija()
        collisions(prev_y)
        platforme_premik()

        screen.blit(slika_macke, macka)
        draw_every_platform()

        pygame.display.update()
        clock.tick(120)

while True:
    game_loop()