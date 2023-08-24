import math
import pygame
from config import *

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
        self.orbit = []

        self.xv = 0
        self.yv = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        points = [] #list of scaled points

        for point in self.orbit:
            xp, yp = point
            scaled_x = xp * self.SCALE + WIDTH/2
            scaled_y = yp * self.SCALE + HEIGHT/2
            points.append((scaled_x, scaled_y))
        if len(self.orbit) > 1:
            pygame.draw.lines(window, self.color, False, points)

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
        self.orbit.append((self.x, self.y))