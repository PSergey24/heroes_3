from .units import Units


class Gtita(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gtita'
        self.ai = 7500

        self.characteristics = {"base_characteristics": {"attack": 24, "defense": 24, "damage": [40, 60],
                                                         "health": 300, "speed": 11},
                                "current_health": 300, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "21", "22", "23", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"],
            "shoot_up": ["01", "57", "58", "59", "60", "61", "62"],
            "shoot_straight": ["01", "63", "64", "65", "66", "67", "68"],
            "shoot_down": ["01", "69", "70", "71", "72", "73", "74"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Mind Control Immunity – The unit is immune to mind-affecting spells.
    # todo: Hatred of Black Dragons => +50% additional attack damage.
    # todo: No penalty - fight in hand-to-hand combat at full strength.


class Ltita(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ltita'
        self.ai = 3718

        self.characteristics = {"base_characteristics": {"attack": 19, "defense": 16, "damage": [40, 60],
                                                         "health": 150, "speed": 7},
                                "current_health": 150, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "21", "22", "23", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Mind Control Immunity – The unit is immune to mind-affecting spells.


class Nagag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'nagag'
        self.ai = 2840

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 13, "damage": [30, 30],
                                                         "health": 110, "speed": 7},
                                "current_health": 110, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["30", "31", "32", "33", "34", "35", "36", "37"],
            "mouse_over": ["20", "21", "22", "23", "23", "22", "21", "20"],
            "standing": ["48", "24", "25", "26", "27", "26", "25", "24"],
            "getting_hit": ["40", "41", "42", "43", "44", "45"],
            "defend": ["16", "17", "18", "19", "19", "19", "19", "19", "18", "17", "16"],
            "death": ["40", "41", "10", "11", "12", "13", "14", "15"],
            "dead": ["15"],
            "attack_up": ["01", "02", "03", "04", "05", "06", "07", "08", "09"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08", "09"],
            "attack_down": ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 5, "y_shift": -10}

        self.init(i, j)

    # todo: attack w/o answer


class Naga(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'naga'
        self.ai = 2016

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 13, "damage": [20, 20],
                                                         "health": 110, "speed": 5},
                                "current_health": 110, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["29", "30", "31", "32", "32", "31", "30", "29"],
            "standing": ["57", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["49", "50", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 5, "y_shift": -10}

        self.init(i, j)

    # todo: attack w/o answer


class Sulta(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'sulta'
        self.ai = 942

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 12, "damage": [13, 16],
                                                         "health": 40, "speed": 11},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["15", "16", "17", "18"],
            "mouse_over": ["08", "09", "10", "11", "12", "13"],
            "standing": ["01", "02", "03", "04", "05", "06", "07"],
            "getting_hit": ["01", "46", "47", "48", "49", "50", "51"],
            "defend": ["01", "22", "23", "24", "25", "26", "27"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58"],
            "dead": ["58"],
            "attack_up": ["01", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: Hatred of Efreets and Efreet Sultans => +50% additional damage when attacking and counterattacking.
    # todo: 3 times per battle, the High Djinn can cast a random advanced buff spell on the target friendly unit.


class Genie(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'genie'
        self.ai = 884

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 12, "damage": [13, 16],
                                                         "health": 40, "speed": 7},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["15", "16", "17", "18"],
            "mouse_over": ["01", "08", "09", "10", "11", "12", "13"],
            "standing": ["01", "02", "03", "04", "05", "06", "07"],
            "getting_hit": ["01", "46", "47", "48", "49", "50", "51"],
            "defend": ["01", "22", "23", "24", "25", "26", "27"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58"],
            "dead": ["58"],
            "attack_up": ["01", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: Hatred of Efreets and Efreet Sultans => +50% additional damage when attacking and counterattacking.


class Amage(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'amage'
        self.ai = 680

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 9, "damage": [7, 9],
                                                         "health": 30, "speed": 7},
                                "current_health": 30, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["56", "57", "58", "59", "60", "61", "62", "63"],
            "mouse_over": ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"],
            "standing": ["74", "50", "51", "52", "53", "52", "51", "50"],
            "getting_hit": ["66", "67", "68", "69", "70", "71"],
            "defend": ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"],
            "death": ["34", "35", "36", "37", "38", "39", "40", "41"],
            "dead": ["41"],
            "attack_up": ["16", "17", "18", "19", "26", "27", "28", "29", "24", "25"],
            "attack_straight": ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
            "attack_down": ["16", "17", "18", "19", "30", "31", "32", "33", "24", "25"],
            "shoot_up": ["06", "07", "08", "09", "10", "10", "10", "10", "10", "09", "08", "07", "06"],
            "shoot_straight": ["01", "02", "03", "04", "05", "05", "05", "05", "05", "04", "03", "02", "01"],
            "shoot_down": ["11", "12", "13", "14", "15", "15", "15", "15", "15", "14", "13", "12", "11"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: No penalty - fight in hand-to-hand combat at full strength.
    # todo: There is no penalty when shooting through fortress walls
    # todo: reduces the cost of all spells for heroes by 2 points.


class Mage(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'mage'
        self.ai = 570

        self.characteristics = {"base_characteristics": {"attack": 11, "defense": 8, "damage": [7, 9],
                                                         "health": 25, "speed": 5},
                                "current_health": 25, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["56", "57", "58", "59", "60", "61", "62", "63"],
            "mouse_over": ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"],
            "standing": ["74", "50", "51", "52", "53", "52", "51", "50"],
            "getting_hit": ["66", "67", "68", "69", "70", "71"],
            "defend": ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"],
            "death": ["34", "35", "36", "37", "38", "39", "40", "41"],
            "dead": ["41"],
            "attack_up": ["16", "17", "18", "19", "26", "27", "28", "29", "24", "25"],
            "attack_straight": ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
            "attack_down": ["16", "17", "18", "19", "30", "31", "32", "33", "24", "25"],
            "shoot_up": ["06", "07", "08", "09", "10", "10", "10", "10", "10", "09", "08", "07", "06"],
            "shoot_straight": ["01", "02", "03", "04", "05", "05", "05", "05", "05", "04", "03", "02", "01"],
            "shoot_down": ["11", "12", "13", "14", "15", "15", "15", "15", "15", "14", "13", "12", "11"]
        }

        self.image = {"x_size": 120, "y_size": 120 / 1.125, "x_shift": 0, "y_shift": 10}

        self.init(i, j)

    # todo: No penalty - fight in hand-to-hand combat at full strength.
    # todo: There is no penalty when shooting through fortress walls
    # todo: reduces the cost of all spells for heroes by 2 points.


class Igole(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'igole'
        self.ai = 412

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 10, "damage": [4, 5],
                                                         "health": 35, "speed": 5},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "46", "47", "48", "49", "50", "51"],
            "defend": ["01", "22", "23", "24", "24", "25", "26", "27"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45"],
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)

    # todo: can not be resurrected; fighting spirit is always neutral
    # todo: Absorb Magic - Offensive spells only deal 25% damage to these units.


class Sgole(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'sgole'
        self.ai = 250

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 10, "damage": [4, 5],
                                                         "health": 30, "speed": 3},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "46", "47", "48", "49", "50", "51"],
            "defend": ["01", "22", "23", "24", "24", "25", "26", "27"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39"],
            "attack_down": ["01", "40", "41", "42", "43", "44", "45"],
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: can not be resurrected; fighting spirit is always neutral
    # todo: Absorb Magic - Offensive spells only deal 50% damage to these units.


class Ogarg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ogarg'
        self.ai = 201

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 7, "damage": [2, 3],
                                                         "health": 16, "speed": 9},
                                "current_health": 16, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46"],
            "mouse_over": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "standing": ["57", "35", "36", "37", "38", "37", "36", "35"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"],
            "death": ["49", "50", "51", "52", "53", "19", "20", "21", "22", "22", "22", "22", "22", "23", "24", "25", "26"],
            "dead": ["26"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"],
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: can not be resurrected


class Gargo(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gargo'
        self.ai = 165

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 6, "damage": [2, 3],
                                                         "health": 16, "speed": 6},
                                "current_health": 16, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46"],
            "mouse_over": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "standing": ["57", "35", "36", "37", "38", "37", "36", "35"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"],
            "death": ["49", "50", "51", "52", "53", "19", "20", "21", "22", "22", "22", "22", "22", "23", "24", "25", "26"],
            "dead": ["26"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"],
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: can not be resurrected


class GremM(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gremm'
        self.ai = 66

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 4, "damage": [1, 2],
                                                         "health": 4, "speed": 5},
                                "current_health": 4, "current_count": count, "current_arrows": 8,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17"],
            "mouse_over": ["01", "05", "06", "05", "01", "07", "08", "07", "01", "05", "06", "05", "01", "07"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "22", "23", "23", "23", "22", "21", "20"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "30", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["01", "30", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "30", "37", "38", "39", "40", "41", "42"],
            "shoot_up": ["01", "60", "61", "62", "63", "64", "65", "66", "63", "57", "58", "59", "68", "69", "70", "08", "07"],
            "shoot_straight": ["01", "01", "60", "61", "62", "63", "64", "65", "66", "63", "67", "68", "69", "70", "08", "07"],
            "shoot_down": ["01", "01", "60", "61", "62", "63", "64", "65", "66", "71", "72", "73", "69", "70", "08", "07"]
        }

        self.image = {"x_size": 190, "y_size": 190 / 1.125, "x_shift": -15, "y_shift": 0}

        self.init(i, j)


class Grema(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'grema'
        self.ai = 44

        self.characteristics = {"base_characteristics": {"attack": 3, "defense": 3, "damage": [1, 2],
                                                         "health": 4, "speed": 4},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17"],
            "mouse_over": ["01", "05", "06", "05", "01", "07", "08", "07", "01", "05", "06", "05", "01", "07"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "22", "23", "23", "23", "22", "21", "20"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "30", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["01", "30", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "30", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": 10}

        self.init(i, j)
