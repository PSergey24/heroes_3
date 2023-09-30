from .units import Units


class Ddrag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ddrag'
        self.attack = 27
        self.defense = 27
        self.damage = [40, 50]
        self.health = 250
        self.speed = 16
        self.ai = 8613

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["13", "14", "13", "12"]
        self.mouse_over = ["01", "04", "05", "06", "07"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01", "01"]
        self.getting_hit = ["48", "49", "50", "50", "51", "52"]
        self.defend = ["58", "59", "60", "60", "61", "62"]
        self.death = ["48", "49", "50", "53", "54", "55", "56", "57"]
        self.dead = "57"
        self.attack_up = ["21", "22", "23", "24", "25", "26", "27", "28", "29"]
        self.attack_straight = ["30", "31", "32", "33", "34", "35", "36", "37", "38"]
        self.attack_down = ["39", "40", "41", "42", "43", "44", "45", "46", "47"]
        self.dhex_attack_up = ["21", "22", "23", "24", "63", "64", "65", "28", "29"]
        self.dhex_attack_straight = ["30", "31", "32", "66", "67", "68", "69", "37", "38"]
        self.dhex_attack_down = ["39", "40", "41", "70", "71", "72", "73", "46", "47"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = 20

        self.update_hex(i, j)
        self.create_animation('standing')


class Gdrag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gdrag'
        self.attack = 18
        self.defense = 18
        self.damage = [40, 50]
        self.health = 180
        self.speed = 10
        self.ai = 4872

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["13", "14", "13", "12"]
        self.mouse_over = ["01", "04", "05", "06", "07"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["48", "49", "50", "50", "51", "52"]
        self.defend = ["58", "59", "60", "60", "61", "62"]
        self.death = ["48", "49", "50", "53", "54", "55", "56", "57"]
        self.dead = "57"
        self.attack_up = ["21", "22", "23", "24", "25", "26", "27", "28", "29"]
        self.attack_straight = ["30", "31", "32", "33", "34", "35", "36", "37", "38"]
        self.attack_down = ["39", "40", "41", "42", "43", "44", "45", "46", "47"]
        self.dhex_attack_up = ["21", "22", "23", "24", "63", "64", "65", "28", "29"]
        self.dhex_attack_straight = ["30", "31", "32", "66", "67", "68", "69", "37", "38"]
        self.dhex_attack_down = ["39", "40", "41", "70", "71", "72", "73", "46", "47"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = 10

        self.update_hex(i, j)
        self.create_animation('standing')


class Wunic(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'wunic'
        self.attack = 15
        self.defense = 14
        self.damage = [18, 22]
        self.health = 110
        self.speed = 9
        self.ai = 2030

        self.cur_health = self.health

        self.moving = ["09", "10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "04", "05", "06", "07"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "45", "46", "47", "48", "49", "50"]
        self.defend = ["01", "19", "20", "21", "22", "23", "22", "21", "20", "19", "01"]
        self.death = ["01", "51", "52", "53", "54", "55", "56", "57"]
        self.dead = "57"
        self.attack_up = ["01", "24", "25", "26", "27", "28", "29", "30", "01"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36", "37", "01"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43", "44", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 10
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Unico(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'unico'
        self.attack = 15
        self.defense = 14
        self.damage = [18, 22]
        self.health = 90
        self.speed = 7
        self.ai = 1806

        self.cur_health = self.health

        self.moving = ["09", "10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "04", "05", "06", "07"]
        self.standing = ["01", "02", "03", "03", "03", "02", "01", "01"]
        self.getting_hit = ["01", "45", "46", "47", "48", "49", "50"]
        self.defend = ["01", "19", "20", "21", "22", "23", "22", "21", "20", "19", "01"]
        self.death = ["01", "51", "52", "53", "54", "55", "56", "57"]
        self.dead = "57"
        self.attack_up = ["01", "24", "25", "26", "27", "28", "29", "30", "01"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36", "37", "01"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43", "44", "01"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 10
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


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


class Apegs(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'apegs'
        self.attack = 9
        self.defense = 10
        self.damage = [5, 9]
        self.health = 30
        self.speed = 12
        self.ai = 532

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["39", "40", "41", "42", "43", "44"]
        self.mouse_over = ["29", "30", "31", "32", "32", "32", "31", "30", "29"]
        self.standing = ["56", "33", "34", "35", "36", "35", "34", "33"]
        self.getting_hit = ["47", "48", "49", "50", "51", "52"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["47", "48", "19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "13"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "14", "15", "16", "17", "18"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Pegas(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pegas'
        self.attack = 9
        self.defense = 8
        self.damage = [5, 9]
        self.health = 30
        self.speed = 8
        self.ai = 518

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["39", "40", "41", "42", "43", "44"]
        self.mouse_over = ["29", "30", "31", "32", "32", "32", "31", "30", "29"]
        self.standing = ["56", "33", "34", "35", "36", "35", "34", "33"]
        self.getting_hit = ["47", "48", "49", "50", "51", "52"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["47", "48", "19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "13"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "14", "15", "16", "17", "18"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Grelf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'grelf'
        self.attack = 9
        self.defense = 5
        self.damage = [3, 5]
        self.health = 15
        self.speed = 7
        self.arrows = 0  # todo:
        self.ai = 331

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

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -15
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
        self.arrows = 0  # todo:
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


class Bdwar(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'bdwar'
        self.attack = 7
        self.defense = 7
        self.damage = [2, 4]
        self.health = 20
        self.speed = 5
        self.ai = 209

        self.cur_health = self.health

        self.moving = ["35", "36", "37", "38", "39", "40", "41", "42"]
        self.mouse_over = ["25", "26", "27", "28", "27", "26", "25"]
        self.standing = ["53", "29", "30", "31", "32", "31", "30", "29"]
        self.getting_hit = ["45", "46", "47", "48", "49", "50"]
        self.defend = ["21", "22", "23", "24", "24", "24", "24", "24", "23", "22", "21"]
        self.death = ["45", "46", "17", "18", "19", "20"]
        self.dead = "20"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "13", "14", "15", "16", "08"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -15
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')


class Dwarf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'dwarf'
        self.attack = 6
        self.defense = 7
        self.damage = [2, 4]
        self.health = 20
        self.speed = 3
        self.ai = 138

        self.cur_health = self.health

        self.moving = ["35", "36", "37", "38", "39", "40", "41", "42"]
        self.mouse_over = ["25", "26", "27", "28", "27", "26", "25"]
        self.standing = ["53", "29", "30", "31", "32", "31", "30", "29"]
        self.getting_hit = ["45", "46", "47", "48", "49", "50"]
        self.defend = ["21", "22", "23", "24", "24", "24", "24", "24", "23", "22", "21"]
        self.death = ["45", "46", "17", "18", "19", "20"]
        self.dead = "20"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "13", "14", "15", "16", "08"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -15
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Ecent(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ecent'
        self.attack = 6
        self.defense = 3
        self.damage = [2, 3]
        self.health = 10
        self.speed = 8
        self.ai = 138

        self.cur_health = self.health

        self.moving = ["53", "54", "55", "56", "57", "58", "59", "60"]
        self.mouse_over = ["43", "44", "45", "46", "46", "46", "45", "44", "43"]
        self.standing = ["72", "47", "48", "49", "50", "49", "48", "47", "72"]
        self.getting_hit = ["63", "64", "65", "66", "67", "68"]
        self.defend = ["39", "40", "41", "42", "42", "42", "42", "42", "41", "40", "39"]
        self.death = ["63", "64", "33", "34", "35", "36", "37", "38"]
        self.dead = "38"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "13", "14", "15", "16", "08"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Centr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'centr'
        self.attack = 5
        self.defense = 3
        self.damage = [2, 3]
        self.health = 8
        self.speed = 6
        self.ai = 100

        self.cur_health = self.health

        self.moving = ["53", "54", "55", "56", "57", "58", "59", "60"]
        self.mouse_over = ["43", "44", "45", "46"]
        self.standing = ["72", "47", "48", "49", "50", "49", "48", "47"]
        self.getting_hit = ["63", "64", "65", "66", "67", "68"]
        self.defend = ["39", "40", "41", "42", "42", "42", "42", "42", "41", "40", "39"]
        self.death = ["63", "64", "33", "34", "35", "36", "37", "38"]
        self.dead = "38"
        self.attack_up = ["01", "02", "03", "09", "10", "11", "12", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "13", "14", "15", "16", "08"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')
