import os
import math
import pygame

import queue

from modules.settings import Settings, States
from modules.hex import Hex


class HexWorker:

    def __init__(self):
        pass

    def create_hexagons(self):
        for i in range(Settings.n_rows):
            rows = []
            for j in range(Settings.n_columns):
                rows.append(self.create_hex(i, j))
            States.hexagons.append(rows)

    def create_hex(self, i, j):
        hexagon = Hex(i, j)
        hexagon.cube = self.offset2cube(i, j)
        return hexagon

    @staticmethod
    def offset2cube(row, col):
        x = int(col - (row + (row & 1)) / 2)
        z = int(row)
        y = int(-x-z)
        return x, y, z

    @staticmethod
    def cube2offset(x, y, z):
        col = x + (z + (z & 1)) / 2
        row = z
        return int(row), int(col)

    def update_point_over(self):
        row, col = self.pixel_to_hex(States.point_over[0], States.point_over[1])
        States.point_x, States.point_y, States.point_z = self.cube_round(col, -col - row, row)
        States.point_r, States.point_c = self.cube2offset(States.point_x, States.point_y, States.point_z)

    def update_cursor(self):
        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        r_over, c_over = States.point_r, States.point_c

        States.point_attack, States.whom_attack, States.cursor_direction = None, None, None
        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))

        if 0 <= r_over < Settings.n_rows and 0 <= c_over < Settings.n_columns and States.is_animate is False:
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom009.png"))
            if States.queue.current[0].is_flyer:
                States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom012.png"))

            dist = self.cube_distance(self.offset2cube(row_active, col_active), [States.point_x, States.point_y, States.point_z])

            if (r_over, c_over) not in States.reachable_points:
                States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom006.png"))

            #todo: connect cursor with action
            if States.hexagons[r_over][c_over].who_engaged is not None and States.hexagons[r_over][c_over].who_engaged.team == States.unit_active.team:
                States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom028.png"))

            if States.btn_shooter:
                if States.hexagons[r_over][c_over].who_engaged is not None and States.hexagons[r_over][c_over].who_engaged.team != States.unit_active.team:
                    is_neighbor_enemy = self.enemy_is_neighbor(row_active, col_active)
                    if is_neighbor_enemy is False:
                        States.whom_attack = States.hexagons[r_over][c_over].who_engaged
                        if dist <= 10:
                            States.penalty_shooter = 1
                            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom023.png"))
                        else:
                            States.penalty_shooter = 0.5
                            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom026.png"))
            elif States.hexagons[r_over][c_over].who_engaged is not None and States.hexagons[r_over][c_over].who_engaged.team != States.unit_active.team:
                if dist <= States.speed_active:
                    available_positions = self.get_available_positions()
                    degree = self.get_degree(r_over, c_over)
                    direction = self.get_direction_by_degree(degree)
                    direction = self.update_direction(direction, available_positions)
                    if direction is not False:
                        self.update_cursor_by_direction(direction)
                        States.whom_attack = States.hexagons[r_over][c_over].who_engaged
                        States.point_attack = self.get_point_attack(direction)

    def get_available_positions(self):
        if States.active_is_double:
            return self.get_available_double_positions()
        else:
            return self.get_available_single_positions()

    def get_available_single_positions(self):
        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        x_over, y_over, z_over = States.point_x, States.point_y, States.point_z
        positions = {}
        for i in range(6):
            nb_x, nb_y, nb_z = self.cube_neighbor((x_over, y_over, z_over), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)

            if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns and (States.hexagons[nb_r][nb_c].who_engaged is None or (row_active == nb_r and col_active == nb_c)) and (nb_r, nb_c) in States.reachable_points:
                positions.update({i: True})
            else:
                positions.update({i: False})

        return positions

    def get_available_double_positions(self):
        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        positions = {6: False, 7: False}
        p = {}

        for i in range(6):
            nb_x, nb_y, nb_z = self.cube_neighbor((States.point_x, States.point_y, States.point_z), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)

            if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns and (States.hexagons[nb_r][nb_c].who_engaged is None or [nb_r, nb_c] in States.hexagons[row_active][col_active].who_engaged.hex) and (nb_r, nb_c) in States.reachable_points:
                p.update({i: True})
                if (i in [0, 1, 5] and 0 <= nb_c + 1 < Settings.n_columns and (nb_r, nb_c + 1) in States.reachable_points and (States.hexagons[nb_r][nb_c + 1].who_engaged is None or [nb_r, nb_c + 1] in States.hexagons[row_active][col_active].who_engaged.hex)) or (i in [2, 3, 4] and 0 <= nb_c - 1 < Settings.n_columns and (nb_r, nb_c) in States.reachable_points and (States.hexagons[nb_r][nb_c - 1].who_engaged is None or [nb_r, nb_c - 1] in States.hexagons[row_active][col_active].who_engaged.hex)):
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

    @staticmethod
    def get_degree(r_over, c_over):
        center_x = States.hexagons[r_over][c_over].corner[0] + Settings.r
        center_y = States.hexagons[r_over][c_over].corner[1] + Settings.R

        degrees = ((math.atan2(States.point_over[1] - center_y,
                               States.point_over[0] - center_x) + 2 * math.pi) * 180 / math.pi) % 360
        return degrees

    @staticmethod
    def get_direction_by_degree(degrees):
        if 0 <= degrees < 45 or 315 <= degrees < 360:
            return 0
        elif 45 <= degrees < 75 and States.active_is_double:
            return 7
        elif 75 <= degrees < 105 and States.active_is_double:
            return 6
        elif (105 <= degrees < 135 and States.active_is_double) or (45 <= degrees < 90 and not States.active_is_double):
            return 5
        elif (135 <= degrees < 225 and States.active_is_double) or (90 <= degrees < 135 and not States.active_is_double):
            return 4
        elif (225 <= degrees < 255 and States.active_is_double) or (135 <= degrees < 225 and not States.active_is_double):
            return 3
        elif (255 <= degrees < 285 and States.active_is_double) or (225 <= degrees < 270 and not States.active_is_double):
            return 2
        elif (285 <= degrees < 315 and States.active_is_double) or (270 <= degrees < 315 and not States.active_is_double):
            return 1

    @staticmethod
    def update_direction(direction, available_positions):
        pos_count = len(available_positions)

        i = 0
        while i < pos_count and not available_positions[direction]:
            direction = (direction + 1) % pos_count
            i += 1

        if i == pos_count:
            return False
        return direction

    @staticmethod
    def update_cursor_by_direction(direction):
        if direction == 0:
            States.cursor_direction = True
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom021.png"))
        if direction == 1:
            States.cursor_direction = True
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom020.png"))
        if (direction == 2 and not States.active_is_double) or (direction == 3 and States.active_is_double):
            States.cursor_direction = False
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom018.png"))
        if (direction == 3 and not States.active_is_double) or (direction == 4 and States.active_is_double):
            States.cursor_direction = False
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom017.png"))
        if (direction == 4 and not States.active_is_double) or (direction == 5 and States.active_is_double):
            States.cursor_direction = False
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom016.png"))
        if (direction == 5 and not States.active_is_double) or (direction == 7 and States.active_is_double):
            States.cursor_direction = True
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom022.png"))
        if direction == 2 and States.active_is_double:
            States.cursor_direction = True
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom019.png"))
        if direction == 6 and States.active_is_double:
            States.cursor_direction = False
            States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom015.png"))

    def get_point_attack(self, direction):
        if States.active_is_double:
            i = self.get_neighbor_direction(direction)
            nb_x, nb_y, nb_z = self.cube_neighbor((States.point_x, States.point_y, States.point_z), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
            nb_r, nb_c = self.correct_point_attack(direction, nb_r, nb_c)
        else:
            nb_x, nb_y, nb_z = self.cube_neighbor((States.point_x, States.point_y, States.point_z), direction)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
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

    def enemy_is_neighbor(self, row_active, col_active):
        x, y, z = self.offset2cube(row_active, col_active)
        for i in range(6):
            nb_x, nb_y, nb_z = self.cube_neighbor((x, y, z), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
            if 0 <= nb_c < Settings.n_columns and 0 <= nb_r < Settings.n_rows:
                if States.hexagons[nb_r][nb_c].who_engaged is not None and States.hexagons[nb_r][nb_c].who_engaged.team != States.hexagons[row_active][col_active].who_engaged.team:
                    return True
        return False

    def get_neighbors(self, row, col):
        neighbors = []

        x, y, z = self.offset2cube(row, col)
        for i in range(6):
            nb_x, nb_y, nb_z = self.cube_neighbor((x, y, z), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
            if 0 <= nb_c < Settings.n_columns and 0 <= nb_r < Settings.n_rows and \
                    States.hexagons[nb_r][nb_c].who_engaged is not None and \
                    id(States.hexagons[nb_r][nb_c].who_engaged) != id(States.hexagons[row][col].who_engaged):
                neighbors.append(States.hexagons[nb_r][nb_c].who_engaged)
        return neighbors

    def update_hexagons(self):
        for r in range(len(States.hexagons)):
            for c in range(len(States.hexagons[0])):
                self.update_hexagon(r, c, Settings.COLOR_BORDER, Settings.bold)
                self.update_reachable_hexagons(r, c)

        self.update_hover_hexagons()
        self.update_active_hexagons()

    def update_reachable_hexagons(self, r, c):
        if (r, c) in States.reachable_points and States.hexagons[r][c].who_engaged is None and \
                States.is_animate is False:
            self.update_hexagon(r, c, Settings.COLOR_POSSIBLE, 0)

    def update_hover_hexagons(self):
        if 0 <= States.point_r < Settings.n_rows and 0 <= States.point_c < Settings.n_columns and \
                States.is_animate is False:
            self.update_hexagon(States.point_r, States.point_c, Settings.COLOR_HOVER, 0)

    def update_active_hexagons(self):
        for r, c in States.unit_active.hex:
            self.update_hexagon(r, c, Settings.COLOR_ACTIVE, 3)

    @staticmethod
    def update_hexagon(r, c, color, bold):
        States.hexagons[r][c].color = color
        States.hexagons[r][c].bold = bold

    @staticmethod
    def pixel_to_hex(x, y):
        x -= Settings.start_battle_filed[0] + Settings.r
        y -= Settings.start_battle_filed[1] + Settings.R

        q = (x * math.sqrt(3) / 3 - y / 3) / Settings.R
        r = y * 2 / 3 / Settings.R
        return r, q

    @staticmethod
    def cube_round(x, y, z):
        rx, ry, rz = round(x), round(y), round(z)
        x_diff, y_diff, z_diff = abs(rx - x), abs(ry - y), abs(rz - z)

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry - rz
        elif y_diff > z_diff:
            ry = -rx - rz
        else:
            rz = -rx - ry
        return rx, ry, rz

    def update_reachable_points(self):
        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        is_double_hex = States.queue.current[0].character in Settings.double_hex_units

        x_active, y_active, z_active = self.offset2cube(row_active, col_active)
        speed_active = States.queue.current[0].speed
        States.reachable_points = self.cube_reachable((x_active, y_active, z_active), speed_active,
                                                      States.queue.current[0].is_flyer)

        if is_double_hex:
            x_active, y_active, z_active = self.offset2cube(row_active, col_active + 1)
            reachable = self.cube_reachable((x_active, y_active, z_active), speed_active,
                                            States.queue.current[0].is_flyer)
            States.double_reachable_points = reachable - States.reachable_points
            States.reachable_points = States.reachable_points.union(reachable)
            self.correct_reachable_points()

    def cube_reachable(self, start, movement, is_flyer):
        visited = set()
        visited.add(self.cube2offset(start[0], start[1], start[2]))

        level = 0
        queue = [(start, level)]
        while queue:
            (x, y, z), level = queue.pop(0)
            level += 1

            for i in range(6):
                neighbor = self.cube_neighbor((x, y, z), i)

                r, c = self.cube2offset(neighbor[0], neighbor[1], neighbor[2])
                if 0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns:
                    if (r, c) not in visited and (States.hexagons[r][c].who_engaged is None or is_flyer is True) and level <= movement:
                        visited.add(self.cube2offset(neighbor[0], neighbor[1], neighbor[2]))
                        queue.append((neighbor, level))
        return visited

    @staticmethod
    def cube_neighbor(current, i):
        directions = [
            (+1, -1, 0), (+1, 0, -1), (0, +1, -1),
            (-1, +1, 0), (-1, 0, +1), (0, -1, +1)
        ]
        return current[0] + directions[i][0], current[1] + directions[i][1], current[2] + directions[i][2]

    @staticmethod
    def correct_reachable_points():
        States.reachable_points = list(States.reachable_points)
        for r, c in reversed(States.reachable_points):
            if 0 < c < Settings.n_columns - 1 and States.hexagons[r][c - 1].who_engaged is not None and States.hexagons[r][c + 1].who_engaged is not None and id(States.hexagons[r][c - 1].who_engaged) != id(States.queue.current[0]) and id(States.hexagons[r][c + 1].who_engaged) != id(States.queue.current[0]):
                States.reachable_points.remove((r, c))
            elif c == 0 and States.hexagons[r][c + 1].who_engaged is not None and id(States.hexagons[r][c + 1].who_engaged) != id(States.queue.current[0]):
                States.reachable_points.remove((r, c))
            elif c == Settings.n_columns - 1 and States.hexagons[r][c - 1].who_engaged is not None and id(States.hexagons[r][c - 1].who_engaged) != id(States.queue.current[0]):
                States.reachable_points.remove((r, c))
        States.reachable_points = set(States.reachable_points)

    @staticmethod
    def cube_distance(a, b):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

    @staticmethod
    def get_move_type():
        if States.whom_attack:
            if States.btn_shooter:
                if States.point_r > States.whom_attack.hex[0][0]:
                    return 'shoot_up'
                if States.point_r < States.whom_attack.hex[0][0]:
                    return 'shoot_down'
                return 'shoot_straight'
            else:
                if States.point_r > States.whom_attack.hex[0][0]:
                    return 'attack_up'
                if States.point_r < States.whom_attack.hex[0][0]:
                    return 'attack_down'
                return 'attack_straight'

        if 0 <= States.point_r < Settings.n_rows and 0 <= States.point_c < Settings.n_columns:
            is_empty_hex = States.hexagons[States.point_r][States.point_c].who_engaged is None and (States.point_r, States.point_c) in States.reachable_points

            is_double_itself = False
            if States.active_is_double:
                is_double_back = (States.unit_active.team == 1 and States.unit_active.hex[0] == [States.point_r, States.point_c] and States.hexagons[States.point_r][States.point_c - 1].who_engaged is None) or (States.unit_active.team == 2 and States.unit_active.hex[1] == [States.point_r, States.point_c] and States.hexagons[States.point_r][States.point_c + 1].who_engaged is None)
                is_double_itself = (States.hexagons[States.point_r][States.point_c].who_engaged is not None and id(States.hexagons[States.point_r][States.point_c].who_engaged) == id(States.unit_active) and is_double_back)

            if is_empty_hex or is_double_itself:
                return 'moving'
        return False

    @staticmethod
    def update_double_hex_position():
        if States.point_c > 0:
            if States.point_c + 1 >= Settings.n_columns or \
                    (States.point_r, States.point_c + 1) not in States.double_reachable_points and (States.point_r, States.point_c + 1) not in States.reachable_points or \
                    States.hexagons[States.point_r][States.point_c + 1].who_engaged is not None and id(States.hexagons[States.point_r][States.point_c + 1].who_engaged) != id(States.queue.current[0]):
                States.point_c -= 1

    # way search
    def update_character_position(self, goal_row, goal_col):
        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        start, goal = self.offset2cube(row_active, col_active), self.offset2cube(goal_row, goal_col)

        way = self.way_search(start, goal)
        # here need to correct movement for double hex units near border

        if States.queue.current[0].is_jumper is False:
            self.generate_steps(way)

        self.update_engaged_points(goal_row, goal_col, row_active, col_active)

    def way_search(self, start, goal):
        frontier = queue.PriorityQueue()
        frontier.put(start)

        came_from, cost_so_far = dict(), dict()
        came_from[start], cost_so_far[start] = None, 0

        while not frontier.empty():
            current = frontier.get()

            for i in range(6):
                neighbor = self.cube_neighbor(current, i)
                row, col = self.cube2offset(neighbor[0], neighbor[1], neighbor[2])
                if 0 <= row < Settings.n_rows and 0 <= col < Settings.n_columns:
                    new_cost = cost_so_far[current] + 1
                    if (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]) and \
                            (States.hexagons[row][col].who_engaged is None or id(States.hexagons[row][col].who_engaged) == id(States.unit_active) or States.queue.current[0].is_flyer is True or States.queue.current[0].is_jumper is True):
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + self.cube_distance(goal, neighbor)
                        frontier.put(neighbor, priority)
                        came_from[neighbor] = current

        way = []
        row, col = self.cube2offset(goal[0], goal[1], goal[2])
        way.insert(0, (row, col))
        while came_from[goal]:
            row, col = self.cube2offset(came_from[goal][0], came_from[goal][1], came_from[goal][2])
            way.insert(0, (row, col))
            goal = came_from[goal]
        return way

    def generate_steps(self, way):
        States.queue.current[0].path.clear()
        for i in range(1, len(way), 1):
            States.queue.current = self.generate_step(way[i - 1], way[i])

    def generate_step(self, old_point, new_point):
        move_order = States.queue.current

        old = States.hexagons[old_point[0]][old_point[1]].corner
        new = States.hexagons[new_point[0]][new_point[1]].corner

        step = 4
        if int(old[1]) > int(new[1]) and int(old[0]) == int(new[0]):
            move_order[0].path.extend((old[0], y) for y in range(int(old[1]), int(new[1]), -step))
        elif int(old[1]) < int(new[1]) and int(old[0]) == int(new[0]):
            move_order[0].path.extend((old[0], y) for y in range(int(old[1]), int(new[1]), step))
        elif int(old[1]) == int(new[1]) and int(old[0]) > int(new[0]):
            move_order[0].path.extend((x, old[1]) for x in range(int(old[0]), int(new[0]), -step))
        elif int(old[1]) == int(new[1]) and int(old[0]) < int(new[0]):
            move_order[0].path.extend((x, old[1]) for x in range(int(old[0]), int(new[0]), step))
        elif int(old[1]) < int(new[1]) and int(old[0]) < int(new[0]):
            x, y = int(old[0]), int(old[1])
            while y < int(new[1]) and x < int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, step, step)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), step))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), step))
        elif int(old[1]) >= int(new[1]) and int(old[0]) >= int(new[0]):
            x, y = int(old[0]), int(old[1])

            while y >= int(new[1]) and x >= int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, -step, -step)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), -step))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), -step))
        elif int(old[1]) < int(new[1]) and int(old[0]) >= int(new[0]):
            x, y = int(old[0]), int(old[1])

            while y < int(new[1]) and x >= int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, -step, step)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), -step))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), step))
        elif int(old[1]) >= int(new[1]) and int(old[0]) < int(new[0]):
            x, y = int(old[0]), int(old[1])

            while y >= int(new[1]) and x < int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, step, -step)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), step))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), -step))

        return move_order

    @staticmethod
    def append_(move_order, x, y, step_x, step_y):
        move_order[0].path.append((x, y))
        x += step_x
        move_order[0].path.append((x, y))
        y += step_y
        return move_order, x, y

    @staticmethod
    def update_engaged_points(goal_row, goal_col, row_active, col_active):
        new, old = (goal_row, goal_col), (row_active, col_active)

        States.hexagons[old[0]][old[1]].who_engaged = None
        if States.queue.current[0].character in Settings.double_hex_units:
            States.hexagons[old[0]][old[1] + 1].who_engaged = None

        States.hexagons[new[0]][new[1]].who_engaged = States.queue.current[0]
        if States.queue.current[0].character in Settings.double_hex_units:
            States.hexagons[new[0]][new[1] + 1].who_engaged = States.queue.current[0]

        States.queue.current[0].hex.clear()
        States.queue.current[0].hex.append([new[0], new[1]])
        if States.queue.current[0].character in Settings.double_hex_units:
            States.queue.current[0].hex.append([new[0], new[1] + 1])

    def is_neighbors(self, a, b):
        a = self.offset2cube(a[0], a[1])
        b = self.offset2cube(b[0], b[1])
        for i in range(6):
            if self.cube_neighbor(a, i) == b:
                return True
        return False

    @staticmethod
    def draw_hexagons(screen):
        for rows in States.hexagons:
            for item in rows:
                item.draw(screen)
