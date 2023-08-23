import pygame
import math
pygame.init()

HEIGHT, WIDTH = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Gravity Simulation")

BACKGROUND = (2, 11, 18)
YELLOW = (255, 255, 0)
BLUE = (70, 130, 180)
RED = (255, 69, 0)
GREY = (192, 192, 192)
WHITE = (255, 245, 238)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67430e-11 # gravitational constant
    SCALE = 200 / AU
    TIME_STEP = 3600*24 # 1 day in seconds


    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.xv = 0
        self.yv = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(window, self.color, (x,y), self.radius)

    def calcforce(self, planet):
        planet_x, planet_y = planet.x, planet.y
        dx = planet_x - self.x
        dy = planet_y - self.y
        angle = math.atan2(dy, dx)
        distance = math.sqrt(dx ** 2 + dy ** 2)
        force = (Planet.G * self.mass * planet.mass) / (distance ** 2)
        fx = math.cos(angle) * force
        fy = math.sin(angle) * force
        return fx, fy
    
    def updatepos(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.calcforce(planet)
            total_fx += fx
            total_fy += fy
        self.xv += total_fx / self.mass * Planet.TIME_STEP
        self.yv += total_fy / self.mass * Planet.TIME_STEP

        self.x += self.xv * Planet.TIME_STEP
        self.y += self.yv * Planet.TIME_STEP

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
