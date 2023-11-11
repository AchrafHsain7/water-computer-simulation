import pygame, sys
from computer import Computer
from settings import *




class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Water Computer Simulation")
        self.clock = pygame.time.Clock()
        self.computer = Computer()

    def run(self):
        pause = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        pause = not pause
            if not pause:
                self.screen.fill('black')
                self.computer.run()
                pygame.display.update()
                self.clock.tick(FPS)

if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()
