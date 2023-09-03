from .units import Units


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
