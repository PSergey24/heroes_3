import os
import pygame
from copy import copy
from modules.settings import Settings
from modules.fields import Field
from modules.dijkstra import Graph, Node


class InfoUpdater:

    def __init__(self):
        pass

    def create_fields(self, fields):
        corner = copy(Settings.start_battle_filed)

        x = 1
        for i in range(Settings.n_rows):
            row = []
            for j in range(Settings.n_columns):
                field = Field(copy(corner), Settings.COLOR_BORDER, Settings.bold)
                field.coordinates = copy(self.get_coordinates(corner, 0))
                field.position = copy(self.get_position(0))
                field.surf = pygame.Surface((2 * (Settings.r + Settings.bold), 2 * (Settings.R + Settings.bold)),
                                            pygame.SRCALPHA)
                row.append(field)
                corner[1] += 2 * Settings.r

            fields.append(row)
            corner[0] += 1.5 * Settings.R
            corner[1] = (corner[1] - Settings.n_columns * 2 * Settings.r) + x * Settings.r
            x *= (-1)
        return fields

    @staticmethod
    def get_position(indent):
        return [[indent, (Settings.R + indent) / 2], [indent, (Settings.R * 3 - indent) / 2],
                [Settings.r, Settings.R * 2 - indent], [2 * Settings.r - indent, (Settings.R * 3 - indent) / 2],
                [2 * Settings.r - indent, (Settings.R + indent) / 2], [Settings.r, indent]]

    @staticmethod
    def get_coordinates(corner, indent):
        return [[corner[1] + indent, corner[0] + Settings.R / 2 + indent],
                [corner[1] + indent, corner[0] + Settings.R * 3 / 2 - indent],
                [corner[1] + Settings.r, corner[0] + Settings.R * 2 - indent],
                [corner[1] + 2 * Settings.r - indent, corner[0] + Settings.R * 3 / 2 - indent],
                [corner[1] + 2 * Settings.r - indent, corner[0] + Settings.R / 2 + indent],
                [corner[1] + Settings.r, corner[0] + indent]]

    def create_characters(self, fields, team):
        for i, character in enumerate(team):
            character.x, character.y = self.get_cell_corner(fields, character.position)
            fields[character.position[0]][character.position[1]].is_engaged = True
            fields[character.position[0]][character.position[1]].who_engaged = team[i]
        return fields

    @staticmethod
    def get_cell_corner(fields, position):
        return fields[position[0]][position[1]].corner[1], fields[position[0]][position[1]].corner[0]

    @staticmethod
    def generate_move_order(left_team, right_team):
        left = sorted(left_team, key=lambda x: (x.speed, x.position[0], x.position[1]), reverse=True)
        right = sorted(right_team, key=lambda x: (x.speed, x.position[0], x.position[1]), reverse=True)

        move_order = []
        while left and right:
            if left[0].speed >= right[0].speed:
                move_order.append(left.pop(0))
            else:
                move_order.append(right.pop(0))
        move_order.extend(left)
        move_order.extend(right)
        return move_order

    def update_character_position(self, fields, move_order, new_point):
        move_order = self.generate_way(fields, move_order, move_order[0].position, new_point)
        fields = self.update_engaged_points(fields, move_order, move_order[0].position, new_point)
        move_order[0].position = new_point
        return fields, move_order

    @staticmethod
    def get_way(pos_x, pos_y, speed):
        dp = {}

        def dfs(i, j, cur_speed):
            if i < 0 or i > Settings.n_rows - 1:
                return
            if j < 0 or j > Settings.n_columns - 1:
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

    def generate_way(self, fields, move_order, old_point, new_point):
        move_order[0].is_animation = True
        path = self.find_path(fields, old_point, new_point)
        for i in range(1, len(path), 1):
            move_order = self.generate_steps(fields, move_order, path[i - 1], path[i])
        return move_order

    def find_path(self, fields, old_point, new_point):
        nodes = [Node(i * len(fields[0]) + j) for i in range(len(fields)) for j in range(len(fields[0]))]
        w_graph = Graph.create_from_nodes(nodes)

        for i in range(len(fields)):
            for j in range(len(fields[0])):
                idx = i * len(fields[0]) + j
                nearest_fields = self.get_nearest_fields(fields, i, idx)
                if fields[i][j].is_engaged is False:
                    for neighbour in nearest_fields:
                        if 0 < neighbour < Settings.n_columns * Settings.n_rows:
                            w_graph.connect(idx, neighbour, 1)

        idx_old = old_point[0] * len(fields[0]) + old_point[1]
        idx_new = new_point[0] * len(fields[0]) + new_point[1]

        path = self.get_path(w_graph, idx_old, idx_new)
        return [(item // Settings.n_columns, item % Settings.n_columns) for item in path]

    @staticmethod
    def get_nearest_fields(fields, i, idx):
        return [idx - len(fields[0]) - 1, idx - len(fields[0]), idx - 1, idx + 1,
                idx + len(fields[0]) - 1, idx + len(fields[0])] if i % 2 == 0 else \
            [idx - len(fields[0]), idx - len(fields[0]) + 1, idx - 1, idx + 1,
             idx + len(fields[0]), idx + len(fields[0]) + 1]

    @staticmethod
    def get_path(w_graph, idx_old, idx_new):
        for (weight, node) in w_graph.dijkstra(idx_old):
            path = [n.data for n in node]
            if path[len(path) - 1] == idx_new and path[0] == idx_old:
                return path

    def generate_steps(self, fields, move_order, old_point, new_point):
        old = self.get_cell_corner(fields, old_point)
        new = self.get_cell_corner(fields, new_point)

        move_order[0].direction = True
        if int(old[1]) > int(new[1]) and int(old[0]) == int(new[0]):
            move_order[0].path.extend((old[0], y) for y in range(int(old[1]), int(new[1]), -2))
        elif int(old[1]) < int(new[1]) and int(old[0]) == int(new[0]):
            move_order[0].path.extend((old[0], y) for y in range(int(old[1]), int(new[1]), 2))
        elif int(old[1]) == int(new[1]) and int(old[0]) > int(new[0]):
            move_order[0].path.extend((x, old[1]) for x in range(int(old[0]), int(new[0]), -2))
        elif int(old[1]) == int(new[1]) and int(old[0]) < int(new[0]):
            move_order[0].direction = False
            move_order[0].path.extend((x, old[1]) for x in range(int(old[0]), int(new[0]), 2))
        elif int(old[1]) < int(new[1]) and int(old[0]) < int(new[0]):
            move_order[0].direction = False
            x, y = int(old[0]), int(old[1])
            while y < int(new[1]) and x < int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, 2, 2)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), 2))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), 2))
        elif int(old[1]) >= int(new[1]) and int(old[0]) >= int(new[0]):
            x, y = int(old[0]), int(old[1])

            while y >= int(new[1]) and x >= int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, -2, -2)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), -2))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), -2))
        elif int(old[1]) < int(new[1]) and int(old[0]) >= int(new[0]):
            x, y = int(old[0]), int(old[1])

            while y < int(new[1]) and x >= int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, -2, 2)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), -2))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), 2))
        elif int(old[1]) >= int(new[1]) and int(old[0]) < int(new[0]):
            move_order[0].direction = False
            x, y = int(old[0]), int(old[1])

            while y >= int(new[1]) and x < int(new[0]):
                move_order, x, y = self.append_(move_order, x, y, 2, -2)

            move_order[0].path.extend((x, y) for x in range(x, int(new[0]), 2))
            move_order[0].path.extend((x, y) for y in range(y, int(new[1]), -2))

        return move_order

    @staticmethod
    def append_(move_order, x, y, step_x, step_y):
        move_order[0].path.append((x, y))
        x += step_x
        move_order[0].path.append((x, y))
        y += step_y
        return move_order, x, y

    @staticmethod
    def update_engaged_points(fields, move_order, old_point, new_point):
        fields[old_point[0]][old_point[1]].is_engaged = False
        fields[old_point[0]][old_point[1]].who_engaged = None
        fields[new_point[0]][new_point[1]].is_engaged = True
        fields[new_point[0]][new_point[1]].who_engaged = move_order[0]
        return fields

    @staticmethod
    def update_cursor_info(fields, move_order, point_over, cursor, coordinates):
        pos_x, pos_y = point_over
        point_attack = None
        whom_attack = None

        if Settings.n_rows - 1 > pos_x >= 0 and Settings.n_columns - 1 > pos_y >= 0:
            if pos_x % 2 == 0:
                if fields[pos_x - 1][pos_y].is_engaged and fields[pos_x - 1][pos_y].who_engaged.team != move_order[0].team:
                    if fields[pos_x - 1][pos_y].bottom + Settings.R / 2 > coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x - 1][pos_y].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom016.png"))
                if fields[pos_x - 1][pos_y - 1].is_engaged and fields[pos_x - 1][pos_y - 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x - 1][pos_y - 1].bottom + Settings.R / 2 > coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x - 1][pos_y - 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom022.png"))
                if fields[pos_x][pos_y - 1].is_engaged and fields[pos_x][pos_y - 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x][pos_y - 1].right + Settings.r > coordinates[0]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x][pos_y - 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom021.png"))
                if fields[pos_x][pos_y + 1].is_engaged and fields[pos_x][pos_y + 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x][pos_y + 1].left - Settings.r < coordinates[0]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x][pos_y + 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom017.png"))
                if fields[pos_x + 1][pos_y].is_engaged and fields[pos_x + 1][pos_y].who_engaged.team != move_order[0].team:
                    if fields[pos_x + 1][pos_y].top - Settings.R / 2 < coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x + 1][pos_y].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom018.png"))
                if fields[pos_x + 1][pos_y - 1].is_engaged and fields[pos_x + 1][pos_y - 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x + 1][pos_y - 1].top - Settings.R / 2 < coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x + 1][pos_y - 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom020.png"))

            if pos_x % 2 == 1:
                if fields[pos_x - 1][pos_y].is_engaged and fields[pos_x - 1][pos_y].who_engaged.team != move_order[0].team:
                    if fields[pos_x - 1][pos_y].bottom + Settings.R / 2 > coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x - 1][pos_y].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom022.png"))
                if fields[pos_x - 1][pos_y + 1].is_engaged and fields[pos_x - 1][pos_y + 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x - 1][pos_y + 1].bottom + Settings.R / 2 > coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x - 1][pos_y + 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom016.png"))
                if fields[pos_x][pos_y - 1].is_engaged and fields[pos_x][pos_y - 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x][pos_y - 1].right + Settings.r > coordinates[0]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x][pos_y - 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom021.png"))
                if fields[pos_x][pos_y + 1].is_engaged and fields[pos_x][pos_y + 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x][pos_y + 1].left - Settings.r < coordinates[0]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x][pos_y + 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom017.png"))
                if fields[pos_x + 1][pos_y].is_engaged and fields[pos_x + 1][pos_y].who_engaged.team != move_order[0].team:
                    if fields[pos_x + 1][pos_y].top - Settings.R / 2 < coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x + 1][pos_y].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom020.png"))
                if fields[pos_x + 1][pos_y + 1].is_engaged and fields[pos_x + 1][pos_y + 1].who_engaged.team != move_order[0].team:
                    if fields[pos_x + 1][pos_y + 1].top - Settings.R / 2 < coordinates[1]:
                        point_attack = [pos_x, pos_y]
                        whom_attack = fields[pos_x + 1][pos_y + 1].who_engaged
                        cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom018.png"))
        pygame.mouse.set_cursor(pygame.cursors.Cursor((15, 0), cursor))
        return point_attack, whom_attack

    def update_fields_info(self, fields, move_order, point_over):
        pos_x, pos_y = point_over
        old_pos = move_order[0].position
        possible_ways = self.get_way(old_pos[0], old_pos[1], move_order[0].speed)

        for i in range(len(fields)):
            for j in range(len(fields[0])):
                is_hover, is_possible, is_current = False, False, False
                if i == pos_x and j == pos_y:
                    is_hover = True
                if (i, j) in possible_ways:
                    is_possible = True
                if i == old_pos[0] and j == old_pos[1]:
                    is_current = True

                fields[i][j].indent, fields[i][j].color, fields[i][j].bold = \
                    self.get_features(is_hover, is_possible, is_current)
                fields[i][j].coordinates = self.get_coordinates(fields[i][j].corner, 0)
                fields[i][j].position = self.get_position(fields[i][j].indent)

        if fields[pos_x][pos_y].is_engaged:
            speed = fields[pos_x][pos_y].who_engaged.speed
            possible_ways = self.get_way(pos_x, pos_y, speed)
            for i, j in possible_ways:
                fields[i][j].color = (40, 40, 40, 120)
                fields[i][j].bold = 0
                fields[i][j].indent = 6
                fields[i][j].position = self.get_position(fields[i][j].indent)
        return fields

    @staticmethod
    def get_features(is_hover, is_possible, is_current):
        if is_hover:
            return 6, Settings.COLOR_HOVER, 0
        if is_current:
            return 0, Settings.COLOR_ACTIVE, Settings.bold
        if is_possible:
            return 2, Settings.COLOR_POSSIBLE, 0
        return 0, Settings.COLOR_BORDER, Settings.bold
