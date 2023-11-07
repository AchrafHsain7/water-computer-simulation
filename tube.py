import pygame
from settings import *


class Tube(pygame.sprite.Sprite):
    def __init__(self, input_pos, output_pos, groups, have_output_container, gate_input_type=None):
        super().__init__(groups)

        #pos
        self.input_pos = input_pos
        self.output_pos = output_pos

        #physical properties
        self.water_inflow = 0.5
        self.water_outflow = 1.5
        self.water_capacity = 100
        self.current_water = 0
        self.have_output = have_output_container

        self.mode = 'water_in'
 
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, 'white', self.input_pos, self.output_pos, TUBE_WIDTH)
        if self.mode == 'water_in':
            output_x = (self.output_pos[0] - self.input_pos[0]) * self.current_water/self.water_capacity + self.input_pos[0]
            output_y = (self.output_pos[1] - self.input_pos[1]) * self.current_water/self.water_capacity + self.input_pos[1]
            if  output_y > self.output_pos[1]:
                output_x = self.output_pos[0]
                output_y = self.output_pos[1]

            pygame.draw.line(screen, 'blue', self.input_pos, (output_x, output_y), TUBE_WIDTH-5)
        else:
           input_x = self.input_pos[0] + (self.output_pos[0] - self.input_pos[0]) * (1 - self.current_water/self.water_capacity)
           input_y = self.input_pos[1] + (self.output_pos[1] - self.input_pos[1]) * (1 - self.current_water/self.water_capacity)
           if  input_y > self.output_pos[1]:
                input_x = self.output_pos[0]
                input_y = self.output_pos[1]
           pygame.draw.line(screen, 'blue',(input_x, input_y), self.output_pos, TUBE_WIDTH-5) 

    def get_mode(self):
        if self.current_water <= 0:
            self.mode = 'water_in'
            self.current_water = 0

    def get_inflow(self):
        if self.current_water < self.water_capacity:
            self.current_water += self.water_inflow
            return self.water_inflow
        else:
            return 0
    
    def get_outflow(self):
        if self.current_water >= self.water_capacity or self.mode == 'water_out': 
            self.current_water -= self.water_outflow
            return self.water_outflow
        else:
            return 0
        
    def set_mode(self, mode):
        self.mode = mode

    def update(self):
        self.get_mode()
        self.draw()

 

    