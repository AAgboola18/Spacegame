import pygame
from os.path import join
# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter game')
running = True

# Main game loop
surf = pygame.Surface((100, 200))
x = 100


player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display with blue color
    display_surface.fill('dark gray')
    x += 0.1
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()


pygame.quit()
