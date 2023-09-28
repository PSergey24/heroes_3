from .units import Units


class Fbird(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'fbird'
        self.attack = 18
        self.defense = 18
        self.damage = [30, 40]
        self.health = 150
        self.speed = 15
        self.ai = 4336

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["45", "46", "47", "48", "49", "50"]
        self.mouse_over = ["35", "36", "37", "38", "38", "37", "36", "35"]
        self.standing = ["63", "39", "40", "41", "42", "41", "40", "39"]
        self.getting_hit = ["54", "55", "56", "57", "58", "59"]
        self.defend = ["31", "32", "33", "34", "34", "34", "33", "32", "31"]
        self.death = ["24", "25", "26", "27", "28", "29", "30"]
        self.dead = "30"
        self.attack_up = ["01", "09", "10", "11", "12", "13", "12", "13", "12", "13", "14", "15"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "05", "06", "05", "06", "07", "08"]
        self.attack_down = ["16", "17", "18", "19", "20", "21", "20", "21", "20", "21", "22", "23"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -35
        self.img_shift_y = -20

        self.update_hex(i, j)
        self.create_animation('standing')


class Magel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'magel'
        self.attack = 15
        self.defense = 13
        self.damage = [15, 25]
        self.health = 80
        self.speed = 9
        self.ai = 2012

        self.cur_health = self.health

        self.moving = ["30", "31", "32", "33", "34", "35", "36", "37"]
        self.mouse_over = ["17", "18", "19", "20", "21", "22", "23"]
        self.standing = ["48", "24", "25", "26", "27", "26", "25", "24"]
        self.getting_hit = ["40", "41", "42", "43", "44", "45"]
        self.defend = ["11", "12", "13", "14", "15", "16", "16", "16", "15", "14", "13", "12", "11"]
        self.death = ["05", "06", "07", "08", "09", "10"]
        self.dead = "10"
        self.attack_up = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        self.attack_straight = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        self.attack_down = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -20

        self.update_hex(i, j)
        self.create_animation('standing')


class Psyel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'psyel'
        self.attack = 15
        self.defense = 13
        self.damage = [10, 20]
        self.health = 75
        self.speed = 7
        self.ai = 1669

        self.cur_health = self.health

        self.moving = ["30", "31", "32", "33", "34", "35", "36", "37"]
        self.mouse_over = ["17", "18", "19", "20", "21", "22", "23"]
        self.standing = ["48", "24", "25", "26", "27", "26", "25", "24"]
        self.getting_hit = ["40", "41", "42", "43", "44", "45"]
        self.defend = ["11", "12", "13", "14", "15", "16", "16", "16", "15", "14", "13", "12", "11"]
        self.death = ["05", "06", "07", "08", "09", "10"]
        self.dead = "10"
        self.attack_up = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        self.attack_straight = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        self.attack_down = ["01", "02", "03", "04", "04", "04", "03", "02", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -20

        self.update_hex(i, j)
        self.create_animation('standing')


class Eelem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'eelem'
        self.attack = 10
        self.defense = 10
        self.damage = [4, 8]
        self.health = 40
        self.speed = 4
        self.ai = 330

        self.cur_health = self.health

        self.moving = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.mouse_over = ["28", "29", "30", "31", "32", "29", "30", "31", "32"]
        self.standing = ["57", "33", "34", "35", "36", "35", "34", "33"]
        self.getting_hit = ["49", "50", "51", "52", "53", "54"]
        self.defend = ["24", "25", "26", "27", "27", "27", "27", "27", "26", "25", "24"]
        self.death = ["18", "19", "20", "21", "22", "23"]
        self.dead = "23"
        self.attack_up = ["01", "08", "09", "10", "11", "12", "07"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07"]
        self.attack_down = ["01", "13", "14", "15", "16", "17", "07"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Nrg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nrg'
        self.attack = 12
        self.defense = 8
        self.damage = [4, 6]
        self.health = 35
        self.speed = 8
        self.ai = 470

        self.cur_health = self.health
        self.is_jumper = True

        self.moving = ["56", "57", "58", "59", "60", "61", "62"]
        self.mouse_over = ["41", "42", "43", "44", "45", "46"]
        self.standing = ["80", "47", "48", "49", "50", "51", "52"]
        self.getting_hit = ["65", "66", "67", "68", "69", "70"]
        self.defend = ["34", "35", "36", "37", "38", "39", "40", "37", "36", "35", "34"]
        self.death = ["25", "26", "27", "28", "29", "30", "31", "32", "33"]
        self.dead = "33"
        self.attack_up = ["09", "10", "11", "12", "13", "14", "15", "16"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["17", "18", "19", "20", "21", "22", "23", "24"]
        self.start_moving = ["53", "54", "55"]
        self.stop_moving = ["62", "61", "60", "59", "58", "57", "56", "63", "64"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')


class Storm(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'storm'
        self.attack = 9
        self.defense = 9
        self.damage = [2, 8]
        self.health = 25
        self.speed = 8
        self.ai = 486

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["45", "46", "47", "48"]
        self.mouse_over = ["34", "35", "36", "37", "38"]
        self.standing = ["63", "39", "40", "41", "42", "43", "42", "41", "40", "39"]
        self.getting_hit = ["49", "50", "51", "52", "53", "54"]
        self.defend = ["28", "29", "30", "31", "32", "33", "32", "31", "30", "29", "28"]
        self.death = ["19", "20", "21", "22", "23", "24", "25", "26", "27"]
        self.dead = "27"
        self.attack_up = ["07", "08", "09", "10", "11", "12"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06"]
        self.attack_down = ["13", "14", "15", "16", "17", "18"]
        self.shoot_up = ["55", "56", "57", "58", "59", "60"]
        self.shoot_straight = ["55", "56", "57", "58", "59", "60"]
        self.shoot_down = ["55", "56", "57", "58", "59", "60"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -15

        self.update_hex(i, j)
        self.create_animation('standing')


class Sprit(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'sprit'
        self.attack = 2
        self.defense = 2
        self.damage = [1, 3]
        self.health = 3
        self.speed = 9
        self.ai = 95

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["48", "49", "50", "51", "52", "53"]
        self.mouse_over = ["35", "36", "37", "38", "38", "38", "39", "40"]
        self.standing = ["67", "41", "42", "43", "44", "43", "42", "41"]
        self.getting_hit = ["57", "58", "59", "60", "61", "62", "63", "64"]
        self.defend = ["31", "32", "33", "34", "34", "34", "33", "32", "31"]
        self.death = ["25", "26", "27", "28", "29", "30"]
        self.dead = "30"
        self.attack_up = ["09", "10", "11", "12", "13", "12", "13", "14", "15", "16"]
        self.attack_straight = ["01", "02", "03", "04", "05", "04", "05", "06", "07", "08"]
        self.attack_down = ["17", "18", "19", "20", "21", "20", "21", "22", "23", "24"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')
