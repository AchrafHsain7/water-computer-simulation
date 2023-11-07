import pygame
from settings import *
from tube import Tube
from container import Container
from gate import Gate



class Computer:
    def __init__(self):
        self.tubes = pygame.sprite.Group()
        self.containers = pygame.sprite.Group()

        self.create_computer()


    def create_computer(self):
        #input pos = input container pos (heigth + inside_heigth/2)
        #output pos = outpu_pos container - inside_height/2
        tube_1 = Tube((300, 50 + INSIDE_HEIGHT/2), (300, 350 - INSIDE_HEIGHT/2), [self.tubes], True)
        tube_2 = Tube((300, 350 + INSIDE_HEIGHT/2), (300, 600 - INSIDE_HEIGHT/2), [self.tubes], True)
        #tube_3 = Tube((700, 200 + INSIDE_HEIGHT/2), (300, 100 - INSIDE_HEIGHT/2), [self.tubes], True)

        container_1 = Container([self.containers], None, tube_1, (300, 50), 150)
        container_2 = Container([self.containers], [tube_1], tube_2, (300, 350), 0)
        container_3 = Container([self.containers], [tube_2], None, (300, 600), 0)

        gate_1 = Gate([self.containers], 'and', (700, 300), None, None, None)

        


    def run(self):
        self.containers.update()
        self.tubes.update()
