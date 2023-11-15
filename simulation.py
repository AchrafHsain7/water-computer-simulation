import pygame, sys
from computer import Computer
from settings import *




class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Water Computer Simulation")
        self.clock = pygame.time.Clock()

        binary1 = '1111'
        if len(sys.argv) >= 2: binary1 = str(sys.argv[1])
        binary2 = '1111'
        if len(sys.argv) >= 3: binary2 = str(sys.argv[2])
        self.computer = Computer(binary1, binary2)

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
