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
