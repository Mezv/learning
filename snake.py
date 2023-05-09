import pygame
import random

# Set up the Pygame library
pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Define the game variables
snake_speed = 5
food_spawn_chance = 0.1
food_velocity = 5
snake_segments = [{'x': 0, 'y': 0}]
current_position = {'x': 100, 'y': 300}
winning_score = 1000
losing_score = 0
pygame.mixer.music.load('snake.mp3')
pygame.mixer.music.play(-1)
font = pygame.font.Font(None, 32)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = ord(event.unicode)
            if key == pygame.K_LEFT:
                current_direction = "left"
            elif key == pygame.K_RIGHT:
                current_direction = "right"
            elif key == pygame.K_UP:
                current_direction = "up"
            elif key == pygame.K_DOWN:
                current_direction = "down"
        
    # Move snake based on input
    new_head_x = int(current_position['x']) + (1 if current_direction == "right" else -1)
    new_head_y = int(current_position[