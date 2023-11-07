from typing import Any
import pygame
from settings import *
from general_container import GeneralContainer


class Gate(GeneralContainer):
    def __init__(self, groups, gate_type, pos, input_tubes, and_tube, xor_tube=None):
        super().__init__(groups)

        
        self.type = gate_type
        self.input_tubes = input_tubes
        self.and_tube = and_tube
        self.xor_tube = xor_tube
        self.pos = pos

        #graphics
        self.container = pygame.Surface((CONTAINER_WIDTH, CONTAINER_HEIGHT))
        self.container.fill('yellow')
        self.rect = self.container.get_rect(center = pos)


        self.void = pygame.Surface((INSIDE_WIDTH, CONTAINER_HEIGHT))
        self.void.fill('black')
        self.void_rect = self.void.get_rect(center = (pos[0], pos[1]-10))

        self.water = pygame.Surface((INSIDE_WIDTH-2, INSIDE_HEIGHT/2))
        self.water.fill('blue')
        self.water_rect = self.water.get_rect(bottomleft = (pos[0]-INSIDE_WIDTH/2, pos[1] + INSIDE_HEIGHT/2))

        self.water_2 = pygame.Surface((40, CONTAINER_HEIGHT))
        self.water_2.fill('blue')
        self.water_rect_2 = self.water_2.get_rect(topright = (self.pos[0] - 25, self.pos[1] + CONTAINER_HEIGHT/4 - CONTAINER_HEIGHT))


    

    def draw(self):
        screen = pygame.display.get_surface()
        self.update_water_level()
        
        screen.blit(self.container, self.rect)
        screen.blit(self.void, self.void_rect)
        screen.blit(self.water, self.water_rect)
        if self.current_capacity >= self.max_capacity:
            screen.blit(self.water_2, self.water_rect_2)
            

        x1 = self.pos[0] - 25
        x2 = x1 - 40
        y1 = self.pos[1] + CONTAINER_HEIGHT/4
        y2 = y1 - CONTAINER_HEIGHT
        width = 7
        pygame.draw.line(screen, 'yellow', (x1, y1), (x1, y2), width)
        pygame.draw.line(screen, 'yellow', (x1, y2), (x2, y2), width )
        pygame.draw.line(screen, 'yellow', (x2, y2), (x2, y1), width)
        
        
            

    def update(self):
        self.current_capacity += 0.5
        self.draw()