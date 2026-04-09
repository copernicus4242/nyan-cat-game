import pygame
import random

pygame.init()

#Osnovne nastavitve ekrana
window_height = 800
window_width = 1200
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()
difficulty = 120

#Navodila
print("press SPACE to jump")
print("press r to restart")
print("press q to quit")

#Nastavitve glasbe
pygame.mixer.init()
pygame.mixer.music.load("nyan_cat_soundtrack.wav")
pygame.mixer.music.play(-1)

#Nastavitve macke
font = pygame.font.Font(pygame.font.get_default_font(), 36)

slika_macke = pygame.image.load('Nyan-cat-slika.png').convert_alpha()
slika_macke = pygame.transform.scale(slika_macke, (150, 100))

platform_img = pygame.image.load("Klobasa.png").convert_alpha()
platform_img = pygame.transform.scale(platform_img, (300, 50))

bg = pygame.image.load("Background.jpg").convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

macka = slika_macke.get_rect()
macka.x = 200
macka.y = 300

#Nastavitve mavrice za macko
trail = []
trail_length = 140

barve = [
    (255, 0, 0), #rdeca
    (255, 127, 0), #oranzna
    (255, 255, 0), #rumena
    (0, 255, 0), #zelena
    (0, 0, 255), #modra
    (75, 0, 130), #vijolicna
]

scrol_speed = 2

#Fizikalne kolicine
velocity_y = 0
gravity = 0.2
jump_strength = -10

#Nastavitve platform
velocity_x = -4
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
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

#Nastavitve ozadja
bg = pygame.image.load("Background.jpg").convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

#Funkcije
def gravitacija():
    global velocity_y
    velocity_y += gravity
    macka.y += velocity_y

def jump():
    global velocity_y
    velocity_y = jump_strength

def move_platforms():
    for platform in platform_list:
        platform.x += velocity_x

def collisions(prev_y):
    global velocity_y

    for platform in platform_list:
        if macka.colliderect(platform):
            if velocity_y > 0 and prev_y + macka.height <= platform.top + 5:
                macka.bottom = platform.top
                velocity_y = 0

        if platform.x < -300:
            platform.x = window_width
            platform.y = random.choice(platforme_y_list)

    if macka.bottom > window_height:
        macka.bottom = window_height
        velocity_y = 0

def draw_every_platform():
    for rect in platform_list:
        screen.blit(platform_img, rect)

def premik_trail():
    for t in trail:
        t[0] -= scrol_speed

#Glavna zanka
def game_loop():
    global velocity_y
    global difficulty

    macka.x = 200
    macka.y = 300
    velocity_y = 0

    while True:
        difficulty = difficulty + 0.01
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

        #Programiranje ozadja
        screen.fill((255, 255, 255))
        bg_x -= 2

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + bg.get_width(), 0))
        if bg_x <= -bg.get_width():
            bg_x = 0

        #Osnovni dejavniki igrice
        screen.blit(bg, (0, 0))

        gravitacija()
        move_platforms()
        collisions(prev_y)

        #Mavrica
        trail.append([macka.x + 40, macka.y + 20])

        premik_trail()

        if len(trail) > trail_length:
            trail.pop(0)

        for i, t in enumerate(trail):
            for j, barva in enumerate(barve):
                pygame.draw.rect(screen, barva, (t[0], t[1] + j*10, 40, 10))

        #Macka
        screen.blit(slika_macke, macka)

        #Platforme
        draw_every_platform()

        #Osnovna koda
        pygame.display.update()
        clock.tick(difficulty)

start_game()

while True:
    game_loop()