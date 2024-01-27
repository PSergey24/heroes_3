import os
import pygame

from modules.settings import Settings
from modules.states import Objects, States


class Units:

    def __init__(self, team):
        # coordinates
        self.position = None
        self.hex = []

        self.name = None
        self.ai = None
        self.team = team

        self.characteristics = {"base_characteristics": {"attack": None, "defense": None, "damage": None,
                                                         "health": None, "speed": None},
                                "current_health": None, "current_count": None, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        # self.status = {"is_answer": 1, "is_wait": False, "is_defense": False}
        self.status = {}
        self.is_answer = 1
        self.is_wait = False
        self.is_defense = False

        # animations
        self.animations = None
        self.next_actions = []
        self.animation_id = None
        self.current_animation = None
        self.to_attack = None
        self.current_animation_images = []
        self.current_animation_points = []

        # image
        self.image = None

    def init(self, i, j):
        self.init_hex(i, j)
        self.init_field()
        self.init_coordinates()
        self.init_animation("standing")

    def init_hex(self, i, j):
        self.hex.clear()
        self.hex.append([i, j])
        if self.characteristics["is_double"]:
            self.hex.append([i, j + 1])

    def init_field(self):
        Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].engaged = self
        if self.characteristics["is_double"]:
            Objects.field.hexagons[self.hex[1][0]][self.hex[1][1]].engaged = self

    def reset_field(self):
        for hexagon in self.hex:
            Objects.field.hexagons[hexagon[0]][hexagon[1]].engaged = None

    def init_coordinates(self):
        x = Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].corner[0]
        y = Objects.field.hexagons[self.hex[0][0]][self.hex[0][1]].corner[1]

        self.position = (x, y)

    def init_animation(self, name):
        self.current_animation = name
        self.get_animation_images()
        self.get_animation_points()

        self.animation_id = States.current_animation

        if name in ["standing", "dead"]:
            self.animation_id = 0

        if name == "moving":
            self.reset_moving()

        if name == "start_moving":
            pass

        if name == "stop_moving":
            self.reset_field()
            self.init_hex(Objects.cursor.destination_point[0], Objects.cursor.destination_point[1])
            self.init_field()
            self.init_coordinates()

        if name == "getting_hit":
            pass

        if name in ["attack_down", "attack_up", "attack_straight"]:
            pass

        if name in ["shoot_down", "shoot_up", "shoot_straight"]:
            pass

    def reset_moving(self):
        self.reset_field()
        self.init_hex(Objects.cursor.destination_point[0], Objects.cursor.destination_point[1])
        self.init_field()

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

    def handle_click(self):
        self.update_actions()

        if States.current_animation == States.stack_animations[0]["n"]:
            item = States.stack_animations.pop(0)
            self.init_animation(item["animation"])

    def update_actions(self):
        States.is_animate = True
        Objects.queue.handle_move()
        Objects.info_block.handle_move()

        if Objects.cursor.action is not None:
            if Objects.cursor.action == "moving":
                self.add_animation_moving_()
            elif Objects.cursor.action.find("attack") != -1 and Objects.cursor.destination_point == self.hex[0]:
                self.add_animation_attack_()
            elif Objects.cursor.action.find("attack") != -1 and Objects.cursor.destination_point != self.hex[0]:
                self.add_moving_and_attack_()
            elif Objects.cursor.action.find("shoot") != -1:
                self.add_animation_shoot_()

    def add_moving_and_attack_(self):
        self.add_animation_moving_()
        self.add_animation_attack_()

    def add_animation_moving_(self):
        self.add_animation(self, "moving")

    def add_animation_attack_(self):
        self.update_fight_info()
        self.add_animation(self, Objects.cursor.action)
        self.add_animation(Objects.cursor.whom_attack, "getting_hit")

        if Objects.cursor.whom_attack.is_answer > 0:
            Objects.cursor.whom_attack.is_answer -= 1
            self.add_animation(Objects.cursor.whom_attack, self.get_answer_animation(Objects.cursor.action))
            self.add_animation(self, "getting_hit")

    def add_animation_shoot_(self):
        self.update_fight_info()
        self.add_animation(self, Objects.cursor.action)
        self.add_animation(Objects.cursor.whom_attack, "getting_hit")

    def update_fight_info(self):
        self.to_attack = Objects.cursor.whom_attack
        Objects.cursor.whom_attack.to_attack = self

    @staticmethod
    def add_animation(unit_, animation):
        States.stack_animations.append({"unit": unit_, "animation": animation, "n": States.active_animation})
        States.active_animation += 1

    @staticmethod
    def get_answer_animation(animation):
        if animation.find("up") != -1:
            return animation.replace("up", "down")
        if animation.find("down") != -1:
            return animation.replace("down", "up")
        return animation

    def update(self):
        self.update_animation()
        self.update_image_animation()
        self.update_unit_position()

        if len(self.current_animation_images) > 0 and self.current_animation == "moving":
            States.is_animate = True

    def update_animation(self):
        if (len(self.current_animation_points) == 0 and self.current_animation == "moving") or len(self.current_animation_images) == 0 or self.current_animation == "standing":
            if self.animation_id == States.current_animation:
                is_exist_parallel = self.is_exist_parallel_animation()
                if is_exist_parallel is False:
                    States.current_animation += 1

            if len(States.stack_animations) > 0 and States.stack_animations[0]["unit"] == self:
                if States.current_animation == States.stack_animations[0]["n"]:
                    item = States.stack_animations.pop(0)
                    self.init_animation(item["animation"])
            elif self.current_animation != "standing":
                self.init_animation("standing")

    def is_exist_parallel_animation(self):
        for unit_ in reversed(Objects.queue.sequence):
            if id(self) == id(unit_):
                return False

            if unit_.animation_id == States.current_animation and id(self) != id(unit_):
                return True
        return False

    def update_image_animation(self):
        current_image = self.current_animation_images.pop(0)
        if self.current_animation in ["standing", "moving", "dead"]:
            self.current_animation_images.append(current_image)

    def update_unit_position(self):
        if len(self.current_animation_points) > 0:
            self.position = self.current_animation_points.pop(0)

    def reset_round(self):
        self.reset_buttons()
        self.reset_answers()

    def reset_buttons(self):
        self.is_wait = False
        self.is_defense = False

    def reset_answers(self):
        self.is_answer = 1

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
            if (self.hex[0][1] < self.to_attack.hex[0][1] and self.team == 2) or (self.hex[0][1] > self.to_attack.hex[0][1] and self.team == 1):
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

        text = Settings.FONT.render(str(self.characteristics["current_count"]), True, (255, 255, 255))
        x_, y_ = get_position(self.position, self.team)
        len_ = get_text_shift(self.characteristics["current_count"])

        pygame.draw.rect(screen, (67, 19, 104), (x_, y_, 40, 15))
        pygame.draw.rect(screen, (255, 255, 255), (x_, y_, 40, 15), 1)
        screen.blit(text, (x_ + 15 + len_, y_))
