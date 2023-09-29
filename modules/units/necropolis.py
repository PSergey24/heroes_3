from .units import Units


class Ndrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ndrgn'
        self.attack = 17
        self.defense = 15
        self.damage = [25, 50]
        self.health = 150
        self.speed = 9
        self.ai = 3388

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["43", "44", "45", "46", "47", "48"]
        self.mouse_over = ["31", "32", "33", "34", "35"]
        self.standing = ["61", "36", "37", "38", "39", "38", "37", "36"]
        self.getting_hit = ["52", "53", "54", "55", "56", "57"]
        self.defend = ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"]
        self.death = ["19", "20", "21", "22", "23", "24", "25", "26"]
        self.dead = "26"
        self.attack_up = ["01", "08", "09", "10", "11", "12", "07"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07"]
        self.attack_down = ["13", "14", "15", "16", "17", "18", "07"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -20

        self.update_hex(i, j)
        self.create_animation('standing')


class PLich(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'plich'
        self.attack = 13
        self.defense = 10
        self.damage = [11, 15]
        self.health = 40
        self.speed = 7
        self.ai = 1049

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

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Lich(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'lich'
        self.attack = 13
        self.defense = 10
        self.damage = [11, 13]
        self.health = 30
        self.speed = 6
        self.ai = 848

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


class Nosfe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nosfe'
        self.attack = 10
        self.defense = 10
        self.damage = [5, 8]
        self.health = 40
        self.speed = 9
        self.ai = 783

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["14", "15", "14", "16", "17", "16"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "25", "25", "24", "23", "22"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 215
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Wrait(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'wrait'
        self.attack = 7
        self.defense = 7
        self.damage = [3, 5]
        self.health = 18
        self.speed = 7
        self.ai = 315

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["41", "42", "43", "44", "45", "46", "47", "48"]
        self.mouse_over = ["32", "33", "34", "35", "35", "35", "35", "34", "33", "32"]
        self.standing = ["57", "36", "37", "38", "39", "38", "37", "36"]
        self.getting_hit = ["49", "50", "51", "52", "53", "54"]
        self.defend = ["28", "29", "30", "31", "31", "31", "31", "30", "29", "28"]
        self.death = ["49", "50", "22", "23", "24", "25", "26", "27"]
        self.dead = "27"
        self.attack_up = ["08", "09", "10", "11", "12", "13", "14"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07"]
        self.attack_down = ["15", "16", "17", "18", "19", "20", "21"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Zombi(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'zombi'
        self.attack = 5
        self.defense = 5
        self.damage = [2, 3]
        self.health = 15
        self.speed = 3
        self.ai = 98

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "47", "48", "49", "50", "51", "52"]
        self.defend = ["01", "23", "24", "25", "26", "27", "28"]
        self.death = ["01", "53", "54", "55", "56", "57", "58", "59", "60"]
        self.dead = "60"
        self.attack_up = ["01", "29", "30", "31", "32", "33", "34"]
        self.attack_straight = ["01", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "41", "42", "43", "44", "45", "46"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Wskel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'wskel'
        self.attack = 6
        self.defense = 6
        self.damage = [1, 3]
        self.health = 6
        self.speed = 5
        self.ai = 85

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

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Skele(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'skele'
        self.attack = 5
        self.defense = 4
        self.damage = [1, 3]
        self.health = 6
        self.speed = 4
        self.ai = 60

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
