from base import PyVector
import pygame, random


class World(object):
    def __init__(self):
        self.collision_rects = []
        self._gravity = PyVector(x=0.0, y=0.0)

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, f):
        self._gravity.y = float(f)

    @gravity.deleter
    def gravity(self):
        self._gravity = PyVector(x=0.0, y=0.0)

    def add_collision(self, other):
        self.collision_rects.append(other)


class PhysicsObject(object):
    def __init__(self, position):

        if isinstance(position, tuple):
            self.position = PyVector(x=position[0], y=position[1])
        elif isinstance(position, PyVector):
            self.position = position
        else:
            self.position = PyVector()

        self.velocity = PyVector()
        self.acceleration = PyVector()

    def apply_force(self, force):
        self.acceleration += force

    def update_physics(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        self.acceleration *= 0


class PhysicsCircle(PhysicsObject):
    def __init__(self, x, y, parent):
        super().__init__((x, y))
        self.radius = 32
        self.parent = parent
        self.color = (255, 255, 255)
        self.surface = pygame.Surface((64, 64), pygame.SRCALPHA, 32)
        self.rect = pygame.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        self.velocity.limit_y_maximum = 0.01

    def move(self, i):
        self.position.x += i * 8

    def collided(self, objects):

        for rect in objects:
            if self.position.x in range(rect.x, rect.x + rect.width):
                if self.position.y + self.rect.height >= rect.top:
                    self.velocity.y = 0.0
                    self.position.y = rect.y - self.rect.height

            if self.position.y in range(rect.y, rect.y + rect.height):
                dif = self.rect.y - rect.y
                if dif <= self.rect.height/2:
                    print('good')
                else:
                    print('bad')

    def update(self):
        self.update_physics()

    def show(self, surface):
        self.parent.blit(self.surface, self.position.convert())



