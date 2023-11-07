import pygame
from settings import *


class GeneralContainer(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.max_capacity = 200
        self.current_capacity = 0
        self.value = 0


    def update_water_level(self):
        water_ratio = self.current_capacity / self.max_capacity
        height = INSIDE_HEIGHT * water_ratio
        self.water = pygame.Surface((INSIDE_WIDTH, height))
        self.water.fill('blue')
        self.water_rect = self.water.get_rect(bottomleft = (self.pos[0]-INSIDE_WIDTH/2, self.pos[1] + INSIDE_HEIGHT/2))  