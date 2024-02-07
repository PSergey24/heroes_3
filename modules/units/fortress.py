from .units import Units
from modules.states import Objects, States


class Chydr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'chydr'
        self.ai = 5931

        self.characteristics = {"base_characteristics": {"attack": 18, "defense": 20, "damage": [25, 45],
                                                         "health": 250, "speed": 7},
                                "current_health": 250, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": True
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["28", "29", "30", "31", "32", "33"],
            "standing": ["58", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["24", "25", "26", "27", "27", "27", "27", "26", "25", "24"],
            "death": ["50", "51", "18", "19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "attack_down": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_up": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_down": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init()

    # special ability: circular attack
    def get_defenders(self):
        return self.to_circular_attack()


class Hydra(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'hydra'
        self.ai = 4120

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 18, "damage": [25, 45],
                                                         "health": 175, "speed": 5},
                                "current_health": 175, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": True
                                }

        self.animations = {
            "moving": ["38", "39", "40", "41", "42", "43", "44", "45"],
            "mouse_over": ["28", "29", "30", "31", "30", "29", "28"],
            "standing": ["56", "32", "33", "34", "35", "34", "33", "32"],
            "getting_hit": ["48", "49", "50", "51", "52", "53"],
            "defend": ["24", "25", "26", "27", "27", "27", "27", "26", "25", "24"],
            "death": ["48", "49", "18", "19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "attack_down": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_up": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
            "dhex_attack_down": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
        }

        self.image = {"x_size": 144, "y_size": 144 / 1.125, "x_shift": 30, "y_shift": 0}

        self.init()

    # special ability: circular attack
    def get_defenders(self):
        return self.to_circular_attack()


class Wyvmn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'wyvmn'
        self.ai = 1518

        self.characteristics = {"base_characteristics": {"attack": 14, "defense": 14, "damage": [18, 22],
                                                         "health": 70, "speed": 11},
                                "current_health": 70, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["12", "10", "11", "10", "12", "13"],
            "mouse_over": ["01", "04", "05", "06", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49", "44", "01"],
            "defend": ["01", "20", "21", "22", "23", "24", "25", "01"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "01"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37", "01"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init()

    # todo: Poisoning - 30% chance - the health of each of them will be reduced by 10% of the original every turn for 3 turns. Only affects living beings.


class Wyver(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'wyver'
        self.ai = 1350

        self.characteristics = {"base_characteristics": {"attack": 14, "defense": 14, "damage": [14, 18],
                                                         "health": 70, "speed": 7},
                                "current_health": 70, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["12", "10", "11", "10", "12", "13"],
            "mouse_over": ["01", "04", "05", "06", "06", "05", "04", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49", "44", "01"],
            "defend": ["01", "20", "21", "22", "23", "24", "25", "01"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "01"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37", "01"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init()


class Bgorg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'bgorg'
        self.ai = 1028

        self.characteristics = {"base_characteristics": {"attack": 11, "defense": 16, "damage": [12, 16],
                                                         "health": 70, "speed": 6},
                                "current_health": 70, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["06", "07", "08", "09"],
            "standing": ["01", "02", "03", "04", "05", "04", "03", "02"],
            "getting_hit": ["19", "20", "21", "22", "23", "24"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["50", "51", "52", "53", "54"],
            "dead": ["54"],
            "attack_up": ["36", "37", "38", "39", "40", "41", "42", "43"],
            "attack_straight": ["29", "30", "31", "32", "33", "34", "35"],
            "attack_down": ["44", "45", "46", "47", "48", "49", "46", "45", "44"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()

    # todo: Death glare – additionally destroy N enemy. Calculation – 1 destroyed unit for every 10 gorgons.


class Cgorg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'cgorg'
        self.ai = 890

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 14, "damage": [12, 16],
                                                         "health": 70, "speed": 5},
                                "current_health": 70, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["06", "07", "08", "09"],
            "standing": ["01", "02", "03", "04", "05", "04", "03", "02"],
            "getting_hit": ["19", "20", "21", "22", "23", "24"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["48", "49", "50", "51", "52"],
            "dead": ["52"],
            "attack_up": ["35", "36", "37", "38", "39", "40", "41"],
            "attack_straight": ["29", "30", "31", "32", "33", "34"],
            "attack_down": ["42", "43", "44", "45", "46", "47"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()


class Gbasi(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'gbasi'
        self.ai = 714

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 12, "damage": [6, 10],
                                                         "health": 40, "speed": 7},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["51", "52", "53", "54", "55", "56", "57", "58"],
            "mouse_over": ["41", "42", "43", "44"],
            "standing": ["69", "45", "46", "47", "48", "47", "46", "45"],
            "getting_hit": ["61", "62", "63", "64", "65", "66"],
            "defend": ["37", "38", "39", "40", "40", "40", "40", "39", "38", "37"],
            "death": ["31", "32", "33", "34", "35", "36"],
            "dead": ["36"],
            "attack_up": ["07", "08", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06"],
            "attack_down": ["13", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()

    # todo: 20% chance Petrification for 3 turns; and if they were previously attacked, then the damage inflicted on such units will be reduced – 50% of the original


class Basil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'basil'
        self.ai = 552

        self.characteristics = {"base_characteristics": {"attack": 11, "defense": 11, "damage": [6, 10],
                                                         "health": 35, "speed": 5},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["51", "52", "53", "54", "55", "56", "57", "58"],
            "mouse_over": ["41", "42", "43", "44"],
            "standing": ["69", "45", "46", "47", "48", "47", "46", "45"],
            "getting_hit": ["61", "62", "63", "64", "65", "66"],
            "defend": ["37", "38", "39", "40", "40", "40", "40", "39", "38", "37"],
            "death": ["31", "32", "33", "34", "35", "36"],
            "dead": ["36"],
            "attack_up": ["07", "08", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06"],
            "attack_down": ["13", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()

    # todo: 20% chance Petrification for 3 turns; and if they were previously attacked, then the damage inflicted on such units will be reduced – 50% of the original


class Drfir(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'drfir'
        self.ai = 312

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 10, "damage": [2, 5],
                                                         "health": 20, "speed": 13},
                                "current_health": 20, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16"],
            "mouse_over": ["01", "06", "07", "08", "09"],
            "standing": ["01", "02", "03", "03", "04", "05"],
            "getting_hit": ["01", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "22", "23", "24", "25"],
            "death": ["01", "49", "50", "51", "52", "53", "54"],
            "dead": ["54"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init()

    # todo: Dispel Magic – When attacking, units remove all positive spell effects from the enemy unit.
    # todo: weakness - -6 to the attack indicator. Duration – 3 turns.


class Drfly(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'drfly'
        self.ai = 268

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 9, "damage": [2, 5],
                                                         "health": 20, "speed": 9},
                                "current_health": 20, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16"],
            "mouse_over": ["01", "06", "07", "08", "09"],
            "standing": ["01", "02", "03", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "22", "23", "24", "25"],
            "death": ["01", "49", "50", "51", "52", "53", "54"],
            "dead": ["54"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init()

    # todo: Dispel Magic – When attacking, units remove all positive spell effects from the enemy unit.


class Aliza(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'aliza'
        self.ai = 156

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 8, "damage": [2, 5],
                                                         "health": 15, "speed": 5},
                                "current_health": 15, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["54", "55", "56", "57", "58", "59", "60"],
            "mouse_over": ["44", "45", "46", "47", "47", "47", "47", "46", "45", "44"],
            "standing": ["72", "48", "49", "50", "51", "50", "49", "48"],
            "getting_hit": ["64", "65", "66", "67", "68", "69"],
            "defend": ["40", "41", "42", "43", "43", "43", "43", "42", "41", "40"],
            "death": ["64", "65", "34", "35", "36", "37", "38", "39"],
            "dead": ["39"],
            "attack_up": ["19", "20", "21", "22", "28", "29", "30", "26", "27"],
            "attack_straight": ["19", "20", "21", "22", "23", "24", "25", "26", "27"],
            "attack_down": ["19", "20", "21", "22", "31", "32", "33", "26", "27"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()


class Pliza(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'pliza'
        self.ai = 126

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 6, "damage": [2, 3],
                                                         "health": 14, "speed": 4},
                                "current_health": 14, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["57", "58", "59", "60", "61", "62", "63"],
            "mouse_over": ["47", "48", "49", "50", "50", "50", "50", "49", "48", "47"],
            "standing": ["75", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["67", "68", "69", "70", "71", "72"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "45", "44", "43"],
            "death": ["67", "68", "37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["25", "26", "27", "28", "29", "30"],
            "attack_straight": ["19", "20", "21", "22", "23", "24"],
            "attack_down": ["31", "32", "33", "34", "35", "36"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()


class Gnolm(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'gnolm'
        self.ai = 90

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 6, "damage": [2, 3],
                                                         "health": 6, "speed": 5},
                                "current_health": 6, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["29", "30", "31", "32", "33", "32", "33", "32", "33", "32", "33", "32", "31", "30", "29"],
            "standing": ["58", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init()


class Gnoll(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'gnoll'
        self.ai = 56

        self.characteristics = {"base_characteristics": {"attack": 3, "defense": 5, "damage": [2, 3],
                                                         "health": 6, "speed": 4},
                                "current_health": 6, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is_not_answer": False
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["29", "30", "31", "32", "33", "32", "33", "32", "33", "32", "33", "32", "31", "30", "29"],
            "standing": ["58", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init()
