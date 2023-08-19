
from modules.settings import Settings, States


class UnitWorker:

    def __init__(self):
        pass

    @staticmethod
    def create_units(team):
        for unit in team:
            States.hexagons[unit.hex[0]][unit.hex[1]].who_engaged = unit
            unit.x = States.hexagons[unit.hex[0]][unit.hex[1]].corner[0]
            unit.y = States.hexagons[unit.hex[0]][unit.hex[1]].corner[1]

    @staticmethod
    def draw_units(screen):
        for item in States.queue.current:
            item.draw(screen)
