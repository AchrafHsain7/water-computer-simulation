import pygame
from settings import *
from tube import Tube
from container import Container
from gate import Gate



class Computer:
    def __init__(self, binary1, binary2):
        self.tubes = pygame.sprite.Group()
        self.containers = pygame.sprite.Group()

        self.create_computer_2(binary1, binary2)



    def create_computer_1(self):
       
        tube_1 = Tube([self.tubes], True)
        tube_2 = Tube([self.tubes], True)
        container_1 = Container([self.containers], None, tube_1, (300, 50), 150)
        container_2 = Container([self.containers], [tube_1], tube_2, (300, 350), 0)
        container_3 = Container([self.containers], [tube_2], None, (300, 600), 0)
        tube_3 = Tube([self.tubes], True)
        tube_3_2 = Tube([self.tubes], True)
        container_4 = Container([self.containers], None, tube_3, (700, 50), 100)
        container_4_2 = Container([self.containers], None, tube_3_2, (850, 50), 100)
        tube_4 = Tube([self.tubes], True)
        tube_5 = Tube([self.tubes], True)
        gate_1 = Gate([self.containers], 'and', (700, 300), [tube_3, tube_3_2], tube_4, tube_5)
        container_5 = Container([self.containers], [tube_4], None, (650, 600))
        container_6 = Container([self.containers], [tube_5], None, (800, 600))

    def create_computer_2(self, number1='1111', number2='1111'):
        #creating the tubes
        tube_1 = Tube([self.tubes])
        tube_2 = Tube([self.tubes])
        tube_3 = Tube([self.tubes])
        tube_4 = Tube([self.tubes])
        tube_5 = Tube([self.tubes])
        tube_6 = Tube([self.tubes])
        tube_7 = Tube([self.tubes])
        tube_8 = Tube([self.tubes])

        tube_9 = Tube([self.tubes])
        tube_10 = Tube([self.tubes])
        tube_11 = Tube([self.tubes])
        tube_12 = Tube([self.tubes])
        tube_13 = Tube([self.tubes])
        tube_14 = Tube([self.tubes])
        tube_15 = Tube([self.tubes])
        tube_16 = Tube([self.tubes])
        tube_17 = Tube([self.tubes])
        tube_18 = Tube([self.tubes])
        tube_19 = Tube([self.tubes])

        #creating the starting containers
        tubes_group_1 = [tube_1, tube_3, tube_5, tube_7]
        tubes_group_2 = [tube_2, tube_4, tube_6, tube_8]

        for i, integer in enumerate(number1):
            if integer == '0':
                Container([self.containers], None, tubes_group_1[i], (150 + i*200, 50), 0)
            else:
                Container([self.containers], None, tubes_group_1[i], (150 + i*200, 50), 100)

        for i, integer in enumerate(number2):
            if integer == '0':
                Container([self.containers], None, tubes_group_2[i], (250 + i*200, 50), 0)
            else:
                Container([self.containers], None, tubes_group_2[i], (250 + i*200, 50), 100)


        #the first level of gates
        Gate([self.containers], (800, 200), [tube_7, tube_8], tube_10, tube_9)
        Gate([self.containers], (600, 200), [tube_5, tube_6], tube_14, tube_11)
        Gate([self.containers], (400, 200), [tube_4, tube_3], tube_16, tube_13)
        Gate([self.containers], (200, 200), [tube_2, tube_1], tube_18, tube_17)

        #second level of gates
        Container([self.containers], [tube_9], None, (800, 500), final_container=True, final_pos=(690, 700))
        Gate([self.containers], (600, 400), [tube_10, tube_11], tube_12, None, True, (660, 700))
        Gate([self.containers], (400, 600), [tube_12, tube_13, tube_14], tube_15, None, True, (630, 700))
        Gate([self.containers], (200, 700), [tube_15, tube_16, tube_17], tube_19, None, True, (600, 700))
        Container([self.containers], [tube_18, tube_19], None, (50, 750), final_container=True, final_pos=(570, 700))


    def create_a_bar(self):
        tube_1 = Tube([self.containers])
        tube_2 = Tube([self.containers])
        tube_3 = Tube([self.containers])

        Container([self.containers], None, tube_1, (250, 250), 00)
        Container([self.containers], None, tube_2, (500, 250), 100)
        Gate([self.containers], (375, 500), [tube_1, tube_2], tube_3, None)
        Container([self.containers], [tube_3], None, (375, 700), 0)
        


    def run(self):
        self.containers.update()
        self.tubes.update()
