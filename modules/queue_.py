import gc
from modules.states import States


class Queue:

    def __init__(self, left_team, right_team):
        self.sequence = None
        self.sequence_ids = None
        self.dead_units = []

        self.init(left_team, right_team)

    def init(self, left_team, right_team):
        self.generate_move_order(left_team, right_team)
        self.get_sequence_ids()

    def generate_move_order(self, left_team, right_team):
        left = sorted(left_team, key=lambda x: (x.characteristics["base_characteristics"]["speed"], x.hex[0][0], x.hex[0][1]), reverse=True)
        right = sorted(right_team, key=lambda x: (x.characteristics["base_characteristics"]["speed"], x.hex[0][0], x.hex[0][1]), reverse=True)

        self.sequence = []
        while left and right:
            if left[0].characteristics["base_characteristics"]["speed"] >= right[0].characteristics["base_characteristics"]["speed"]:
                self.sequence.append(left.pop(0))
            else:
                self.sequence.append(right.pop(0))

        self.sequence.extend(left)
        self.sequence.extend(right)

    def get_sequence_ids(self):
        self.sequence_ids = [id(unit) for unit in self.sequence]

    def reset_queue(self):
        self.sequence = self.get_sequence()
        self.reset_units()

    def reset_units(self):
        for unit in self.sequence:
            unit.reset_round()

    def get_sequence(self):
        return [self.objects_by_id(id_) for id_ in self.sequence_ids]

    @staticmethod
    def objects_by_id(id_):
        for obj in gc.get_objects():
            if id(obj) == id_:
                return obj

    def drop_unit_by_id(self, id_):
        self.sequence_ids.remove(id_)
        for i, unit in enumerate(self.sequence):
            if id(unit) == id_:
                self.dead_units.append(self.sequence.pop(i))

    def handle_wait(self):
        index = self.get_wait_index()
        self.sequence[0].is_wait = True
        self.sequence.insert(index, self.sequence.pop(0))

    def get_wait_index(self):
        for i, item in reversed(list(enumerate(self.sequence))):
            if item.is_wait is False:
                return i
        return 0

    def handle_defense(self):
        States.step += 1
        self.sequence[0].is_defense, self.sequence[0].is_wait = True, True
        self.sequence.append(self.sequence.pop(0))

    def handle_move(self):
        States.step += 1
        self.sequence[0].is_defense, self.sequence[0].is_wait = True, True
        self.sequence.append(self.sequence.pop(0))

    def handle_death(self, id_):
        self.drop_unit_by_id(id_)
