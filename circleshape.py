import pygame
from abc import abstractmethod

# Base class for Game Objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def collides_with(self, other: "CircleShape"):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    @abstractmethod
    def draw(self, screen):
        raise NotImplementedError("child must implement draw method")

    @abstractmethod
    def update(self, delta_time):
        raise NotImplementedError("child must implement draw method")
