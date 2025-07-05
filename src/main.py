import os
import pygame
import grid as Grid
from input import InputHandler
from snake import Snake
from spritesheet import Spritesheet

TILES_HORIZONTAL = 10
TILES_VERTICAL = 10
TILES_WIDTH = 64
TILES_HEIGHT = 64
WINDOW_WIDTH = TILES_HORIZONTAL * TILES_WIDTH
WINDOW_HEIGHT = TILES_VERTICAL * TILES_HEIGHT

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
running = True

grid = Grid.grid(TILES_HORIZONTAL, TILES_VERTICAL, WINDOW_WIDTH, WINDOW_HEIGHT)
background = Grid.surface(grid, TILES_HORIZONTAL, TILES_VERTICAL, WINDOW_WIDTH, WINDOW_HEIGHT)
screen.blit(background, (0, 0))

spritesheet = Spritesheet(os.path.join(os.getcwd(), "sprites", "spritesheet.png"))

snake_turn_texture = spritesheet.image_at((3, 0), (64, 64))
snake_head_texture = spritesheet.image_at((2, 0), (64, 64))
snake_body_texture = spritesheet.image_at((1, 0), (64, 64))
snake_tail_texture = spritesheet.image_at((0, 0), (64, 64))

# Initialize the snake
snake = Snake(snake_turn_texture, snake_head_texture, snake_body_texture, snake_tail_texture, [4, 5], grid)

MOVE_SNAKE = pygame.event.custom_type()

# Controls the speed of the snake
pygame.time.set_timer(MOVE_SNAKE, 800) 

input_handler = InputHandler()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == MOVE_SNAKE:
            snake.move_forward(grid)

    input_handler.handle_input(snake, grid)

    rect = snake.draw(screen)
    pygame.display.update(rect)
    snake.clear(screen, background)

    clock.tick(60)

pygame.quit()
