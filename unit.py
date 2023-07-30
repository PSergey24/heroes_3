import os.path

import pygame
import math

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
        self.wait = False

        self.path = []
        self.standing = None
        self.moving = None

        self.avatar = None
        self.is_animation = False
        self.direction = True
        self.img = None
        self.current_animation = []
        self.animation_count = 0
        self.path_pos = 0
        self.move_count = 0
        self.dis = 0

        self.img_size_x = None
        self.img_size_y = None

    def draw(self, screen):
        self.draw_character(screen)
        self.draw_character_count(screen)

        if self.is_animation:
            self.is_animation = self.move()

    def draw_character(self, screen):
        self.img = self.current_animation[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.current_animation):
            self.animation_count = 0

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

            for i, img in enumerate(self.current_animation):
                self.current_animation[i] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

            if self.path_pos == len(self.path) - 1:
                self.change_animation('standing')
                self.x = x2
                self.y = y2
                return False

        self.x = x2
        self.y = y2
        return True

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True

    def change_animation(self, animation):
        self.current_animation.clear()
        self.animation_count = 0

        speed, images = self.choose_animation_info(animation)
        for x in images:
            for j in range(speed):
                unit = pygame.image.load(os.path.join(f"data/{self.character}/{animation}/c{self.character}{x}.png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                if self.team == 2:
                    unit = pygame.transform.flip(unit, True, False)
                self.current_animation.append(unit)

    def choose_animation_info(self, animation):
        if animation == 'standing':
            return 10, self.standing
        if animation == 'moving':
            return 6, self.moving


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

        self.current_animation = []
        self.img_size_x = 140
        self.img_size_y = self.img_size_x / 1.125

        self.create_animation()

    def create_animation(self):
        for x in self.standing:
            for j in range(30):
                unit = pygame.image.load(os.path.join("data/angel/standing/", "cangel" + str(x) + ".png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                if self.team == 2:
                    unit = pygame.transform.flip(unit, True, False)
                self.current_animation.append(unit)


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

        self.current_animation = []
        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.create_animation()

    def create_animation(self):
        for x in self.standing:
            for j in range(30):
                unit = pygame.image.load(os.path.join("data/elf/standing/", "celf" + str(x) + ".png"))
                unit = pygame.transform.scale(unit, (self.img_size_x, self.img_size_y))
                if self.team == 2:
                    unit = pygame.transform.flip(unit, True, False)
                self.current_animation.append(unit)


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
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]

        self.current_animation = []
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
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]

        self.img_standing = []
        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.change_animation('standing')

