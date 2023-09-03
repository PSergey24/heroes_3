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
