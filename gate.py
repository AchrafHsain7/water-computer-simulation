from typing import Any
import pygame
from settings import *
from general_container import GeneralContainer


class Gate(GeneralContainer):
    def __init__(self, groups, pos, input_tubes, and_tube, xor_tube=None):
        super().__init__(groups)

        
        self.input_tubes = input_tubes
        self.and_tube = and_tube
        self.xor_tube = xor_tube
        self.pos = pos
        self.mode = 'containing'


        #key positions
        self.border_width = int((CONTAINER_WIDTH - INSIDE_WIDTH)/2)
        self.x_left = pos[0] - CONTAINER_WIDTH/2 + self.border_width/2
        self.y_down = pos[1] + CONTAINER_HEIGHT/2 
        self.x1 = self.pos[0] - CONTAINER_WIDTH/4
        self.x2 = self.x1 - 0.4 * CONTAINER_WIDTH
        self.y1 = self.pos[1] + CONTAINER_HEIGHT/4
        self.y2 = self.y1 - CONTAINER_HEIGHT
        

        #graphics
        self.container = pygame.Surface((CONTAINER_WIDTH, CONTAINER_HEIGHT))
        self.container.fill('yellow')
        self.rect = self.container.get_rect(center = pos)


        self.void = pygame.Surface((INSIDE_WIDTH, CONTAINER_HEIGHT))
        self.void.fill('black')
        self.void_rect = self.void.get_rect(center = (pos[0], pos[1]-CONTAINER_HEIGHT*0.1))

        self.water = pygame.Surface((INSIDE_WIDTH-2, INSIDE_HEIGHT/2))
        self.water.fill('blue')
        self.water_rect = self.water.get_rect(bottomleft = (pos[0]-INSIDE_WIDTH/2, pos[1] + INSIDE_HEIGHT/2))

        self.water_2 = pygame.Surface((CONTAINER_WIDTH*0.4, CONTAINER_HEIGHT))
        self.water_2.fill('blue')
        self.water_rect_2 = self.water_2.get_rect(topright = (self.x1, self.y2))


        #setting the tubes pos
        self.set_input_tubes()
        self.set_and_tube()
        self.set_xor_tube()


    

    def draw(self):
        screen = pygame.display.get_surface()
        self.update_water_level()
        
        color = 'yellow'
        if self.current_capacity >= self.max_capacity/2:
            color = 'green'

        screen.blit(self.container, self.rect)
        self.container.fill(color)
        screen.blit(self.void, self.void_rect)
        screen.blit(self.water, self.water_rect)

        if self.mode == 'and_outflowing':
            self.water_2.fill('blue')
            screen.blit(self.water_2, self.water_rect_2)
            pygame.draw.line(screen, color, (self.x_left, self.y_down), (self.x_left, self.y_down - CONTAINER_HEIGHT), self.border_width)

        if self.current_capacity<=40 and self.mode == 'and_outflowing':
            self.water_2.fill('black')
            screen.blit(self.water_2, self.water_rect_2)
            pygame.draw.line(screen, color, (self.x_left, self.y_down), (self.x_left, self.y_down - CONTAINER_HEIGHT), self.border_width+1)
            
            
        pygame.draw.line(screen, color, (self.x1, self.y1), (self.x1, self.y2), self.border_width)
        pygame.draw.line(screen, color, (self.x1, self.y2), (self.x2, self.y2), self.border_width)
        pygame.draw.line(screen, color, (self.x2, self.y2), (self.x2, self.y1), self.border_width)
        

    #receive water from tubes
    def get_water(self):
        for tube in self.input_tubes:
            self.current_capacity += tube.get_outflow()
        
    def get_status(self):
        if self.current_capacity >= self.max_capacity*0.9 and self.mode == 'containing':
            self.mode = 'and_outflowing'   
        if self.current_capacity <= 0 and self.mode == 'and_outflowing':
            self.mode = 'containing'


    def water_and_outflow(self):
        if self.and_tube != None:
            if self.mode == 'and_outflowing' and self.current_capacity >= 0:
                self.current_capacity -= self.and_tube.get_inflow()

    def water_xor_outflow(self):
        if self.xor_tube != None:
            if self.current_capacity >= 0:
                self.current_capacity -= self.xor_tube.get_inflow()
                if self.current_capacity <= 0.8 and self.xor_tube.mode == 'water_in' and self.mode == 'and_outflowing':
                    self.xor_tube.set_mode('no_more_inflow')



    def set_input_tubes(self):
        if self.input_tubes != None:
            for tube in self.input_tubes:
                tube.set_output_pos(self.pos[0], self.pos[1] - INSIDE_HEIGHT/2)

    def set_and_tube(self):
        if self.and_tube != None:
            self.and_tube.set_input_pos(self.x2+ CONTAINER_WIDTH*0.1, self.y1)
            self.and_tube.set_double_output()

    def set_xor_tube(self):
        if self.xor_tube != None:
            self.xor_tube.set_input_pos(self.pos[0]+CONTAINER_WIDTH*0.2, self.pos[1] + INSIDE_HEIGHT/2)
            self.xor_tube.set_slow_waterflow()

    def debug(self):
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 20)
        debug_text = font.render(f'{self.current_capacity}', True, 'white')
        screen.blit(debug_text, self.rect)

    def update(self):
        self.get_water()
        self.get_status()
        self.water_and_outflow()
        self.water_xor_outflow()
        self.draw()
        #self.debug()


