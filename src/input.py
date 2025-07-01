import pygame
from abc import ABC

class Keymap(ABC):
    def execute(self):
        pass

class K_w(Keymap):
    def execute(self):
        print("Pressed w")

class K_a(Keymap):
    def execute(self):
        print("Pressed a")

class K_s(Keymap):
    def execute(self):
        print("Pressed s")

class K_d(Keymap):
    def execute(self):
        print("Pressed d")

class InputHandler:
    def __init__(self):
        self._K_w = K_w()
        self._K_a = K_a()
        self._K_s = K_s()
        self._K_d = K_d()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if(pressed[pygame.K_w]):
            self._K_w.execute()
        elif(pressed[pygame.K_a]):
            self._K_a.execute()
        elif(pressed[pygame.K_s]):
            self._K_s.execute()
        elif(pressed[pygame.K_d]):
            self._K_d.execute()
