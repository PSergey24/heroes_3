from .units import Units


class Adrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'adrgn'
        self.attack = 50
        self.defense = 50
        self.damage = [70, 80]
        self.health = 1000
        self.speed = 19
        self.ai = 78845

        self.cur_health = self.health

        self.moving = ["13", "14", "15", "16", "15", "14"]
        self.mouse_over = ["01", "05", "06", "07", "08", "07", "06", "05"]
        self.standing = ["01", "01", "02", "03", "04", "04", "04", "04", "03", "02", "01", "01"]
        self.getting_hit = ["01", "57", "58", "59", "60", "61", "62"]
        self.defend = ["01", "51", "52", "53", "54", "55", "56"]
        self.death = ["01", "63", "64", "65", "66", "67", "68", "69"]
        self.dead = "69"
        self.attack_up = ["01", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
        self.attack_straight = ["01", "33", "34", "35", "36", "37", "38", "39", "40", "41"]
        self.attack_down = ["01", "42", "43", "44", "45", "46", "47", "48", "49", "50"]
        self.dhex_attack_up = ["01", "23", "24", "25", "78", "79", "80", "81", "82", "83", "84"]
        self.dhex_attack_straight = ["01", "33", "34", "35", "36", "70", "71", "72", "73", "41"]
        self.dhex_attack_down = ["01", "42", "43", "74", "75", "76", "77", "50"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = 20

        self.update_hex(i, j)
        self.create_animation('standing')
