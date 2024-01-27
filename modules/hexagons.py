import math
import pygame

from modules.settings import Settings


class Hex:

    def __init__(self, row, col):
        self.engaged = None
        self.corner = None
        self.points = None

        self.surf = pygame.Surface((2 * (Settings.r + Settings.bold), 2 * (Settings.R + Settings.bold)), pygame.SRCALPHA)
        self.color = Settings.COLOR_BORDER
        self.bold = Settings.bold

        self.init(row, col)

    def init(self, row, col):
        self.get_corner(row, col)
        self.get_points()

    def get_corner(self, row, col):
        x = col * 2 * Settings.r - (row & 1) * Settings.r + Settings.bold + Settings.field_position[0]
        y = row * 1.5 * Settings.R + Settings.bold + Settings.field_position[1]
        self.corner = (x, y)

    def get_points(self):
        self.points = [self.get_point(i) for i in range(6)]

    @staticmethod
    def get_point(i):
        angle_deg = 60 * i + 30
        angle_rad = math.pi / 180 * angle_deg
        x = Settings.r + Settings.R * math.cos(angle_rad)
        y = Settings.R + Settings.R * math.sin(angle_rad)
        return x, y

    def draw(self, screen):
        self.surf.fill(0)
        pygame.draw.polygon(self.surf, self.color, self.points, self.bold)
        screen.blit(self.surf, (self.corner[0], self.corner[1]))
