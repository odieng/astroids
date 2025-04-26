import circleshape
import pygame as pg
from constants import PLAYER_RADIUS

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        circleshape.CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        list_points = self.triangle()
        pg.draw.polygon(screen, color=(255, 255, 255), points=list_points, width=2)