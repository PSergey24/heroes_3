import queue
import numpy as np

from modules.settings import Settings
from modules.states import States, Objects
from modules.hexagons import Hex


class Field:

    def __init__(self):
        self.hexagons = None

        self.init()

    def init(self):
        self.create_hexagons()

    def create_hexagons(self):
        self.hexagons = [[Hex(row, col) for col in range(Settings.n_columns)] for row in range(Settings.n_rows)]

    def handle_motion(self):
        self.update_default_hexagons()
        self.update_active_hexagons()
        self.update_hover_hexagons()

    def update_default_hexagons(self):
        for r in range(len(self.hexagons)):
            for c in range(len(self.hexagons[0])):
                self.update_hexagon(r, c, Settings.COLOR_BORDER, Settings.bold)
                self.update_reachable_hexagons(r, c)

    def update_reachable_hexagons(self, r, c):
        if (r, c) in Objects.active_unit.reachable_points and self.hexagons[r][c].engaged is None and States.is_animate is False:
            self.update_hexagon(r, c, Settings.COLOR_POSSIBLE, 0)

    def update_hover_hexagons(self):
        if 0 <= Objects.cursor.offset[0] < Settings.n_rows and 0 <= Objects.cursor.offset[1] < Settings.n_columns and States.is_animate is False:
            self.update_hexagon(Objects.cursor.offset[0], Objects.cursor.offset[1], Settings.COLOR_HOVER, 0)

    def update_active_hexagons(self):
        for r, c in Objects.active_unit.info.hex:
            self.update_hexagon(r, c, Settings.COLOR_ACTIVE, 3)

    @staticmethod
    def update_hexagon(r, c, color, bold):
        Objects.field.hexagons[r][c].color = color
        Objects.field.hexagons[r][c].bold = bold

    def get_route(self):
        start, goal = Objects.tools.offset2cube(Objects.active_unit.info.hex[0][0], Objects.active_unit.info.hex[0][1]), Objects.tools.offset2cube(Objects.cursor.destination_point[0], Objects.cursor.destination_point[1])
        route = self.route_search(start, goal)
        return route

    @staticmethod
    def route_search(start, goal):
        frontier = queue.PriorityQueue()
        frontier.put(start)

        came_from, cost_so_far = dict(), dict()
        came_from[start], cost_so_far[start] = None, 0

        while not frontier.empty():
            current = frontier.get()

            for i in range(6):
                neighbor = Objects.tools.cube_neighbor(current, i)
                row, col = Objects.tools.cube2offset(neighbor[0], neighbor[1], neighbor[2])
                if 0 <= row < Settings.n_rows and 0 <= col < Settings.n_columns:
                    new_cost = cost_so_far[current] + 1
                    if (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]) and \
                            (Objects.field.hexagons[row][col].engaged is None or id(Objects.field.hexagons[row][col].engaged) == id(Objects.active_unit.info) or Objects.active_unit.info.characteristics["is_flyer"] is True or Objects.active_unit.info.characteristics["is_jumper"] is True):
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + Objects.tools.cube_distance(goal, neighbor)
                        frontier.put(neighbor, priority)
                        came_from[neighbor] = current

        way = []
        row, col = Objects.tools.cube2offset(goal[0], goal[1], goal[2])
        way.insert(0, (row, col))

        while came_from[goal]:
            row, col = Objects.tools.cube2offset(came_from[goal][0], came_from[goal][1], came_from[goal][2])
            way.insert(0, (row, col))
            goal = came_from[goal]
        return way

    @staticmethod
    def route_update(route):
        if Objects.active_unit.info.characteristics["is_flyer"] or Objects.active_unit.info.characteristics["is_jumper"]:
            return route

        route_cube = [Objects.tools.offset2cube(r, c) for r, c in route]

        new_route = []
        for x, y, z in route_cube:
            if len(new_route) > 1 and x == new_route[-2][0] and x == new_route[-1][0]:
                new_route[-1][1] = y
                new_route[-1][2] = z
            elif len(new_route) > 1 and y == new_route[-2][1] and y == new_route[-1][1]:
                new_route[-1][0] = x
                new_route[-1][2] = z
            elif len(new_route) > 1 and z == new_route[-2][2] and z == new_route[-1][2]:
                new_route[-1][0] = x
                new_route[-1][1] = y
            else:
                new_route.append([x, y, z])

        return [Objects.tools.cube2offset(x, y, z) for x, y, z in new_route]

    def get_steps(self, route):
        steps = []
        if Objects.active_unit.info.characteristics["is_jumper"] is False:
            for i in range(1, len(route), 1):
                steps.extend(self.generate_step(route[i - 1], route[i]))

            last_point = Objects.field.hexagons[route[-1][0]][route[-1][1]].corner
            steps.append(last_point)
        return steps

    @staticmethod
    def generate_step(start_point, finish_point):
        """
        Function converts points to pixel's coordinates
        :param start_point:
        :param finish_point:
        :return: pixel's route
        """
        old = Objects.field.hexagons[start_point[0]][start_point[1]].corner
        new = Objects.field.hexagons[finish_point[0]][finish_point[1]].corner

        a = Objects.tools.offset2cube(start_point[0], start_point[1])
        b = Objects.tools.offset2cube(finish_point[0], finish_point[1])
        distance = Objects.tools.cube_distance(a, b)
        points_count = 20

        # equation of a line: k = (y2 — y1) / (x2 — x1); b = y1 — k * x1
        k = (new[1] - old[1]) / (new[0] - old[0])
        b = old[1] - k * old[0]

        x_list = np.round(np.linspace(old[0], new[0], num=distance * points_count), 1)
        return [(x, round(k * x + b, 1)) for x in x_list]

    @staticmethod
    def update_engaged_points():
        new, old = Objects.cursor.destination_point, Objects.active_unit.info.hex[0]

        Objects.field.hexagons[old[0]][old[1]].engaged = None
        if Objects.active_unit.info.characteristics["is_double"]:
            Objects.field.hexagons[old[0]][old[1] + 1].engaged = None

        Objects.field.hexagons[new[0]][new[1]].engaged = Objects.active_unit.info
        if Objects.active_unit.info.characteristics["is_double"]:
            Objects.field.hexagons[new[0]][new[1] + 1].engaged = Objects.active_unit.info

        Objects.active_unit.info.hex.clear()
        Objects.active_unit.info.hex.append([new[0], new[1]])
        if Objects.active_unit.info.characteristics["is_double"]:
            Objects.active_unit.info.hex.append([new[0], new[1] + 1])

    def draw(self, screen):
        [item.draw(screen) for rows in self.hexagons for item in rows]
