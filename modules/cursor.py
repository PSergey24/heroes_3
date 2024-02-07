import os
import math
import pygame

from modules.settings import Settings
from modules.states import States, Objects


class Cursor:

    def __init__(self):
        self.img = None
        self.pixel = None
        self.offset = None
        self.cube = None

        self.point_attack = None
        self.whom_attack = None
        self.direction_to_fire = None
        self.direction_to_three_heads = None

        self.destination_point = None
        self.action = None

        self.init()

    def init(self):
        self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))
        self.point_attack, self.whom_attack, self.direction_to_fire, self.direction_to_three_heads = None, None, None, None
        self.destination_point = None
        self.action = None

    def handle_motion(self):
        self.pixel = pygame.mouse.get_pos()

        self.init()
        self.update_position()
        self.update_image()

    def update_position(self):
        row, col = self.pixel_to_raw_hex(self.pixel[0], self.pixel[1])
        self.cube = self.raw_hex_to_cube(col, -col - row, row)
        self.offset = Objects.tools.cube2offset(self.cube[0], self.cube[1], self.cube[2])

    @staticmethod
    def pixel_to_raw_hex(x, y):
        x -= Settings.field_position[0] + Settings.r
        y -= Settings.field_position[1] + Settings.R
        return y * 2 / 3 / Settings.R, (x * math.sqrt(3) / 3 - y / 3) / Settings.R

    @staticmethod
    def raw_hex_to_cube(x, y, z):
        rx, ry, rz = round(x), round(y), round(z)
        x_diff, y_diff, z_diff = abs(rx - x), abs(ry - y), abs(rz - z)

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry - rz
        elif y_diff > z_diff:
            ry = -rx - rz
        else:
            rz = -rx - ry
        return rx, ry, rz

    def update_image(self):
        if 0 <= self.offset[0] < Settings.n_rows and 0 <= self.offset[1] < Settings.n_columns and States.is_animate is False:
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom009.png"))
            if Objects.active_unit.info.characteristics["is_flyer"]:
                self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom012.png"))

            if Objects.active_unit.info.characteristics["is_double"]:
                dist_l = Objects.tools.cube_distance(Objects.tools.offset2cube(Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1]), self.cube)
                dist_r = Objects.tools.cube_distance(Objects.tools.offset2cube(Objects.active_unit.info.hex[1][0], Objects.active_unit.info.hex[1][1]), self.cube)
                distance = min(dist_l, dist_r)
            else:
                distance = Objects.tools.cube_distance(Objects.tools.offset2cube(Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1]), self.cube)

            if (self.offset[0], self.offset[1]) not in Objects.active_unit.reachable_points:
                self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom006.png"))

            is_double_back = False
            if Objects.active_unit.info.characteristics["is_double"]:
                is_double_back = (Objects.active_unit.info.team == 1 and Objects.active_unit.info.hex[0] == list(self.offset) and self.offset[1] - 1 >= 0 and
                                  Objects.field.hexagons[self.offset[0]][self.offset[1] - 1].engaged is None) or \
                                 (Objects.active_unit.info.team == 2 and Objects.active_unit.info.hex[1] == list(self.offset) and self.offset[1] + 1 < Settings.n_columns and
                                  Objects.field.hexagons[self.offset[0]][self.offset[1] + 1].engaged is None)

            if Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged is not None and Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged.team == Objects.active_unit.info.team and not is_double_back:
                self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom028.png"))

            if States.btn_shooter:
                if Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged is not None and Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged.team != Objects.active_unit.info.team:
                    is_neighbor_enemy = (Objects.tools.enemy_is_neighbor(Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1]) and len(Objects.active_unit.info.hex) == 1) or (len(Objects.active_unit.info.hex) == 2 and (Objects.tools.enemy_is_neighbor(Objects.active_unit.info.hex[1][0], Objects.active_unit.info.hex[1][1]) or Objects.tools.enemy_is_neighbor(Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1])))
                    if is_neighbor_enemy is False and Objects.active_unit.info.characteristics["current_arrows"] > 0:
                        self.whom_attack = Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged
                        self.point_attack = Objects.active_unit.info.hex[0]
                        if distance <= 10:
                            States.penalty_shooter = 1
                            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom023.png"))
                        else:
                            States.penalty_shooter = 0.5
                            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom026.png"))
            elif Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged is not None and Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged.team != Objects.active_unit.info.team:
                if distance <= Objects.active_unit.info.characteristics["base_characteristics"]["speed"] + 1:
                    degree = self.get_degree()
                    direction = self.get_direction_by_degree(degree)
                    direction = self.update_direction(direction)
                    if direction is not False:
                        self.update_cursor_by_direction(direction)
                        self.whom_attack = Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged
                        self.point_attack = self.get_point_attack(direction)

    def get_degree(self):
        center_x = Objects.field.hexagons[self.offset[0]][self.offset[1]].corner[0] + Settings.r
        center_y = Objects.field.hexagons[self.offset[0]][self.offset[1]].corner[1] + Settings.R

        degrees = ((math.atan2(self.pixel[1] - center_y, self.pixel[0] - center_x) + 2 * math.pi) * 180 / math.pi) % 360
        return degrees

    @staticmethod
    def get_direction_by_degree(degrees):
        if 0 <= degrees < 45 or 315 <= degrees < 360:
            return 0
        elif 45 <= degrees < 75 and Objects.active_unit.info.characteristics["is_double"]:
            return 7
        elif 75 <= degrees < 105 and Objects.active_unit.info.characteristics["is_double"]:
            return 6
        elif (105 <= degrees < 135 and Objects.active_unit.info.characteristics["is_double"]) or (45 <= degrees < 90 and not Objects.active_unit.info.characteristics["is_double"]):
            return 5
        elif (135 <= degrees < 225 and Objects.active_unit.info.characteristics["is_double"]) or (90 <= degrees < 135 and not Objects.active_unit.info.characteristics["is_double"]):
            return 4
        elif (225 <= degrees < 255 and Objects.active_unit.info.characteristics["is_double"]) or (135 <= degrees < 225 and not Objects.active_unit.info.characteristics["is_double"]):
            return 3
        elif (255 <= degrees < 285 and Objects.active_unit.info.characteristics["is_double"]) or (225 <= degrees < 270 and not Objects.active_unit.info.characteristics["is_double"]):
            return 2
        elif (285 <= degrees < 315 and Objects.active_unit.info.characteristics["is_double"]) or (270 <= degrees < 315 and not Objects.active_unit.info.characteristics["is_double"]):
            return 1

    def update_direction(self, direction):
        available_positions = self.get_available_positions()

        i = 0
        while i < len(available_positions) and not available_positions[direction]:
            direction = (direction + 1) % len(available_positions)
            i += 1

        if i == len(available_positions):
            return False
        return direction

    def get_available_positions(self):
        if Objects.active_unit.info.characteristics["is_double"]:
            return self.get_available_double_positions()
        else:
            return self.get_available_single_positions()

    def get_available_single_positions(self):
        positions = {}
        for i in range(6):
            nb_x, nb_y, nb_z = Objects.tools.cube_neighbor(self.cube, i)
            nb_r, nb_c = Objects.tools.cube2offset(nb_x, nb_y, nb_z)

            if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns and (Objects.field.hexagons[nb_r][nb_c].engaged is None or (Objects.active_unit.info.hex[0][0] == nb_r and Objects.active_unit.info.hex[0][1] == nb_c)) and (nb_r, nb_c) in Objects.active_unit.reachable_points:
                positions.update({i: True})
            else:
                positions.update({i: False})

        return positions

    def get_available_double_positions(self):
        row_active, col_active = Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1]
        positions = {6: False, 7: False}
        p = {}

        for i in range(6):
            nb_x, nb_y, nb_z = Objects.tools.cube_neighbor(self.cube, i)
            nb_r, nb_c = Objects.tools.cube2offset(nb_x, nb_y, nb_z)

            if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns and (Objects.field.hexagons[nb_r][nb_c].engaged is None or [nb_r, nb_c] in Objects.field.hexagons[row_active][col_active].engaged.hex) and (nb_r, nb_c) in Objects.active_unit.reachable_points:
                p.update({i: True})
                if (i in [0, 1, 5] and 0 <= nb_c + 1 < Settings.n_columns and (nb_r, nb_c + 1) in Objects.active_unit.reachable_points and (nb_r, nb_c + 1) not in Objects.active_unit.only_left_points and (Objects.field.hexagons[nb_r][nb_c + 1].engaged is None or [nb_r, nb_c + 1] in Objects.field.hexagons[row_active][col_active].engaged.hex)) or (i in [2, 3, 4] and 0 <= nb_c - 1 < Settings.n_columns and (nb_r, nb_c - 1) in Objects.active_unit.reachable_points and (nb_r, nb_c - 1) not in Objects.active_unit.only_right_points and (Objects.field.hexagons[nb_r][nb_c - 1].engaged is None or [nb_r, nb_c - 1] in Objects.field.hexagons[row_active][col_active].engaged.hex)):
                    positions.update({i: True})
                else:
                    positions.update({i: False})
            else:
                p.update({i: False})
                positions.update({i: False})

        if p[1] and p[2]:
            positions.update({6: True})

        if p[4] and p[5]:
            positions.update({7: True})

        positions.update({0: positions[0], 1: positions[1], 2: positions[6], 3: positions[2], 4: positions[3],
                          5: positions[4], 6: positions[7], 7: positions[5]})
        return positions

    def update_cursor_by_direction(self, direction):
        if direction == 0:
            self.direction_to_fire, self.direction_to_three_heads = 3, 3
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom021.png"))
        if direction == 1:
            self.direction_to_fire, self.direction_to_three_heads = 4, 4
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom020.png"))
        if (direction == 2 and not Objects.active_unit.info.characteristics["is_double"]) or (direction == 3 and Objects.active_unit.info.characteristics["is_double"]):
            self.direction_to_fire, self.direction_to_three_heads = 5, 5
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom018.png"))
        if (direction == 3 and not Objects.active_unit.info.characteristics["is_double"]) or (direction == 4 and Objects.active_unit.info.characteristics["is_double"]):
            self.direction_to_fire, self.direction_to_three_heads = 0, 0
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom017.png"))
        if (direction == 4 and not Objects.active_unit.info.characteristics["is_double"]) or (direction == 5 and Objects.active_unit.info.characteristics["is_double"]):
            self.direction_to_fire, self.direction_to_three_heads = 1, 1
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom016.png"))
        if (direction == 5 and not Objects.active_unit.info.characteristics["is_double"]) or (direction == 7 and Objects.active_unit.info.characteristics["is_double"]):
            self.direction_to_fire, self.direction_to_three_heads = 2, 2
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom022.png"))
        if direction == 2 and Objects.active_unit.info.characteristics["is_double"]:
            self.direction_to_fire = 4 if Objects.active_unit.info.team == 1 else 5
            self.direction_to_three_heads = 6
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom019.png"))
        if direction == 6 and Objects.active_unit.info.characteristics["is_double"]:
            self.direction_to_fire = 2 if Objects.active_unit.info.team == 1 else 1
            self.direction_to_three_heads = 7
            self.img = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom015.png"))

    def get_point_attack(self, direction):
        if Objects.active_unit.info.characteristics["is_double"]:
            i = self.get_neighbor_direction(direction)
            nb_x, nb_y, nb_z = Objects.tools.cube_neighbor(self.cube, i)
            nb_r, nb_c = Objects.tools.cube2offset(nb_x, nb_y, nb_z)
            nb_r, nb_c = self.correct_point_attack(direction, nb_r, nb_c)
        else:
            nb_x, nb_y, nb_z = Objects.tools.cube_neighbor(self.cube, direction)
            nb_r, nb_c = Objects.tools.cube2offset(nb_x, nb_y, nb_z)
        return [nb_r, nb_c]

    @staticmethod
    def get_neighbor_direction(direction):
        if direction == 2 or direction == 3:
            return 2
        elif direction == 4:
            return 3
        elif direction == 5 or direction == 6:
            return 4
        elif direction == 7:
            return 5
        return direction

    @staticmethod
    def correct_point_attack(direction, nb_r, nb_c):
        if direction == 3 or direction == 4 or direction == 5:
            nb_c -= 1
        return nb_r, nb_c

    def handle_click(self):
        if self.pixel is not None:
            self.get_destination_position()
            self.get_action()

            print(f"action is {self.action}")

    def get_destination_position(self):
        if self.point_attack is None and (self.offset[0], self.offset[1]) in Objects.active_unit.reachable_points:
            if Objects.field.hexagons[self.offset[0]][self.offset[1]].engaged is None and Objects.active_unit.info.characteristics["is_double"] is False:
                self.destination_point = [self.offset[0], self.offset[1]]

            if Objects.active_unit.info.characteristics["is_double"]:
                if Objects.active_unit.info.team == 1:
                    self.destination_point = [self.offset[0], self.offset[1] - 1]
                    if self.offset[1] == 0 or (Objects.field.hexagons[self.offset[0]][self.offset[1] - 1].engaged is not None and id(Objects.field.hexagons[self.offset[0]][self.offset[1] - 1].engaged) != id(Objects.active_unit.info)) or (self.offset[0], self.offset[1]) in Objects.active_unit.only_left_points:
                        self.destination_point = [self.offset[0], self.offset[1]]
                    if (self.offset[1] == 0 or Objects.field.hexagons[self.offset[0]][self.offset[1] - 1].engaged is not None or (self.offset[0], self.offset[1]) in Objects.active_unit.only_left_points) and [self.offset[0], self.offset[1]] in Objects.active_unit.info.hex:
                        self.destination_point = None

                if Objects.active_unit.info.team == 2:
                    self.destination_point = [self.offset[0], self.offset[1]]
                    if self.offset[1] == 14 or (Objects.field.hexagons[self.offset[0]][self.offset[1] + 1].engaged is not None and id(Objects.field.hexagons[self.offset[0]][self.offset[1] + 1].engaged) != id(Objects.active_unit.info)) or (self.offset[0], self.offset[1]) in Objects.active_unit.only_right_points:
                        self.destination_point = [self.offset[0], self.offset[1] - 1]
                    if (self.offset[1] == 14 or Objects.field.hexagons[self.offset[0]][self.offset[1] + 1].engaged is not None or (self.offset[0], self.offset[1]) in Objects.active_unit.only_right_points) and [self.offset[0], self.offset[1]] in Objects.active_unit.info.hex:
                        self.destination_point = None

        elif self.point_attack is not None:
            self.destination_point = [self.point_attack[0], self.point_attack[1]]

    def get_action(self):
        if self.whom_attack:
            if States.btn_shooter:
                if self.offset[0] > Objects.active_unit.info.hex[0][0]:
                    self.action = 'shoot_down'
                elif self.offset[0] < Objects.active_unit.info.hex[0][0]:
                    self.action = 'shoot_up'
                else:
                    self.action = 'shoot_straight'
            else:
                if self.offset[0] > self.destination_point[0]:
                    self.action = 'attack_down'
                elif self.offset[0] < self.destination_point[0]:
                    self.action = 'attack_up'
                else:
                    self.action = 'attack_straight'

        elif self.destination_point is not None:
            self.action = 'moving'

    def draw(self):
        pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), self.img))
