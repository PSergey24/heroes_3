from .units import Units
from modules.states import Objects


class Adevl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'adevl'
        self.ai = 7115

        self.characteristics = {"base_characteristics": {"attack": 26, "defense": 28, "damage": [30, 40],
                                                         "health": 200, "speed": 17},
                                "current_health": 200, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": True
                                }

        self.animations = {
            "moving": ["54"],
            "mouse_over": ["29", "30", "31", "32", "33", "32", "31", "32", "33", "32", "31", "30", "29"],
            "standing": ["54", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["46", "47", "48", "49", "50", "51"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["17", "18", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "04", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "04", "13", "14", "15", "16"],
            "start_moving": ["38", "39", "40", "41", "42", "43", "44", "45", "59", "60", "61", "62", "63", "64"],
            "stop_moving": ["65", "66", "67", "68", "69", "70", "71", "72", "73", "74"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -15}

        self.init(i, j)

        # todo: Hatred of Angels and Archangels => +50% additional attack damage.
        # todo: Failure => -1point to good fortune of all enemy warriors; works even after the destruction of devils.

    def add_animation_moving(self):
        self.add_animation(self, "start_moving")
        self.add_animation(self, "stop_moving")

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()


class Devil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'devil'
        self.ai = 5101

        self.characteristics = {"base_characteristics": {"attack": 19, "defense": 21, "damage": [30, 40],
                                                         "health": 160, "speed": 11},
                                "current_health": 160, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": True
                                }

        self.animations = {
            "moving": ["54"],
            "mouse_over": ["29", "30", "31", "32", "33", "32", "31", "32", "33", "32", "31", "30", "29"],
            "standing": ["54", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["46", "47", "48", "49", "50", "51"],
            "defend": ["25", "26", "27", "28", "28", "28", "28", "28", "27", "26", "25"],
            "death": ["17", "18", "19", "20", "21", "22", "23", "24"],
            "dead": ["24"],
            "attack_up": ["01", "02", "03", "04", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "03", "04", "13", "14", "15", "16"],
            "start_moving": ["38", "39", "40", "41", "42", "43", "44", "45", "55", "56", "57", "58", "59", "60"],
            "stop_moving": ["61", "62", "63", "64", "65", "66", "67", "68", "69", "70"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

        # todo: Hatred of Angels and Archangels => +50% additional attack damage.
        # todo: Failure => -1point to good fortune of all enemy warriors; works even after the destruction of devils.

    def add_animation_moving(self):
        self.add_animation(self, "start_moving")
        self.add_animation(self, "stop_moving")

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()


class Efres(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'efres'
        self.ai = 2343

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 14, "damage": [16, 24],
                                                         "health": 90, "speed": 13},
                                "current_health": 90, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["17", "18", "19", "20", "21", "22", "23"],
            "mouse_over": ["06", "07", "08", "09", "10"],
            "standing": ["01", "02", "03", "04", "05"],
            "getting_hit": ["26", "27", "28", "29", "30"],
            "defend": ["31", "32", "33", "34", "35", "34", "35", "34", "32", "31", "30"],
            "death": ["53", "54", "55", "56", "57", "58", "59", "60"],
            "dead": ["60"],
            "attack_up": ["36", "37", "38", "42", "43", "44", "43", "44", "42"],
            "attack_straight": ["36", "37", "38", "39", "40", "41", "40", "41", "39"],
            "attack_down": ["36", "37", "38", "39", "45", "46", "47", "46", "47", "45"],
            "dhex_attack_straight": ["48", "49", "50", "51", "52", "51", "52", "51", "50", "49", "48"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

        # todo: Immune to all Fire Magic spells
        # todo: Hatred of Djinn and High Djinn => +50% additional attack damage.
        # todo: Fire Shield – deals damage equal to 20% of that received in melee combat.


class Efree(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'efree'
        self.ai = 1670

        self.characteristics = {"base_characteristics": {"attack": 16, "defense": 12, "damage": [16, 24],
                                                         "health": 90, "speed": 9},
                                "current_health": 90, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["17", "18", "19", "20", "21", "22", "23"],
            "mouse_over": ["06", "07", "08", "09", "10"],
            "standing": ["01", "02", "03", "04", "05"],
            "getting_hit": ["26", "27", "28", "29", "30"],
            "defend": ["31", "32", "33", "34", "35", "34", "35", "34", "32", "31", "30"],
            "death": ["53", "54", "55", "56", "57", "58", "59", "60"],
            "dead": ["60"],
            "attack_up": ["36", "37", "38", "42", "43", "44", "43", "44", "42"],
            "attack_straight": ["36", "37", "38", "39", "40", "41", "40", "41", "39"],
            "attack_down": ["36", "37", "38", "39", "45", "46", "47", "46", "47", "45"],
            "dhex_attack_straight": ["48", "49", "50", "51", "52", "51", "52", "51", "50", "49", "48"]
        }

        self.image = {"x_size": 162, "y_size": 162 / 1.125, "x_shift": -10, "y_shift": 0}

        self.init(i, j)

        # todo: Immune to all Fire Magic spells
        # todo: Hatred of Djinn and High Djinn => +50% additional attack damage.


class Pfoe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pfoe'
        self.ai = 1224

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 13, "damage": [13, 17],
                                                         "health": 45, "speed": 7},
                                "current_health": 45, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["30", "31", "32", "33", "32", "33", "32", "33", "32", "31", "30"],
            "standing": ["64", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["26", "27", "28", "29", "29", "29", "29", "29", "28", "27", "26"],
            "death": ["21", "22", "23", "24", "25"],
            "dead": ["25"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "14"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "15", "16", "17", "18", "19", "20"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: Raising Demons


class Pfien(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pfien'
        self.ai = 765

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 13, "damage": [13, 17],
                                                         "health": 45, "speed": 6},
                                "current_health": 45, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["30", "31", "32", "33", "32", "33", "32", "33", "32", "31", "30"],
            "standing": ["58", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["26", "27", "28", "29", "29", "29", "29", "29", "28", "27", "26"],
            "death": ["21", "22", "23", "24", "25"],
            "dead": ["25"],
            "attack_up": ["01", "02", "09", "10", "11", "12", "13", "14"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["01", "02", "15", "16", "17", "18", "19", "20"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)


class Thdem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'thdem'
        self.ai = 480

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 10, "damage": [7, 9],
                                                         "health": 40, "speed": 6},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "21", "22", "23", "24", "24", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Ohdem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ohdem'
        self.ai = 445

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 10, "damage": [7, 9],
                                                         "health": 35, "speed": 5},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05", "01"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "21", "22", "23", "24", "24", "24", "23", "22", "21"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -15}

        self.init(i, j)


class Cerbu(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'cerbu'
        self.ai = 392

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 8, "damage": [2, 7],
                                                         "health": 25, "speed": 8},
                                "current_health": 25, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "19", "20", "21", "22", "21", "20", "19"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "23", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["01", "30", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 215, "y_size": 215 / 1.125, "x_shift": 0, "y_shift": 0}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()

    # todo: attack all units in 3 cells before heads


class Hhoun(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'hhoun'
        self.ai = 357

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 6, "damage": [2, 7],
                                                         "health": 25, "speed": 7},
                                "current_health": 25, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "19", "20", "21", "22", "21", "20", "19"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "23", "24", "25", "26", "27", "28", "29"],
            "attack_straight": ["01", "30", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 215, "y_size": 215 / 1.125, "x_shift": 0, "y_shift": -15}

        self.init(i, j)


class Magog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'magog'
        self.ai = 240

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 4, "damage": [2, 4],
                                                         "health": 13, "speed": 6},
                                "current_health": 13, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "09", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "03", "02"],
            "getting_hit": ["01", "53", "54", "55", "56", "57", "58"],
            "defend": ["01", "21", "22", "23", "24", "25", "26"],
            "death": ["01", "59", "60", "61", "62", "63", "64", "63", "64"],
            "dead": ["64"],
            "attack_up": ["01", "38", "39", "30", "27", "28", "29", "34"],
            "attack_straight": ["01", "38", "39", "40", "35", "36", "37", "44"],
            "attack_down": ["01", "38", "39", "40", "48", "45", "46", "47", "52"],
            "shoot_up": ["01", "38", "39", "30", "31", "32", "33", "34"],
            "shoot_straight": ["01", "38", "39", "40", "41", "42", "43", "44"],
            "shoot_down": ["01", "38", "39", "40", "48", "49", "50", "51", "52"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Fireball attack - damage not only to the target unit, but to all units within a radius of cell


class Gog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gog'
        self.ai = 159

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 4, "damage": [2, 4],
                                                         "health": 13, "speed": 4},
                                "current_health": 13, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["05", "06", "07", "08", "09", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "03", "02"],
            "getting_hit": ["01", "53", "54", "55", "56", "57", "58"],
            "defend": ["01", "21", "22", "23", "24", "25", "26"],
            "death": ["01", "59", "60", "61", "62", "63", "64", "63", "64"],
            "dead": ["64"],
            "attack_up": ["01", "38", "39", "30", "27", "28", "29", "34"],
            "attack_straight": ["01", "38", "39", "40", "35", "36", "37", "44"],
            "attack_down": ["01", "38", "39", "40", "48", "45", "46", "47", "52"],
            "shoot_up": ["01", "38", "39", "30", "31", "32", "33", "34"],
            "shoot_straight": ["01", "38", "39", "40", "41", "42", "43", "44"],
            "shoot_down": ["01", "38", "39", "40", "48", "49", "50", "51", "52"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Famil(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'famil'
        self.ai = 60

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 4, "damage": [1, 2],
                                                         "health": 4, "speed": 7},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "21", "22", "23", "24"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: Mana Steal – once turn, units transfer 20% of the mana spent by an enemy hero on a spell to a friendly hero.


class Imp(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'imp'
        self.ai = 50

        self.characteristics = {"base_characteristics": {"attack": 2, "defense": 3, "damage": [1, 2],
                                                         "health": 4, "speed": 5},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "20", "21", "21", "22", "23", "24"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)
