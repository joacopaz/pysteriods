from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys



def main():
    # init process
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # global setup
    clock = pygame.time.Clock()
    delta_time = 0

    # game object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # appling groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # instantiation of game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        # draw start

        screen.fill("black")

        for updatable_object in updatable:
            updatable_object.update(delta_time)

        # collision detection
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                exit(0)
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        # draw end
        pygame.display.flip()
        delta_time = clock.tick(60) / 1_000

if __name__ == "__main__":
    main()
