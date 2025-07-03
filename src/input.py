import pygame
from abc import ABC

class Keymap(ABC):
    def execute(self):
        pass

class K_w(Keymap):
    def execute(self, snake, grid):
        if not snake.is_horizontal(): return

        snake.rotate(pygame.Vector2(0, -1), grid)

class K_a(Keymap):
    def execute(self, snake, grid):
        if snake.is_horizontal(): return

        snake.rotate(pygame.Vector2(-1, 0), grid)

class K_s(Keymap):
    def execute(self, snake, grid):
        if not snake.is_horizontal(): return

        snake.rotate(pygame.Vector2(0, 1), grid)

class K_d(Keymap):
    def execute(self, snake, grid):
        if snake.is_horizontal(): return

        snake.rotate(pygame.Vector2(1, 0), grid)

class InputHandler:
    def __init__(self):
        self._K_w = K_w()
        self._K_a = K_a()
        self._K_s = K_s()
        self._K_d = K_d()

    def handle_input(self, snake, grid):
        pressed = pygame.key.get_pressed()

        if(pressed[pygame.K_w]):
            self._K_w.execute(snake, grid)
        elif(pressed[pygame.K_a]):
            self._K_a.execute(snake, grid)
        elif(pressed[pygame.K_s]):
            self._K_s.execute(snake, grid)
        elif(pressed[pygame.K_d]):
            self._K_d.execute(snake, grid)
