from modules.settings import Settings
from modules.states import Objects
from modules.tools import Tools


class ActiveUnit:

    def __init__(self):
        self.info = None

        self.reachable_points = None
        self.only_left_points = None
        self.only_right_points = None

        self.init()

    def init(self):
        self.info = Objects.queue.sequence[0]

        self.reachable_points = None
        self.only_left_points = None
        self.only_right_points = None

        self.update_reachable_points()

    def update_reachable_points(self):
        x_active, y_active, z_active = Tools.offset2cube(self.info.hex[0][0], self.info.hex[0][1])

        if self.info.characteristics["is_double"]:
            x_active_, y_active_, z_active_ = Tools.offset2cube(self.info.hex[0][0], self.info.hex[0][1] + 1)

            reachable_left = self.cube_reachable_double((x_active, y_active, z_active))
            reachable_right = self.cube_reachable_double((x_active_, y_active_, z_active_), is_left=False)

            self.only_left_points = list(reachable_left - reachable_right)
            self.only_right_points = list(reachable_right - reachable_left)
            self.reachable_points = list(reachable_left.union(reachable_right))

            self.correct_reachable_points()
        else:
            self.cube_reachable_single((x_active, y_active, z_active))

    def cube_reachable_single(self, start):
        self.reachable_points = set()
        self.reachable_points.add(Tools.cube2offset(start[0], start[1], start[2]))

        level = 0
        queue = [(start, level)]
        while queue:
            (x, y, z), level = queue.pop(0)
            level += 1

            for i in range(6):
                neighbor = Tools.cube_neighbor((x, y, z), i)

                r, c = Tools.cube2offset(neighbor[0], neighbor[1], neighbor[2])
                if 0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns:
                    if (r, c) not in self.reachable_points and (Objects.field.hexagons[r][c].engaged is None or self.info.characteristics["is_flyer"] is True or self.info.characteristics["is_jumper"] is True) and level <= self.info.characteristics["base_characteristics"]["speed"]:
                        self.reachable_points.add(Tools.cube2offset(neighbor[0], neighbor[1], neighbor[2]))
                        queue.append((neighbor, level))

    def cube_reachable_double(self, start, is_left=True):
        visited = set()
        visited.add(Tools.cube2offset(start[0], start[1], start[2]))

        level = 0
        queue = [(start, level)]
        while queue:
            (x, y, z), level = queue.pop(0)
            level += 1

            for i in range(6):
                neighbor = Tools.cube_neighbor((x, y, z), i)

                r, c = Tools.cube2offset(neighbor[0], neighbor[1], neighbor[2])
                if (0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns and is_left and c + 1 < Settings.n_columns) or (0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns and not is_left):
                    if is_left:
                        is_left_ = (Objects.field.hexagons[r][c].engaged is None or id(Objects.field.hexagons[r][c].engaged) == id(Objects.queue.sequence[0]))
                        is_right_ = (Objects.field.hexagons[r][c + 1].engaged is None or id(Objects.field.hexagons[r][c + 1].engaged) == id(Objects.queue.sequence[0]))
                    else:
                        is_left_ = (Objects.field.hexagons[r][c - 1].engaged is None or id(Objects.field.hexagons[r][c - 1].engaged) == id(Objects.queue.sequence[0]))
                        is_right_ = (Objects.field.hexagons[r][c].engaged is None or id(Objects.field.hexagons[r][c].engaged) == id(Objects.queue.sequence[0]))

                    if ((r, c) not in visited and ((is_left_ and is_right_) or self.info.characteristics["is_flyer"] is True or self.info.characteristics["is_jumper"] is True)) and level <= self.info.characteristics["base_characteristics"]["speed"]:
                        visited.add(Tools.cube2offset(neighbor[0], neighbor[1], neighbor[2]))
                        queue.append((neighbor, level))

                        if not is_left and Objects.field.hexagons[r][c].engaged is None:
                            visited.add((r, c))
                        if is_left and Objects.field.hexagons[r][c].engaged is None:
                            visited.add((r, c))
        return visited

    def correct_reachable_points(self):

        for r, c in reversed(self.reachable_points):
            if Objects.field.hexagons[r][c].engaged is not None and id(Objects.field.hexagons[r][c].engaged) != id(Objects.queue.sequence[0]):
                self.reachable_points.remove((r, c))
                if (r, c) in self.only_left_points:
                    self.only_left_points.remove((r, c))
                if (r, c) in self.only_right_points:
                    self.only_right_points.remove((r, c))

        for r, c in reversed(self.reachable_points):
            if (r, c + 1) not in self.reachable_points and (r, c - 1) not in self.reachable_points:
                self.reachable_points.remove((r, c))
                if (r, c) in self.only_left_points:
                    self.only_left_points.remove((r, c))
                if (r, c) in self.only_right_points:
                    self.only_right_points.remove((r, c))

        self.reachable_points = set(self.reachable_points)

    def handle_click(self):
        if Objects.cursor.action is not None:
            self.info.handle_click()

    def update(self):
        self.init()
