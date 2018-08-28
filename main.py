import pygame, sys
from objects import PhysicsCircle
from base import PyVector

gound_collision = [((0, 600), 100), ((100, 610), 200), ((300, 600), 300), ((600, 540), 680)]


class Game(object):
    def __init__(self):
        self.window = pygame.display.set_mode((1280, 720))
        self.window_rect = self.window.get_rect()
        self.circle = PhysicsCircle(100, 100, self.window)
        self.clock = pygame.time.Clock()
        self.gravity = PyVector(0, 0.01)
        self.collision_rect = []
        self.moving_left = False
        self.moving_right = False

    def main(self):
        self.event_handler()
        self.update()
        self.blit()

    def event_handler(self):
        """
        This method handles mouse and keyboard events for the scene and passes
        them on as is needed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('jump')
                    self.circle.apply_force(PyVector(0, -1))
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False

        if self.moving_left:
            self.circle.move(-5)
        if self.moving_right:
            self.circle.move(5)

    def update(self):
        self.circle.apply_force(self.gravity)
        self.circle.update()

    def blit(self):
        self.window.fill(128)

        for piece in gound_collision:
            rect = (piece[0][0], piece[0][1], piece[1], 60)
            piece = pygame.draw.rect(self.window, (150, 150, 150), rect)
            self.collision_rect.append(piece)

        self.circle.show(self.window)
        self.circle.collided(self.collision_rect)

        pygame.display.update()
        self.clock.tick(60)


pygame.init()
pygame.font.init()
scene = Game()


while scene is not None:
    scene.main()
