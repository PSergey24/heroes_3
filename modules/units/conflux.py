from .units import Units
from modules.states import Objects


class Phx(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'phx'
        self.ai = 6721

        self.characteristics = {"base_characteristics": {"attack": 21, "defense": 18, "damage": [30, 40],
                                                         "health": 200, "speed": 21},
                                "current_health": 200, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["51", "52", "53", "54", "55", "56"],
            "mouse_over": ["36", "37", "38", "39", "40", "39", "38", "37", "36"],
            "standing": ["66", "41", "42", "43", "44", "45", "46", "47"],
            "getting_hit": ["57", "58", "59", "60", "61", "62"],
            "defend": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "death": ["24", "25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["01", "09", "10", "11", "12", "13", "12", "13", "12", "13", "14", "15"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "05", "06", "05", "06", "07", "08"],
            "attack_down": ["16", "17", "18", "19", "20", "21", "20", "21", "20", "21", "22", "23"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -15, "y_shift": -20}

        self.init(i, j)

    # todo: Dragon's Breath - full damage is caused to both the target itself and the unit directly behind it
    # todo: ability to be revived of a squad of 20% of its original size. 20% chance


class Fbird(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'fbird'
        self.ai = 4336

        self.characteristics = {"base_characteristics": {"attack": 18, "defense": 18, "damage": [30, 40],
                                                         "health": 150, "speed": 15},
                                "current_health": 150, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["45", "46", "47", "48", "49", "50"],
            "mouse_over": ["35", "36", "37", "38", "38", "37", "36", "35"],
            "standing": ["63", "39", "40", "41", "42", "41", "40", "39"],
            "getting_hit": ["54", "55", "56", "57", "58", "59"],
            "defend": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "death": ["24", "25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["01", "09", "10", "11", "12", "13", "12", "13", "12", "13", "14", "15"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "05", "06", "05", "06", "07", "08"],
            "attack_down": ["16", "17", "18", "19", "20", "21", "20", "21", "20", "21", "22", "23"]
        }

        self.image = {"x_size": 268, "y_size": 268 / 1.125, "x_shift": -5, "y_shift": -15}

        self.init(i, j)

    # todo: Dragon's Breath - full damage is caused to both the target itself and the unit directly behind it.
    # todo: Immunity to all Fire magic spells


class Magel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'magel'
        self.ai = 2012

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 13, "damage": [15, 25],
                                                         "health": 80, "speed": 9},
                                "current_health": 80, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["30", "31", "32", "33", "34", "35", "36", "37"],
            "mouse_over": ["17", "18", "19", "20", "21", "22", "23"],
            "standing": ["48", "24", "25", "26", "27", "26", "25", "24"],
            "getting_hit": ["40", "41", "42", "43", "44", "45"],
            "defend": ["11", "12", "13", "14", "15", "16", "16", "16", "15", "14", "13", "12", "11"],
            "death": ["05", "06", "07", "08", "09", "10"],
            "dead": ["10"],
            "attack_up": ["01", "02", "03", "04", "04", "04", "03", "02", "01"],
            "attack_straight": ["01", "02", "03", "04", "04", "04", "03", "02", "01"],
            "attack_down": ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -20}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Circular attack - attacks all nearby enemy units.
    # todo: magic Attack - Thought elementals only deal 50% damage to black dragons and other magical elementals.


class Psyel(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'psyel'
        self.ai = 1669

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 13, "damage": [10, 20],
                                                         "health": 75, "speed": 7},
                                "current_health": 75, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["30", "31", "32", "33", "34", "35", "36", "37"],
            "mouse_over": ["17", "18", "19", "20", "21", "22", "23"],
            "standing": ["48", "24", "25", "26", "27", "26", "25", "24"],
            "getting_hit": ["40", "41", "42", "43", "44", "45"],
            "defend": ["11", "12", "13", "14", "15", "16", "16", "16", "15", "14", "13", "12", "11"],
            "death": ["05", "06", "07", "08", "09", "10"],
            "dead": ["10"],
            "attack_up": ["01", "02", "03", "04", "04", "04", "03", "02", "01"],
            "attack_straight": ["01", "02", "03", "04", "04", "04", "03", "02", "01"],
            "attack_down": ["01", "02", "03", "04", "04", "04", "03", "02", "01"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -20}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Circular attack - attacks all nearby enemy units.
    # todo: Psychic Attack - Thought elementals only deal 50% damage to all units immune to mind affecting spells.


class Ston(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ston'
        self.ai = 490

        self.characteristics = {"base_characteristics": {"attack": 11, "defense": 11, "damage": [6, 10],
                                                         "health": 40, "speed": 6},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["45", "46", "47", "48", "49", "50", "51", "52"],
            "mouse_over": ["30", "31", "32", "33", "34", "35", "36", "37", "38"],
            "standing": ["71", "39", "40", "41", "42", "41", "40", "39"],
            "getting_hit": ["55", "56", "57", "58", "59", "60"],
            "defend": ["24", "25", "26", "27", "28", "29", "28", "27", "26", "25", "24"],
            "death": ["18", "19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["01", "08", "09", "10", "11", "12", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["01", "13", "14", "15", "16", "17", "07"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Meteor Rain
    # todo: Immunity to the Lightning, Chain Lightning, Armageddon.
    # todo: double damage to air elementals
    # todo: Earth Mage: units are able to cast the spell Protection from Earth, which lasts for 3 turns.


class Eelem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'eelem'
        self.ai = 330

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 10, "damage": [4, 8],
                                                         "health": 40, "speed": 4},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "mouse_over": ["28", "29", "30", "31", "32", "29", "30", "31", "32"],
            "standing": ["57", "33", "34", "35", "36", "35", "34", "33"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["24", "25", "26", "27", "27", "27", "27", "27", "26", "25", "24"],
            "death": ["18", "19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["01", "08", "09", "10", "11", "12", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07"],
            "attack_down": ["01", "13", "14", "15", "16", "17", "07"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Meteor Rain
    # todo: Immunity to the Lightning, Chain Lightning, Armageddon.
    # todo: double damage to air elementals


class Nrg(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'nrg'
        self.ai = 470

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 8, "damage": [4, 6],
                                                         "health": 35, "speed": 8},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": True
                                }

        self.animations = {
            "moving": ["56", "57", "58", "59", "60", "61", "62"],
            "mouse_over": ["41", "42", "43", "44", "45", "46"],
            "standing": ["80", "47", "48", "49", "50", "51", "52"],
            "getting_hit": ["65", "66", "67", "68", "69", "70"],
            "defend": ["34", "35", "36", "37", "38", "39", "40", "37", "36", "35", "34"],
            "death": ["25", "26", "27", "28", "29", "30", "31", "32", "33"],
            "dead": ["33"],
            "attack_up": ["09", "10", "11", "12", "13", "14", "15", "16"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "attack_down": ["17", "18", "19", "20", "21", "22", "23", "24"],
            "start_moving": ["53", "54", "55"],
            "stop_moving": ["62", "61", "60", "59", "58", "57", "56", "63", "64"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)

    def add_animation_moving(self):
        self.add_animation(self, "start_moving")
        self.add_animation(self, "stop_moving")

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Ring of Frost and Frostbolt
    # todo: Immunity to the Fire magic
    # todo: double damage to water elementals
    # todo: Fire Mage: units are able to cast the spell Protection from Fire, which lasts for 3 turns.


class Felem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'felem'
        self.ai = 345

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 8, "damage": [4, 6],
                                                         "health": 35, "speed": 6},
                                "current_health": 35, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["44", "45", "46", "47", "48", "49"],
            "mouse_over": ["31", "32", "33", "34", "33", "32", "31"],
            "standing": ["35", "36", "37", "38", "39", "40"],
            "getting_hit": ["54", "55", "56", "57", "58", "59"],
            "defend": ["26", "27", "28", "29", "30", "29", "30", "29", "30", "29", "28", "27", "26"],
            "death": ["54", "55", "19", "20", "21", "22", "23", "24", "25"],
            "dead": ["25"],
            "attack_up": ["07", "08", "09", "10", "11", "12", "11", "12", "11", "12", "11", "10", "09", "08", "07"],
            "attack_straight": ["01", "02", "03", "04", "05", "06", "05", "06", "05", "06", "05", "04", "03", "02", "01"],
            "attack_down": ["13", "14", "15", "16", "17", "18", "17", "18", "17", "18", "17", "16", "15", "14", "13"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -15, "y_shift": -10}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Ring of Frost and Frostbolt
    # todo: Immunity to the Fire magic
    # todo: double damage to water elementals


class Icee(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'icee'
        self.ai = 280

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 10, "damage": [3, 7],
                                                         "health": 30, "speed": 6},
                                "current_health": 30, "current_count": count, "current_arrows": 24,
                                "is_double": True, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["53", "54", "55", "56", "57", "58", "59"],
            "mouse_over": ["43", "44", "45", "46", "45", "44", "43"],
            "standing": ["77", "47", "48", "49", "50", "49", "48", "47"],
            "getting_hit": ["63", "64", "65", "66", "67", "68"],
            "defend": ["38", "39", "40", "41", "42", "42", "42", "41", "40", "39", "38"],
            "death": ["28", "29", "30", "31", "32", "33", "33", "33", "34", "35", "36", "37"],
            "dead": ["37"],
            "attack_up": ["19", "20", "21", "22", "23", "24", "25", "26", "27"],
            "attack_straight": ["19", "20", "21", "22", "23", "24", "25", "26", "27"],
            "attack_down": ["19", "20", "21", "22", "23", "24", "25", "26", "27"],
            "shoot_up": ["01", "09", "10", "11", "12", "13", "07", "08"],
            "shoot_straight": ["01", "02", "03", "04", "05", "06", "07", "08"],
            "shoot_down": ["01", "14", "15", "16", "17", "18", "07", "08"]
        }

        self.image = {"x_size": 196, "y_size": 196 / 1.125, "x_shift": 10, "y_shift": 0}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Fireball, Inferno, Armageddon.
    # todo: Immunity to the Ring of Frost and Frostbolt
    # todo: double damage to fire elementals
    # todo: Water Mage: units are able to cast the spell Protection from Water, which lasts for 3 turns.


class Welem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'welem'
        self.ai = 315

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 10, "damage": [3, 7],
                                                         "health": 30, "speed": 5},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["40", "41", "42", "43", "44", "45", "46", "47"],
            "mouse_over": ["30", "31", "32", "33", "32", "31", "30"],
            "standing": ["59", "34", "35", "36", "37", "36", "35", "34"],
            "getting_hit": ["50", "51", "52", "53", "54", "55"],
            "defend": ["24", "25", "26", "27", "28", "29", "27", "28", "29", "27", "28", "29", "26", "25", "24"],
            "death": ["16", "17", "18", "19", "20", "21", "22", "23"],
            "dead": ["23"],
            "attack_up": ["01", "02", "03", "04", "05", "06", "10", "11"],
            "attack_straight": ["01", "02", "03", "04", "05", "07", "08", "09"],
            "attack_down": ["01", "02", "03", "04", "12", "13", "14", "15"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Fireball, Inferno, Armageddon.
    # todo: Immunity to the Ring of Frost and Frostbolt
    # todo: double damage to fire elementals


class Storm(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'storm'
        self.ai = 486

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 9, "damage": [2, 8],
                                                         "health": 25, "speed": 8},
                                "current_health": 25, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["45", "46", "47", "48"],
            "mouse_over": ["34", "35", "36", "37", "38"],
            "standing": ["63", "39", "40", "41", "42", "43", "42", "41", "40", "39"],
            "getting_hit": ["49", "50", "51", "52", "53", "54"],
            "defend": ["28", "29", "30", "31", "32", "33", "32", "31", "30", "29", "28"],
            "death": ["19", "20", "21", "22", "23", "24", "25", "26", "27"],
            "dead": ["27"],
            "attack_up": ["07", "08", "09", "10", "11", "12"],
            "attack_straight": ["01", "02", "03", "04", "05", "06"],
            "attack_down": ["13", "14", "15", "16", "17", "18"],
            "shoot_up": ["55", "56", "57", "58", "59", "60"],
            "shoot_straight": ["55", "56", "57", "58", "59", "60"],
            "shoot_down": ["55", "56", "57", "58", "59", "60"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Lightning, Chain Lightning, Armageddon
    # todo: Immunity to the Meteor Shower
    # todo: double damage to Earth elementals
    # todo: Air Mage: units are able to cast the spell Protection from Air, which lasts for 3 turns.


class Aelem(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'aelem'
        self.ai = 356

        self.characteristics = {"base_characteristics": {"attack": 9, "defense": 9, "damage": [2, 8],
                                                         "health": 25, "speed": 7},
                                "current_health": 25, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["13", "14", "15", "16"],
            "mouse_over": ["01", "07", "08", "09", "10", "11"],
            "standing": ["01", "02", "03", "04", "05", "06"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "20", "21", "22", "23", "24", "25", "23", "22", "21", "20"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56", "57", "58"],
            "dead": ["58"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    # todo: They cannot be resurrected, their morale is always neutral, and they are immune to mind-affecting spells
    # todo: Receive double damage from spells: Lightning, Chain Lightning, Armageddon
    # todo: Immunity to the Meteor Shower
    # todo: double damage to Earth elementals


class Sprit(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'sprit'
        self.ai = 95

        self.characteristics = {"base_characteristics": {"attack": 2, "defense": 2, "damage": [1, 3],
                                                         "health": 3, "speed": 9},
                                "current_health": 3, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["48", "49", "50", "51", "52", "53"],
            "mouse_over": ["35", "36", "37", "38", "38", "38", "39", "40"],
            "standing": ["67", "41", "42", "43", "44", "43", "42", "41"],
            "getting_hit": ["57", "58", "59", "60", "61", "62", "63", "64"],
            "defend": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "death": ["25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["09", "10", "11", "12", "13", "12", "13", "14", "15", "16"],
            "attack_straight": ["01", "02", "03", "04", "05", "04", "05", "06", "07", "08"],
            "attack_down": ["17", "18", "19", "20", "21", "20", "21", "22", "23", "24"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()


class Pixie(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pixie'
        self.ai = 55

        self.characteristics = {"base_characteristics": {"attack": 2, "defense": 2, "damage": [1, 2],
                                                         "health": 3, "speed": 7},
                                "current_health": 3, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["48", "49", "50", "51", "52", "53"],
            "mouse_over": ["35", "36", "36", "37", "38", "38", "38", "39", "40"],
            "standing": ["67", "41", "42", "43", "44", "43", "42", "41"],
            "getting_hit": ["57", "58", "59", "60", "61", "62", "63", "64"],
            "defend": ["31", "32", "33", "34", "34", "34", "33", "32", "31"],
            "death": ["25", "26", "27", "28", "29", "30"],
            "dead": ["30"],
            "attack_up": ["09", "10", "11", "12", "13", "12", "13", "14", "15", "16"],
            "attack_straight": ["01", "02", "03", "04", "05", "04", "05", "06", "07", "08"],
            "attack_down": ["17", "18", "19", "20", "21", "20", "21", "22", "23", "24"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)
