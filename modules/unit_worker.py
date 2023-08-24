import random

from modules.hex_worker import HexWorker
from modules.settings import Settings, States


class UnitWorker:

    def __init__(self):
        self.hex_worker = HexWorker()

    @staticmethod
    def create_units(team):
        for unit in team:
            States.hexagons[unit.hex[0]][unit.hex[1]].who_engaged = unit
            unit.x = States.hexagons[unit.hex[0]][unit.hex[1]].corner[0]
            unit.y = States.hexagons[unit.hex[0]][unit.hex[1]].corner[1]

    # action and damage handler
    def update_units(self, action):
        States.step += 1
        States.queue.current[0].btn_defense, States.queue.current[0].btn_wait = True, True
        print(f"action: {action}")

        if action == 'moving':
            States.is_animate = True
            States.queue.current[0].change_animation('moving', who=States.queue.current[0])
            self.hex_worker.update_character_position()

        if action.find('attack') != -1:
            States.is_animate = True
            if States.row_active != States.point_r or States.col_active != States.point_c:
                States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                self.hex_worker.update_character_position()

            States.queue.current[0].change_animation(action, who=States.queue.current[0])
            States.whom_attack.change_animation('getting_hit', who=States.whom_attack)
            damage = self.damage_counter(States.queue.current[0], States.whom_attack)
            States.whom_attack = self.update_health(States.whom_attack, damage)

            if States.whom_attack.is_answer > 0 and States.whom_attack.count > 0:
                States.whom_attack.change_animation('attack_straight', who=States.whom_attack)
                States.queue.current[0].change_animation('getting_hit', who=States.queue.current[0])
                damage = self.damage_counter(States.whom_attack, States.queue.current[0])
                States.queue.current[0] = self.update_health(States.queue.current[0], damage)
                States.whom_attack.is_answer -= 1
                if States.queue.current[0].count < 1:
                    States.queue.current[0].change_animation('death', who=States.queue.current[0])
                    if States.queue.current[0].btn_defense is True:
                        States.step -= 1
                    States.queue.drop_unit_by_id(id(States.queue.current[0]))
                    States.hexagons[States.queue.current[0].hex[0]][States.queue.current[0].hex[1]].who_engaged = None

            if States.whom_attack.count < 1:
                States.whom_attack.change_animation('death', who=States.whom_attack)
                if States.whom_attack.btn_defense is True:
                    States.step -= 1
                States.queue.drop_unit_by_id(id(States.whom_attack))
                States.hexagons[States.whom_attack.hex[0]][States.whom_attack.hex[1]].who_engaged = None

        if action.find('shoot') != -1:
            States.is_animate = True
            States.queue.current[0].change_animation(action, who=States.queue.current[0])
            States.whom_attack.change_animation('getting_hit', who=States.whom_attack)

        States.queue.current.append(States.queue.current.pop(0))

    def damage_counter(self, attacker, defender):
        k = self.get_damage_k(attacker, defender)
        luck = self.get_luck_k()

        damage = attacker.count * random.randint(attacker.damage[0], attacker.damage[1]) * k * luck
        return damage

    @staticmethod
    def get_damage_k(attacker, defender):
        if attacker.attack - defender.defense > 0:
            k = 0.05 * (attacker.attack - defender.defense)
            k = 1 + (3 if k > 3 else k)
        else:
            k = 0.025 * (defender.defense - attacker.attack)
            k = 1 - (0.7 if k > 0.7 else k)
        return k

    @staticmethod
    def get_luck_k():
        return 1

    @staticmethod
    def update_health(defender, damage):
        count_dead, count_health = int(damage // defender.health), damage % defender.health
        defender.count -= count_dead
        defender.health = count_health
        return defender

    @staticmethod
    def draw_units(screen):
        id_ = None
        if len(States.animations) > 0:
            id_ = id(States.animations[0].who)
            if States.animations[0].who.is_active is False:
                States.animations[0].who.is_active = True
                States.animations[0].who.animation_count = 0
            States.animations[0].who.draw(screen)

        for item in States.queue.current:
            if id_ != id(item):
                item.draw(screen)
