import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
# Create Screen
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

# Background
BACKGROUND = pygame.image.load(os.path.join("assets", "background-black.png"))

# Main loop to run game logic
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        # Tick clock based on FPS Rate (Allows our game to stay consistent on any device)
        clock.tick(FPS)
        # Check for events 
        for event in pygame.event.get():
            # If user exits stop the game
            if event.type == pygame.QUIT:
                run = False

main()