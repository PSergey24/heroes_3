from .units import Units
from modules.states import Objects, States


class Hdrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'hdrgn'
        self.ai = 4696

        self.characteristics = {"base_characteristics": {"attack": 19, "defense": 17, "damage": [25, 50],
                                                         "health": 200, "speed": 14},
                                "current_health": 200, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["43", "44", "45", "46", "47", "48"],
            "mouse_over": ["31", "32", "33", "34", "35", "34", "33", "32", "31"],
            "standing": ["61", "36", "37", "38", "39", "38", "37", "36"],
            "getting_hit": ["52", "53", "54", "55", "56", "57"],
            "defend": ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"],
            "death": ["19", "20", "21", "22", "23", "24", "25", "26"],
            "dead": ["26"],
            "attack_up": ["01", "08", "09", "10", "11", "12", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["13", "14", "15", "16", "17", "18", "07"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": -20}

        self.init()

        # todo: Terrifying Presence => -1 point to the fighting spirit of enemies, works even after destroying dragons
        # todo: Aging – 20% chance – the health of enemy will be reduced by 50%. Duration – 3 turns.


class Ndrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'ndrgn'
        self.ai = 3388

        self.characteristics = {"base_characteristics": {"attack": 17, "defense": 15, "damage": [25, 50],
                                                         "health": 150, "speed": 9},
                                "current_health": 150, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["43", "44", "45", "46", "47", "48"],
            "mouse_over": ["31", "32", "33", "34", "35"],
            "standing": ["61", "36", "37", "38", "39", "38", "37", "36"],
            "getting_hit": ["52", "53", "54", "55", "56", "57"],
            "defend": ["27", "28", "29", "30", "30", "30", "30", "30", "29", "28", "27"],
            "death": ["19", "20", "21", "22", "23", "24", "25", "26"],
            "dead": ["26"],
            "attack_up": ["01", "08", "09", "10", "11", "12", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["13", "14", "15", "16", "17", "18", "07"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -20}

        self.init()

        # todo: Terrifying Presence => -1 point to the fighting spirit of enemies, works even after destroying dragons


class Blord(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'blord'
        self.ai = 2382

        self.characteristics = {"base_characteristics": {"attack": 18, "defense": 18, "damage": [15, 30],
                                                         "health": 120, "speed": 9},
                                "current_health": 120, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"],
            "standing": ["62", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["49", "50", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "13"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -15}

        self.init()

        # todo: a curse - 20% probability (curse base level, 3 step)
        # todo: Mortal Strike - 20% chance to deal double damage


class Bknig(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'bknig'
        self.ai = 2087

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 16, "damage": [15, 30],
                                                         "health": 120, "speed": 7},
                                "current_health": 120, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"],
            "standing": ["58", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["49", "50", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "09", "10", "11", "12", "13"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "14", "15", "16", "17", "18"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init()

        # todo: a curse - 20% probability (curse base level, 3 step)


class PLich(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'plich'
        self.ai = 1049

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 10, "damage": [11, 15],
                                                         "health": 40, "speed": 7},
                                "current_health": 40, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False, "is_melee_penalty": True
                                }

        self.animations = {
            "moving": ["56", "57", "58", "59", "60", "61", "62", "63"],
            "mouse_over": ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"],
            "standing": ["74", "50", "51", "52", "53", "52", "51", "50"],
            "getting_hit": ["66", "67", "68", "69", "70", "71"],
            "defend": ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"],
            "death": ["35", "36", "37", "38", "39", "40", "41"],
            "dead": ["41"],
            "attack_up": ["13", "14", "21", "22", "23", "24", "25", "26"],
            "attack_straight": ["13", "14", "15", "16", "17", "18", "19", "20"],
            "attack_down": ["27", "28", "29", "30", "31", "32", "33", "34"],
            "shoot_up": ["05", "06", "07", "08", "08", "08", "08", "08", "07", "06", "05"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "03", "02", "01"],
            "shoot_down": ["09", "10", "11", "12", "12", "12", "12", "12", "11", "10", "09"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init()

        # todo: cloud of death - all teams in radius


class Lich(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'lich'
        self.ai = 848

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 10, "damage": [11, 13],
                                                         "health": 30, "speed": 6},
                                "current_health": 30, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False, "is_melee_penalty": True
                                }

        self.animations = {
            "moving": ["56", "57", "58", "59", "60", "61", "62", "63"],
            "mouse_over": ["46", "47", "48", "49", "49", "49", "49", "49", "48", "47", "46"],
            "standing": ["74", "50", "51", "52", "53", "52", "51", "50"],
            "getting_hit": ["66", "67", "68", "69", "70", "71"],
            "defend": ["42", "43", "44", "45", "45", "45", "45", "45", "44", "43", "42"],
            "death": ["35", "36", "37", "38", "39", "40", "41"],
            "dead": ["41"],
            "attack_up": ["13", "14", "21", "22", "23", "24", "25", "26"],
            "attack_straight": ["13", "14", "15", "16", "17", "18", "19", "20"],
            "attack_down": ["27", "28", "29", "30", "31", "32", "33", "34"],
            "shoot_up": ["05", "06", "07", "08", "08", "08", "08", "08", "07", "06", "05"],
            "shoot_straight": ["01", "02", "03", "04", "04", "04", "04", "04", "03", "02", "01"],
            "shoot_down": ["09", "10", "11", "12", "12", "12", "12", "12", "11", "10", "09"]
        }

        self.image = {"x_size": 120, "y_size": 120 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()

        # todo: cloud of death - all teams in radius


class Nosfe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'nosfe'
        self.ai = 783

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 10, "damage": [5, 8],
                                                         "health": 40, "speed": 9},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": True
                                }

        self.animations = {
            "moving": ["14", "15", "14", "16", "17", "16"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "22", "23", "24", "25", "25", "24", "23", "22"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 215, "y_size": 215 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init()

    # todo: health recovery - 1 point of damage = 1 point of health


class Vamp(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'vamp'
        self.ai = 555

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 9, "damage": [5, 8],
                                                         "health": 30, "speed": 6},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": True
                                }

        self.animations = {
            "moving": ["14", "15", "14", "16", "17", "16"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "22", "23", "24", "25", "25", "24", "23", "22"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 215, "y_size": 215 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init()


class Wrait(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'wrait'
        self.ai = 315

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 7, "damage": [3, 5],
                                                         "health": 18, "speed": 7},
                                "current_health": 18, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46", "47", "48"],
            "mouse_over": ["32", "33", "34", "35", "35", "35", "35", "34", "33", "32"],
            "standing": ["57", "36", "37", "38", "39", "38", "37", "36"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["28", "29", "30", "31", "31", "31", "31", "30", "29", "28"],
            "death": ["49", "50", "22", "23", "24", "25", "26", "27"],
            "dead": ["27"],
            "attack_up": ["08", "09", "10", "11", "12", "13", "14"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["15", "16", "17", "18", "19", "20", "21"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()

        # todo: Regeneration > start of it's step - full health
        # todo: Mana drain > -2 magic point, each step


class Wight(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'wight'
        self.ai = 252

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 7, "damage": [3, 5],
                                                         "health": 18, "speed": 5},
                                "current_health": 18, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["41", "42", "43", "44", "45", "46", "47", "48"],
            "mouse_over": ["32", "33", "34", "35", "35", "35", "35", "34", "33", "32"],
            "standing": ["57", "36", "37", "38", "39", "38", "37", "36"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["28", "29", "30", "31", "31", "31", "31", "30", "29", "28"],
            "death": ["49", "50", "22", "23", "24", "25", "26", "27"],
            "dead": ["27"],
            "attack_up": ["08", "09", "10", "11", "12", "13", "14"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["15", "16", "17", "18", "19", "20", "21"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()

        # todo: Regeneration > start of it's step - full health


class Zomlo(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'zomlo'
        self.ai = 128

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 5, "damage": [2, 3],
                                                         "health": 20, "speed": 4},
                                "current_health": 20, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "47", "48", "49", "50", "51", "52"],
            "defend": ["01", "23", "24", "25", "26", "27", "28"],
            "death": ["01", "53", "54", "55", "56", "57", "58", "59", "60"],
            "dead": ["60"],
            "attack_up": ["01", "29", "30", "31", "32", "33", "34"],
            "attack_straight": ["01", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "41", "42", "43", "44", "45", "46"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()


class Zombi(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'zombi'
        self.ai = 98

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 5, "damage": [2, 3],
                                                         "health": 15, "speed": 3},
                                "current_health": 15, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "47", "48", "49", "50", "51", "52"],
            "defend": ["01", "23", "24", "25", "26", "27", "28"],
            "death": ["01", "53", "54", "55", "56", "57", "58", "59", "60"],
            "dead": ["60"],
            "attack_up": ["01", "29", "30", "31", "32", "33", "34"],
            "attack_straight": ["01", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "41", "42", "43", "44", "45", "46"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init()


class Wskel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'wskel'
        self.ai = 85

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 6, "damage": [1, 3],
                                                         "health": 6, "speed": 5},
                                "current_health": 6, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"],
            "standing": ["57", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init()


class Skele(Units):

    def __init__(self, i, j, count, team):
        super().__init__(i, j, team)

        self.name = 'skele'
        self.ai = 60

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 4, "damage": [1, 3],
                                                         "health": 6, "speed": 4},
                                "current_health": 6, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False,
                                "is": "walking_dead", "is_not_answer": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["29", "30", "31", "32", "32", "32", "32", "32", "31", "30", "29"],
            "standing": ["57", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "08"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "14", "15", "16", "17", "18", "08"]
        }

        self.image = {"x_size": 144, "y_size": 144 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init()
