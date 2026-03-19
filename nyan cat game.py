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
macka  = slika_macke.get_rect()
platform = pygame.rect.Rect(100, 100, 500, 50)
velocity_y = 0
velocity_x = -5
gravity = 1
jump_strength = -20
platform.y = random.randrange(window_height)
def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y
def platforme_premik():
    global velocity_y
    platform.x += velocity_x
def jump():
    global velocity_y
    velocity_y = jump_strength

def collisions():
    if macka.bottom > window_height:
        macka.bottom = window_height
    if macka.colliderect(platform) == True:
        macka.y -= velocity_y
    if platform.x < -200:
        platform.x = 1200
        platform.y = random.randrange(window_height)
def spawn_platform():
    return

def game_loop():
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
        screen.blit(slika_macke, macka)

        gravitacija()
        collisions()
        platforme_premik()

        pygame.draw.rect(screen, "black", platform)
        pygame.display.update()
        clock.tick(60)
spawn_platform()
while True:
    game_loop()