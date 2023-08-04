from copy import copy


class Queue:

    def __init__(self, move_order):
        self.original = copy(move_order)
        self.current = copy(move_order)

    def reset_characters(self):
        for ch in self.original:
            ch.btn_wait = False
            ch.btn_defense = False

    def reset_queue(self):
        self.current = copy(self.original)
