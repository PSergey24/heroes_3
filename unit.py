import os.path

import pygame
import math


class Unit:
    img_standing = []
    img_size_x = None
    img_size_y = None

    def __init__(self, x, y, count):
        self.count = count
        self.position = [x, y]

        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = []
        self.img = None
        self.path_pos = 0
        self.move_count = 0

    def draw(self, screen, x, y):
        self.img = self.img_standing[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.img_standing):
            self.animation_count = 0

        screen.blit(self.img, (x - self.img_size_x/4, y - self.img_size_y * (1/2)))
        # self.move()

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

    def __init__(self, x, y, count):
        super().__init__(x, y, count)


class Elf(Unit):
    img_standing = []
    img_size_x = 140
    img_size_y = img_size_x / 1.125

    for x in ["72", "48", "49", "50", "51", "50", "49", "48"]:
        for j in range(30):
            unit = pygame.image.load(os.path.join("data/elf/standing/", "celf" + str(x) + ".png"))
            unit = pygame.transform.scale(unit, (img_size_x, img_size_y))
            img_standing.append(unit)

    def __init__(self, x, y, count):
        super().__init__(x, y, count)







