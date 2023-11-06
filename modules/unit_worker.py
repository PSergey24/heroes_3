import os
import pygame

from modules.hex_worker import HexWorker
from modules.damage_counter import DamageCounter
from modules.settings import Settings, States


class UnitWorker:

    def __init__(self):
        self.hex_worker = HexWorker()
        self.damage_counter = DamageCounter()

    @staticmethod
    def create_units(team):
        for unit in team:
            States.hexagons[unit.hex[0][0]][unit.hex[0][1]].who_engaged = unit
            if unit.character in Settings.double_hex_units:
                States.hexagons[unit.hex[1][0]][unit.hex[1][1]].who_engaged = unit

            unit.x = States.hexagons[unit.hex[0][0]][unit.hex[0][1]].corner[0]
            unit.y = States.hexagons[unit.hex[0][0]][unit.hex[0][1]].corner[1]

    def update_units(self, action):
        States.step += 1
        States.queue.current[0].btn_defense, States.queue.current[0].btn_wait = True, True

        row_active, col_active = States.unit_active.hex[0][0], States.unit_active.hex[0][1]
        print(f"action: {action}")

        States.is_animate = True
        if action == 'moving':
            if States.active_is_double:
                if (States.point_c > 0 and (States.hexagons[States.point_r][States.point_c - 1].who_engaged is None or id(States.hexagons[States.point_r][States.point_c - 1].who_engaged) == id(States.unit_active)) and (States.point_r, States.point_c) not in States.reachable_left_points and States.unit_active.team == 1) or ((States.point_c == Settings.n_columns - 1 or (States.hexagons[States.point_r][States.point_c + 1].who_engaged is not None and id(States.hexagons[States.point_r][States.point_c + 1].who_engaged) != id(States.unit_active))) and (States.point_r, States.point_c) not in States.reachable_right_points and States.unit_active.team == 2):
                    States.queue.current[0].create_animation('moving', States.point_r, States.point_c - 1)
                else:
                    States.queue.current[0].create_animation('moving', States.point_r, States.point_c)
            else:
                States.queue.current[0].create_animation('moving', States.point_r, States.point_c)

        if action is not None and action.find('attack') != -1:
            if (not States.active_is_double and (row_active != States.point_attack[0] or col_active != States.point_attack[1])) or (States.point_attack != States.unit_active.hex[0] and States.active_is_double):
                States.queue.current[0].create_animation('moving', States.point_attack[0], States.point_attack[1])

            States.queue.current[0].create_animation(action)
            self.getting_hit(States.queue.current[0], States.whom_attack)

            if States.whom_attack.is_answer > 0 and States.whom_attack.count > 0 and States.queue.current[0].character not in Settings.without_answer:
                States.whom_attack.create_animation('attack_straight')
                self.getting_hit(States.whom_attack, States.queue.current[0], is_answer=True)
                States.whom_attack.is_answer -= 1

            if States.queue.current[0].character in Settings.double_punch and States.queue.current[0].count > 0:
                States.queue.current[0].create_animation(action)
                self.getting_hit(States.queue.current[0], States.whom_attack)

        if action is not None and action.find('shoot') != -1:
            States.queue.current[0].create_animation(action)
            self.getting_hit(States.queue.current[0], States.whom_attack)
            States.unit_active.arrows -= 1

            if States.queue.current[0].character in Settings.double_shot and States.queue.current[0].arrows > 0:
                States.queue.current[0].create_animation(action)
                self.getting_hit(States.queue.current[0], States.whom_attack)
                States.unit_active.arrows -= 1

        States.queue.current.append(States.queue.current.pop(0))

    def getting_hit(self, attacker, defender, is_answer=False):
        defenders = self.get_defenders(attacker, defender, is_answer)

        for defender in defenders:
            damage = self.damage_counter.count_damage(attacker, defender)
            defender = self.damage_counter.update_health(defender, damage)
            self.animation_updater(defender)

    def get_defenders(self, attacker, defender, is_answer):
        defenders = []
        if is_answer:
            defenders.append(defender)
            return defenders

        if attacker.character in Settings.mass_attack_around:
            defenders = self.get_defenders_mass_attack_around(attacker)
            return defenders

        if attacker.character in Settings.mass_attack_3:
            defenders = self.get_defenders_mass_attack_3(attacker)
            return defenders

        if attacker.character in Settings.mass_fired:
            pass

        if attacker.character in Settings.mass_arrows and States.btn_shooter:
            defenders = self.get_defenders_mass_arrows(defender)
            return defenders

        defenders.append(defender)
        return defenders

    def get_defenders_mass_attack_around(self, attacker):
        defenders = []
        for hexagon in attacker.hex:
            neighbors = self.hex_worker.get_neighbors(hexagon[0], hexagon[1])
            defenders.extend(neighbors)

        return self.drop_own_team(attacker, list(set(defenders)))

    def get_defenders_mass_attack_3(self, attacker):
        point_attack = None
        a = []
        for i in range(6):
            nb_x, nb_y, nb_z = self.hex_worker.cube_neighbor((States.point_x, States.point_y, States.point_z), i)
            nb_r, nb_c = self.hex_worker.cube2offset(nb_x, nb_y, nb_z)
            a.append((nb_r, nb_c))
            if [nb_r, nb_c] in attacker.hex:
                point_attack = [nb_r, nb_c]

        x, y, z = self.hex_worker.offset2cube(point_attack[0], point_attack[1])
        b = []
        for i in range(6):
            nb_x, nb_y, nb_z = self.hex_worker.cube_neighbor((x, y, z), i)
            nb_r, nb_c = self.hex_worker.cube2offset(nb_x, nb_y, nb_z)
            b.append((nb_r, nb_c))

        defenders = [States.hexagons[point[0]][point[1]].who_engaged for point in set(a).intersection(set(b)) if States.hexagons[point[0]][point[1]].who_engaged is not None]
        defenders.append(States.hexagons[States.point_r][States.point_c].who_engaged)
        return defenders

    def get_defenders_mass_arrows(self, defender):
        defenders = []
        for hexagon in defender.hex:
            neighbors = self.hex_worker.get_neighbors(hexagon[0], hexagon[1])
            defenders.extend(neighbors)

        defenders.append(defender)
        return list(set(defenders))

    @staticmethod
    def drop_own_team(attacker, neighbors):
        return [nb for nb in neighbors if nb.team != attacker.team]

    @staticmethod
    def animation_updater(defender):
        if defender.count < 1:
            defender.create_animation('death')
            if defender.btn_defense is True:
                States.step -= 1
        else:
            defender.create_animation('getting_hit')

    def draw_units(self, screen):
        for item in States.queue.dead:
            if self.is_animate(item) is False:
                unit = pygame.image.load(os.path.join(f"data/units/{item.character}/clean/c{item.character}{item.dead}.png"))
                unit = pygame.transform.scale(unit, (item.img_size_x, item.img_size_y))

                if item.team == 2:
                    unit = pygame.transform.flip(unit, True, False)
                screen.blit(unit, (item.x - item.img_size_x / 4 + item.img_shift_x, item.y - item.img_size_y * (1 / 2) + item.img_shift_y))

        ids_ = []
        if len(States.animations) > 0:
            last_idx = self.get_active_animations()
            for i in range(last_idx - 1, -1, -1):
                ids_.append(id(States.animations[i].who))
                if States.animations[i].who.is_active is False:
                    States.animations[i].who.is_active = True
                    States.animations[i].who.animation_count = 0
                States.animations[i].who.draw(screen)

        for item in States.queue.current:
            if id(item) not in ids_:
                item.draw(screen)

    @staticmethod
    def is_animate(item):
        for animation in States.animations:
            if id(item) == id(animation.who):
                return True
        return False

    @staticmethod
    def get_active_animations():
        last_idx = 0
        for animation in States.animations:
            if animation.name in ['getting_hit', 'death']:
                last_idx += 1
            else:
                break
        if last_idx == 0:
            last_idx += 1
        return last_idx
