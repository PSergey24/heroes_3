from .units import Units


class Lich(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'lich'
        self.attack = 13
        self.defense = 10
        self.damage = [11, 13]
        self.health = 30
        self.speed = 6

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["35", "36", "37", "38", "39", "40", "41"]
        self.dead = "41"
        self.attack_up = ["13", "14", "21", "22", "23", "24", "25", "26"]
        self.attack_straight = ["13", "14", "15", "16", "17", "18", "19", "20"]
        self.attack_down = ["27", "28", "29", "30", "31", "32", "33", "34"]
        self.shoot_up = ["05", "06", "07", "08", "08", "08", "08", "08", "07", "06", "05"]
        self.shoot_straight = ["01", "02", "03", "04", "04", "04", "04", "04", "03", "02", "01"]
        self.shoot_down = ["09", "10", "11", "12", "12", "12", "12", "12", "11", "10", "09"]

        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class Skele(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'skele'
        self.attack = 5
        self.defense = 4
        self.damage = [1, 3]
        self.health = 6
        self.speed = 4

        self.cur_health = self.health

        self.moving = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.mouse_over = ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"]
        self.standing = ["57", "33", "34", "35", "36", "35", "34", "33"]
        self.getting_hit = ["49", "50", "51", "52", "53", "54"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "09", "10", "11", "12", "13", "08"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "14", "15", "16", "17", "18", "08"]

        self.img_size_x = 144
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')
