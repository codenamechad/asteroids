import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateables, drawables)
    Player.containers = (updateables, drawables)
    AsteroidField.containers = updateables
    Shot.containers = (shots, updateables, drawables)
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateables.update(dt)
        for asteroid in asteroids:
            if ship.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    break  # stop checking this asteroid if it's already destroyed
        screen.fill((0,0,0))
        for drawable in drawables:
            drawable.draw(screen)
      
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000        
if __name__ == "__main__":
    main()
