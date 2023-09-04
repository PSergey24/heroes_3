from .units import Units


class BDragon(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'bdrgn'
        self.attack = 25
        self.defense = 25
        self.damage = [40, 50]
        self.health = 300
        self.speed = 15
        self.ai = 8721

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


class Cmcor(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'cmcor'
        self.attack = 16
        self.defense = 14
        self.damage = [14, 20]
        self.health = 80
        self.speed = 11
        self.ai = 1589

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


class Minok(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'minok'
        self.attack = 15
        self.defense = 15
        self.damage = [12, 20]
        self.health = 50
        self.speed = 8
        self.ai = 1068

        self.cur_health = self.health

        self.moving = ["09", "10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["59", "05", "06", "07", "08", "59"]
        self.standing = ["59", "02", "03", "04", "04", "03", "02", "59"]
        self.getting_hit = ["01", "41", "42", "43", "44", "45", "46"]
        self.defend = ["01", "18", "19", "19", "20", "20", "21", "01"]
        self.death = ["01", "47", "48", "49", "50", "51", "52"]
        self.dead = "52"
        self.attack_up = ["01", "22", "23", "24", "25", "26", "27", "01"]
        self.attack_straight = ["01", "28", "29", "30", "31", "32", "33", "01"]
        self.attack_down = ["01", "34", "35", "36", "37", "38", "39", "40"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Harph(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'harph'
        self.attack = 6
        self.defense = 6
        self.damage = [1, 4]
        self.health = 14
        self.speed = 9
        self.ai = 238

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["54", "55", "56", "57", "58", "59", "60"]
        self.mouse_over = ["42", "43", "44", "45", "46", "45", "46", "45", "44", "43", "42"]
        self.standing = ["47", "48", "49", "50", "49", "48", "47"]
        self.getting_hit = ["66", "68", "67", "65", "64", "21"]
        self.defend = ["35", "36", "37", "38", "39", "40", "41", "21"]
        self.death = ["28", "29", "30", "31", "32", "33", "34"]
        self.dead = "34"
        self.attack_up = ["21", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
        self.attack_straight = ["21", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "21"]
        self.attack_down = ["21", "22", "23", "24", "26", "27", "26", "25", "24", "22"]
        self.start_moving = ["51", "52", "53"]
        self.stop_moving = ["61", "62", "63"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Harpy(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'harpy'
        self.attack = 6
        self.defense = 5
        self.damage = [1, 4]
        self.health = 14
        self.speed = 6
        self.ai = 154

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["54", "55", "56", "57", "58", "59", "60"]
        self.mouse_over = ["42", "43", "44", "45", "46", "45", "46", "45", "44", "43", "42"]
        self.standing = ["47", "48", "49", "50", "49", "48", "47"]
        self.getting_hit = ["66", "68", "67", "65", "64", "21"]
        self.defend = ["35", "36", "37", "38", "39", "40", "41", "21"]
        self.death = ["28", "29", "30", "31", "32", "33", "34"]
        self.dead = "34"
        self.attack_up = ["21", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
        self.attack_straight = ["21", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "21"]
        self.attack_down = ["21", "22", "23", "24", "26", "27", "26", "25", "24", "22"]
        self.start_moving = ["21", "51", "52", "53"]
        self.stop_moving = ["54", "61", "62", "63", "21"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')

