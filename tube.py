import pygame
from settings import *


class Tube(pygame.sprite.Sprite):
    def __init__(self, groups, have_output_container=True, double_output=False):
        super().__init__(groups)

        #pos
        self.input_pos = None
        self.output_pos = None
        self.double_output = double_output

        #physical properties
        self.water_inflow = 0.75
        self.water_outflow = 0.75
        self.water_capacity = 100
        self.current_water = 0
        self.have_output = have_output_container

        self.mode = 'water_in'
 
    def draw(self):
        middle_x = (self.output_pos[0] + self.input_pos[0])/2 
        middle_y = (self.output_pos[1] + self.input_pos[1])/2 
        current_vector = pygame.math.Vector2(middle_x, middle_y)
        perp_vector = current_vector.normalize().rotate(90)
        throw_x = perp_vector[0] * -50 + middle_x
        throw_y = perp_vector[1] * 50 + middle_y
        screen = pygame.display.get_surface()
        pygame.draw.aaline(screen, 'white', self.input_pos, self.output_pos, TUBE_WIDTH)
    
        if self.double_output:
            direction_vector = pygame.math.Vector2(self.output_pos[0] - self.input_pos[0], self.output_pos[1] - self.input_pos[1]).normalize
            pygame.draw.aaline(screen, 'white', (middle_x, middle_y), (throw_x, throw_y))

        if self.mode == 'water_in':
            output_x = (self.output_pos[0] - self.input_pos[0]) * self.current_water/self.water_capacity + self.input_pos[0]
            output_y = (self.output_pos[1] - self.input_pos[1]) * self.current_water/self.water_capacity + self.input_pos[1]
            if  output_y > self.output_pos[1]:
                output_x = self.output_pos[0]
                output_y = self.output_pos[1]

            if self.double_output and self.current_water>=self.water_capacity/2:
               pygame.draw.aaline(screen, 'blue',(middle_x, middle_y), (throw_x, throw_y))
               #self.current_water -= self.water_outflow/2 - 0.1

            pygame.draw.aaline(screen, 'blue', self.input_pos, (output_x, output_y), TUBE_WIDTH-5)
        elif self.mode == 'water_out':
           input_x = self.input_pos[0] + (self.output_pos[0] - self.input_pos[0]) * (1 - self.current_water/self.water_capacity)
           input_y = self.input_pos[1] + (self.output_pos[1] - self.input_pos[1]) * (1 - self.current_water/self.water_capacity)
           if  input_y > self.output_pos[1]:
                input_x = self.output_pos[0]
                input_y = self.output_pos[1]
           pygame.draw.aaline(screen, 'blue',(input_x, input_y), self.output_pos, TUBE_WIDTH-5) 
           if self.double_output and self.current_water>=self.water_capacity/2:
               pygame.draw.aaline(screen, 'blue',(middle_x, middle_y), (throw_x, throw_y))
               self.current_water -= self.water_outflow/2 - 0.1

        elif self.mode == 'stable':
            pygame.draw.aaline(screen, 'blue',self.input_pos, self.output_pos, TUBE_WIDTH-5)
            if self.double_output:
                pygame.draw.aaline(screen, 'blue',(middle_x, middle_y), (throw_x, throw_y))




    def get_mode(self):
        if self.current_water <= 0:
            self.mode = 'water_in'
        if self.current_water >= self.water_capacity and self.mode == 'water_in':
            self.mode = 'stable'
        if self.current_water <= self.water_capacity and self.mode == 'stable':
            self.mode = 'water_out'

    #send water to tube
    def get_inflow(self):
        if self.current_water <= self.water_capacity:
            self.current_water += self.water_inflow
            return self.water_inflow
        else:
            return 0
    
    #get water from tube
    def get_outflow(self):
        if self.mode == 'water_out' or self.mode == 'stable' or self.mode == 'no_more_inflow': 
            self.current_water -= self.water_outflow
            return self.water_outflow
        else:
            return 0
        
    def set_mode(self, mode):
        self.mode = mode

    def set_input_pos(self, x, y):
        self.input_pos = (x, y)
    
    def set_double_output(self):
        self.double_output = True

    def set_output_pos(self, x, y):
        self.output_pos = (x, y)

    def set_slow_waterflow(self):
        self.water_inflow = 0.1
        self.water_outflow = 0.1

    def update(self):
        self.get_mode()
        self.draw()

 

    