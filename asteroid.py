import pygame
from random import uniform
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        random_angle = uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_velocity = self.velocity.rotate(random_angle)
        first_asteroid = Asteroid(*self.position, new_radius)
        first_asteroid.velocity = first_velocity

        second_velocity = self.velocity.rotate(-random_angle)
        second_asteroid = Asteroid(*self.position, new_radius)
        second_asteroid.velocity = second_velocity
