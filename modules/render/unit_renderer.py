class UnitRenderer:

    def __init__(self):
        pass

    @staticmethod
    def draw_unit(screen, unit_):
        if hasattr(unit_, 'draw'):
            unit_.draw(screen)


