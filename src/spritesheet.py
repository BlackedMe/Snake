import pygame

class Spritesheet:
    def __init__(self, imageSrc):
        self.spritesheet = pygame.image.load(imageSrc).convert_alpha()
    def image_at(self, grid, size):
        return self.spritesheet.subsurface(pygame.Rect(size[0] * grid[0], size[1] * grid[1], size[0], size[1]))
