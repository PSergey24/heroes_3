from .units import Units
from modules.states import Objects


class BDragon(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'bdrgn'
        self.ai = 8721

        self.characteristics = {"base_characteristics": {"attack": 25, "defense": 25, "damage": [40, 50],
                                                         "health": 300, "speed": 15},
                                "current_health": 300, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "11", "10"],
            "mouse_over": ["01", "04", "05", "06", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "49", "50", "51", "52", "53", "01"],
            "defend": ["01", "20", "21", "22", "23", "23", "24", "25", "01"],
            "death": ["01", "49", "50", "51", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "32", "33", "01"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "01"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45", "46", "47", "48", "01"],
            "dhex_attack_up": ["01", "26", "27", "28", "60", "61", "62", "63", "33", "01"],
            "dhex_attack_straight": ["01", "64", "65", "66", "67", "68", "69", "01"],
            "dhex_attack_down": ["01", "40", "41", "42", "70", "71", "72", "73", "47", "48", "01"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": -5}

        self.init(i, j)

    # todo: Dragon's Breath - the attack behind
    # todo: Immunity to all magic
    # todo: Titan Hatred => +50% additional attack damage


class Rdrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'rdrgn'
        self.ai = 4702

        self.characteristics = {"base_characteristics": {"attack": 19, "defense": 19, "damage": [40, 50],
                                                         "health": 180, "speed": 11},
                                "current_health": 180, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "11", "10"],
            "mouse_over": ["01", "04", "05", "06", "01"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "49", "50", "51", "52", "53", "01"],
            "defend": ["01", "20", "21", "22", "23", "23", "24", "25", "01"],
            "death": ["01", "49", "50", "51", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "32", "33", "01"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "01"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45", "46", "47", "48", "01"],
            "dhex_attack_up": ["01", "26", "27", "28", "60", "61", "62", "63", "33", "01"],
            "dhex_attack_straight": ["01", "64", "65", "66", "67", "68", "69", "01"],
            "dhex_attack_down": ["01", "40", "41", "42", "70", "71", "72", "73", "47", "48", "01"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": -5}

        self.init(i, j)

    # todo: Dragon's Breath - the attack behind
    # todo: Immunity to all spells of levels 1-3, including positive spells.


class Cmcor(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'cmcor'
        self.ai = 1589

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 14, "damage": [14, 20],
                                                         "health": 80, "speed": 11},
                                "current_health": 80, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["58", "59", "60", "61", "62", "63"],
            "mouse_over": ["47", "48", "49", "50", "50", "49", "48", "47"],
            "standing": ["76", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["67", "68", "69", "70", "71", "72"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "46", "45", "44", "43"],
            "death": ["67", "68", "37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init(i, j)

    # todo: Paralyzing Sting - 20% chance, 3 duration, -25% attack


class Mcore(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'mcore'
        self.ai = 1547

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 13, "damage": [14, 20],
                                                         "health": 80, "speed": 7},
                                "current_health": 80, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["58", "59", "60", "61", "62", "63"],
            "mouse_over": ["47", "48", "49", "50", "50", "49", "48", "47"],
            "standing": ["76", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["67", "68", "69", "70", "71", "72"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "46", "45", "44", "43"],
            "death": ["67", "68", "37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -15}

        self.init(i, j)


class Minok(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'minok'
        self.ai = 1068

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 15, "damage": [12, 20],
                                                         "health": 50, "speed": 8},
                                "current_health": 50, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["59", "05", "06", "07", "08", "59"],
            "standing": ["59", "02", "03", "04", "04", "03", "02", "59"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "46"],
            "defend": ["01", "18", "19", "19", "20", "20", "21", "01"],
            "death": ["01", "47", "48", "49", "50", "51", "52"],
            "dead": ["52"],
            "attack_up": ["01", "22", "23", "24", "25", "26", "27", "01"],
            "attack_straight": ["01", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)

    # todo: Bravery – unit morale never drops below +1


class Minot(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'minot'
        self.ai = 835

        self.characteristics = {"base_characteristics": {"attack": 14, "defense": 12, "damage": [12, 20],
                                                         "health": 50, "speed": 6},
                                "current_health": 50, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["53", "05", "06", "07", "08", "53"],
            "standing": ["53", "02", "03", "04", "04", "03", "02", "53"],
            "getting_hit": ["01", "41", "42", "43", "44", "45", "46", "01"],
            "defend": ["01", "18", "19", "19", "20", "20", "21", "01"],
            "death": ["01", "47", "48", "49", "50", "51", "52"],
            "dead": ["52"],
            "attack_up": ["01", "22", "23", "24", "25", "26", "27", "01"],
            "attack_straight": ["01", "28", "29", "30", "31", "32", "33", "01"],
            "attack_down": ["01", "34", "35", "36", "37", "38", "39", "40", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)

    # todo: Bravery – unit morale never drops below +1


class Meduq(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'meduq'
        self.ai = 577

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 10, "damage": [6, 8],
                                                         "health": 30, "speed": 6},
                                "current_health": 30, "current_count": count, "current_arrows": 8,
                                "is_double": True, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["57", "58", "59", "60", "61", "62", "63", "64"],
            "mouse_over": ["47", "48", "49", "50", "50", "50", "50", "49", "48", "47"],
            "standing": ["00", "51", "52", "53", "54", "53", "52", "51"],
            "getting_hit": ["67", "68", "69", "70", "71", "72"],
            "defend": ["43", "44", "45", "46", "46", "46", "46", "45", "44", "43"],
            "death": ["67", "68", "37", "38", "39", "40", "41", "42"],
            "dead": ["42"],
            "attack_up": ["25", "26", "27", "28", "28", "28", "28", "28", "29", "30"],
            "attack_straight": ["19", "20", "21", "22", "22", "22", "22", "22", "23", "24"],
            "attack_down": ["31", "32", "33", "33", "34", "34", "34", "34", "34", "35", "36"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -5}

        self.init(i, j)

    # todo: No melee penalty
    # todo: Petrification - 20% chance, duration 3 step, -50% attack after


class Medus(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'medus'
        self.ai = 517

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 9, "damage": [6, 8],
                                                         "health": 25, "speed": 5},
                                "current_health": 25, "current_count": count, "current_arrows": 4,
                                "is_double": True, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["51", "52", "53", "54", "55", "56", "57"],
            "mouse_over": ["41", "42", "43", "44", "44", "44", "44", "43", "42", "41"],
            "standing": ["00", "45", "46", "47", "48", "47", "46", "45"],
            "getting_hit": ["61", "62", "63", "64", "65", "66"],
            "defend": ["37", "38", "39", "40", "40", "40", "40", "39", "38", "37"],
            "death": ["61", "62", "31", "32", "33", "34", "35", "36"],
            "dead": ["36"],
            "attack_up": ["23", "24", "25", "26", "26", "26", "26", "26", "25", "24", "23"],
            "attack_straight": ["19", "20", "21", "22", "22", "22", "22", "22", "21", "20", "19"],
            "attack_down": ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"],
            "shoot_up": ["07", "08", "09", "10", "10", "10", "10", "10", "11", "12"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "05", "06"],
            "shoot_down": ["13", "14", "15", "16", "16", "16", "16", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init(i, j)

    # todo: No melee penalty
    # todo: Petrification - 20% chance, duration 3 step, -50% attack after


class Eveye(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'eveye'
        self.ai = 367

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 8, "damage": [3, 5],
                                                         "health": 22, "speed": 7},
                                "current_health": 22, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["31", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["28", "29", "30"],
            "standing": ["31", "32", "33", "34", "33", "32", "31"],
            "getting_hit": ["51", "52", "53", "54", "55", "56"],
            "defend": ["24", "25", "26", "27", "27", "27", "27", "27", "26", "25", "24"],
            "death": ["19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["07", "08", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "02"],
            "attack_down": ["13", "14", "15", "16", "17", "18", "14"],
            "shoot_up": ["71", "72", "72", "72", "72", "73", "74", "75"],
            "shoot_straight": ["66", "67", "68", "68", "68", "69", "70"],
            "shoot_down": ["76", "77", "78", "78", "78", "79", "80"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: No melee penalty


class Behol(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'behol'
        self.ai = 336

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 7, "damage": [3, 5],
                                                         "health": 22, "speed": 5},
                                "current_health": 22, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["31", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["28", "29", "30"],
            "standing": ["31", "32", "33", "34", "33", "32", "31"],
            "getting_hit": ["51", "52", "53", "54", "55", "56"],
            "defend": ["24", "25", "26", "27", "27", "27", "27", "27", "26", "25", "24"],
            "death": ["19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["07", "08", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "02"],
            "attack_down": ["13", "14", "15", "16", "17", "18", "14"],
            "shoot_up": ["71", "72", "72", "72", "72", "73", "74", "75"],
            "shoot_straight": ["66", "67", "68", "68", "68", "69", "70"],
            "shoot_down": ["76", "77", "78", "78", "78", "79", "80"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: No melee penalty


class Harph(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'harph'
        self.ai = 238

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 6, "damage": [1, 4],
                                                         "health": 14, "speed": 9},
                                "current_health": 14, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.status = {"destination_back": [0, 0]}

        self.animations = {
            "moving": ["54", "55", "56", "57", "58", "59", "60"],
            "mouse_over": ["42", "43", "44", "45", "46", "45", "46", "45", "44", "43", "42"],
            "standing": ["47", "48", "49", "50", "49", "48", "47"],
            "getting_hit": ["66", "68", "67", "65", "64", "21"],
            "defend": ["35", "36", "37", "38", "39", "40", "41", "21"],
            "death": ["28", "29", "30", "31", "32", "33", "34"],
            "dead": ["34"],
            "attack_up": ["21", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"],
            "attack_straight": ["21", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "21"],
            "attack_down": ["21", "22", "23", "24", "26", "27", "26", "25", "24", "22"],
            "start_moving": ["51", "52", "53"],
            "stop_moving": ["61", "62", "63"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)

    def reset_moving(self):
        self.reset_field()
        self.init_hex(Objects.cursor.destination_point[0], Objects.cursor.destination_point[1])
        self.init_field()
        self.reset_cursor()

    def reset_cursor(self):
        Objects.cursor.destination_point = self.status["destination_back"]
        Objects.cursor.offset = tuple(self.status["destination_back"])
        Objects.cursor.point_attack = None
        Objects.cursor.whom_attack = None

    def add_moving_and_attack_(self):
        self.add_animation_moving_()
        self.add_animation_attack_()
        self.add_animation_moving_back_()

    def add_animation_attack_(self):
        self.update_fight_info()
        self.add_animation(self, Objects.cursor.action)
        self.add_animation(Objects.cursor.whom_attack, "getting_hit")

    def add_animation_moving_back_(self):
        self.status["destination_back"] = self.hex[0]
        self.add_animation_moving_()


class Harpy(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'harpy'
        self.ai = 154

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 5, "damage": [1, 4],
                                                         "health": 14, "speed": 6},
                                "current_health": 14, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.status = {"destination_back": [0, 0]}

        self.animations = {
            "moving": ["54", "55", "56", "57", "58", "59", "60"],
            "mouse_over": ["42", "43", "44", "45", "46", "45", "46", "45", "44", "43", "42"],
            "standing": ["47", "48", "49", "50", "49", "48", "47"],
            "getting_hit": ["66", "68", "67", "65", "64", "21"],
            "defend": ["35", "36", "37", "38", "39", "40", "41", "21"],
            "death": ["28", "29", "30", "31", "32", "33", "34"],
            "dead": ["34"],
            "attack_up": ["21", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"],
            "attack_straight": ["21", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "21"],
            "attack_down": ["21", "22", "23", "24", "26", "27", "26", "25", "24", "22"],
            "start_moving": ["21", "51", "52", "53"],
            "stop_moving": ["54", "61", "62", "63", "21"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -5}

        self.init(i, j)

    def reset_moving(self):
        self.reset_field()
        self.init_hex(Objects.cursor.destination_point[0], Objects.cursor.destination_point[1])
        self.init_field()
        self.reset_cursor()

    def reset_cursor(self):
        Objects.cursor.destination_point = self.status["destination_back"]
        Objects.cursor.offset = tuple(self.status["destination_back"])
        Objects.cursor.point_attack = None
        Objects.cursor.whom_attack = None

    def add_moving_and_attack_(self):
        self.add_animation_moving_()
        self.add_animation_attack_()
        self.add_animation_moving_back_()

    def add_animation_moving_back_(self):
        self.status["destination_back"] = self.hex[0]
        self.add_animation_moving_()


class Itrog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'itrog'
        self.ai = 84

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 4, "damage": [1, 3],
                                                         "health": 6, "speed": 5},
                                "current_health": 6, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["32", "33", "34", "35", "36", "37", "38"],
            "mouse_over": ["04", "05", "06", "07", "06", "05", "04"],
            "standing": ["00", "01", "02", "03", "02", "01"],
            "getting_hit": ["20", "21", "22", "23", "24", "25"],
            "defend": ["26", "27", "28", "29", "30", "31"],
            "death": ["20", "21", "22", "44", "45", "46", "47", "48", "47"],
            "dead": ["47"],
            "attack_up": ["39", "40", "41", "42", "43", "44", "40", "39"],
            "attack_straight": ["08", "09", "10", "11", "12", "13", "12", "11", "10", "09"],
            "attack_down": ["14", "15", "16", "17", "18", "19", "18", "17"]
        }

        self.image = {"x_size": 196, "y_size": 196 / 1.125, "x_shift": -15, "y_shift": 0}

        self.init(i, j)

    # todo: Immune to the Blind and Petrify spells of jellyfish and basilisks, as well as to the Death Glare of Gorgons


class Trogl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'trogl'
        self.ai = 59

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 3, "damage": [1, 3],
                                                         "health": 4, "speed": 3},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["35", "36", "37", "38", "39", "40", "41"],
            "mouse_over": ["47", "48", "49", "50", "49", "48", "47"],
            "standing": ["01", "02", "03", "02"],
            "getting_hit": ["04", "05", "06", "07", "08", "09"],
            "defend": ["24", "25", "26", "27", "28", "29"],
            "death": ["04", "07", "30", "31", "32", "33", "34"],
            "dead": ["34"],
            "attack_up": ["42", "43", "44", "45", "46", "44", "43", "42"],
            "attack_straight": ["12", "13", "14", "15", "16", "17", "16", "15", "14", "13"],
            "attack_down": ["18", "19", "20", "21", "22", "23", "22", "21"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Immune to the Blind and Petrify spells of jellyfish and basilisks, as well as to the Death Glare of Gorgons
