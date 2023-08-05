import os.path

import pygame
import math
from copy import copy

from modules.settings import Settings


class Unit:

    def __init__(self, i, j, count, team):
        self.count = count
        self.team = team
        self.position = [i, j]
        self.x = None
        self.y = None

        self.character = None
        self.attack = None
        self.defense = None
        self.damage = None
        self.health = None
        self.speed = None

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
        self.attack_up = None
        self.attack_straight = None
        self.attack_down = None
        self.shoot_up = None
        self.shoot_straight = None
        self.shoot_down = None

        # animations
        self.avatar = None
        self.is_animation = False
        self.direction = True
        self.img = None
        self.list_animations = []
        # self.current_animation = []
        self.animation_count = 0
        self.path_pos = 0
        self.move_count = 0
        self.dis = 0

        self.img_size_x = None
        self.img_size_y = None

    def draw(self, screen):
        self.draw_character(screen)

        if self.list_animations[0].name == 'moving':
            self.move()

        self.draw_character_count(screen)

    def draw_character(self, screen):
        self.img = self.list_animations[0].animation[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.list_animations[0].animation):
            self.animation_count = 0
            if self.list_animations[0].name != 'standing' and self.list_animations[0].name != 'moving':
                self.list_animations.pop(0)

        if self.list_animations[0].name == 'standing' and len(self.list_animations) > 1:
            self.list_animations.pop(0)

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

        if (not self.direction and self.team == 2) or (self.direction and self.team == 1):
            if self.team == 2:
                self.direction = True
            if self.team == 1:
                self.direction = False

            for i, img in enumerate(self.list_animations[0].animation):
                self.list_animations[0].animation[i] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

            if self.path_pos == len(self.path) - 1:
                self.list_animations.pop(0)
                self.x = x2
                self.y = y2

        self.x = x2
        self.y = y2

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True

    def change_animation(self, animation):
        self.animation_count = 0
        speed, images = self.choose_animation_info(animation)

        current_animation = []
        for x in images:
            for j in range(speed):
                unit = pygame.image.load(os.path.join(f"data/{self.character}/{animation}/c{self.character}{x}.png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                if self.team == 2:
                    unit = pygame.transform.flip(unit, True, False)
                current_animation.append(unit)

        self.update_states(animation, current_animation)

    def choose_animation_info(self, animation):
        if animation == 'standing':
            return 10, self.standing
        if animation == 'moving':
            return 6, self.moving
        if animation == 'attack_straight':
            return 6, self.attack_straight

    def update_states(self, animation, current_animation):
        self.list_animations.append(Animation(animation, current_animation))


class Animation:

    def __init__(self, name, animation):
        self.name = name
        self.animation = copy(animation)


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

        self.standing = ["00", "51", "52", "53", "54", "53", "52", "51"]

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
        self.standing = ["72", "48", "49", "50", "51", "50", "49", "48"]

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

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["35", "36", "37", "38", "39", "40", "41"]
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

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["34", "35", "36", "37", "38", "39", "40", "41"]
        self.attack_up = ["16", "17", "18", "19", "26", "27", "28", "29", "24", "25"]
        self.attack_straight = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
        self.attack_down = ["16", "17", "18", "19", "30", "31", "32", "33", "24", "25"]
        self.shoot_up = ["06", "07", "08", "09", "10", "10", "10", "10", "10", "09", "08", "07", "06"]
        self.shoot_straight = ["01", "02", "03", "04", "05", "05", "05", "05", "05", "04", "03", "02", "01"]
        self.shoot_down = ["11", "12", "13", "14", "15", "15", "15", "15", "15", "14", "13", "12", "11"]

        self.img_standing = []
        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')

