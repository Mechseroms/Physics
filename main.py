import pygame, sys
from objects import PhysicsCircle, World
from base import PyVector

gound_collision = [((0, 16), 3), ((3, 17), 6), ((9, 16), 12), ((16, 7), 8)]


class Game(World, object):
    def __init__(self):
        super(Game, self).__init__()
        self.window = pygame.display.set_mode((1280, 760))
        self.window_rect = self.window.get_rect()
        self.circle = PhysicsCircle(96, 96, self.window)
        self.clock = pygame.time.Clock()
        self.gravity = 0.1
        self.moving_left = False
        self.moving_right = False
        for piece in gound_collision:
            difference = self.window_rect.height - (piece[0][1] * 32)
            rect = (piece[0][0] * 32, piece[0][1] * 32, piece[1] * 32, difference)
            c = pygame.draw.rect(self.window, (150, 150, 150), rect)
            print(piece[0][0] * 32, piece[0][1] * 32)
            print(c.top)
            self.add_collision(c)
        self.window.set_colorkey((255, 0, 255))

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
                    self.circle.apply_force(PyVector(0, -5))
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
            self.circle.move(-1)
        if self.moving_right:
            self.circle.move(1)

    def update(self):
        self.circle.apply_force(self.gravity)
        self.circle.update()

    def blit(self):
        self.window.fill((51, 51, 51))

        for collision in gound_collision:
            difference = self.window_rect.height - (collision[0][1] * 32)
            rect = (collision[0][0] * 32, collision[0][1] * 32, collision[1] * 32, difference)
            pygame.draw.rect(self.window, (150, 150, 150), rect)

        for y in range(1, int(self.window_rect.height/32) + 1):
            pygame.draw.line(self.window, (255, 255, 255), (0, y * 32), (self.window_rect.width, y * 32))

        for x in range(1, int(self.window_rect.width/32) + 1):
            pygame.draw.line(self.window, (255, 255, 255), (x * 32, 0), (x * 32, self.window_rect.height))

        self.circle.show(self.window)
        self.circle.collided(self.collision_rects)

        pygame.display.flip()
        self.clock.tick(60)


pygame.init()
pygame.font.init()
scene = Game()


while scene is not None:
    scene.main()
