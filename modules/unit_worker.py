
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
        if len(States.animations) > 0:
            if States.animations[0].who.is_active is False:
                States.animations[0].who.is_active = True
                States.animations[0].who.animation_count = 0

            States.animations[0].who.draw(screen)

        for item in States.queue.current:
            if len(States.animations) == 0 or (len(States.animations) > 0 and item != States.animations[0]):
                item.draw(screen)

