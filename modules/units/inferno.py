from .units import Units


class Adevl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'adevl'
        self.attack = 26
        self.defense = 28
        self.damage = [30, 40]
        self.health = 200
        self.speed = 17
        self.ai = 7115

        self.cur_health = self.health
        self.is_jumper = True

        self.moving = ["54"]
        self.mouse_over = ["29", "30", "31", "32", "33", "32", "31", "32", "33", "32", "31", "30", "29"]
        self.standing = ["54", "34", "35", "36", "37", "36", "35", "34"]
        self.getting_hit = ["46", "47", "48", "49", "50", "51"]
        self.defend = ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"]
        self.death = ["17", "18", "19", "20", "21", "22", "23", "24"]
        self.dead = "24"
        self.attack_up = ["01", "02", "03", "04", "09", "10", "11", "12"]
        self.attack_straight = ["01", "02", "03", "04", "05", "06", "07", "08"]
        self.attack_down = ["01", "02", "03", "04", "13", "14", "15", "16"]
        self.start_moving = ["38", "39", "40", "41", "42", "43", "44", "45", "59", "60", "61", "62", "63", "64"]
        self.stop_moving = ["65", "66", "67", "68", "69", "70", "71", "72", "73", "74"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')


class Efree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'efree'
        self.attack = 16
        self.defense = 12
        self.damage = [16, 24]
        self.health = 90
        self.speed = 9
        self.ai = 1670

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["17", "18", "19", "20", "21", "22", "23"]
        self.mouse_over = ["06", "07", "08", "09", "10"]
        self.standing = ["01", "02", "03", "04", "05"]
        self.getting_hit = ["26", "27", "28", "29", "30"]
        self.defend = ["31", "32", "33", "34", "35", "34", "35", "34", "32", "31", "30"]
        self.death = ["53", "54", "55", "56", "57", "58", "59", "60"]
        self.dead = "60"
        self.attack_up = ["36", "37", "38", "42", "43", "44", "43", "44", "42"]
        self.attack_straight = ["36", "37", "38", "39", "40", "41", "40", "41", "39"]
        self.attack_down = ["36", "37", "38", "39", "45", "46", "47", "46", "47", "45"]
        self.dhex_attack_straight = ["48", "49", "50", "51", "52", "51", "52", "51", "50", "49", "48"]

        self.img_size_x = 162
        self.img_size_y = self.img_size_x / 1.125

        self.update_hex(i, j)
        self.create_animation('standing')
