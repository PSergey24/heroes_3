import os.path

import pygame
import math

from modules.settings import Settings, States
from modules.block_updater import BlockUpdater
from modules.hex_worker import HexWorker


class Unit:

    def __init__(self, i, j, count, team):
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


class Angel(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'angel'
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

        self.update_hex(i, j)
        self.create_animation('standing')


class Elf(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'elf'
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

        self.update_hex(i, j)
        self.create_animation('standing')


class Lich(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'lich'
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

        self.update_hex(i, j)
        self.create_animation('standing')


class Mage(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'mage'
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

        self.update_hex(i, j)
        self.create_animation('standing')


class BDragon(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'bdrgn'
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

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Hydra(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'hydra'
        self.attack = 16
        self.defense = 18
        self.damage = [25, 45]
        self.health = 175
        self.speed = 5

        self.cur_health = self.health

        self.moving = ["38", "39", "40", "41", "42", "43", "44", "45"]
        self.mouse_over = ["28", "29", "30", "31", "30", "29", "28"]
        self.standing = ["56", "32", "33", "34", "35", "34", "33", "32"]
        self.getting_hit = ["48", "49", "50", "51", "52", "53"]
        self.defend = ["24", "25", "26", "27", "27", "27", "27", "26", "25", "24"]
        self.death = ["48", "49", "18", "19", "20", "21", "22", "23"]
        self.dead = "23"
        self.attack_up = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.attack_down = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]

        self.dhex_attack_up = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.dhex_attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.dhex_attack_down = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]

        self.img_size_x = 144
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 30

        self.update_hex(i, j)
        self.create_animation('standing')


class RGrif(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'rgrif'
        self.attack = 9
        self.defense = 9
        self.damage = [3, 6]
        self.health = 25
        self.speed = 9

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["11", "12", "11", "10"]
        self.mouse_over = ["01", "04", "05", "06", "06", "05", "04", "01"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "41", "42", "43", "44", "45", "01"]
        self.defend = ["01", "17", "18", "19", "19", "18", "17", "01"]
        self.death = ["01", "46", "47", "48", "49", "50", "51", "52", "53"]
        self.dead = "53"
        self.attack_up = ["01", "20", "21", "22", "23", "24", "25", "26", "01"]
        self.attack_straight = ["01", "27", "28", "29", "30", "31", "32", "33", "01"]
        self.attack_down = ["01", "34", "35", "36", "37", "38", "39", "40", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Skele(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'skele'
        self.attack = 5
        self.defense = 4
        self.damage = [1, 3]
        self.health = 6
        self.speed = 4

        self.cur_health = self.health

        self.moving = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.mouse_over = ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"]
        self.standing = ["57", "33", "34", "35", "36", "35", "34", "33"]
        self.getting_hit = ["49", "50", "51", "52", "53", "54"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "14", "15", "16", "17", "18", "08"]

        self.img_size_x = 144
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Cmcor(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'cmcor'
        self.attack = 16
        self.defense = 14
        self.damage = [14, 20]
        self.health = 80
        self.speed = 11

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["47", "48", "49", "50", "50", "49", "48", "47"]
        self.standing = ["76", "51", "52", "53", "54", "53", "52", "51"]
        self.getting_hit = ["67", "68", "69", "70", "71", "72"]
        self.defend = ["43", "44", "45", "46", "46", "46", "46", "46", "45", "44", "43"]
        self.death = ["67", "68", "37", "38", "39", "40", "41", "42"]
        self.dead = "42"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "14", "15", "16", "17", "18", "08"]
        self.dhex_attack_up = ["19", "20", "27", "28", "29", "30", "31", "26"]
        self.dhex_attack_straight = ["19", "20", "21", "22", "23", "24", "25", "26"]
        self.dhex_attack_down = ["19", "20", "32", "33", "34", "35", "36", "26"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Hcbow(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'hcbow'
        self.attack = 6
        self.defense = 3
        self.damage = [2, 3]
        self.health = 10
        self.speed = 6

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["55", "56", "57", "58", "59", "60", "61", "62"]
        self.mouse_over = ["73", "74", "75", "76", "76", "76", "75", "74", "73"]
        self.standing = ["00", "49", "50", "51", "52", "51", "50", "49"]
        self.getting_hit = ["65", "66", "67", "68", "69", "70"]
        self.defend = ["43", "44", "45", "46", "46", "46", "46", "45", "44", "43"]
        self.death = ["37", "38", "39", "40", "41", "42"]
        self.dead = "42"
        self.attack_up = ["25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["19", "20", "21", "22", "23", "24"]
        self.attack_down = ["31", "32", "33", "34", "35", "36"]
        self.shoot_up = ["07", "08", "09", "10", "10", "10", "11", "12"]
        self.shoot_straight = ["01", "02", "03", "04", "04", "04", "05", "06"]
        self.shoot_down = ["13", "14", "15", "16", "16", "16", "17", "18"]

        self.img_size_x = 144
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Cyclp(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'cyclp'
        self.attack = 15
        self.defense = 12
        self.damage = [16, 20]
        self.health = 70
        self.speed = 6
        self.ai = 1266

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["45", "46", "47", "48", "49", "50", "51", "52"]
        self.mouse_over = ["39", "40", "41", "42", "41", "40", "39"]
        self.standing = ["01", "02", "03", "04", "05", "06"]
        self.getting_hit = ["31", "30", "29"]
        self.defend = ["38", "37", "36", "35"]
        self.death = ["31", "30", "32", "33", "34"]
        self.dead = "34"
        self.attack_up = ["74", "53", "19", "20", "21", "22", "23"]
        self.attack_straight = ["74", "53", "24", "25", "26", "27", "28"]
        self.attack_down = ["74", "53", "14", "15", "16", "17", "18"]
        self.shoot_up = ["74", "53", "59", "60", "61", "62", "63", "64", "65", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_straight = ["01", "01", "74", "53", "53", "54", "55", "56", "57", "58", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_down = ["01", "01", "01", "74", "53", "66", "67", "68", "69", "70", "09", "08", "07", "10", "11", "12", "13"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25

        self.update_hex(i, j)
        self.create_animation('standing')


class Efree(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'efree'
        self.attack = 16
        self.defense = 12
        self.damage = [16, 24]
        self.health = 90
        self.speed = 9
        self.ai = 1670

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["17", "18", "19", "20", "21", "22", "23"]
        self.mouse_over = ["06", "07", "08", "09", "10"]
        self.standing = ["01", "02", "03", "04", "05"]
        self.getting_hit = ["26", "27", "28", "29", "30"]
        self.defend = ["31", "32", "33", "34", "35", "34", "35", "34", "32", "31", "30"]
        self.death = ["53", "54", "55", "56", "57", "58", "59", "60"]
        self.dead = "60"
        self.attack_up = ["36", "37", "38", "42", "43", "44", "43", "44", "42"]
        self.attack_straight = ["36", "37", "38", "39", "40", "41", "40", "41", "39"]
        self.attack_down = ["36", "37", "38", "39", "45", "46", "47", "46", "47", "45"]
        self.dhex_attack_straight = ["48", "49", "50", "51", "52", "51", "52", "51", "50", "49", "48"]

        self.img_size_x = 162
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Adevl(Unit):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, count, team)

        self.character = 'adevl'
        self.attack = 26
        self.defense = 28
        self.damage = [30, 40]
        self.health = 200
        self.speed = 17
        self.ai = 7115

        self.cur_health = self.health
        self.is_jumper = True

        self.moving = ["54"]
        self.mouse_over = ["29", "30", "31", "32", "33", "32", "31", "32", "33", "32", "31", "30", "29"]
        self.standing = ["54", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["46", "47", "48", "49", "50", "51"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["17", "18", "19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "03", "04", "09", "10", "11", "12"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "04", "13", "14", "15", "16"]
        self.start_moving = ["38", "39", "40", "41", "42", "43", "44", "45", "59", "60", "61", "62", "63", "64"]
        self.stop_moving = ["65", "66", "67", "68", "69", "70", "71", "72", "73", "74"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')
