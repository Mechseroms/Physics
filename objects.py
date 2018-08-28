from base import PyVector
import pygame, random


class World(object):
    def __init__(self):
        self.collision_rects = []

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
        self.surface = pygame.Surface((64, 64))
        self.rect = pygame.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)

    def move(self, i):
        self.position.x += i

    def collided(self, objects):

        for rect in objects:
            if self.position.y >= rect.top:
                self.velocity.y = 0.0
                self.position.y = rect.top

    def update(self):
        self.update_physics()

    def show(self, surface):
        self.parent.blit(self.surface, self.position.convert())



