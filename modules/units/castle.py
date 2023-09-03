from .units import Units


class Angel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'angel'
        self.attack = 20
        self.defense = 20
        self.damage = [50, 50]
        self.health = 200
        self.speed = 12
        self.ai = 5019

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


class Crusd(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'crusd'
        self.attack = 12
        self.defense = 12
        self.damage = [7, 10]
        self.health = 35
        self.speed = 6
        self.ai = 588

        self.cur_health = self.health

        self.moving = ["36", "37", "38", "39", "40", "41", "42", "43"]
        self.mouse_over = ["26", "27", "28", "29", "29", "28", "27", "26"]
        self.standing = ["54", "30", "31", "32", "33", "32", "31", "30"]
        self.getting_hit = ["46", "47", "48", "49", "50", "51"]
        self.defend = ["22", "23", "24", "25", "25", "25", "25", "25", "24", "23", "22"]
        self.death = ["16", "17", "18", "19", "20", "21"]
        self.dead = "21"
        self.attack_up = ["01", "02", "08", "09", "10", "11", "07"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07"]
        self.attack_down = ["01", "02", "12", "13", "14", "15", "07"]

        self.img_size_x = 144
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class RGrif(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'rgrif'
        self.attack = 9
        self.defense = 9
        self.damage = [3, 6]
        self.health = 25
        self.speed = 9
        self.ai = 488

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


class Hcbow(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'hcbow'
        self.attack = 6
        self.defense = 3
        self.damage = [2, 3]
        self.health = 10
        self.speed = 6
        self.ai = 184

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
