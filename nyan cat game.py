import pygame
import random
pygame.init()
#za dodat se ce pade na tla = konec igre
window_height = 500
window_width = 800
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

slika_macke = pygame.image.load("nyan-cat-slika.png").convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (100, 75))

slika_klobase = pygame.image.load("Klobasa.png").convert_alpha()
slika_klobase = pygame.transform.scale(slika_klobase, (200,25))

bg = pygame.image.load("Background.jpg").convert()

print("press SPACE to jump")
print("press r to restart")
print("press q to quit")


macka = slika_macke.get_rect()
velocity_y = 0
gravity = 1
jump_strength = -20

platform_list = []
platform_width = slika_klobase.get_width()
platform_height = slika_klobase.get_height()
scroll_speed = 4
st_platform = 5

for i in range(st_platform):
    platform = slika_klobase.get_rect()
    x = window_width + i * 300
    y = random.randint(250, window_height - 50)
    platform.topleft = (x, y)
    platform_list.append(platform)

def gravitacija():
    global velocity_y
    velocity_y += gravity
    if velocity_y > 15:
        velocity_y = 15
    macka.y += velocity_y

def jump():
    global velocity_y
    on_platform = any(abs(macka.bottom - p.top) < 5 and
                      macka.right > p.left and
                      macka.left < p.right for p in platform_list)
    if macka.bottom >= window_height or on_platform:
        velocity_y = jump_strength

def screen_collision():
    global velocity_y
    if macka.bottom > window_height:
        macka.bottom = window_height
        velocity_y = 0

def platform_collision():
    global velocity_y
    for platform in platform_list:
        if macka.colliderect(platform) and velocity_y > 0:
            macka.bottom = platform.top
            velocity_y = 0

def move_platforms():
    for platform in platform_list:
        platform.x -= scroll_speed
        if platform.right < 0:
            platform.x = window_width + random.randint(50, 200)
            platform.y = random.randint(250, window_height - 50)

def game_loop():
    macka.midbottom = (200, platform_list[0].top)
    bg_x = 0
    global velocity_y

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
        platform_collision()
        screen_collision()
        move_platforms()

        screen.blit(slika_macke, macka)
        for platform in platform_list:
            screen.blit(slika_klobase, platform)

        pygame.display.update()
        clock.tick(60)

while True:
    game_loop()