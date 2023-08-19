import math
import pygame

from modules.settings import Settings, States


class Hex:

    def __init__(self, i, j):
        self.offset = (i, j)
        self.cube = None
        self.corner = self.get_corner(i, j)
        self.points = []

        self.surf = pygame.Surface((2 * (Settings.r + Settings.bold), 2 * (Settings.R + Settings.bold)), pygame.SRCALPHA)
        self.color = Settings.COLOR_BORDER
        self.bold = Settings.bold

        self.who_engaged = None

        self.get_points()

    @staticmethod
    def get_corner(row, col):
        x = col * 2 * Settings.r - (row & 1) * Settings.r + Settings.bold + Settings.start_battle_filed[0]
        y = row * 1.5 * Settings.R + Settings.bold + Settings.start_battle_filed[1]
        return x, y

    def get_points(self):
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            x = Settings.r + Settings.R * math.cos(angle_rad)
            y = Settings.R + Settings.R * math.sin(angle_rad)
            self.points.append((x, y))

    def draw(self, screen):
        self.surf.fill(0)
        pygame.draw.polygon(self.surf, self.color, self.points, self.bold)
        screen.blit(self.surf, (self.corner[0], self.corner[1]))
