from .units import Units


class Mage(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'mage'
        self.attack = 11
        self.defense = 18
        self.damage = [7, 9]
        self.health = 25
        self.speed = 5

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["56", "57", "58", "59", "60", "61", "62", "63"]
        self.mouse_over = ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"]
        self.standing = ["74", "50", "51", "52", "53", "52", "51", "50"]
        self.getting_hit = ["66", "67", "68", "69", "70", "71"]
        self.defend = ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"]
        self.death = ["34", "35", "36", "37", "38", "39", "40", "41"]
        self.dead = "41"
        self.attack_up = ["16", "17", "18", "19", "26", "27", "28", "29", "24", "25"]
        self.attack_straight = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
        self.attack_down = ["16", "17", "18", "19", "30", "31", "32", "33", "24", "25"]
        self.shoot_up = ["06", "07", "08", "09", "10", "10", "10", "10", "10", "09", "08", "07", "06"]
        self.shoot_straight = ["01", "02", "03", "04", "05", "05", "05", "05", "05", "04", "03", "02", "01"]
        self.shoot_down = ["11", "12", "13", "14", "15", "15", "15", "15", "15", "14", "13", "12", "11"]

        self.img_size_x = 120
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')


class GremM(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gremm'
        self.attack = 4
        self.defense = 4
        self.damage = [1, 2]
        self.health = 4
        self.speed = 5
        self.arrows = 8
        self.ai = 66

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17"]
        self.mouse_over = ["01", "05", "06", "05", "01", "07", "08", "07", "01", "05", "06", "05", "01", "07"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "20", "21", "22", "23", "23", "23", "22", "21", "20"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "30", "24", "25", "26", "27", "28", "29"]
        self.attack_straight = ["01", "30", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "30", "37", "38", "39", "40", "41", "42"]
        self.shoot_up = ["01", "60", "61", "62", "63", "64", "65", "66", "63", "57", "58", "59", "68", "69", "70", "08", "07"]
        self.shoot_straight = ["01", "01", "60", "61", "62", "63", "64", "65", "66", "63", "67", "68", "69", "70", "08", "07"]
        self.shoot_down = ["01", "01", "60", "61", "62", "63", "64", "65", "66", "71", "72", "73", "69", "70", "08", "07"]

        self.img_size_x = 190
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -15

        self.update_hex(i, j)
        self.create_animation('standing')
