from modules.settings import Settings, States
from modules.hex_worker import HexWorker


class AIActionWorker:

    def __init__(self):
        self.matrix = None

        self.hex_worker = HexWorker()

    def num_to_action(self, ai_move):
        index_move = ai_move.index(1)

        if index_move == 1155:
            print(f"Press wait")
            return "wait", 0
        if index_move == 1156:
            print(f"Press defend")
            return "defend", 0

        cell_number = index_move // 7
        direction = index_move % 7

        States.point_attack, States.whom_attack = None, None
        print(f"index_move is {index_move}, cell number is {cell_number}")

        row = cell_number // Settings.n_columns
        col = cell_number % Settings.n_columns

        States.point_r, States.point_c = row, col

        if (row, col) not in States.reachable_points:
            return False, -5
        if direction == 6 and (row, col) in States.reachable_points:
            return 'moving', 0

        x, y, z = self.hex_worker.offset2cube(row, col)
        nb_x, nb_y, nb_z = self.hex_worker.cube_neighbor((x, y, z), direction)
        nb_r, nb_c = self.hex_worker.cube2offset(nb_x, nb_y, nb_z)

        if 0 <= nb_r < Settings.n_rows and 0 <= nb_c < Settings.n_columns:
            States.point_attack = [nb_r, nb_c]
            States.whom_attack = States.hexagons[row][col].who_engaged
            if not States.whom_attack or States.whom_attack.team == States.queue.current[0].team:
                return False, -5
            if States.point_r < States.whom_attack.hex[0][0]:
                return 'attack_down', 5
            if States.point_r > States.whom_attack.hex[0][0]:
                return 'attack_up', 5
            return 'attack_straight', 5
        else:
            return False, -5
