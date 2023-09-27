from .units import Units


class Nixwarr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nixwarr'
        self.attack = 14
        self.defense = 17
        self.damage = [18, 22]
        self.health = 100
        self.speed = 7
        self.ai = 2116

        self.cur_health = self.health

        self.moving = ["14", "15", "16", "17", "18", "19", "20", "21"]
        self.mouse_over = ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"]
        self.standing = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["25", "26", "27", "28", "29", "30", "31", "32"]
        self.defend = ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"]
        self.death = ["48", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["61", "62", "63", "64", "65", "66", "67", "68", "69"]
        self.attack_straight = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.attack_down = ["70", "71", "72", "73", "74", "75", "76", "77"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Nix(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nix'
        self.attack = 13
        self.defense = 16
        self.damage = [18, 20]
        self.health = 90
        self.speed = 6
        self.ai = 1415

        self.cur_health = self.health

        self.moving = ["14", "15", "16", "17", "18", "19", "20", "21"]
        self.mouse_over = ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"]
        self.standing = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["25", "26", "27", "28", "29", "30", "31", "32"]
        self.defend = ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"]
        self.death = ["48", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["61", "62", "63", "64", "65", "66", "67", "68", "69"]
        self.attack_straight = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.attack_down = ["70", "71", "72", "73", "74", "75", "76", "77"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')
