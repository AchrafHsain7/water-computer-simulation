import pygame
from settings import *


class Gate(pygame.sprite.Sprite):
    def __init__(self, groups, gate_type):
        super().__init__(groups)

        self.max_capacity = 200
        self.current_capacity = 0
        self.value = 0
        self.type = gate_type