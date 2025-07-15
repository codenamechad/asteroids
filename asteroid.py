import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

        
    def draw(self, screen,):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
    # Destroy the current asteroid
        self.kill()

    # Stop splitting if the asteroid is already at minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

    # Calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # Generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

    # Create two new velocity vectors, rotated in opposite directions
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2

        for new_vel in [vel1, vel2]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_vel
