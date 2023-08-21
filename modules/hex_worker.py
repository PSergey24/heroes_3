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
        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))

        if 0 <= States.point_r < Settings.n_rows and 0 <= States.point_c < Settings.n_columns and \
                States.is_animate is False:
            if States.hexagons[States.point_r][States.point_c].who_engaged is None or \
                    ((States.row_active == States.point_r) and (States.col_active == States.point_c)):
                States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom009.png"))
                if States.queue.current[0].is_flyer:
                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom012.png"))
                if (States.row_active == States.point_r) and (States.col_active == States.point_c):
                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom028.png"))

                States.point_attack, States.whom_attack = None, None
                if States.btn_shooter is False:
                    x = States.hexagons[States.point_r][States.point_c].corner[0] + Settings.r
                    y = States.hexagons[States.point_r][States.point_c].corner[1] + Settings.R
                    degrees = ((math.atan2(States.point_over[1] - y,
                                           States.point_over[0] - x) + 2 * math.pi) * 180 / math.pi) % 360

                    for i in range(6):
                        nb_x, nb_y, nb_z = self.cube_neighbor((States.point_x, States.point_y, States.point_z), i)
                        nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)

                        if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns and \
                                (States.point_r, States.point_c) in States.reachable_points:
                            if States.hexagons[nb_r][nb_c].who_engaged is not None and \
                                    States.hexagons[States.row_active][States.col_active].who_engaged.team != States.hexagons[nb_r][nb_c].who_engaged.team:
                                if (0 <= degrees < 45 or 315 <= degrees < 360) and i == 0:
                                    States.point_attack = [States.point_r, States.point_c]
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom017.png"))
                                elif 45 <= degrees < 90 and i == 5:
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom018.png"))
                                elif 90 <= degrees < 135 and i == 4:
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom020.png"))
                                elif 135 <= degrees < 225 and i == 3:
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom021.png"))
                                elif 225 <= degrees < 270 and i == 2:
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom022.png"))
                                elif 270 <= degrees < 315 and i == 1:
                                    States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged
                                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom016.png"))
            else:
                x, y, z = self.offset2cube(States.row_active, States.col_active)
                is_neighbor_enemy = False
                for i in range(6):
                    nb_x, nb_y, nb_z = self.cube_neighbor((x, y, z), i)
                    nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
                    if States.hexagons[nb_r][nb_c].who_engaged is not None and States.hexagons[nb_r][nb_c].who_engaged.team != States.hexagons[States.row_active][States.col_active].who_engaged.team:
                        is_neighbor_enemy = True
                        break

                if is_neighbor_enemy is False and States.btn_shooter is True and States.hexagons[States.row_active][States.col_active].who_engaged.team != States.hexagons[States.point_r][States.point_c].who_engaged.team:
                    States.whom_attack = States.hexagons[States.point_r][States.point_c].who_engaged
                    dist = self.cube_distance(self.offset2cube(States.row_active, States.col_active), [States.point_x, States.point_y, States.point_z])
                    if dist <= 10:
                        States.penalty_shooter = 1
                        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom023.png"))
                    else:
                        States.penalty_shooter = 0.5
                        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom026.png"))
                else:
                    States.whom_attack = None
                    States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom028.png"))

    @staticmethod
    def update_hexagons():
        for r in range(len(States.hexagons)):
            for c in range(len(States.hexagons[0])):
                States.hexagons[r][c].color = Settings.COLOR_BORDER
                States.hexagons[r][c].bold = Settings.bold

                if (r, c) in States.reachable_points and States.hexagons[r][c].who_engaged is None and \
                        States.is_animate is False:
                    States.hexagons[r][c].color = Settings.COLOR_POSSIBLE
                    States.hexagons[r][c].bold = 0

        if 0 <= States.point_r < Settings.n_rows and 0 <= States.point_c < Settings.n_columns and \
                States.is_animate is False:
            States.hexagons[States.point_r][States.point_c].color = Settings.COLOR_HOVER
            States.hexagons[States.point_r][States.point_c].bold = 0

        States.hexagons[States.row_active][States.col_active].color = Settings.COLOR_ACTIVE
        States.hexagons[States.row_active][States.col_active].bold = 3

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
        x_active, y_active, z_active = self.offset2cube(States.row_active, States.col_active)
        speed_active = States.queue.current[0].speed
        States.reachable_points = self.cube_reachable((x_active, y_active, z_active), speed_active,
                                                      States.queue.current[0].is_flyer)

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
    def cube_distance(a, b):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

    @staticmethod
    def get_move_type():
        if States.whom_attack:
            if States.queue.current[0].team != States.whom_attack.team:
                States.point_attack = (States.point_r, States.point_c)
                if States.btn_shooter:
                    if States.point_r > States.whom_attack.hex[0]:
                        return 'shoot_up'
                    if States.point_r < States.whom_attack.hex[0]:
                        return 'shoot_down'
                    return 'shoot_straight'
                else:
                    if States.point_r > States.whom_attack.hex[0]:
                        return 'attack_up'
                    if States.point_r < States.whom_attack.hex[0]:
                        return 'attack_down'
                    return 'attack_straight'

        if 0 <= States.point_r < Settings.n_rows and 0 <= States.point_c < Settings.n_columns and \
                States.hexagons[States.point_r][States.point_c].who_engaged is None and \
                (States.point_r, States.point_c) in States.reachable_points:
            return 'moving'
        return False

    # way search
    def update_character_position(self):
        start = self.offset2cube(States.row_active, States.col_active)
        goal = (States.point_x, States.point_y, States.point_z)

        way = self.way_search(start, goal)
        self.generate_steps(way)

        self.update_engaged_points()

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
                            (States.hexagons[row][col].who_engaged is None or States.queue.current[0].is_flyer is True):
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
    def update_engaged_points():
        new, old = (States.point_r, States.point_c), (States.row_active, States.col_active)

        States.hexagons[old[0]][old[1]].who_engaged = None
        States.hexagons[new[0]][new[1]].who_engaged = States.queue.current[0]

        States.queue.current[0].hex = [new[0], new[1]]

    @staticmethod
    def draw_hexagons(screen):
        for rows in States.hexagons:
            for item in rows:
                item.draw(screen)
