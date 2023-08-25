import os
import random
import pygame

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

            damage = self.damage_counter(States.queue.current[0], States.whom_attack)
            States.whom_attack = self.health_updater(States.whom_attack, damage)
            States.whom_attack = self.animation_updater(States.whom_attack)

            if States.whom_attack.is_answer > 0 and States.whom_attack.count > 0:
                States.whom_attack.change_animation('attack_straight', who=States.whom_attack)

                damage = self.damage_counter(States.whom_attack, States.queue.current[0])
                States.queue.current[0] = self.health_updater(States.queue.current[0], damage)
                States.queue.current[0] = self.animation_updater(States.queue.current[0])
                States.whom_attack.is_answer -= 1

        if action.find('shoot') != -1:
            States.is_animate = True
            States.queue.current[0].change_animation(action, who=States.queue.current[0])

            damage = self.damage_counter(States.queue.current[0], States.whom_attack)
            States.whom_attack = self.health_updater(States.whom_attack, damage)
            States.whom_attack = self.animation_updater(States.whom_attack)

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
    def health_updater(defender, damage):
        count_dead, count_health = int(damage // defender.health), damage % defender.health
        defender.count -= count_dead
        defender.health = count_health
        return defender

    @staticmethod
    def animation_updater(defender):
        if defender.count < 1:
            defender.change_animation('death', who=defender)
            if defender.btn_defense is True:
                States.step -= 1
        else:
            defender.change_animation('getting_hit', who=defender)
        return defender

    def draw_units(self, screen):
        for item in States.queue.dead:
            if self.is_animate(item) is False:
                unit = pygame.image.load(os.path.join(f"data/{item.character}/dead/c{item.character}{item.dead}.png"))
                unit = pygame.transform.scale(unit, (item.img_size_x, item.img_size_y))
                screen.blit(unit, (item.x - item.img_size_x / 4, item.y - item.img_size_y * (1 / 2)))

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

    @staticmethod
    def is_animate(item):
        for animation in States.animations:
            if id(item) == id(animation.who):
                return True
        return False
