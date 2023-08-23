import pygame
from planet import Planet
from config import HEIGHT, WIDTH
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Gravity Simulation")

BACKGROUND = (2, 11, 18)
YELLOW = (255, 255, 0)
BLUE = (70, 130, 180)
RED = (255, 69, 0)
GREY = (80, 80, 80)
WHITE = (255, 245, 238)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 40, YELLOW, 1.98892 * 10**30)
    earth = Planet(-1 * Planet.AU, 0, 18, BLUE, 5.97219 * 10**24)
    earth.yv = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 14, RED, 6.39* 10**23)
    mars.yv = 24.077 * 1000
    mercury = Planet(0.387 * Planet.AU, 0, 10, GREY, 3.30 * 10**23)
    mercury.yv = 47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0, 16, WHITE, 4.8685 * 10**24)
    venus.yv = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WIN.fill(BACKGROUND)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.updatepos(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
