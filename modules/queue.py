from copy import copy


class Queue:

    def __init__(self, move_order):
        self.original = copy(move_order)
        self.current = copy(move_order)
