import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(
                ASTEROID_SPLIT_RANGE_MIN, ASTEROID_SPLIT_RANGE_MAX
            )
            vel1 = self.velocity.rotate(split_angle)
            vel2 = self.velocity.rotate(-split_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS

            for vel in [vel1, vel2]:
                asteroid = Asteroid(self.position.x, self.position.y, radius)
                asteroid.velocity = vel * 1.2
