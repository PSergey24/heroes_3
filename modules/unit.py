import os.path

import pygame
import math

from modules.settings import Settings, States
from modules.block_updater import BlockUpdater


class Unit:

    def __init__(self, i, j, count, team):
        self.count = count
        self.team = team
        self.hex = [i, j]
        self.x = None
        self.y = None

        self.character = None
        self.attack = None
        self.defense = None
        self.damage = None
        self.health = None
        self.cur_health = None
        self.speed = None
        self.is_shooter = False
        self.is_flyer = False
        self.is_answer = 1

        # btn
        self.btn_wait = False
        self.btn_defense = False

        # type of animations
        self.path = []
        self.moving = None
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
        self.avatar = None
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

        self.block_updater = BlockUpdater()
        self.reset_direction()

    def reset_direction(self):
        self.direction = False if self.team == 1 else True

    def update_direction(self, animation):
        if self.team == 2:
            self.direction = True
            if animation == 'getting_hit':
                if States.cursor_direction is not None:
                    self.direction = not States.cursor_direction
                    States.cursor_direction = not States.cursor_direction
                elif States.col_active > States.point_c:
                    self.direction = False
            else:
                if animation != 'moving' and States.cursor_direction is not None:
                    self.direction = States.cursor_direction
                elif States.col_active < States.point_c:
                    self.direction = False

        if self.team == 1:
            self.direction = False
            if animation == 'getting_hit':
                if States.cursor_direction is not None:
                    self.direction = not States.cursor_direction
                    States.cursor_direction = not States.cursor_direction
                elif States.col_active < States.point_c:
                    self.direction = True
            else:
                if animation != 'moving' and States.cursor_direction is not None:
                    self.direction = States.cursor_direction
                elif States.col_active > States.point_c:
                    self.direction = True

    def draw(self, screen):
        self.draw_character(screen)

        if self.is_active and States.animations[0].name == 'moving':
            self.move()

        self.draw_character_count(screen)

    def draw_character(self, screen):
        animation = self.list_animations
        if self.is_active:
            animation = States.animations[0]

        self.img = animation.animation[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(animation.animation):
            self.animation_count = 0
            self.reset_direction()

            if animation.name not in ['standing', 'moving']:
                self.is_active, States.is_animate = False, False
                States.animations.pop(0)

            if animation.name == 'death':
                States.queue.drop_unit_by_id(id(animation.who))
                States.hexagons[animation.who.hex[0]][animation.who.hex[1]].who_engaged = None

                if animation.who.character in States.double_hex_units:
                    States.hexagons[animation.who.hex[0]][animation.who.hex[1] + 1].who_engaged = None
                self.block_updater.update_avatars()

        screen.blit(self.img, (self.x - self.img_size_x / 4, self.y - self.img_size_y * (1 / 2)))

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
                self.animation_count, self.path_pos = 0, 0
                self.is_active, States.is_animate = False, False
                States.animations.pop(0)
                if len(States.animations) > 0:
                    States.animations[0].who.is_active = True

        self.x = x2
        self.y = y2

    def change_animation(self, animation_name, who=None):
        self.animation_count = 0
        speed, images = self.choose_animation_info(animation_name)

        animation_img = []
        for x in images:
            for j in range(speed):
                unit = pygame.image.load(os.path.join(f"data/{self.character}/{animation_name}/c{self.character}{x}.png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                unit = pygame.transform.flip(unit, self.direction, False)
                animation_img.append(unit)

        self.update_states(animation_name, animation_img, who)

    def choose_animation_info(self, animation):
        if animation == 'standing':
            self.reset_direction()
            self.is_active = False
            return 10, self.standing

        States.is_animate = True
        self.update_direction(animation)
        if animation == 'death':
            return 6, self.death
        if animation == 'moving':
            return 6, self.moving
        if animation == 'attack_straight':
            return 6, self.attack_straight
        if animation == 'attack_down':
            return 6, self.attack_down
        if animation == 'attack_up':
            return 6, self.attack_up
        if animation == 'shoot_straight':
            return 6, self.shoot_straight
        if animation == 'shoot_down':
            return 6, self.shoot_down
        if animation == 'shoot_up':
            return 6, self.shoot_up

        if animation == 'getting_hit':
            return 6, self.getting_hit

    def update_states(self, animation_name, animation_img, who):
        if animation_name != 'standing':
            if len(States.animations) == 0:
                self.is_active = True
            States.animations.append(Animation(animation_name, animation_img, who))
        else:
            self.list_animations = Animation(animation_name, animation_img, who)


class Animation:

    def __init__(self, name, animation, who):
        self.name = name
        self.animation = animation
        self.who = who


class Angel(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'angel'
        self.avatar = 'CPrL012C.bmp'
        self.attack = 20
        self.defense = 20
        self.damage = [50, 50]
        self.health = 200
        self.speed = 12

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["41", "42", "43", "44", "45", "46", "47"]
        self.mouse_over = ["35", "36", "37", "38", "38", "38", "38", "37", "36", "35"]
        self.standing = ["00", "51", "52", "53", "54", "53", "52", "51"]
        self.getting_hit = ["19", "20", "21", "22", "23", "24"]
        self.defend = ["31", "32", "33", "34", "34", "34", "34", "33", "32", "31", "42"]
        self.death = ["19", "20", "25", "26", "27", "28", "29", "30"]
        self.dead = "30"
        self.attack_up = ["07", "08", "09", "10", "11", "12"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06"]
        self.attack_down = ["13", "14", "15", "16", "17", "18"]

        self.img_size_x = 140
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')


class Elf(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'elf'
        self.avatar = 'CPrL018R.bmp'
        self.attack = 9
        self.defense = 5
        self.damage = [3, 5]
        self.health = 15
        self.speed = 6

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["54", "55", "56", "57", "58", "59", "60", "61"]
        self.mouse_over = ["44", "45", "46", "47", "47", "47", "47", "47", "46", "45", "44"]
        self.standing = ["72", "48", "49", "50", "51", "50", "49", "48"]
        self.getting_hit = ["64", "65", "66", "67", "68", "69"]
        self.defend = ["40", "41", "42", "43", "43", "43", "43", "43", "42", "41", "40"]
        self.death = ["64", "65", "37", "38", "39"]
        self.dead = "39"
        self.attack_up = ["19", "20", "27", "28", "29", "30", "31", "26"]
        self.attack_straight = ["19", "20", "21", "22", "23", "24", "25", "26"]
        self.attack_down = ["19", "20", "32", "33", "34", "35", "36", "26"]
        self.shoot_up = ["01", "02", "09", "10", "11", "12", "12", "12", "12", "12", "13", "08"]
        self.shoot_straight = ["01", "02", "03", "04", "05", "06", "06", "06", "06", "06", "07", "08"]
        self.shoot_down = ["01", "02", "14", "15", "16", "17", "17", "17", "17", "17", "18", "08"]

        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')


class Lich(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'lich'
        self.avatar = 'CPrL064N.bmp'
        self.attack = 13
        self.defense = 10
        self.damage = [11, 13]
        self.health = 30
        self.speed = 6

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["35", "36", "37", "38", "39", "40", "41"]
        self.dead = "41"
        self.attack_up = ["13", "14", "21", "22", "23", "24", "25", "26"]
        self.attack_straight = ["13", "14", "15", "16", "17", "18", "19", "20"]
        self.attack_down = ["27", "28", "29", "30", "31", "32", "33", "34"]
        self.shoot_up = ["05", "06", "07", "08", "08", "08", "08", "08", "07", "06", "05"]
        self.shoot_straight = ["01", "02", "03", "04", "04", "04", "04", "04", "03", "02", "01"]
        self.shoot_down = ["09", "10", "11", "12", "12", "12", "12", "12", "11", "10", "09"]

        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')


class Mage(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'mage'
        self.avatar = 'CPrL034T.bmp'
        self.attack = 11
        self.defense = 18
        self.damage = [7, 9]
        self.health = 25
        self.speed = 5

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["34", "35", "36", "37", "38", "39", "40", "41"]
        self.dead = "41"
        self.attack_up = ["16", "17", "18", "19", "26", "27", "28", "29", "24", "25"]
        self.attack_straight = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
        self.attack_down = ["16", "17", "18", "19", "30", "31", "32", "33", "24", "25"]
        self.shoot_up = ["06", "07", "08", "09", "10", "10", "10", "10", "10", "09", "08", "07", "06"]
        self.shoot_straight = ["01", "02", "03", "04", "05", "05", "05", "05", "05", "04", "03", "02", "01"]
        self.shoot_down = ["11", "12", "13", "14", "15", "15", "15", "15", "15", "14", "13", "12", "11"]

        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')


class BDragon(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'bdrgn'
        self.avatar = 'CPrLBlk.bmp'
        self.attack = 25
        self.defense = 25
        self.damage = [40, 50]
        self.health = 300
        self.speed = 15

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["11", "12", "11", "10"]
        self.mouse_over = ["01", "04", "05", "06", "01"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "49", "50", "51", "52", "53", "01"]
        self.defend = ["01", "20", "21", "22", "23", "23", "24", "25", "01"]
        self.death = ["01", "49", "50", "51", "54", "55", "56", "57", "58", "59"]
        self.dead = "59"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "32", "33", "01"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "01"]
        self.attack_down = ["01", "40", "41", "42", "43", "44", "45", "46", "47", "48", "01"]
        self.dhex_attack_up = ["01", "26", "27", "28", "60", "61", "62", "63", "33", "01"]
        self.dhex_attack_straight = ["01", "64", "65", "66", "67", "68", "69", "01"]
        self.dhex_attack_down = ["01", "40", "41", "42", "70", "71", "72", "73", "47", "48", "01"]

        self.img_size_x = 280
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')
