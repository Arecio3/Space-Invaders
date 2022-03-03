import pygame
import os
import time
import random
# Initialize font
pygame.font.init()

WIDTH, HEIGHT = 750, 750
# Create Screen (Main Surface)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot That Shit")

# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BlUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Load background and scale it to match screen size
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Main loop to run game logic
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    clock = pygame.time.Clock()
    # Render Game
    def redraw_window():
        # Draws an image or anything to the specific coord (top left)
        WIN.blit(BACKGROUND, (0,0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (0,255,0))
        level_label = main_font.render(f"Level: {level}", 1, (255,0,0))

        # Put text on screen
        WIN.blit(lives_label, (10,10))
        # Dynamic width
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        # Refreshes Screen so it has updated version
        pygame.display.update()

    while run:
        # Tick clock based on FPS Rate (Allows our game to stay consistent on any device)
        clock.tick(FPS)
        redraw_window()
        # Check for events 
        for event in pygame.event.get():
            # If user exits stop the game
            if event.type == pygame.QUIT:
                run = False

main()