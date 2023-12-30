from modules.settings import Settings, States
from modules.hex_worker import HexWorker
import math


class AIActionWorker:

    def __init__(self):
        self.matrix = None

        self.hex_worker = HexWorker()

    def num_to_action(self, ai_move):
        index_move = ai_move.index(1)

        cell_move, direction = math.floor(index_move / 7), index_move % 7
        States.point_r, States.point_c = math.floor(cell_move / Settings.n_columns), cell_move % Settings.n_columns

        States.point_attack, States.whom_attack = None, None

        print(f"New move. Row: {States.point_r}, col: {States.point_c}, direction: {direction}")

        if direction == 6 and (States.point_r, States.point_c) not in States.reachable_points:
            print(f"Point ({States.point_r}, {States.point_c}) is far!")
            return False, -1

        if direction == 6 and (States.point_r, States.point_c) in States.reachable_points:
            print(f"Unit {States.unit_active.character} is moving to ({States.point_r}, {States.point_c})")
            return 'moving', 0

        x, y, z = self.hex_worker.offset2cube(States.point_r, States.point_c)
        nb_x, nb_y, nb_z = self.hex_worker.cube_neighbor((x, y, z), direction)
        nb_r, nb_c = self.hex_worker.cube2offset(nb_x, nb_y, nb_z)

        States.point_attack = [States.point_r, States.point_c]
        States.whom_attack = States.hexagons[nb_r][nb_c].who_engaged

        if States.point_r < States.whom_attack.hex[0][0]:
            print(f"Unit is attacking down")
            return 'attack_down', 0.2
        if States.point_r > States.whom_attack.hex[0][0]:
            print(f"Unit is attacking up")
            return 'attack_up', 0.2
        if States.point_r == States.whom_attack.hex[0][0]:
            print(f"Unit is attacking straight")
            return 'attack_straight', 0.2

        print("Unexpected action!")
        return False, -1
