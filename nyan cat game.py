import pygame
import random

pygame.init()

window_height = 800
window_width = 1200
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()
difficulty = 120

font = pygame.font.Font(pygame.font.get_default_font(), 36)

slika_macke = pygame.image.load('Nyan-cat-slika.png').convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (150, 100))

platform_img = pygame.image.load("Klobasa.png").convert_alpha()
platform_img = pygame.transform.scale(platform_img, (300, 50))

bg = pygame.image.load("Background.jpg").convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

macka = slika_macke.get_rect()
jump_counter = 0
lives = 3

velocity_y = 0
gravity = 0.2
jump_strength = -10

velocity_x = -4
platform_list = [
    pygame.Rect(300, 400, 300, 50),
    pygame.Rect(600, 400, 300, 50),
    pygame.Rect(900, 400, 300, 50),
    pygame.Rect(1200, 400, 300, 50),
    pygame.Rect(1500, 400, 300, 50)
]

platforme_y_list = [600, 500, 400, 300, 200, 100]

def start_game():
    while True:
        screen.fill((0, 0, 0))
        text = font.render("Press SPACE to start | Q to quit", True, "white")
        screen.blit(text, (250, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.init()
                    pygame.mixer.music.load("nyan_cat_soundtrack.wav")
                    pygame.mixer.music.play(-1)
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def game_over():
    while True:
        screen.fill((0, 0, 0))
        text = font.render("GAME OVER | Press R to restart | Q to quit", True, "red")
        screen.blit(text, (200, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y

def jump():
    global jump_counter
    global velocity_y


    if jump_counter < 0:
        return
    else:
        jump_counter -= 1
        velocity_y = jump_strength


def move_platforms():
    for platform in platform_list:
        platform.x += velocity_x

def collisions(prev_y):
    global velocity_y
    global lives
    global jump_counter
    for platform in platform_list:
        if macka.colliderect(platform):
            if velocity_y > 0 and prev_y + macka.height <= platform.top + 5:
                macka.bottom = platform.top
                velocity_y = 0
                jump_counter = 1

        if platform.x < -300:
            platform.x = window_width
            platform.y = random.choice(platforme_y_list)

    if macka.bottom > window_height:
        lives -= 1
        macka.y = 300
        velocity_y = 0
        jump_counter = 1
        if lives <= 0:
            game_over()


def draw_every_platform():
    for rect in platform_list:
        screen.blit(platform_img, rect)



def game_loop():
    global velocity_y
    global lives

    lives = 3
    macka.x = 200
    macka.y = 300
    velocity_y = 0

    while True:
        global  velocity_x
        velocity_x -= 0.005
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

        screen.blit(bg, (0, 0))

        gravitacija()
        move_platforms()


        if collisions(prev_y):
            if game_over():
                return

        screen.blit(slika_macke, macka)
        draw_every_platform()


        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (20, 20))

        pygame.display.update()
        clock.tick(120)


start_game()