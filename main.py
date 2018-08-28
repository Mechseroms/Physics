from base import PyVector
import pygame, sys


class Game(object):
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((400, 400))

    def main(self):
        self.event_handler()

    @staticmethod
    def event_handler():
        """
        This method handles mouse and keyboard events for the scene and passes
        them on as is needed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


scene = Game()

while scene is not None:
    scene.main()
