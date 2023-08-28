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
            States.hexagons[unit.hex[0][0]][unit.hex[0][1]].who_engaged = unit
            if unit.character in Settings.double_hex_units:
                States.hexagons[unit.hex[1][0]][unit.hex[1][1]].who_engaged = unit

            unit.x = States.hexagons[unit.hex[0][0]][unit.hex[0][1]].corner[0]
            unit.y = States.hexagons[unit.hex[0][0]][unit.hex[0][1]].corner[1]

    # action and damage handler
    def update_units(self, action):
        States.step += 1
        States.queue.current[0].btn_defense, States.queue.current[0].btn_wait = True, True
        is_double_hex = States.queue.current[0].character in Settings.double_hex_units

        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        print(f"action: {action}")

        if action == 'moving':
            States.is_animate = True
            States.queue.current[0].change_animation('moving', who=States.queue.current[0])
            if is_double_hex:
                self.hex_worker.update_double_hex_position()
            self.hex_worker.update_character_position()

        if action.find('attack') != -1:
            States.is_animate = True
            if is_double_hex:
                is_left_nb = self.hex_worker.is_neighbors(States.unit_active.hex[0], States.point_attack)
                is_right_nb = self.hex_worker.is_neighbors(States.unit_active.hex[1], States.point_attack)
                is_enemy_hex = States.whom_attack.character in Settings.double_hex_units
                if States.point_attack not in States.unit_active.hex:
                    if is_left_nb is False and is_right_nb is False:
                        States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                        self.hex_worker.update_double_hex_position()
                        self.hex_worker.update_character_position()
                    elif is_left_nb is True and is_right_nb is True:
                        States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                        self.hex_worker.update_double_hex_position()
                        self.hex_worker.update_character_position()
                    elif is_left_nb is True and is_right_nb is False:
                        if (col_active - States.point_attack[1] == 1) and (row_active == States.point_attack[0]) or is_enemy_hex is True:
                            States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                            self.hex_worker.update_double_hex_position()
                            self.hex_worker.update_character_position()
                    elif is_left_nb is False and is_right_nb is True:
                        if (States.point_attack[1] - col_active == 2) and (row_active == States.point_attack[0]) or is_enemy_hex is True or (row_active != States.point_attack[0]):
                            States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                            self.hex_worker.update_double_hex_position()
                            self.hex_worker.update_character_position()
                elif States.point_attack == States.unit_active.hex[1] and (States.point_attack[1] + 1 < Settings.n_columns and States.hexagons[States.point_attack[0]][States.point_attack[1] + 1].who_engaged is None):
                    States.queue.current[0].change_animation('moving', who=States.queue.current[0])
                    self.hex_worker.update_double_hex_position()
                    self.hex_worker.update_character_position()
            else:
                if row_active != States.point_attack[0] or col_active != States.point_attack[1]:
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
        total_health = (defender.count - 1) * defender.health + defender.cur_health

        count_alive, count_health = int((total_health - damage) // defender.health) + 1, (total_health - damage) % defender.health
        defender.count = count_alive
        defender.cur_health = count_health
        if defender.count <= 0:
            defender.count, defender.cur_health = 0, 0
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
