import pygame
from circleshape import *
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt