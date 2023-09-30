from .units import Units


class Adevl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

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
        self.img_shift_x = -30
        self.img_shift_y = -15

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')


class Devil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'devil'
        self.attack = 19
        self.defense = 21
        self.damage = [30, 40]
        self.health = 160
        self.speed = 11
        self.ai = 5101

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
        self.start_moving = ["38", "39", "40", "41", "42", "43", "44", "45", "55", "56", "57", "58", "59", "60"]
        self.stop_moving = ["61", "62", "63", "64", "65", "66", "67", "68", "69", "70"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -30
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')


class Efree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

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


class Pfoe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pfoe'
        self.attack = 13
        self.defense = 13
        self.damage = [13, 17]
        self.health = 45
        self.speed = 7
        self.ai = 1224

        self.cur_health = self.health

        self.moving = ["40", "41", "42", "43", "44", "45", "46", "47"]
        self.mouse_over = ["30", "31", "32", "33", "32", "33", "32", "33", "32", "31", "30"]
        self.standing = ["64", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["50", "51", "52", "53", "54", "55"]
        self.defend = ["26", "27", "28", "29", "29", "29", "29", "29", "28", "27", "26"]
        self.death = ["21", "22", "23", "24", "25"]
        self.dead = "25"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "14"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "15", "16", "17", "18", "19", "20"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Pfien(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pfien'
        self.attack = 13
        self.defense = 13
        self.damage = [13, 17]
        self.health = 45
        self.speed = 6
        self.ai = 765

        self.cur_health = self.health

        self.moving = ["40", "41", "42", "43", "44", "45", "46", "47"]
        self.mouse_over = ["30", "31", "32", "33", "32", "33", "32", "33", "32", "31", "30"]
        self.standing = ["58", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["50", "51", "52", "53", "54", "55"]
        self.defend = ["26", "27", "28", "29", "29", "29", "29", "29", "28", "27", "26"]
        self.death = ["21", "22", "23", "24", "25"]
        self.dead = "25"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "14"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "15", "16", "17", "18", "19", "20"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Thdem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'thdem'
        self.attack = 10
        self.defense = 10
        self.damage = [7, 9]
        self.health = 40
        self.speed = 6
        self.ai = 480

        self.cur_health = self.health

        self.moving = ["11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "21", "22", "23", "24", "24", "24", "23", "22", "21"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Ohdem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ohdem'
        self.attack = 10
        self.defense = 10
        self.damage = [7, 9]
        self.health = 35
        self.speed = 5
        self.ai = 445

        self.cur_health = self.health

        self.moving = ["11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05", "01"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "21", "22", "23", "24", "24", "24", "23", "22", "21"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Cerbu(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'cerbu'
        self.attack = 10
        self.defense = 8
        self.damage = [2, 7]
        self.health = 25
        self.speed = 8
        self.ai = 392

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "19", "20", "21", "22", "21", "20", "19"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "23", "24", "25", "26", "27", "28", "29"]
        self.attack_straight = ["01", "30", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 215
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Gog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gog'
        self.attack = 6
        self.defense = 4
        self.damage = [2, 4]
        self.health = 13
        self.speed = 4
        self.arrows = 12
        self.ai = 159

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["05", "06", "07", "08", "09", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "03", "02"]
        self.getting_hit = ["01", "53", "54", "55", "56", "57", "58"]
        self.defend = ["01", "21", "22", "23", "24", "25", "26"]
        self.death = ["01", "59", "60", "61", "62", "63", "64", "63", "64"]
        self.dead = "64"
        self.attack_up = ["01", "38", "39", "30", "27", "28", "29", "34"]
        self.attack_straight = ["01", "38", "39", "40", "35", "36", "37", "44"]
        self.attack_down = ["01", "38", "39", "40", "48", "45", "46", "47", "52"]
        self.shoot_up = ["01", "38", "39", "30", "31", "32", "33", "34"]
        self.shoot_straight = ["01", "38", "39", "40", "41", "42", "43", "44"]
        self.shoot_down = ["01", "38", "39", "40", "48", "49", "50", "51", "52"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Famil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'famil'
        self.attack = 4
        self.defense = 4
        self.damage = [1, 2]
        self.health = 4
        self.speed = 7
        self.ai = 60

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "05", "06", "07", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "20", "21", "21", "22", "23", "24"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')
