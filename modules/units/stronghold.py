from .units import Units


class Cyclp(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

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


class Roc(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'roc'
        self.attack = 13
        self.defense = 1
        self.damage = [11, 15]
        self.health = 60
        self.speed = 7
        self.ai = 1027

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["12", "13", "14", "15", "14", "13"]
        self.mouse_over = ["01", "05", "06", "07", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "49", "50", "51", "52", "53", "54"]
        self.defend = ["01", "22", "23", "24", "25", "25", "24", "23", "22"]
        self.death = ["01", "55", "56", "57", "58", "59", "60", "61"]
        self.dead = "61"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "41", "42", "43", "44", "45", "46", "47", "48"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 5
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Ogmag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ogmag'
        self.attack = 13
        self.defense = 7
        self.damage = [6, 12]
        self.health = 60
        self.speed = 5
        self.ai = 672

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "24", "25", "25", "23", "22"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Gobli(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gobli'
        self.attack = 4
        self.defense = 2
        self.damage = [1, 2]
        self.health = 5
        self.speed = 5
        self.ai = 60

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "24", "25", "26", "27", "28"]
        self.death = ["01", "52", "53", "54", "55", "56", "57", "58", "59"]
        self.dead = "59"
        self.attack_up = ["01", "34", "35", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "34", "35", "41", "42", "43", "44", "45"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')
