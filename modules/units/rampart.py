from .units import Units


class Btree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'btree'
        self.attack = 9
        self.defense = 12
        self.damage = [10, 14]
        self.health = 65
        self.speed = 4
        self.ai = 803

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "22", "23", "24", "24", "24", "23", "22", "21"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55"]
        self.dead = "55"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Tree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'tree'
        self.attack = 9
        self.defense = 12
        self.damage = [10, 14]
        self.health = 55
        self.speed = 3
        self.ai = 517

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "22", "23", "24", "24", "24", "23", "22", "21"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55"]
        self.dead = "55"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Elf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'elf'
        self.attack = 9
        self.defense = 5
        self.damage = [3, 5]
        self.health = 15
        self.speed = 6
        self.ai = 234

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
