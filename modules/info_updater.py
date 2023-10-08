from modules.hex_worker import HexWorker
from modules.settings import Settings, States


class InfoUpdater:

    def __init__(self):
        self.hex_worker = HexWorker()

    @staticmethod
    def generate_move_order(left_team, right_team):
        left = sorted(left_team, key=lambda x: (x.speed, x.hex[0][0], x.hex[0][1]), reverse=True)
        right = sorted(right_team, key=lambda x: (x.speed, x.hex[0][0], x.hex[0][1]), reverse=True)

        move_order = []
        while left and right:
            if left[0].speed >= right[0].speed:
                move_order.append(left.pop(0))
            else:
                move_order.append(right.pop(0))
        move_order.extend(left)
        move_order.extend(right)
        return move_order

    @staticmethod
    def update_steps():
        States.step = 0

    @staticmethod
    def update_rounds():
        States.round += 1

    def update_step_info(self):
        if not States.is_animate:
            self.update_active_info()
            self.hex_worker.update_reachable_points()

    @staticmethod
    def update_active_info():
        States.unit_active = States.queue.current[0]
        States.speed_active = States.queue.current[0].speed

        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        States.active_is_double = States.hexagons[row_active][col_active].who_engaged.character in Settings.double_hex_units
