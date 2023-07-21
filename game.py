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
        self.who_engaged = None
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

        self.left_team = [Elf(6, 5, 59), Angel(0, 2, 59)]
        self.right_team = [Angel(0, 0, 41)]
        self.move_order = []

        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.COLOR_BORDER = (128, 140, 64)

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))
        self.create_fields()
        self.create_characters()
        self.generate_move_order()

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

    def create_characters(self):
        for i, character in enumerate(self.left_team):
            position = character.position
            self.fields[position[0]][position[1]].is_engaged = True
            self.fields[position[0]][position[1]].who_engaged = self.left_team[i]

        for i, character in enumerate(self.right_team):
            position = character.position
            self.fields[position[0]][position[1]].is_engaged = True
            self.fields[position[0]][position[1]].who_engaged = self.right_team[i]

    def generate_move_order(self):
        left = sorted(self.left_team, key=lambda x: (x.speed, x.position[0], x.position[1]), reverse=True)
        right = sorted(self.right_team, key=lambda x: (x.speed, x.position[0], x.position[1]), reverse=True)
        while left and right:
            if left[0].speed >= right[0].speed:
                self.move_order.append(left.pop(0))
            else:
                self.move_order.append(right.pop(0))
        self.move_order.extend(left)
        self.move_order.extend(right)

    def get_cell(self, pos):
        for i, row in enumerate(self.fields):
            for j, cell in enumerate(row):
                if cell.left <= pos[0] < cell.right and cell.top <= pos[1] < cell.bottom:
                    return i, j
        return None

    def update_character_info(self, position):
        old_pos = self.move_order[0].position
        possible_ways = self.get_way(old_pos[0], old_pos[1], self.move_order[0].speed)

        if self.fields[position[0]][position[1]].is_engaged is False and position in possible_ways:
            self.fields[old_pos[0]][old_pos[1]].is_engaged = False
            self.fields[old_pos[0]][old_pos[1]].who_engaged = None

            self.move_order[0].position = position
            self.fields[position[0]][position[1]].is_engaged = True
            self.fields[position[0]][position[1]].who_engaged = self.move_order[0]
            self.move_order.append(self.move_order.pop(0))

    def update_fields_info(self, position):
        pos_x, pos_y = position
        old_pos = self.move_order[0].position
        possible_ways = self.get_way(old_pos[0], old_pos[1], self.move_order[0].speed)

        for i in range(len(self.fields)):
            for j in range(len(self.fields[0])):
                is_hover, is_possible, is_current = False, False, False
                if i == pos_x and j == pos_y:
                    is_hover = True
                if (i, j) in possible_ways:
                    is_possible = True
                if i == old_pos[0] and j == old_pos[1]:
                    is_current = True

                self.fields[i][j].indent, self.fields[i][j].color, self.fields[i][j].bold = \
                    self.get_features(is_hover, is_possible, is_current)
                self.fields[i][j].coordinates = self.get_coordinates(self.fields[i][j].corner, 0)
                self.fields[i][j].position = self.get_position(self.fields[i][j].indent)

        if self.fields[pos_x][pos_y].is_engaged:
            speed = self.fields[pos_x][pos_y].who_engaged.speed
            res = self.get_way(pos_x, pos_y, speed)
            for i, j in res:
                self.fields[i][j].color = (40, 40, 40, 120)
                self.fields[i][j].bold = 0
                self.fields[i][j].indent = 6
                self.fields[i][j].position = self.get_position(self.fields[i][j].indent)

    def get_way(self, pos_x, pos_y, speed):
        dp = {}

        def dfs(i, j, cur_speed):
            if i < 0 or i > self.n_rows - 1:
                return
            if j < 0 or j > self.n_columns - 1:
                return
            if cur_speed > speed:
                return
            if (i, j) in dp and cur_speed > dp[(i, j)]:
                return

            dp[(i, j)] = cur_speed

            if i % 2 == 0:
                dfs(i - 1, j - 1, cur_speed + 1)
                dfs(i + 1, j - 1, cur_speed + 1)
            else:
                dfs(i - 1, j + 1, cur_speed + 1)
                dfs(i + 1, j + 1, cur_speed + 1)

            dfs(i, j + 1, cur_speed + 1)
            dfs(i, j - 1, cur_speed + 1)
            dfs(i - 1, j, cur_speed + 1)
            dfs(i + 1, j, cur_speed + 1)

        dfs(pos_x, pos_y, 0)
        return list(dp.keys())

    def get_features(self, is_hover, is_possible, is_current):
        if is_hover:
            return 6, (40, 40, 40, 120), 0
        if is_current:
            return 0, (255, 215, 0), self.bold
        if is_possible:
            return 2, (0, 0, 140, 60), 0
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

        for item in self.right_team:
            x, y = self.get_cell_corner(item.position)
            item.draw(self.screen, x, y)

    def get_cell_corner(self, position):
        field = self.fields[position[0]][position[1]]
        return field.corner[1], field.corner[0]
