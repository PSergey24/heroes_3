import os.path

import pygame
import math

from modules.settings import Settings, States
from modules.block_updater import BlockUpdater
from modules.hex_worker import HexWorker


class Units:

    def __init__(self, count, team):
        self.count = count
        self.team = team
        self.hex = []
        self.x = None
        self.y = None

        self.character = None
        self.attack = None
        self.defense = None
        self.damage = None
        self.health = None
        self.cur_health = None
        self.speed = None
        self.arrows = None
        self.ai = None

        self.is_shooter = False
        self.is_flyer = False
        self.is_jumper = False
        self.is_answer = 1

        # btn
        self.btn_wait = False
        self.btn_defense = False

        # type of animations
        self.path = []
        self.moving = None
        self.start_moving = None
        self.stop_moving = None
        self.mouse_over = None
        self.standing = None
        self.getting_hit = None
        self.defend = None
        self.death = None
        self.dead = None
        self.attack_up = None
        self.attack_straight = None
        self.attack_down = None
        self.shoot_up = None
        self.shoot_straight = None
        self.shoot_down = None

        # animations
        self.direction = None
        self.img = None
        self.list_animations = None
        self.is_active = False

        self.animation_count = 0
        self.path_pos = 0
        self.move_count = 0
        self.dis = 0

        self.img_size_x = None
        self.img_size_y = None
        self.img_shift_x = 0
        self.img_shift_y = 0

        self.block_updater = BlockUpdater()
        self.hex_worker = HexWorker()
        self.reset_direction()

    def update_hex(self, i, j):
        self.hex.append([i, j])
        if self.character in Settings.double_hex_units:
            self.hex.append([i, j + 1])

    def reset_direction(self):
        self.direction = False if self.team == 1 else True

    def update_direction(self, animation):
        col_active = States.unit_active.hex[0][1]

        if self.team == 2:
            self.direction = True
            if animation == 'getting_hit':
                if States.cursor_direction is not None:
                    self.direction = not States.cursor_direction
                    States.cursor_direction = not States.cursor_direction
                elif col_active > States.point_c:
                    self.direction = False
            else:
                if animation != 'moving' and States.cursor_direction is not None:
                    self.direction = States.cursor_direction
                elif col_active < States.point_c:
                    self.direction = False

        if self.team == 1:
            self.direction = False
            if animation == 'getting_hit':
                if States.cursor_direction is not None:
                    self.direction = not States.cursor_direction
                    States.cursor_direction = not States.cursor_direction
                elif col_active < States.point_c:
                    self.direction = True
            else:
                if animation != 'moving' and States.cursor_direction is not None:
                    self.direction = States.cursor_direction
                elif col_active > States.point_c:
                    self.direction = True

    def draw(self, screen):
        self.draw_character(screen)

        if self.is_active and States.animations[0].name == 'moving':
            self.move()

        self.draw_character_count(screen)

    def draw_character(self, screen):
        animation = self.list_animations
        if self.is_active:
            for i, unit in enumerate(States.animations):
                if id(unit.who) == id(self):
                    animation = States.animations[i]
                    break

        self.img = animation.animation[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(animation.animation):
            self.animation_count = 0
            self.reset_direction()

            if animation.name not in ['standing', 'moving', 'getting_hit', 'death']:
                self.is_active, States.is_animate = False, False
                States.animations.pop(0)

            elif animation.name in ['getting_hit', 'death']:
                is_smb_else, current_ind = False, 0
                for i, item in enumerate(States.animations):
                    if item.name not in ['getting_hit', 'death']:
                        break
                    else:
                        if id(item.who) != id(animation.who):
                            is_smb_else = True
                        else:
                            current_ind = i

                self.is_active = False
                States.is_animate = is_smb_else
                States.animations.pop(current_ind)

            if animation.name == 'death':
                States.queue.drop_unit_by_id(id(animation.who))
                States.hexagons[animation.who.hex[0][0]][animation.who.hex[0][1]].who_engaged = None

                if animation.who.character in Settings.double_hex_units:
                    States.hexagons[animation.who.hex[1][0]][animation.who.hex[1][1]].who_engaged = None
                self.block_updater.update_avatars()

            if animation.name == 'start_moving':
                goal_row, goal_col = States.queue.current[len(States.queue.current)-1].hex[0][0], States.queue.current[len(States.queue.current)-1].hex[0][1]
                States.queue.current[len(States.queue.current)-1].x = States.hexagons[goal_row][goal_col].corner[0]
                States.queue.current[len(States.queue.current)-1].y = States.hexagons[goal_row][goal_col].corner[1]

        screen.blit(self.img, (self.x - self.img_size_x / 4 + self.img_shift_x, self.y - self.img_size_y * (1 / 2) + self.img_shift_y))

    def draw_character_count(self, screen):
        txt = Settings.FONT.render(str(self.count), True, (255, 255, 255))
        pygame.draw.rect(screen, (67, 19, 104),
                         (self.x + Settings.R * 2 - txt.get_height() * 2.3,
                          self.y + Settings.r * 2 - txt.get_width() * 1.2, 50, 20))
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.x + Settings.R * 2 - txt.get_height() * 2.3,
                          self.y + Settings.r * 2 - txt.get_width() * 1.2, 50, 20), 1)
        screen.blit(txt, (self.x + Settings.R * 2 - txt.get_height(),
                          self.y + Settings.r * 2 - txt.get_width()))

    def move(self):
        x1, y1 = self.path[self.path_pos]
        x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2 - x1), (y2 - y1)

        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.dis >= move_dis:
            self.dis, self.move_count = 0, 0
            self.path_pos += 1

            if self.path_pos == len(self.path) - 1:
                self.path.clear()
                self.animation_count, self.path_pos = 0, 0
                self.is_active, States.is_animate = False, False
                States.animations.pop(0)
                if len(States.animations) > 0:
                    States.animations[0].who.is_active = True

        self.x = x2
        self.y = y2

    def create_animation(self, animation_name, goal_row=None, goal_col=None):
        if animation_name == "moving":
            self.create_moving(goal_row, goal_col)
        else:
            self.select_animation(animation_name)

    def create_moving(self, goal_row, goal_col):
        self.select_animation('moving')
        self.hex_worker.update_character_position(goal_row, goal_col)

    def select_animation(self, animation_name):
        self.animation_count = 0
        speed, images = self.choose_animation_info(animation_name)

        animation_img = []
        for x in images:
            for j in range(speed):
                unit = pygame.image.load(os.path.join(f"data/units/{self.character}/{animation_name}/c{self.character}{x}.png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                unit = pygame.transform.flip(unit, self.direction, False)
                animation_img.append(unit)

        self.update_states(animation_name, animation_img)

    def choose_animation_info(self, animation):
        if animation == 'standing':
            self.reset_direction()
            self.is_active = False
            return 6, self.standing

        States.is_animate = True
        self.update_direction(animation)
        if animation == 'death':
            return 4, self.death
        if animation == 'moving':
            return 4, self.moving
        if animation == 'start_moving':
            return 4, self.start_moving
        if animation == 'stop_moving':
            return 4, self.stop_moving
        if animation == 'attack_straight':
            return 4, self.attack_straight
        if animation == 'attack_down':
            return 4, self.attack_down
        if animation == 'attack_up':
            return 4, self.attack_up
        if animation == 'shoot_straight':
            return 4, self.shoot_straight
        if animation == 'shoot_down':
            return 4, self.shoot_down
        if animation == 'shoot_up':
            return 4, self.shoot_up

        if animation == 'getting_hit':
            return 4, self.getting_hit

    def update_states(self, animation_name, animation_img):
        if animation_name != 'standing':
            if len(States.animations) == 0:
                self.is_active = True
            States.animations.append(Animation(animation_name, animation_img, self))
        else:
            self.list_animations = Animation(animation_name, animation_img, self)


class Animation:

    def __init__(self, name, animation, who):
        self.name = name
        self.animation = animation
        self.who = who
