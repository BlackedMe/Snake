import pygame

def grid(tiles_horizontal, tiles_vertical, window_width, window_height):
        grid_width = int(window_width / tiles_horizontal)
        grid_height = int(window_height / tiles_vertical)

        grid = []

        for i in range(tiles_vertical):
            col = [] 
            for j in range(tiles_horizontal):
                col.append(pygame.Rect(grid_width * j, grid_height * i, grid_width, grid_height))
            grid.append(col)
        return grid

        
def surface(grid, tiles_horizontal, tiles_vertical, window_width, window_height):
    surface = pygame.Surface((window_width, window_height))
    surface = surface.convert()

    for i in range(tiles_vertical):
        for j in range(tiles_horizontal):
            if (i % 2 == 1) ^ (j % 2 == 1):
                pygame.draw.rect(surface, "chartreuse3", grid[i][j])
            else: 
                pygame.draw.rect(surface, "chartreuse", grid[i][j])
    return surface