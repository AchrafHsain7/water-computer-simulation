import pygame
from settings import *
from general_container import GeneralContainer





class Container(GeneralContainer):
    def __init__(self, groups, input_tubes, output_tube, pos, intial_water):
        super().__init__(groups)
        self.input_tubes = input_tubes
        self.output_tube = output_tube
        self.current_capacity = intial_water
        self.pos = pos
        #graphics
        self.container = pygame.Surface((CONTAINER_WIDTH, CONTAINER_HEIGHT))
        self.container.fill('red')
        self.rect = self.container.get_rect(center = pos)

        self.void = pygame.Surface((INSIDE_WIDTH, INSIDE_HEIGHT))
        self.void.fill('black')
        self.void_rect = self.void.get_rect(center = pos)

        self.water = pygame.Surface((INSIDE_WIDTH-2, INSIDE_HEIGHT/2))
        self.water.fill('blue')
        self.water_rect = self.water.get_rect(bottomleft = (pos[0]-INSIDE_WIDTH/2, pos[1] + INSIDE_HEIGHT/2))


    def draw(self):
        screen = pygame.display.get_surface()
        self.update_water_level()
        screen.blit(self.container, self.rect)
        screen.blit(self.void, self.void_rect)
        screen.blit(self.water, self.water_rect)

    def move_water_to_tube(self):
        if self.current_capacity > 0 and self.output_tube != None:
            self.current_capacity -= self.output_tube.get_inflow()
        if self.current_capacity <= 0 and self.output_tube != None and self.output_tube.current_water > 0:
            self.output_tube.set_mode('water_out')

    def get_water_from_tube(self):
        if self.input_tubes != None:
            for tube in self.input_tubes:
                self.current_capacity += tube.get_outflow()

    def update(self):
        self.move_water_to_tube()
        self.get_water_from_tube()
        self.draw()