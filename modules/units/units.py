import os
import pygame

from modules.settings import Settings
from modules.states import Objects, States


class Units:

    def __init__(self, i, j, team):
        # coordinates
        self.i = i
        self.j = j
        self.position = None
        self.hex = []

        self.name = None
        self.ai = None
        self.team = team

        self.characteristics = {"base_characteristics": {"attack": None, "defense": None, "damage": None,
                                                         "health": None, "speed": None},
                                "current_health": 0, "current_count": 0, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.status = {"is_answer": 1, "is_wait": False, "is_defense": False}

        # animations
        self.animations = None
        self.current_animation = None
        self.next_actions = []

        self.to_attack = None
        self.from_attack = None

        self.current_animation_images = []
        self.current_animation_points = []

        # image
        self.image = None

    def init(self):
        self.init_animation("standing")

    def init_animation(self, name):
        self.current_animation = name
        self.get_animation_images()
        self.get_animation_points()

        if self.current_animation == "standing":
            self.init_standing()

        if self.current_animation == "moving":
            self.init_moving()

        if self.current_animation == "start_moving":
            pass

        if self.current_animation == "stop_moving":
            self.init_stop_moving()

        if self.current_animation.find("attack") != -1:
            self.init_attack()

        if self.current_animation.find("shoot") != -1:
            self.init_shoot()

        if self.current_animation == "getting_hit":
            pass

        if self.current_animation == "death":
            self.init_death()

        if self.current_animation == "dead":
            self.init_dead()

    def get_animation_images(self):
        """
        Method is updating current animation with n repeats. More repeats - slower animation
        :return: None
        """
        self.current_animation_images = [self.get_surface(img) for img in self.animations[self.current_animation] for _ in range(6)]

    def get_surface(self, image):
        direction = False if self.team == 1 else True

        item = pygame.image.load(os.path.join(f"data/units/{self.name}/clean/c{self.name}{image}.png"))
        item = pygame.transform.scale(item, (self.image["x_size"], self.image["y_size"]))
        item = pygame.transform.flip(item, direction, False)
        return item

    def get_animation_points(self):
        if self.current_animation == "moving":
            route = Objects.field.get_route()
            route = Objects.field.route_update(route)
            self.current_animation_points = Objects.field.get_steps(route)

    def init_standing(self):
        self.reset_field()
        self.init_hex()
        self.init_field()
        self.init_coordinates()

    def reset_info(self):
        self.to_attack = None
        self.from_attack = None

    def reset_field(self):
        for hexagon in self.hex:
            Objects.field.hexagons[hexagon[0]][hexagon[1]].engaged = None

    def init_hex(self):
        self.hex.clear()
        self.hex.append([self.i, self.j])
        if self.characteristics["is_double"]:
            self.hex.append([self.i, self.j + 1])

    def init_field(self):
        Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].engaged = self
        if self.characteristics["is_double"]:
            Objects.field.hexagons[self.hex[1][0]][self.hex[1][1]].engaged = self

    def init_coordinates(self):
        x = Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].corner[0]
        y = Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].corner[1]

        self.position = (x, y)

    def init_moving(self):
        self.reset_field()
        self.init_hex()
        self.init_field()

        if id(self) == id(Objects.active_unit.info) and (len(self.next_actions) == 0 or (len(self.next_actions) != 0 and self.next_actions[0].find("attack") == -1)):
            Objects.queue.handle_move()
            Objects.info_block.handle_move()

    def init_stop_moving(self):
        self.reset_field()
        self.init_hex()
        self.init_field()

        if id(self) == id(Objects.active_unit.info) and (len(self.next_actions) == 0 or (len(self.next_actions) != 0 and self.next_actions[0].find("attack") == -1)):
            Objects.queue.handle_move()
            Objects.info_block.handle_move()

    def init_attack(self):
        if id(self) == id(Objects.active_unit.info) and ("is_second_attack" not in self.status or ("is_second_attack" in self.status and self.status["is_second_attack"] is False)):
            Objects.queue.handle_move()
            Objects.info_block.handle_move()

        if "is_second_attack" in self.status and len(self.next_actions) > 0 and self.next_actions[0].find("attack") != -1:
            self.status["is_second_attack"] = not self.status["is_second_attack"]
        else:
            self.status["is_second_attack"] = False

    def init_shoot(self):
        if id(self) == id(Objects.active_unit.info) and ("is_second_shoot" not in self.status or ("is_second_shoot" in self.status and self.status["is_second_shoot"] is False)):
            Objects.queue.handle_move()
            Objects.info_block.handle_move()

        if "is_second_shoot" in self.status and len(self.next_actions) > 0 and self.next_actions[0].find("shoot") != -1:
            self.status["is_second_shoot"] = not self.status["is_second_shoot"]
        else:
            self.status["is_second_shoot"] = False

    def init_death(self):
        pass

    def init_dead(self):
        if self.status["is_defense"]:
            States.step -= 1

        self.reset_field()
        Objects.queue.handle_dead(id(self))
        Objects.info_block.handle_move()

    def update(self):
        self.update_animation()
        self.update_image_animation()
        self.update_unit_position()

    # update animation
    def update_animation(self):
        States.is_animate = self.is_animate()

        if States.is_animate is False and len(States.stack_animations) > 0:
            [item.init_animation("standing") for item in Objects.queue.sequence if item.current_animation not in ["standing", "death", "dead"]]

            States.active = States.stack_animations.pop(0)
            for item in States.active:
                next_animation = item.next_actions.pop(0)
                item.init_animation(next_animation)
        else:
            if States.is_animate is False:
                [item.init_animation("standing") for item in Objects.queue.sequence if item.current_animation not in ["standing", "death", "dead"]]

    @staticmethod
    def is_animate():
        if States.active is None:
            return False

        for item in States.active:
            if (len(item.current_animation_images) > 0 and item.current_animation not in ["standing", "moving", "dead"]) or len(item.current_animation_points) > 0:
                return True
        return False

    def update_image_animation(self):
        if len(self.current_animation_images) > 0:
            current_image = self.current_animation_images.pop(0)
            if self.current_animation in ["standing", "moving", "dead"]:
                self.current_animation_images.append(current_image)

    def update_unit_position(self):
        if len(self.current_animation_points) > 0:
            self.position = self.current_animation_points.pop(0)

    def handle_click(self):
        self.add_actions()

    def add_actions(self):
        if Objects.cursor.action is not None:
            if Objects.cursor.action == "moving":
                self.add_action_moving()
            elif Objects.cursor.action.find("attack") != -1 and Objects.cursor.destination_point == self.hex[0]:
                self.add_action_attack()
            elif Objects.cursor.action.find("attack") != -1 and Objects.cursor.destination_point != self.hex[0]:
                self.add_action_moving_and_attack()
            elif Objects.cursor.action.find("shoot") != -1:
                self.add_action_shoot()

    def add_action_moving(self):
        self.i, self.j = Objects.cursor.destination_point
        self.next_actions.append("moving")

        States.stack_animations.extend([[self]])

    def add_action_attack(self):
        if self.characteristics["current_count"] > 0:
            self.update_fight_info()
            self.add_action_attack_()

    def add_action_moving_and_attack(self):
        self.add_action_moving()
        self.add_action_attack()

    def add_action_shoot(self):
        self.update_fight_info()
        self.add_action_shoot_()

    def update_fight_info(self):
        self.to_attack = self.get_defenders()

    # get defenders: default, to_fire_attack, to_circular_attack, three_heads_attack
    @staticmethod
    def get_defenders():
        return [Objects.cursor.whom_attack]

    def to_fire_attack(self):
        """
        Special ability for dragons, phoenix, fire bird
        The function returns units that will be fired
        :return: list
        """
        cube_ = Objects.tools.cube_neighbor(Objects.cursor.cube, Objects.cursor.direction_to_fire)
        hex_ = Objects.tools.cube2offset(cube_[0], cube_[1], cube_[2])
        if unit_ := Objects.tools.get_unit(hex_[0], hex_[1]):
            if id(unit_) != id(Objects.cursor.whom_attack) and id(unit_) != id(self):
                return [Objects.cursor.whom_attack, unit_]
        return [Objects.cursor.whom_attack]

    def to_circular_attack(self):
        """
        Special ability for chydr and hydra
        The function returns units that will be circular attacked
        :return: list
        """
        hex_ = Objects.cursor.destination_point
        defenders = Objects.tools.get_neighbors(hex_[0], hex_[1])
        defenders.extend(Objects.tools.get_neighbors(hex_[0], hex_[1] + 1))

        defenders = [item for item in defenders if item.team != self.team]
        return list(set(defenders))

    def three_heads_attack(self):
        """
        Special ability for cerbu
        The function returns units that will be attacked
        :return: list
        """
        defenders = [Objects.cursor.whom_attack]

        if Objects.cursor.direction_to_three_heads in [6, 7]:
            next_ = [Objects.cursor.offset[0], Objects.cursor.offset[1] + 1]
            before_ = [Objects.cursor.offset[0], Objects.cursor.offset[1] - 1]
        else:
            point_attack_cube = Objects.tools.offset2cube(Objects.cursor.point_attack[0], Objects.cursor.point_attack[1])
            next_ = Objects.tools.cube_neighbor(point_attack_cube, (Objects.cursor.direction_to_three_heads + 1) % 6)
            before_ = Objects.tools.cube_neighbor(point_attack_cube, (Objects.cursor.direction_to_three_heads - 1) % 6)
            next_ = Objects.tools.cube2offset(next_[0], next_[1], next_[2])
            before_ = Objects.tools.cube2offset(before_[0], before_[1], before_[2])

        if unit_ := Objects.tools.get_unit(next_[0], next_[1]):
            if id(unit_) != id(Objects.cursor.whom_attack):
                defenders.append(unit_)

        if unit_ := Objects.tools.get_unit(before_[0], before_[1]):
            if id(unit_) != id(Objects.cursor.whom_attack):
                defenders.append(unit_)

        defenders = [item for item in defenders if id(item) != id(self)]
        return defenders

    # attack
    def add_action_attack_(self):
        self.to_attack[0].to_attack = [self]

        self.next_actions.append(Objects.cursor.action)
        States.stack_animations.extend([[self], self.to_attack])

        self.to_damage_all(self, self.to_attack)

        if self.characteristics["is_not_answer"] is False:
            if self.to_attack[0].status["is_answer"] > 0 and self.to_attack[0].characteristics["current_count"] > 0:
                self.to_attack[0].status["is_answer"] -= 1

                self.to_attack[0].next_actions.append(self.get_answer_action())
                States.stack_animations.extend([[self.to_attack[0]], [self]])

                self.to_damage_all(self.to_attack[0], [self])

    # second attack, special ability: crusd, uwlfr
    def add_action_second_attack_(self):
        if self.characteristics["current_count"] > 0 and self.to_attack[0].characteristics["current_count"] > 0:
            self.next_actions.append(Objects.cursor.action)
            States.stack_animations.extend([[self], self.to_attack])

            self.to_damage_all(self, self.to_attack)

    def to_damage_all(self, attacker,  defenders):
        defenders = [self.to_damage_item(attacker, defender) for defender in defenders]
        defenders = [defender for defender in defenders if defender is not None]
        if len(defenders) > 0:
            States.stack_animations.extend([defenders])

    @staticmethod
    def to_damage_item(attacker, defender):
        damage = Objects.damage_counter.count_damage(attacker, defender)
        Objects.damage_counter.update_health(defender, damage)

        if defender.characteristics["current_count"] > 0:
            defender.next_actions.append("getting_hit")
            return None

        defender.next_actions.append("death")
        defender.next_actions.append("dead")
        return defender

    @staticmethod
    def get_answer_action():
        if Objects.cursor.action.find("up") != -1:
            return Objects.cursor.action.replace("up", "down")
        if Objects.cursor.action.find("down") != -1:
            return Objects.cursor.action.replace("down", "up")
        return Objects.cursor.action

    # shoot
    def add_action_shoot_(self):
        self.to_attack[0].to_attack = [self]
        self.characteristics["current_arrows"] -= 1

        self.next_actions.append(Objects.cursor.action)
        States.stack_animations.extend([[self], self.to_attack])

        self.to_damage_all(self, self.to_attack)

    # second shoot, special ability: hcbow, grelf
    def add_action_second_shoot_(self):
        if self.characteristics["current_count"] > 0 and self.characteristics["current_arrows"] > 0 and self.to_attack[0].characteristics["current_count"] > 0:
            self.characteristics["current_arrows"] -= 1

            self.next_actions.append(Objects.cursor.action)
            States.stack_animations.extend([[self], self.to_attack])

            self.to_damage_all(self, self.to_attack)

    def reset_round(self):
        self.reset_buttons()
        self.reset_answers()

    def reset_buttons(self):
        self.status["is_wait"] = False
        self.status["is_defense"] = False

    def reset_answers(self):
        self.status["is_answer"] = 1

    def draw(self, screen):
        if len(self.current_animation_images) > 0:
            self.draw_unit(screen)
            self.draw_text(screen)

    def draw_unit(self, screen):
        animation = self.correct_animation()
        screen.blit(animation, (self.position[0] - self.image["x_size"] / 4 + self.image["x_shift"], self.position[1] - self.image["y_size"] * (1 / 2) + self.image["y_shift"]))

    def correct_animation(self):
        item = self.current_animation_images[0]
        if self.current_animation == "moving":
            if len(self.current_animation_points) > 0:
                if (self.current_animation_points[0][0] < self.current_animation_points[-1][0] and self.team == 2) or (self.current_animation_points[0][0] > self.current_animation_points[-1][0] and self.team == 1):
                    item = pygame.transform.flip(item, True, False)

        if (self.current_animation.find("attack") != -1 or self.current_animation.find("shoot") != -1 or self.current_animation == "getting_hit") and self.to_attack is not None:
            if (self.hex[0][1] < self.to_attack[0].hex[0][1] and self.team == 2) or (self.hex[0][1] > self.to_attack[0].hex[0][1] and self.team == 1):
                item = pygame.transform.flip(item, True, False)

        return item

    def draw_text(self, screen):
        def get_position(position, team):
            x, y = position
            if team == 1:
                return x + Settings.R + 8, y + Settings.r + 9
            else:
                return x + Settings.R - 46, y + Settings.r - 9

        def get_text_shift(count):
            if len(str(count)) == 2:
                return -1
            if len(str(count)) == 3:
                return -4
            return 1

        if self.characteristics["current_count"] > 0:
            text = Settings.FONT.render(str(self.characteristics["current_count"]), True, (255, 255, 255))
            x_, y_ = get_position(self.position, self.team)
            len_ = get_text_shift(self.characteristics["current_count"])

            pygame.draw.rect(screen, (67, 19, 104), (x_, y_, 40, 15))
            pygame.draw.rect(screen, (255, 255, 255), (x_, y_, 40, 15), 1)
            screen.blit(text, (x_ + 15 + len_, y_))
