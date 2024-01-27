
from modules.settings import Settings
from modules.states import Objects


class Tools:

    @staticmethod
    def offset2cube(row, col):
        return int(col - (row + (row & 1)) / 2), int((row + (row & 1)) / 2 - col - row), int(row)

    @staticmethod
    def cube2offset(x, y, z):
        return int(z), int(x + (z + (z & 1)) / 2)

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

    def enemy_is_neighbor(self, row, col):
        """
        Function will return True if there is an opponent's unit in the adjacent position.
        :param row: unit's row
        :param col: unit's col
        :return: True or False
        """
        x, y, z = self.offset2cube(row, col)
        for i in range(6):
            nb_x, nb_y, nb_z = self.cube_neighbor((x, y, z), i)
            nb_r, nb_c = self.cube2offset(nb_x, nb_y, nb_z)
            if 0 <= nb_c < Settings.n_columns and 0 <= nb_r < Settings.n_rows:
                if Objects.field.hexagons[nb_r][nb_c].engaged is not None and Objects.field.hexagons[nb_r][nb_c].engaged.team != Objects.field.hexagons[row][col].engaged.team:
                    return True
        return False

