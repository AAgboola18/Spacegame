import pygame
from os.path import join
from random import randint


# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter game')
running = True

# Main game loop
surf = pygame.Surface((100, 200))
x = 100

stars = pygame.image.load(join('images', 'star.png')).convert_alpha()
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))for i in range(20)]

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display with blue color
    display_surface.fill('dark gray')
    x += 0.1
    for pos in star_position:
        display_surface.blit(stars, pos)
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()


pygame.quit()