import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
# Create Screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load Images
Red_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
Blue_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
Green_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
# Player Ship
Yellow_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
Red_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
Blue_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
Green_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Yellow_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
Background = pygame.image.load(os.path.join("assets", "background-black.png"))