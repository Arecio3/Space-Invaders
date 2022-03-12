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

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)

# Abstract Class (inherit class for all the ships and manipulate)
class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        # We define these in General class
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
   
    def draw(self, window):
        # Draw a rectangle
        # pygame.draw.rect(window, (255, 0,0), (self.x, self.y, 50, 50))
        # Draw Ship
        window.blit(self.ship_img, (self.x, self.y))
    # Gets width and height of the ship so it doesnt go off screen
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1


    def shoot(self):
        # If lasers run out
        if self.cool_down_counter == 0:
            laser = Laser(x, y, self.laser_img)
            self.lasers.append(laser)
            # start cooldown counter
            self.cool_down_counter = 1

class Player(Ship):
    def __init__(self, x, y, health=100):
        # Brings all properties from Ship __init__
        super().__init__(x,y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        # Mask (pixel perfect collision) takes ship img and makes mask = tells us where there is and isnt any pixels
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    # DICT OF COLORS
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BlUE_SPACE_SHIP, BLUE_LASER)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        # sets images as the Color Map
        self.ship_img, self.lasers_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    # Method to move ship
    def move(self, vel):
        # If we pass a speed ships move diown
        self.y += vel

# Sees if pixels are overlapping
def collide(obj1, obj2):
    # distance between obj
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # is obj 1 overlapping obj2 with offset?
    return obj1.mask.overlap(obj2.mask, (offset_x,offset_y)) != None # returns (x, y)

# Main loop to run game logic
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # Store all enemies
    enemies = []
    # Increments after every level
    wave_length = 5
    # Enemy speed
    enemy_vel = 1
    player_speed = 5
    # Instantiate a ship
    player = Player(300, 650)

    clock = pygame.time.Clock()

    lost = False
    # Lost message timer
    lost_timer = 0
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
        # Draws enemies to screen
        for enemy in enemies:
            enemy.draw(WIN)
        # Draw Ship to Screen
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Your a Loser !", 1, (255,0,0))
            # (Math to put message in middle)
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        # Refreshes Screen so it has updated version
        pygame.display.update()

    while run:
        # Tick clock based on FPS Rate (Allows our game to stay consistent on any device)
        clock.tick(FPS)

        redraw_window()
        # Check if player lost
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_timer += 1

        if lost:
            # Shows lost message for 3 seconds
            if lost_timer > FPS * 3:
                run = False
            else:
                continue
        # When all enemy ships die increment level
        if len(enemies) == 0:
            level += 1
            # Increase enemies
            wave_length += 5
            # Create new enemies
            for i in range(wave_length):
                # randomly spawn in different locations (max left side 50 and -100 to keep in screen)(smallest value, closest value)
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
        # Check for events 
        for event in pygame.event.get():
            # If user exits stop the game
            if event.type == pygame.QUIT:
                run = False
        # Tracks keys being pressed (gives you ability to hit 2 keys at the same time)
        keys = pygame.key.get_pressed()
        # Returns DICT, after underscore specify what key to check
        if keys[pygame.K_a] and player.x + player_speed > 0: # move left
            # move one pixel to the left
            player.x -= player_speed
        # Checks if your in the screen
        if keys[pygame.K_d] and player.x + player_speed + player.get_width() < WIDTH: # move right
            player.x += player_speed
        # Checks if your in the screen
        if keys[pygame.K_w] and player.y + player_speed > 0: # move up
            player.y -= player_speed
        # Checks if your in the screen
        if keys[pygame.K_s] and player.y + player_speed + player.get_height() < HEIGHT: # move down
            player.y += player_speed

        # For each enemy on screen move down by velocity [copy so we dont modify list we're going through]
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            # Check if enemy went passed Player Ship
            if enemy.y + enemy.get_height() > HEIGHT:
                # Takes life away
                lives -= 1
                # remove enemy from list
                enemies.remove(enemy)

main()