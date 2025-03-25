import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    
    while True:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             return
       screen.fill((0, 0, 0))
       updatables.update(dt)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_SPACE]:
         player.shoot(shots)     
       for asteroid in asteroids:
         if player.collision(asteroid):
            print("Game over!")
            sys.exit()
       for asteroid in asteroids:
          for shot in shots:
             if shot.collision(asteroid):
                asteroid.split(asteroids)
                shot.kill()
       for draw in drawables:
          draw.draw(screen)
       pygame.display.flip()
       clock.tick(60)
       dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()