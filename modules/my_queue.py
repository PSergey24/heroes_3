import gc

from copy import copy


class MyQueue:

    def __init__(self, move_order):
        self.ids = self.get_ids(move_order)
        self.current = copy(move_order)
        self.dead = []

    @staticmethod
    def get_ids(move_order):
        return[id(item) for item in move_order]

    def update_queue(self):
        self.reset_characters()
        self.current = self.get_order()

    def reset_characters(self):
        for ch in self.current:
            ch.btn_wait = False
            ch.btn_defense = False
            ch.is_answer = 1

    def get_order(self):
        return [self.objects_by_id(id_) for id_ in self.ids]

    @staticmethod
    def objects_by_id(id_):
        for obj in gc.get_objects():
            if id(obj) == id_:
                return obj
        raise Exception("No found")

    def drop_unit_by_id(self, id_):
        self.ids.remove(id_)
        for i, unit in enumerate(self.current):
            if id(unit) == id_:
                self.dead.append(self.current.pop(i))
