import pygame
import grid as Grid

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
