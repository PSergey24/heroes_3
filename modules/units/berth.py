from .units import Units
from modules.states import Objects


class Haspid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'haspid'
        self.ai = 7220

        self.characteristics = {"base_characteristics": {"attack": 29, "defense": 20, "damage": [30, 55],
                                                         "health": 300, "speed": 12},
                                "current_health": 300, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["57", "58", "59", "60", "61", "62", "63", "64"],
            "standing": ["85", "86", "87", "88", "89", "90", "89", "88", "87", "86", "85"],
            "getting_hit": ["33", "34", "35", "36", "37", "38", "39"],
            "defend": ["41", "42", "43", "44", "44", "44", "44", "43", "42", "41"],
            "death": ["49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["66", "67", "68", "69", "70", "72", "74"],
            "attack_straight": ["23", "24", "25", "26", "27", "29", "31"],
            "attack_down": ["76", "77", "78", "79", "80", "82", "84"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": -25}

        self.init(i, j)

    # todo: Poisoning - When attacked, there is a 30% chance that units of the target enemy squad will be poisoned with poison - each of them will have their health reduced by 10% of their original health each turn for 3 turns (up to 50%). Only affects living beings.
    # todo: Revenge - Every time a squad of asps suffers losses in health and numbers, their damage parameter increases


class Serpent(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'serpent'
        self.ai = 3953

        self.characteristics = {"base_characteristics": {"attack": 22, "defense": 13, "damage": [30, 55],
                                                         "health": 180, "speed": 9},
                                "current_health": 180, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15"],
            "mouse_over": ["57", "58", "59", "60", "61", "62", "63", "64"],
            "standing": ["85", "86", "87", "88", "89", "90", "89", "88", "87", "86", "85"],
            "getting_hit": ["33", "34", "35", "36", "37", "38", "39"],
            "defend": ["41", "42", "43", "44", "44", "44", "44", "43", "42", "41"],
            "death": ["49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["66", "67", "68", "69", "70", "72", "74"],
            "attack_straight": ["23", "24", "25", "26", "27", "29", "31"],
            "attack_down": ["76", "77", "78", "79", "80", "82", "84"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 5, "y_shift": 10}

        self.init(i, j)

    # todo: Poisoning - When attacked, there is a 30% chance that units of the target enemy squad will be poisoned with poison - each of them will have their health reduced by 10% of their original health each turn for 3 turns (up to 50%). Only affects living beings.


class Nixwarr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'nixwarr'
        self.ai = 2116

        self.characteristics = {"base_characteristics": {"attack": 14, "defense": 17, "damage": [18, 22],
                                                         "health": 100, "speed": 7},
                                "current_health": 100, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["14", "15", "16", "17", "18", "19", "20", "21"],
            "mouse_over": ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"],
            "standing": ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"],
            "getting_hit": ["25", "26", "27", "28", "29", "30", "31", "32"],
            "defend": ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"],
            "death": ["48", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["61", "62", "63", "64", "65", "66", "67", "68", "69"],
            "attack_straight": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "attack_down": ["70", "71", "72", "73", "74", "75", "76", "77"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -40, "y_shift": -20}

        self.init(i, j)

    # todo: Fortified Hide - When calculating damage from an enemy attack, ignore 60% of the attack parameter


class Nix(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'nix'
        self.ai = 1415

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 16, "damage": [18, 20],
                                                         "health": 90, "speed": 6},
                                "current_health": 90, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["14", "15", "16", "17", "18", "19", "20", "21"],
            "mouse_over": ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"],
            "standing": ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"],
            "getting_hit": ["25", "26", "27", "28", "29", "30", "31", "32"],
            "defend": ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"],
            "death": ["48", "49", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["61", "62", "63", "64", "65", "66", "67", "68", "69"],
            "attack_straight": ["39", "40", "41", "42", "43", "44", "45", "46"],
            "attack_down": ["70", "71", "72", "73", "74", "75", "76", "77"]
        }

        self.image = {"x_size": 196, "y_size": 196 / 1.125, "x_shift": -15, "y_shift": -5}

        self.init(i, j)

    # todo: Fortified Hide - When calculating damage from an enemy attack, ignore 30% of the attack parameter


class Sorcss(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'sorcss'
        self.ai = 852

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 9, "damage": [10, 16],
                                                         "health": 35, "speed": 7},
                                "current_health": 35, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["141", "142", "143", "144", "145", "146", "145", "144", "143", "142", "141"],
            "standing": ["120", "121", "122", "123", "122", "121", "120"],
            "getting_hit": ["047", "048", "049", "050", "051", "052"],
            "defend": ["127", "128", "129", "130", "131", "132", "133", "133", "133", "132", "131", "130", "129", "128", "127"],
            "death": ["113", "114", "115", "116", "117", "118", "119"],
            "dead": ["119"],
            "attack_up": ["055", "056", "057", "059", "060", "063", "064", "066", "067", "069"],
            "attack_straight": ["074", "075", "076", "078", "079", "082", "083", "085", "086", "085"],
            "attack_down": ["093", "094", "095", "097", "098", "101", "102", "104", "105", "107"],
            "shoot_up": ["015", "016", "017", "018", "019", "020", "021", "022", "023"],
            "shoot_straight": ["026", "027", "028", "029", "030", "031", "032", "033", "034"],
            "shoot_down": ["037", "038", "039", "040", "041", "042", "043", "044", "045"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Curse Shot - weakness or destructive ray.


class Priest(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'priest'
        self.ai = 790

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 7, "damage": [10, 14],
                                                         "health": 35, "speed": 6},
                                "current_health": 35, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["141", "142", "143", "144", "145", "146", "145", "144", "143", "142", "141"],
            "standing": ["120", "121", "122", "123", "122", "121", "120"],
            "getting_hit": ["047", "048", "049", "050", "051", "052"],
            "defend": ["127", "128", "129", "130", "131", "132", "133", "133", "133", "132", "131", "130", "129", "128", "127"],
            "death": ["113", "114", "115", "116", "117", "118", "119"],
            "dead": ["119"],
            "attack_up": ["055", "056", "057", "059", "060", "063", "064", "066", "067", "069"],
            "attack_straight": ["074", "075", "076", "078", "079", "082", "083", "085", "086", "085"],
            "attack_down": ["093", "094", "095", "097", "098", "101", "102", "104", "105", "107"],
            "shoot_up": ["015", "016", "017", "018", "019", "020", "021", "022", "023"],
            "shoot_straight": ["026", "027", "028", "029", "030", "031", "032", "033", "034"],
            "shoot_down": ["037", "038", "039", "040", "041", "042", "043", "044", "045"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Curse Shot - weakness or destructive ray.


class Assidup(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'assidup'
        self.ai = 645

        self.characteristics = {"base_characteristics": {"attack": 11, "defense": 8, "damage": [6, 10],
                                                         "health": 30, "speed": 11},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13"],
            "mouse_over": ["56", "57", "58", "59", "59", "59", "59", "58", "57", "56"],
            "standing": ["60", "61", "62", "63", "64", "63", "62", "61"],
            "getting_hit": ["45", "46", "47", "48", "49", "50", "51"],
            "defend": ["74", "75", "76", "77", "78", "78", "78", "78", "77", "76", "75", "74"],
            "death": ["65", "66", "67", "68", "69", "70", "71", "72"],
            "dead": ["72"],
            "attack_up": ["27", "28", "29", "30", "31", "32", "33", "34"],
            "attack_straight": ["18", "19", "20", "21", "22", "23", "24", "25"],
            "attack_down": ["36", "37", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init(i, j)

    # todo: Ferocity - If the Assids kill at least one creature from the enemy unit, then they strike a second time. As a rule, the second blow is delivered after a retaliatory attack.


class Assid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'assid'
        self.ai = 502

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 8, "damage": [6, 9],
                                                         "health": 30, "speed": 9},
                                "current_health": 30, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13"],
            "mouse_over": ["56", "57", "58", "59", "59", "59", "59", "58", "57", "56"],
            "standing": ["60", "61", "62", "63", "64", "63", "62", "61"],
            "getting_hit": ["45", "46", "47", "48", "49", "50", "51"],
            "defend": ["74", "75", "76", "77", "78", "78", "78", "78", "77", "76", "75", "74"],
            "death": ["65", "66", "67", "68", "69", "70", "71", "72"],
            "dead": ["72"],
            "attack_up": ["27", "28", "29", "30", "31", "32", "33", "34"],
            "attack_straight": ["18", "19", "20", "21", "22", "23", "24", "25"],
            "attack_down": ["36", "37", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -5}

        self.init(i, j)


class Pr3up(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pr3up'
        self.ai = 602

        self.characteristics = {"base_characteristics": {"attack": 12, "defense": 11, "damage": [3, 7],
                                                         "health": 16, "speed": 8},
                                "current_health": 16, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["014", "015", "016", "017", "018", "019", "020", "021"],
            "standing": ["022", "023", "024", "025", "026", "025", "024", "023"],
            "getting_hit": ["031", "032", "033", "034", "035", "036"],
            "defend": ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"],
            "death": ["043", "044", "045", "046", "047", "048"],
            "dead": ["048"],
            "attack_up": ["053", "054", "055", "056", "057", "058", "059"],
            "attack_straight": ["061", "062", "063", "064", "065", "066", "067"],
            "attack_down": ["069", "070", "071", "072", "073", "074", "075"],
            "shoot_up": ["077", "079", "081", "082", "086", "087", "088", "089", "090"],
            "shoot_straight": ["092", "094", "096", "097", "101", "102", "103", "104", "105"],
            "shoot_down": ["107", "109", "111", "113", "116", "117", "118", "119", "120"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()

    # todo: There is no melee penalty.
    # todo: Accurate shot


class Corsair(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'corsair'
        self.ai = 407

        self.characteristics = {"base_characteristics": {"attack": 10, "defense": 8, "damage": [3, 7],
                                                         "health": 15, "speed": 7},
                                "current_health": 15, "current_count": count, "current_arrows": 4,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["014", "015", "016", "017", "018", "019", "020", "021"],
            "standing": ["022", "023", "024", "025", "026", "025", "024", "023"],
            "getting_hit": ["031", "032", "033", "034", "035", "036"],
            "defend": ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"],
            "death": ["043", "044", "045", "046", "047", "048"],
            "dead": ["048"],
            "attack_up": ["053", "054", "055", "056", "057", "058", "059"],
            "attack_straight": ["061", "062", "063", "064", "065", "066", "067"],
            "attack_down": ["069", "070", "071", "072", "073", "074", "075"],
            "shoot_up": ["077", "079", "081", "082", "086", "087", "088", "089", "090"],
            "shoot_straight": ["092", "094", "096", "097", "101", "102", "103", "104", "105"],
            "shoot_down": ["107", "109", "111", "113", "116", "117", "118", "119", "120"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # special ability: attack w/o answer
    def add_animation_attack(self):
        self.add_animation_attack_no_answer()

    # todo: There is no melee penalty.


class Pirate(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'pirate'
        self.ai = 312

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 6, "damage": [3, 7],
                                                         "health": 15, "speed": 6},
                                "current_health": 15, "current_count": count, "current_arrows": 4,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["014", "015", "016", "017", "018", "019", "020", "021"],
            "standing": ["022", "023", "024", "025", "026", "025", "024", "023"],
            "getting_hit": ["031", "032", "033", "034", "035", "036"],
            "defend": ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"],
            "death": ["043", "044", "045", "046", "047", "048"],
            "dead": ["048"],
            "attack_up": ["053", "054", "055", "056", "057", "058", "059"],
            "attack_straight": ["061", "062", "063", "064", "065", "066", "067"],
            "attack_down": ["069", "070", "071", "072", "073", "074", "075"],
            "shoot_up": ["077", "079", "081", "082", "086", "087", "088", "089", "090"],
            "shoot_straight": ["092", "094", "096", "097", "101", "102", "103", "104", "105"],
            "shoot_down": ["107", "109", "111", "113", "116", "117", "118", "119", "120"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: There is no melee penalty.


class Swash(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'swash'
        self.ai = 174

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 6, "damage": [3, 4],
                                                         "health": 15, "speed": 6},
                                "current_health": 15, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["03", "04", "05", "06", "07", "08", "09", "10"],
            "mouse_over": ["26", "27", "28", "29", "30", "31", "32", "33", "34"],
            "standing": ["00", "68", "69", "70", "71", "72", "71", "70", "69", "68"],
            "getting_hit": ["20", "21", "22", "23", "24", "25", "26"],
            "defend": ["15", "16", "17", "18", "18", "18", "18", "17", "16", "15"],
            "death": ["59", "60", "61", "62", "63", "64"],
            "dead": ["64"],
            "attack_up": ["43", "44", "45", "46", "47", "48", "49"],
            "attack_straight": ["35", "36", "37", "38", "39", "40", "41"],
            "attack_down": ["51", "52", "53", "54", "55", "56", "57"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Seadog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'seadog'
        self.ai = 155

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 4, "damage": [2, 4],
                                                         "health": 15, "speed": 5},
                                "current_health": 15, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["03", "04", "05", "06", "07", "08", "09", "10"],
            "mouse_over": ["26", "27", "28", "29", "30", "31", "32", "33", "34"],
            "standing": ["00", "68", "69", "70", "71", "72", "71", "70", "69", "68"],
            "getting_hit": ["20", "21", "22", "23", "24", "25", "26"],
            "defend": ["15", "16", "17", "18", "18", "18", "18", "17", "16", "15"],
            "death": ["59", "60", "61", "62", "63", "64"],
            "dead": ["64"],
            "attack_up": ["43", "44", "45", "46", "47", "48", "49"],
            "attack_straight": ["35", "36", "37", "38", "39", "40", "41"],
            "attack_down": ["51", "52", "53", "54", "55", "56", "57"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Oceanid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'oceanid'
        self.ai = 75

        self.characteristics = {"base_characteristics": {"attack": 6, "defense": 2, "damage": [1, 3],
                                                         "health": 4, "speed": 8},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": True
                                }

        self.animations = {
            "moving": ["02"],
            "mouse_over": ["71", "72", "73", "74", "75", "75", "75", "74", "73", "72", "71"],
            "standing": ["02", "03", "04", "05", "06", "07", "08", "09"],
            "getting_hit": ["42", "43", "44", "45", "46", "47"],
            "defend": ["38", "39", "40", "41", "41", "41", "41", "40", "39", "38"],
            "death": ["62", "63", "64", "65", "66", "67", "68", "69", "70"],
            "dead": ["70"],
            "attack_up": ["20", "21", "22", "23", "24", "25", "26", "27"],
            "attack_straight": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "attack_down": ["29", "30", "31", "32", "33", "34", "35", "36"],
            "start_moving": ["49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61"],
            "stop_moving": ["61", "60", "59", "58", "57", "56", "55", "54", "53", "52", "51", "50", "49"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    def add_animation_moving(self):
        self.add_animation(self, "start_moving")
        self.add_animation(self, "stop_moving")

    # todo: Immune to Ice magic


class Nimph(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'nimph'
        self.ai = 57

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 2, "damage": [1, 2],
                                                         "health": 4, "speed": 6},
                                "current_health": 4, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": True
                                }

        self.animations = {
            "moving": ["02"],
            "mouse_over": ["71", "72", "73", "74", "75", "75", "75", "74", "73", "72", "71"],
            "standing": ["02", "03", "04", "05", "06", "07", "08", "09"],
            "getting_hit": ["42", "43", "44", "45", "46", "47"],
            "defend": ["38", "39", "40", "41", "41", "41", "41", "40", "39", "38"],
            "death": ["62", "63", "64", "65", "66", "67", "68", "69", "70"],
            "dead": ["70"],
            "attack_up": ["20", "21", "22", "23", "24", "25", "26", "27"],
            "attack_straight": ["11", "12", "13", "14", "15", "16", "17", "18"],
            "attack_down": ["29", "30", "31", "32", "33", "34", "35", "36"],
            "start_moving": ["49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61"],
            "stop_moving": ["61", "60", "59", "58", "57", "56", "55", "54", "53", "52", "51", "50", "49"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": 0}

        self.init(i, j)

    def add_animation_moving(self):
        self.add_animation(self, "start_moving")
        self.add_animation(self, "stop_moving")

    # todo: Immune to Ice magic
