import os.path

import pygame
import math


pygame.init()
FONT = pygame.font.Font('data/fonts/Times New Roman Bold.ttf', 12)

R = 35
r = round(math.sqrt(3) * R / 2, 2)


class Unit:
    img_standing = []
    img_size_x = None
    img_size_y = None

    def __init__(self, i, j, count):
        self.count = count
        self.position = [i, j]
        self.attack = None
        self.defense = None
        self.damage = None
        self.health = None
        self.speed = None

        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.vel = 3
        self.path = []
        self.img = None
        self.path_pos = 0
        self.move_count = 0

    def draw(self, screen, x, y):
        self.draw_character(screen, x, y)
        self.draw_character_count(screen, x, y)

        # self.move()

    def draw_character(self, screen, x, y):
        self.img = self.img_standing[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.img_standing):
            self.animation_count = 0

        screen.blit(self.img, (x - self.img_size_x / 4, y - self.img_size_y * (1 / 2)))

    def draw_character_count(self, screen, x, y):
        txt = FONT.render(str(self.count), True, (255, 255, 255))
        pygame.draw.rect(screen, (67, 19, 104),
                         (x + R * 2 - txt.get_height() * 2.3, y + r * 2 - txt.get_width() * 1.2, 50, 20))
        pygame.draw.rect(screen, (255, 255, 255),
                         (x + R * 2 - txt.get_height() * 2.3, y + r * 2 - txt.get_width() * 1.2, 50, 20), 1)
        screen.blit(txt, (x + R * 2 - txt.get_height(), y + r * 2 - txt.get_width()))

    # def collide(self, X, Y):
    #     if self.x + self.width >= X >= self.x:
    #         if self.y + self.height >= Y >= self.y:
    #             return True
    #     return False

    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        change_x = x2 - x1
        change_y = y2 - y1

        math.tan(change_y/change_x)

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True


class Angel(Unit):
    img_standing = []
    img_size_x = 160
    img_size_y = img_size_x / 1.125

    for x in ["00", "51", "52", "53", "54", "53", "52", "51"]:
        for j in range(30):
            unit = pygame.image.load(os.path.join("data/angel/standing/", "cangel" + str(x) + ".png"))
            unit = pygame.transform.scale(unit, (img_size_x, img_size_y))
            img_standing.append(unit)

    def __init__(self, i, j, count):
        super().__init__(i, j, count)

        self.attack = 20
        self.defense = 20
        self.damage = [50, 50]
        self.health = 200
        self.speed = 12


class Elf(Unit):
    img_standing = []
    img_size_x = 140
    img_size_y = img_size_x / 1.125

    for x in ["72", "48", "49", "50", "51", "50", "49", "48"]:
        for j in range(30):
            unit = pygame.image.load(os.path.join("data/elf/standing/", "celf" + str(x) + ".png"))
            unit = pygame.transform.scale(unit, (img_size_x, img_size_y))
            img_standing.append(unit)

    def __init__(self, i, j, count):
        super().__init__(i, j, count)

        self.attack = 9
        self.defense = 5
        self.damage = [3, 5]
        self.health = 15
        self.speed = 6







