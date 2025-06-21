import pygame
from grid import Grid

TILES_HORIZONTAL = 10
TILES_VERTICAL = 10
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
running = True

background = pygame.Surface((int(WINDOW_WIDTH / TILES_HORIZONTAL), int(WINDOW_HEIGHT / TILES_VERTICAL)))
background = background.convert()
myGrid = Grid(TILES_HORIZONTAL, TILES_VERTICAL, WINDOW_WIDTH, WINDOW_HEIGHT, screen)
myGrid.render()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
