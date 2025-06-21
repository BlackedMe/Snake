import pygame

class Grid:
    def __init__(self, tiles_horizontal, tiles_vertical, window_width, window_height, surface):
        self.tiles_horizontal = tiles_horizontal
        self.tiles_vertical = tiles_vertical
        self.surface = surface


        grid_width = int(window_width / tiles_horizontal)
        grid_height = int(window_height / tiles_vertical)

        self.grid = []

        for i in range(tiles_vertical):
            col = [] 
            for j in range(tiles_horizontal):
                col.append(pygame.Rect(grid_width * j, grid_height * i, grid_width, grid_height))
            self.grid.append(col)

        
    def render(self):
        for i in range(self.tiles_vertical):
            for j in range(self.tiles_horizontal):
                if (i % 2 == 1) ^ (j % 2 == 1):
                    pygame.draw.rect(self.surface, "chartreuse3", self.grid[i][j])
                else: 
                    pygame.draw.rect(self.surface, "chartreuse", self.grid[i][j])