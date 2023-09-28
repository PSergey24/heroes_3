from .units import Units


class Hydra(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'hydra'
        self.attack = 16
        self.defense = 18
        self.damage = [25, 45]
        self.health = 175
        self.speed = 5
        self.ai = 4120

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


class Basil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'basil'
        self.attack = 11
        self.defense = 11
        self.damage = [6, 10]
        self.health = 35
        self.speed = 5
        self.ai = 552

        self.cur_health = self.health

        self.moving = ["51", "52", "53", "54", "55", "56", "57", "58"]
        self.mouse_over = ["41", "42", "43", "44"]
        self.standing = ["69", "45", "46", "47", "48", "47", "46", "45"]
        self.getting_hit = ["61", "62", "63", "64", "65", "66"]
        self.defend = ["37", "38", "39", "40", "40", "40", "40", "39", "38", "37"]
        self.death = ["31", "32", "33", "34", "35", "36"]
        self.dead = "36"
        self.attack_up = ["07", "08", "09", "10", "11", "12"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06"]
        self.attack_down = ["13", "14", "15", "16", "17", "18"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Gnolm(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gnolm'
        self.attack = 4
        self.defense = 6
        self.damage = [2, 3]
        self.health = 6
        self.speed = 5
        self.ai = 90

        self.cur_health = self.health

        self.moving = ["40", "41", "42", "43", "44", "45", "46", "47"]
        self.mouse_over = ["29", "30", "31", "32", "33", "32", "33", "32", "33", "32", "33", "32", "31", "30", "29"]
        self.standing = ["58", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["50", "51", "52", "53", "54", "55"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "14", "15", "16", "17", "18", "08"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')
