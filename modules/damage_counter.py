import random
import copy
from modules.settings import Settings


class DamageCounter:

    def __init__(self):
        pass

    def count_damage(self, attacker, defender):
        k_damage = self.get_damage_k(attacker, defender)
        k_luck = self.get_luck_k()
        damage = round(attacker.characteristics["current_count"] * random.randint(attacker.characteristics["base_characteristics"]["damage"][0], attacker.characteristics["base_characteristics"]["damage"][1]) * k_damage * k_luck, 1)
        print(f"{attacker.name} attack to {defender.name} with damage {damage}")
        return damage

    @staticmethod
    def get_damage_k(attacker, defender):
        difference = attacker.characteristics["base_characteristics"]["attack"] - defender.characteristics["base_characteristics"]["defense"]
        if difference > 0:
            k = 0.05 * difference
            k = 1 + (3 if k > 3 else k)
        else:
            k = 0.025 * abs(difference)
            k = 1 - (0.7 if k > 0.7 else k)
        return k

    @staticmethod
    def get_luck_k():
        return 1

    @staticmethod
    def update_health(defender, damage):
        total_health = (defender.characteristics["current_count"] - 1) * defender.characteristics["base_characteristics"]["health"] + defender.characteristics["current_health"]

        count_alive, count_health = int((total_health - damage) // defender.characteristics["base_characteristics"]["health"]) + 1, (total_health - damage) % defender.characteristics["base_characteristics"]["health"]
        defender.characteristics["current_count"], defender.characteristics["current_health"] = count_alive, count_health
        if defender.characteristics["current_count"] <= 0:
            defender.characteristics["current_count"], defender.characteristics["current_health"] = 0, 0

    # def predict_damage(self):
    #     row_active, col_active = States.point_r, States.point_c
    #     if 0 <= row_active < Settings.n_rows and 0 <= col_active < Settings.n_columns and States.hexagons[row_active][col_active].who_engaged and States.hexagons[row_active][col_active].who_engaged.team != States.unit_active.team:
    #         attacker, defender = States.unit_active, States.hexagons[row_active][col_active].who_engaged
    #         min_damage, max_damage = self.count_min_damage(attacker, defender), self.count_max_damage(attacker, defender)
    #         print(f"{attacker.character} attack to {defender.character} with damage {min_damage}-{max_damage}")
    #
    #         defender, attacker = copy.copy(States.unit_active), copy.copy(States.hexagons[row_active][col_active].who_engaged)
    #         min_attacker, max_attacker = self.update_health(attacker, min_damage), self.update_health(attacker, max_damage)
    #
    #         min_answer_damage, max_answer_damage = self.count_min_damage(min_attacker, defender), self.count_max_damage(max_attacker, defender)
    #         print(f"{attacker.character} attack to {defender.character} with damage {min_answer_damage}-{max_answer_damage}")
    #
    # def count_min_damage(self, attacker, defender):
    #     return round(attacker.count * attacker.damage[0] * self.get_damage_k(attacker, defender), 1)
    #
    # def count_max_damage(self, attacker, defender):
    #     return round(attacker.count * attacker.damage[1] * self.get_damage_k(attacker, defender), 1)
