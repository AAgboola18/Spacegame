import pygame
from os.path import join
from random import randint

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter Game')
running = True

# Load player image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

stars = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# Main game loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display with dark gray color
    display_surface.fill('dark gray')

    # Draw stars
    for pos in star_positions:
        display_surface.blit(stars, pos)

    # Move player and draw player on display surface
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 1

    display_surface.blit(player_surf, player_rect)

    display_surface.blit(meteor_surf, meteor_rect)

    # Update the display
    pygame.display.update()

pygame.quit()