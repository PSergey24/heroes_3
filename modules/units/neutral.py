from .units import Units


class Adrgn(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.character = 'adrgn'
        self.ai = 78845

        self.characteristics = {"base_characteristics": {"attack": 50, "defense": 50, "damage": [70, 80],
                                                         "health": 1000, "speed": 19},
                                "current_health": 1000, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["13", "14", "15", "16", "15", "14"],
            "mouse_over": ["01", "05", "06", "07", "08", "07", "06", "05"],
            "standing": ["01", "01", "02", "03", "04", "04", "04", "04", "03", "02", "01", "01"],
            "getting_hit": ["01", "57", "58", "59", "60", "61", "62"],
            "defend": ["01", "51", "52", "53", "54", "55", "56"],
            "death": ["01", "63", "64", "65", "66", "67", "68", "69"],
            "dead": ["69"],
            "attack_up": ["01", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"],
            "attack_straight": ["01", "33", "34", "35", "36", "37", "38", "39", "40", "41"],
            "attack_down": ["01", "42", "43", "44", "45", "46", "47", "48", "49", "50"],
            "dhex_attack_up": ["01", "23", "24", "25", "78", "79", "80", "81", "82", "83", "84"],
            "dhex_attack_straight": ["01", "33", "34", "35", "36", "70", "71", "72", "73", "41"],
            "dhex_attack_down": ["01", "42", "43", "74", "75", "76", "77", "50"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -15, "y_shift": 10}

        self.init(i, j)

    # todo: “Fear” – 10% chance that the enemy unit will miss a turn in battle
    # todo: Immunity to all spells of levels 1-3
    # todo: fire behind
