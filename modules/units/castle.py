from .units import Units
from modules.states import Objects


class Rangl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'rangl'
        self.ai = 8776

        self.characteristics = {"base_characteristics": {"attack": 30, "defense": 30, "damage": [50, 50],
                                                         "health": 250, "speed": 18},
                                "current_health": 250, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["35", "36", "37", "38", "37", "36", "35"],
            "standing": ["00", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["19", "20", "21", "22", "23", "24"],
            "defend": ["31", "32", "33", "34", "34", "34", "34", "33", "32", "31"],
            "death": ["19", "20", "25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["07", "08", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06"],
            "attack_down": ["13", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 5, "y_shift": -25}

        self.init(i, j)

    # todo: Hatred of Devils and Archdevils => +50% additional attack damage.
    # todo: Inspiration => +1 units. to the morale of all allied soldiers; works even after the destruction of angels.
    # todo: Resurrection of allies - once per battle, resurrect of dead friendly units, 100 health - one archangel


class Angel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'angel'
        self.ai = 5019

        self.characteristics = {"base_characteristics": {"attack": 20, "defense": 20, "damage": [50, 50],
                                                         "health": 200, "speed": 12},
                                "current_health": 200, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["35", "36", "37", "38", "38", "38", "38", "37", "36", "35"],
            "standing": ["00", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["19", "20", "21", "22", "23", "24"],
            "defend": ["31", "32", "33", "34", "34", "34", "34", "33", "32", "31", "42"],
            "death": ["19", "20", "25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["07", "08", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06"],
            "attack_down": ["13", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 140, "y_size": 140 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init(i, j)

    # todo: Hatred of Devils and Archdevils => +50% additional attack damage.
    # todo: Inspiration => +1 units. to the morale of all allied soldiers; works even after the destruction of angels.


class Champ(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'champ'
        self.ai = 2100

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 16, "damage": [20, 25],
                                                         "health": 100, "speed": 9},
                                "current_health": 100, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["52", "53", "54", "55", "56", "57", "58", "59"],
            "mouse_over": ["40", "41", "42", "43", "44"],
            "standing": ["45", "46", "47", "48"],
            "getting_hit": ["67", "70", "69", "68", "67", "66", "65", "64"],
            "defend": ["34", "35", "36", "37", "38", "39"],
            "death": ["26", "27", "28", "29", "30", "31", "32", "33"],
            "dead": ["33"],
            "attack_up": ["01", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
            "attack_down": ["20", "21", "23", "25", "24", "23", "22", "21", "20"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init(i, j)

    # todo: Cavalry Bonus – 5% more damage for each square they travel before attacking.


class Cavlr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'cavlr'
        self.ai = 1946

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 15, "damage": [15, 25],
                                                         "health": 100, "speed": 7},
                                "current_health": 100, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["52", "53", "54", "55", "56", "57", "58", "59"],
            "mouse_over": ["40", "41", "42", "43", "44"],
            "standing": ["45", "46", "47", "48"],
            "getting_hit": ["67", "70", "69", "68", "67", "66", "65", "64"],
            "defend": ["34", "35", "36", "37", "38", "39"],
            "death": ["26", "27", "28", "29", "30", "31", "32", "33"],
            "dead": ["33"],
            "attack_up": ["01", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
            "attack_down": ["20", "21", "23", "25", "24", "23", "22", "21", "20"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init(i, j)

    # todo: Cavalry Bonus – 5% more damage for each square they travel before attacking.


class Zealt(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'zealt'
        self.ai = 750

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 10, "damage": [10, 12],
                                                         "health": 30, "speed": 7},
                                "current_health": 30, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14"],
            "mouse_over": ["01", "04", "05", "06", "07", "07", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "02", "01"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "46", "01"],
            "defend": ["01", "16", "17", "18", "19", "20", "01"],
            "death": ["01", "41", "42", "43", "44", "47", "48", "49", "50", "51", "52"],
            "dead": ["52"],
            "attack_up": ["01", "21", "22", "23", "24", "25", "26", "27", "01"],
            "attack_straight": ["01", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"],
            "shoot_up": ["01", "21", "22", "53", "54", "55", "55", "55", "55", "55", "26", "27", "01"],
            "shoot_straight": ["01", "28", "29", "56", "56", "57", "57", "57", "57", "57", "58", "32", "33", "01"],
            "shoot_down": ["01", "34", "35", "59", "60", "61", "61", "61", "61", "61", "39", "40", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: No penalty in hand-to-hand combat.


class Monkk(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'monkk'
        self.ai = 582

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 7, "damage": [10, 12],
                                                         "health": 30, "speed": 5},
                                "current_health": 30, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14"],
            "mouse_over": ["01", "04", "05", "06", "07", "07", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "02", "01"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "46", "01"],
            "defend": ["01", "16", "17", "18", "19", "20", "01"],
            "death": ["01", "41", "42", "43", "44", "47", "48", "49", "50", "51", "52"],
            "dead": ["52"],
            "attack_up": ["01", "21", "22", "23", "24", "25", "26", "27", "01"],
            "attack_straight": ["01", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"],
            "shoot_up": ["01", "01", "21", "22", "23", "24", "25", "26", "27", "01"],
            "shoot_straight": ["01", "01", "01", "28", "29", "30", "31", "32", "33", "01"],
            "shoot_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Crusd(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'crusd'
        self.ai = 588

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 12, "damage": [7, 10],
                                                         "health": 35, "speed": 6},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["36", "37", "38", "39", "40", "41", "42", "43"],
            "mouse_over": ["26", "27", "28", "29", "29", "28", "27", "26"],
            "standing": ["54", "30", "31", "32", "33", "32", "31", "30"],
            "getting_hit": ["46", "47", "48", "49", "50", "51"],
            "defend": ["22", "23", "24", "25", "25", "25", "25", "25", "24", "23", "22"],
            "death": ["16", "17", "18", "19", "20", "21"],
            "dead": ["21"],
            "attack_up": ["01", "02", "08", "09", "10", "11", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["01", "02", "12", "13", "14", "15", "07"]
        }

        self.image = {"x_size": 144, "y_size": 144 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init(i, j)

    # special ability: double attack
    def add_animation_attack(self):
        self.add_animation_double_attack()


class Sword(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'sword'
        self.ai = 445

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 12, "damage": [6, 9],
                                                         "health": 35, "speed": 5},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["36", "37", "38", "39", "40", "41", "42", "43"],
            "mouse_over": ["26", "27", "28", "29", "29", "28", "27", "26"],
            "standing": ["54", "30", "31", "32", "33", "32", "31", "30"],
            "getting_hit": ["46", "47", "48", "49", "50", "51"],
            "defend": ["22", "23", "24", "25", "25", "25", "25", "25", "24", "23", "22"],
            "death": ["16", "17", "18", "19", "20", "21"],
            "dead": ["21"],
            "attack_up": ["01", "02", "08", "09", "10", "11", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["01", "02", "12", "13", "14", "15", "07"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)


class RGrif(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'rgrif'
        self.ai = 488

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 9, "damage": [3, 6],
                                                         "health": 25, "speed": 9},
                                "current_health": 25, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.is_answer = float('inf')

        self.animations = {
            "moving": ["11", "12", "11", "10"],
            "mouse_over": ["01", "04", "05", "06", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "01"],
            "defend": ["01", "17", "18", "19", "19", "18", "17", "01"],
            "death": ["01", "46", "47", "48", "49", "50", "51", "52", "53"],
            "dead": ["53"],
            "attack_up": ["01", "20", "21", "22", "23", "24", "25", "26", "01"],
            "attack_straight": ["01", "27", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -10}

        self.init(i, j)

    def reset_answers(self):
        self.is_answer = float('inf')


class Griff(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'griff'
        self.ai = 351

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 8, "damage": [3, 6],
                                                         "health": 25, "speed": 6},
                                "current_health": 25, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.is_answer = 2

        self.animations = {
            "moving": ["11", "12", "11", "10"],
            "mouse_over": ["01", "04", "05", "06", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "01"],
            "defend": ["01", "17", "18", "19", "19", "18", "17", "01"],
            "death": ["01", "46", "47", "48", "49", "50", "51", "52", "53"],
            "dead": ["53"],
            "attack_up": ["01", "20", "21", "22", "23", "24", "25", "26", "01"],
            "attack_straight": ["01", "27", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init(i, j)

    def reset_answers(self):
        self.is_answer = 2


class Hcbow(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'hcbow'
        self.ai = 184

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 3, "damage": [2, 3],
                                                         "health": 10, "speed": 6},
                                "current_health": 10, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["55", "56", "57", "58", "59", "60", "61", "62"],
            "mouse_over": ["73", "74", "75", "76", "76", "76", "75", "74", "73"],
            "standing": ["00", "49", "50", "51", "52", "51", "50", "49"],
            "getting_hit": ["65", "66", "67", "68", "69", "70"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "45", "44", "43"],
            "death": ["37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["25", "26", "27", "28", "29", "30"],
            "attack_straight": ["19", "20", "21", "22", "23", "24"],
            "attack_down": ["31", "32", "33", "34", "35", "36"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 144, "y_size": 144 / 1.125, "x_shift": -5, "y_shift": 0}

        self.init(i, j)

    # special ability: double shoot
    def add_animation_shoot(self):
        self.add_animation_double_shoot_()


class Lcbow(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'lcbow'
        self.ai = 126

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 3, "damage": [2, 3],
                                                         "health": 10, "speed": 4},
                                "current_health": 10, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["55", "56", "57", "58", "59", "60", "61", "62"],
            "mouse_over": ["73", "74", "75", "76", "76", "76", "75", "74", "73"],
            "standing": ["00", "49", "50", "51", "52", "51", "50", "49"],
            "getting_hit": ["65", "66", "67", "68", "69", "70"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "47", "48"],
            "death": ["37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["25", "26", "27", "28", "29", "30"],
            "attack_straight": ["19", "20", "21", "22", "23", "24"],
            "attack_down": ["31", "32", "33", "34", "35", "36"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)


class Halbd(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'halbd'
        self.ai = 115

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 5, "damage": [2, 3],
                                                         "health": 10, "speed": 5},
                                "current_health": 10, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["056", "057", "058", "059", "059", "059", "059", "058", "057", "056"],
            "standing": ["079", "078", "077", "076", "075", "076", "077", "078", "079"],
            "getting_hit": ["044", "045", "046", "047", "048", "049"],
            "defend": ["051", "052", "053", "054", "054", "054", "054", "053", "052"],
            "death": ["061", "062", "063", "064", "065", "066", "067"],
            "dead": ["067"],
            "attack_up": ["091", "092", "093", "094", "095", "096", "097", "098"],
            "attack_straight": ["082", "083", "084", "085", "086", "087", "088", "089"],
            "attack_down": ["100", "101", "102", "103", "104", "105", "106", "107"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: Immunity to Cavalry Bonus


class Pkman(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pkman'
        self.ai = 80

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 5, "damage": [1, 3],
                                                         "health": 10, "speed": 4},
                                "current_health": 10, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["03", "04", "05", "06", "07", "08", "09", "10"],
            "mouse_over": ["56", "57", "58", "59", "59", "59", "59", "58", "57", "56"],
            "standing": ["79", "78", "77", "76", "75", "76", "77", "78", "79"],
            "getting_hit": ["44", "45", "46", "47", "48", "49"],
            "defend": ["51", "52", "53", "54", "54", "54", "54", "53", "52"],
            "death": ["61", "62", "63", "64", "65", "66", "67"],
            "dead": ["67"],
            "attack_up": ["26", "27", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["17", "18", "19", "20", "21", "22", "23", "24"],
            "attack_down": ["35", "36", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: Immunity to Cavalry Bonus
