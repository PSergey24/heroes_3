from .units import Units
from modules.states import Objects


class Ddrag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ddrag'
        self.ai = 8613

        self.characteristics = {"base_characteristics": {"attack": 27, "defense": 27, "damage": [40, 50],
                                                         "health": 250, "speed": 16},
                                "current_health": 250, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["13", "14", "13", "12"],
            "mouse_over": ["01", "04", "05", "06", "07"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01", "01"],
            "getting_hit": ["48", "49", "50", "50", "51", "52"],
            "defend": ["58", "59", "60", "60", "61", "62"],
            "death": ["48", "49", "50", "53", "54", "55", "56", "57"],
            "dead": ["57"],
            "attack_up": ["21", "22", "23", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["30", "31", "32", "33", "34", "35", "36", "37", "38"],
            "attack_down": ["39", "40", "41", "42", "43", "44", "45", "46", "47"],
            "dhex_attack_up": ["21", "22", "23", "24", "63", "64", "65", "28", "29"],
            "dhex_attack_straight": ["30", "31", "32", "66", "67", "68", "69", "37", "38"],
            "dhex_attack_down": ["39", "40", "41", "70", "71", "72", "73", "46", "47"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": 20}

        self.init(i, j)

    # todo: Immunity to all spells of levels 1-4, including positive spells.
    # todo: fire


class Gdrag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gdrag'
        self.ai = 4872

        self.characteristics = {"base_characteristics": {"attack": 18, "defense": 18, "damage": [40, 50],
                                                         "health": 180, "speed": 10},
                                "current_health": 180, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["13", "14", "13", "12"],
            "mouse_over": ["01", "04", "05", "06", "07"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["48", "49", "50", "50", "51", "52"],
            "defend": ["58", "59", "60", "60", "61", "62"],
            "death": ["48", "49", "50", "53", "54", "55", "56", "57"],
            "dead": ["57"],
            "attack_up": ["21", "22", "23", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["30", "31", "32", "33", "34", "35", "36", "37", "38"],
            "attack_down": ["39", "40", "41", "42", "43", "44", "45", "46", "47"],
            "dhex_attack_up": ["21", "22", "23", "24", "63", "64", "65", "28", "29"],
            "dhex_attack_straight": ["30", "31", "32", "66", "67", "68", "69", "37", "38"],
            "dhex_attack_down": ["39", "40", "41", "70", "71", "72", "73", "46", "47"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": 10}

        self.init(i, j)

    # todo: Immunity to all spells of levels 1-3, including positive spells.
    # todo: fire


class Wunic(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'wunic'
        self.ai = 2030

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 14, "damage": [18, 22],
                                                         "health": 110, "speed": 9},
                                "current_health": 110, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "04", "05", "06", "07"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "45", "46", "47", "48", "49", "50"],
            "defend": ["01", "19", "20", "21", "22", "23", "22", "21", "20", "19", "01"],
            "death": ["01", "51", "52", "53", "54", "55", "56", "57"],
            "dead": ["57"],
            "attack_up": ["01", "24", "25", "26", "27", "28", "29", "30", "01"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36", "37", "01"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43", "44", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -20}

        self.init(i, j)

    # todo: Blinding Strike - 20% chance, 3 step duration; no answer
    # todo: increases the magic resistance of friendly units by 20% in a one-cell radius around the unit. However, the aura does not protect the unicorns themselves.


class Unico(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'unico'
        self.ai = 1806

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 14, "damage": [18, 22],
                                                         "health": 90, "speed": 7},
                                "current_health": 90, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "04", "05", "06", "07"],
            "standing": ["01", "02", "03", "03", "03", "02", "01", "01"],
            "getting_hit": ["01", "45", "46", "47", "48", "49", "50"],
            "defend": ["01", "19", "20", "21", "22", "23", "22", "21", "20", "19", "01"],
            "death": ["01", "51", "52", "53", "54", "55", "56", "57"],
            "dead": ["57"],
            "attack_up": ["01", "24", "25", "26", "27", "28", "29", "30", "01"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36", "37", "01"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43", "44", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -5}

        self.init(i, j)

    # todo: Blinding Strike - 20% chance, 3 step duration; no answer
    # todo: increases the magic resistance of friendly units by 20% in a one-cell radius around the unit. However, the aura does not protect the unicorns themselves.


class Btree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'btree'
        self.ai = 803

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 12, "damage": [10, 14],
                                                         "health": 65, "speed": 4},
                                "current_health": 65, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "22", "23", "24", "24", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55"],
            "dead": ["55"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: the attacked unit loses the ability to move until the dendroids themselves move or are destroyed.


class Tree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'tree'
        self.ai = 517

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 12, "damage": [10, 14],
                                                         "health": 55, "speed": 3},
                                "current_health": 55, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "22", "23", "24", "24", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55"],
            "dead": ["55"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: the attacked unit loses the ability to move until the dendroids themselves move or are destroyed.


class Apegs(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'apegs'
        self.ai = 532

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 10, "damage": [5, 9],
                                                         "health": 30, "speed": 12},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "31", "30", "29"],
            "standing": ["56", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["47", "48", "49", "50", "51", "52"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["47", "48", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "13"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -15}

        self.init(i, j)

    # todo: Pegasus units increase the cost of all spells for enemy sorcerers by 2 points.


class Pegas(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pegas'
        self.ai = 518

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 8, "damage": [5, 9],
                                                         "health": 30, "speed": 8},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "31", "30", "29"],
            "standing": ["56", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["47", "48", "49", "50", "51", "52"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["47", "48", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "13"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -15}

        self.init(i, j)

    # todo: Pegasus units increase the cost of all spells for enemy sorcerers by 2 points.


class Grelf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'grelf'
        self.ai = 331

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 5, "damage": [3, 5],
                                                         "health": 15, "speed": 7},
                                "current_health": 15, "current_count": count, "current_arrows": 48,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["54", "55", "56", "57", "58", "59", "60", "61"],
            "mouse_over": ["44", "45", "46", "47", "47", "47", "47", "47", "46", "45", "44"],
            "standing": ["72", "48", "49", "50", "51", "50", "49", "48"],
            "getting_hit": ["64", "65", "66", "67", "68", "69"],
            "defend": ["40", "41", "42", "43", "43", "43", "43", "43", "42", "41", "40"],
            "death": ["64", "65", "37", "38", "39"],
            "dead": ["39"],
            "attack_up": ["19", "20", "27", "28", "29", "30", "31", "26"],
            "attack_straight": ["19", "20", "21", "22", "23", "24", "25", "26"],
            "attack_down": ["19", "20", "32", "33", "34", "35", "36", "26"],
            "shoot_up": ["01", "02", "09", "10", "11", "12", "12", "12", "12", "12", "13", "08"],
            "shoot_straight": ["01", "02", "03", "04", "05", "06", "06", "06", "06", "06", "07", "08"],
            "shoot_down": ["01", "02", "14", "15", "16", "17", "17", "17", "17", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)

    # special ability: double shoot
    def add_animation_shoot_(self):
        self.update_fight_info()

        self.add_animation(self, Objects.cursor.action)
        self.add_animation(Objects.cursor.whom_attack, "getting_hit")

        self.add_animation(self, Objects.cursor.action)
        self.add_animation(Objects.cursor.whom_attack, "getting_hit")


class Elf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'elf'
        self.ai = 234

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 5, "damage": [3, 5],
                                                         "health": 15, "speed": 6},
                                "current_health": 15, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["54", "55", "56", "57", "58", "59", "60", "61"],
            "mouse_over": ["44", "45", "46", "47", "47", "47", "47", "47", "46", "45", "44"],
            "standing": ["72", "48", "49", "50", "51", "50", "49", "48"],
            "getting_hit": ["64", "65", "66", "67", "68", "69"],
            "defend": ["40", "41", "42", "43", "43", "43", "43", "43", "42", "41", "40"],
            "death": ["64", "65", "37", "38", "39"],
            "dead": ["39"],
            "attack_up": ["19", "20", "27", "28", "29", "30", "31", "26"],
            "attack_straight": ["19", "20", "21", "22", "23", "24", "25", "26"],
            "attack_down": ["19", "20", "32", "33", "34", "35", "36", "26"],
            "shoot_up": ["01", "02", "09", "10", "11", "12", "12", "12", "12", "12", "13", "08"],
            "shoot_straight": ["01", "02", "03", "04", "05", "06", "06", "06", "06", "06", "07", "08"],
            "shoot_down": ["01", "02", "14", "15", "16", "17", "17", "17", "17", "17", "18", "08"]
        }

        self.image = {"x_size": 130, "y_size": 130 / 1.125, "x_shift": 0, "y_shift": 10}

        self.init(i, j)


class Bdwar(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'bdwar'
        self.ai = 209

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 7, "damage": [2, 4],
                                                         "health": 20, "speed": 5},
                                "current_health": 20, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["35", "36", "37", "38", "39", "40", "41", "42"],
            "mouse_over": ["25", "26", "27", "28", "27", "26", "25"],
            "standing": ["53", "29", "30", "31", "32", "31", "30", "29"],
            "getting_hit": ["45", "46", "47", "48", "49", "50"],
            "defend": ["21", "22", "23", "24", "24", "24", "24", "24", "23", "22", "21"],
            "death": ["45", "46", "17", "18", "19", "20"],
            "dead": ["20"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "13", "14", "15", "16", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": 0}

        self.init(i, j)

    # todo: Magic resistance 40%


class Dwarf(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'dwarf'
        self.ai = 138

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 7, "damage": [2, 4],
                                                         "health": 20, "speed": 3},
                                "current_health": 20, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["35", "36", "37", "38", "39", "40", "41", "42"],
            "mouse_over": ["25", "26", "27", "28", "27", "26", "25"],
            "standing": ["53", "29", "30", "31", "32", "31", "30", "29"],
            "getting_hit": ["45", "46", "47", "48", "49", "50"],
            "defend": ["21", "22", "23", "24", "24", "24", "24", "24", "23", "22", "21"],
            "death": ["45", "46", "17", "18", "19", "20"],
            "dead": ["20"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "13", "14", "15", "16", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: Magic resistance 20%


class Ecent(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ecent'
        self.ai = 138

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 3, "damage": [2, 3],
                                                         "health": 10, "speed": 8},
                                "current_health": 10, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["53", "54", "55", "56", "57", "58", "59", "60"],
            "mouse_over": ["43", "44", "45", "46", "46", "46", "45", "44", "43"],
            "standing": ["72", "47", "48", "49", "50", "49", "48", "47", "72"],
            "getting_hit": ["63", "64", "65", "66", "67", "68"],
            "defend": ["39", "40", "41", "42", "42", "42", "42", "42", "41", "40", "39"],
            "death": ["63", "64", "33", "34", "35", "36", "37", "38"],
            "dead": ["38"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "13", "14", "15", "16", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -5}

        self.init(i, j)


class Centr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'centr'
        self.ai = 100

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 3, "damage": [2, 3],
                                                         "health": 8, "speed": 6},
                                "current_health": 8, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["53", "54", "55", "56", "57", "58", "59", "60"],
            "mouse_over": ["43", "44", "45", "46"],
            "standing": ["72", "47", "48", "49", "50", "49", "48", "47"],
            "getting_hit": ["63", "64", "65", "66", "67", "68"],
            "defend": ["39", "40", "41", "42", "42", "42", "42", "42", "41", "40", "39"],
            "death": ["63", "64", "33", "34", "35", "36", "37", "38"],
            "dead": ["38"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "13", "14", "15", "16", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -5}

        self.init(i, j)
