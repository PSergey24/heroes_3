import pygame
import math
from copy import copy
import os

from unit import Angel, Elf


R = 35
r = round(math.sqrt(3) * R / 2, 2)


class Field:

    def __init__(self, corner, color, bold):
        self.indent = 0
        self.corner = corner
        self.color = color
        self.bold = bold
        self.is_engaged = False
        self.coordinates = None
        self.position = None
        self.surf = None

        self.left = self.corner[1]
        self.right = self.corner[1] + r * 2
        self.top = self.corner[0]
        self.bottom = self.corner[0] + R * 2


class Game:

    def __init__(self):
        self.width = 1000
        self.height = 800

        self.start_battle_filed = [150, 35]
        self.n_columns = 15
        self.n_rows = 11
        self.bold = 1

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.fields = []

        self.left_team = [Angel(0, 0, 41), Angel(0, 2, 59), Elf(0, 5, 59)]
        self.right_team = []

        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.COLOR_BORDER = (128, 140, 64)

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))
        self.create_fields()

        while run:
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_character_info(position)

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_fields_info(position)

            self.draw_fields()
            self.draw_characters()

            pygame.display.update()
        pygame.quit()

    def create_fields(self):
        corner = copy(self.start_battle_filed)

        x = 1
        for i in range(self.n_rows):
            row = []
            for j in range(self.n_columns):
                field = Field(copy(corner), self.COLOR_BORDER, self.bold)
                field.coordinates = copy(self.get_coordinates(corner, 0))
                field.position = copy(self.get_position(0))
                field.surf = pygame.Surface((2 * (r + self.bold), 2 * (R + self.bold)), pygame.SRCALPHA)
                row.append(field)

                corner[1] += 2 * r

            self.fields.append(row)
            corner[0] += 1.5 * R
            corner[1] = (corner[1] - self.n_columns * 2 * r) + x * r
            x *= (-1)

    def get_cell(self, pos):
        for i, row in enumerate(self.fields):
            for j, cell in enumerate(row):
                if cell.left <= pos[0] < cell.right and cell.top <= pos[1] < cell.bottom:
                    return i, j
        return None

    def update_character_info(self, position):
        old_pos = self.left_team[0].position
        if self.fields[position[0]][position[1]].is_engaged is False:
            self.fields[old_pos[0]][old_pos[1]].is_engaged = False
            self.left_team[0].position = position
            self.fields[position[0]][position[1]].is_engaged = True

    def update_fields_info(self, coordinates):
        pos_x, pos_y = coordinates
        for i in range(len(self.fields)):
            for j in range(len(self.fields[0])):
                is_hover = False
                if i == pos_x and j == pos_y:
                    is_hover = True

                self.fields[i][j].indent, self.fields[i][j].color, self.fields[i][j].bold = \
                    self.get_features(is_hover)
                self.fields[i][j].coordinates = self.get_coordinates(self.fields[i][j].corner, 0)
                self.fields[i][j].position = self.get_position(self.fields[i][j].indent)

    def get_features(self, is_hover):
        if is_hover:
            return 6, (40, 40, 40, 120), 0
        return 0, self.COLOR_BORDER, self.bold

    def draw_fields(self):
        for i in range(len(self.fields)):
            for j in range(len(self.fields[0])):
                self.fields[i][j].surf.fill(0)
                pygame.draw.polygon(self.fields[i][j].surf, self.fields[i][j].color, self.fields[i][j].position,
                                    self.fields[i][j].bold)
                self.screen.blit(self.fields[i][j].surf, (self.fields[i][j].corner[1], self.fields[i][j].corner[0]))

    @staticmethod
    def get_position(indent):
        coordinates = [[indent, (R + indent)/2], [indent, (R * 3 - indent)/2],
                       [r, R * 2 - indent], [2 * r - indent, (R * 3 - indent)/2],
                       [2 * r - indent, (R + indent)/2], [r, indent]]
        return coordinates

    @staticmethod
    def get_coordinates(corner, indent):
        coordinates = [[corner[1] + indent, corner[0] + R / 2 + indent],
                       [corner[1] + indent, corner[0] + R * 3 / 2 - indent],
                       [corner[1] + r, corner[0] + R * 2 - indent],
                       [corner[1] + 2 * r - indent, corner[0] + R * 3 / 2 - indent],
                       [corner[1] + 2 * r - indent, corner[0] + R / 2 + indent],
                       [corner[1] + r, corner[0] + indent]]
        return coordinates

    def draw_characters(self):
        for item in self.left_team:
            x, y = self.get_cell_corner(item.position)
            item.draw(self.screen, x, y)

    def get_cell_corner(self, position):
        field = self.fields[position[0]][position[1]]
        return field.corner[1], field.corner[0]
