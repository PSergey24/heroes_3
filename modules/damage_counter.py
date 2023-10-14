import random
import copy
from modules.settings import Settings, States


class DamageCounter:

    def __init__(self):
        pass

    def count_damage(self, attacker, defender):
        k_damage = self.get_damage_k(attacker, defender)
        k_luck = self.get_luck_k()
        damage = round(attacker.count * random.randint(attacker.damage[0], attacker.damage[1]) * k_damage * k_luck, 1)
        print(f"{attacker.character} attack to {defender.character} with damage {damage}")
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
        total_health = (defender.count - 1) * defender.health + defender.cur_health

        count_alive, count_health = int((total_health - damage) // defender.health) + 1, (total_health - damage) % defender.health
        defender.count = count_alive
        defender.cur_health = count_health
        if defender.count <= 0:
            defender.count, defender.cur_health = 0, 0
        return defender

    def predict_damage(self):
        row_active, col_active = States.point_r, States.point_c
        if 0 <= row_active < Settings.n_rows and 0 <= col_active < Settings.n_columns and States.hexagons[row_active][col_active].who_engaged and States.hexagons[row_active][col_active].who_engaged.team != States.unit_active.team:
            attacker, defender = States.unit_active, States.hexagons[row_active][col_active].who_engaged
            min_damage, max_damage = self.count_min_damage(attacker, defender), self.count_max_damage(attacker, defender)
            print(f"{attacker.character} attack to {defender.character} with damage {min_damage}-{max_damage}")

            defender, attacker = copy.copy(States.unit_active), copy.copy(States.hexagons[row_active][col_active].who_engaged)
            min_attacker, max_attacker = self.update_health(attacker, min_damage), self.update_health(attacker, max_damage)

            min_answer_damage, max_answer_damage = self.count_min_damage(min_attacker, defender), self.count_max_damage(max_attacker, defender)
            print(f"{attacker.character} attack to {defender.character} with damage {min_answer_damage}-{max_answer_damage}")

    def count_min_damage(self, attacker, defender):
        return round(attacker.count * attacker.damage[0] * self.get_damage_k(attacker, defender), 1)

    def count_max_damage(self, attacker, defender):
        return round(attacker.count * attacker.damage[1] * self.get_damage_k(attacker, defender), 1)
