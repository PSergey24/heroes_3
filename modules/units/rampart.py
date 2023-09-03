from .units import Units


class Elf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'elf'
        self.attack = 9
        self.defense = 5
        self.damage = [3, 5]
        self.health = 15
        self.speed = 6
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
