

class States:

    # game info:
    step = 0
    round = 1

    # shooter btn info:
    btn_shooter = False
    penalty_shooter = 1

    # animations:
    is_animate = False
    active_animation = 1
    current_animation = 1
    stack_animations = []


class Objects:

    tools = None
    damage_counter = None
    cursor = None
    actions = None
    queue = None
    active_unit = None
    animations = None
    field = None
    info_block = None
