from .units import Units


class Chydr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'chydr'
        self.attack = 18
        self.defense = 20
        self.damage = [25, 45]
        self.health = 250
        self.speed = 7
        self.ai = 5931

        self.cur_health = self.health

        self.moving = ["40", "41", "42", "43", "44", "45", "46", "47"]
        self.mouse_over = ["28", "29", "30", "31", "32", "33"]
        self.standing = ["58", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["50", "51", "52", "53", "54", "55"]
        self.defend = ["24", "25", "26", "27", "27", "27", "27", "26", "25", "24"]
        self.death = ["50", "51", "18", "19", "20", "21", "22", "23"]
        self.dead = "23"
        self.attack_up = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.attack_down = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]

        self.dhex_attack_up = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.dhex_attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.dhex_attack_down = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


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


class Wyvmn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'wyvmn'
        self.attack = 14
        self.defense = 14
        self.damage = [18, 22]
        self.health = 70
        self.speed = 11
        self.ai = 1518

        self.cur_health = self.health

        self.moving = ["12", "10", "11", "10", "12", "13"]
        self.mouse_over = ["01", "04", "05", "06", "06", "05", "04", "01"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49", "44", "01"]
        self.defend = ["01", "20", "21", "22", "23", "24", "25", "01"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "01"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37", "01"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Wyver(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'wyver'
        self.attack = 14
        self.defense = 14
        self.damage = [14, 18]
        self.health = 70
        self.speed = 7
        self.ai = 1350

        self.cur_health = self.health

        self.moving = ["12", "10", "11", "10", "12", "13"]
        self.mouse_over = ["01", "04", "05", "06", "06", "05", "04", "01"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49", "44", "01"]
        self.defend = ["01", "20", "21", "22", "23", "24", "25", "01"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "01"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37", "01"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Cgorg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'cgorg'
        self.attack = 10
        self.defense = 14
        self.damage = [12, 16]
        self.health = 70
        self.speed = 5
        self.ai = 890

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["06", "07", "08", "09"]
        self.standing = ["01", "02", "03", "04", "05", "04", "03", "02"]
        self.getting_hit = ["19", "20", "21", "22", "23", "24"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["48", "49", "50", "51", "52"]
        self.dead = "52"
        self.attack_up = ["35", "36", "37", "38", "39", "40", "41"]
        self.attack_straight = ["29", "30", "31", "32", "33", "34"]
        self.attack_down = ["42", "43", "44", "45", "46", "47"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = 0

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


class Drfly(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'drfly'
        self.attack = 7
        self.defense = 9
        self.damage = [2, 5]
        self.health = 20
        self.speed = 9
        self.ai = 268

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["11", "12", "13", "14", "15", "16"]
        self.mouse_over = ["01", "06", "07", "08", "09"]
        self.standing = ["01", "02", "03", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48"]
        self.defend = ["01", "20", "21", "22", "23", "24", "25"]
        self.death = ["01", "49", "50", "51", "52", "53", "54"]
        self.dead = "54"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Aliza(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'aliza'
        self.attack = 6
        self.defense = 8
        self.damage = [2, 5]
        self.health = 15
        self.speed = 5
        self.arrows = 0 #todo:
        self.ai = 156

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["54", "55", "56", "57", "58", "59", "60"]
        self.mouse_over = ["44", "45", "46", "47", "47", "47", "47", "46", "45", "44"]
        self.standing = ["72", "48", "49", "50", "51", "50", "49", "48"]
        self.getting_hit = ["64", "65", "66", "67", "68", "69"]
        self.defend = ["40", "41", "42", "43", "43", "43", "43", "42", "41", "40"]
        self.death = ["64", "65", "34", "35", "36", "37", "38", "39"]
        self.dead = "39"
        self.attack_up = ["19", "20", "21", "22", "28", "29", "30", "26", "27"]
        self.attack_straight = ["19", "20", "21", "22", "23", "24", "25", "26", "27"]
        self.attack_down = ["19", "20", "21", "22", "31", "32", "33", "26", "27"]
        self.shoot_up = ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"]
        self.shoot_straight = ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"]
        self.shoot_down = ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Pliza(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pliza'
        self.attack = 4
        self.defense = 6
        self.damage = [2, 3]
        self.health = 14
        self.speed = 4
        self.arrows = 0 #todo:
        self.ai = 126

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["47", "48", "49", "50", "50", "50", "50", "49", "48", "47"]
        self.standing = ["75", "51", "52", "53", "54", "53", "52", "51"]
        self.getting_hit = ["67", "68", "69", "70", "71", "72"]
        self.defend = ["43", "44", "45", "46", "46", "46", "46", "45", "44", "43"]
        self.death = ["67", "68", "37", "38", "39", "40", "41", "42"]
        self.dead = "42"
        self.attack_up = ["25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["19", "20", "21", "22", "23", "24"]
        self.attack_down = ["31", "32", "33", "34", "35", "36"]
        self.shoot_up = ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"]
        self.shoot_straight = ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"]
        self.shoot_down = ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

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


class Gnoll(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gnoll'
        self.attack = 3
        self.defense = 5
        self.damage = [2, 3]
        self.health = 6
        self.speed = 4
        self.ai = 56

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
