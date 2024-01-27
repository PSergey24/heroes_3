from .units import Units


class Abehe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'abehe'
        self.ai = 6168

        self.characteristics = {"base_characteristics": {"attack": 19, "defense": 19, "damage": [30, 50],
                                                         "health": 300, "speed": 9},
                                "current_health": 300, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "22", "23", "24", "24", "23", "22"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55"],
            "dead": ["55"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -20}

        self.init(i, j)

    # todo: Ignore defense 80% - (N-1)×(1-0.8)


class Ybehe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ybehe'
        self.ai = 3162

        self.characteristics = {"base_characteristics": {"attack": 17, "defense": 17, "damage": [30, 50],
                                                         "health": 160, "speed": 6},
                                "current_health": 160, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "22", "23", "24", "24", "23", "22"],
            "death": ["01", "49", "50", "51", "52", "53", "54", "55"],
            "dead": ["55"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 10, "y_shift": -10}

        self.init(i, j)

    # todo: Ignore defense 40% - (N-1)×(1-0.4)


class Cyclr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'cyclr'
        self.ai = 1443

        self.characteristics = {"base_characteristics": {"attack": 17, "defense": 13, "damage": [16, 20],
                                                         "health": 70, "speed": 8},
                                "current_health": 70, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["45", "46", "47", "48", "49", "50", "51", "52"],
            "mouse_over": ["39", "40", "41", "42", "41", "40", "39"],
            "standing": ["01", "02", "03", "04", "05", "06"],
            "getting_hit": ["31", "30", "29"],
            "defend": ["38", "37", "36", "35"],
            "death": ["31", "30", "32", "33", "34"],
            "dead": ["34"],
            "attack_up": ["74", "53", "19", "20", "21", "22", "23"],
            "attack_straight": ["74", "53", "24", "25", "26", "27", "28"],
            "attack_down": ["74", "53", "14", "15", "16", "17", "18"],
            "shoot_up": ["74", "53", "59", "60", "61", "62", "63", "64", "65", "09", "08", "07", "10", "11", "12", "13"],
            "shoot_straight": ["01", "01", "74", "53", "53", "54", "55", "56", "57", "58", "09", "08", "07", "10", "11", "12", "13"],
            "shoot_down": ["01", "01", "01", "74", "53", "66", "67", "68", "69", "70", "09", "08", "07", "10", "11", "12", "13"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Destroyer of Fortifications


class Cyclp(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'cyclp'
        self.ai = 1266

        self.characteristics = {"base_characteristics": {"attack": 15, "defense": 12, "damage": [16, 20],
                                                         "health": 70, "speed": 6},
                                "current_health": 70, "current_count": count, "current_arrows": 16,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["45", "46", "47", "48", "49", "50", "51", "52"],
            "mouse_over": ["39", "40", "41", "42", "41", "40", "39"],
            "standing": ["01", "02", "03", "04", "05", "06"],
            "getting_hit": ["31", "30", "29"],
            "defend": ["38", "37", "36", "35"],
            "death": ["31", "30", "32", "33", "34"],
            "dead": ["34"],
            "attack_up": ["74", "53", "19", "20", "21", "22", "23"],
            "attack_straight": ["74", "53", "24", "25", "26", "27", "28"],
            "attack_down": ["74", "53", "14", "15", "16", "17", "18"],
            "shoot_up": ["74", "53", "59", "60", "61", "62", "63", "64", "65", "09", "08", "07", "10", "11", "12", "13"],
            "shoot_straight": ["01", "01", "74", "53", "53", "54", "55", "56", "57", "58", "09", "08", "07", "10", "11", "12", "13"],
            "shoot_down": ["01", "01", "01", "74", "53", "66", "67", "68", "69", "70", "09", "08", "07", "10", "11", "12", "13"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)

    # todo: Destroyer of Fortifications


class Tbird(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'tbird'
        self.ai = 1106

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 11, "damage": [11, 15],
                                                         "health": 60, "speed": 11},
                                "current_health": 60, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["12", "13", "14", "15", "14", "13"],
            "mouse_over": ["01", "05", "06", "07", "07", "06", "05", "01"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "49", "50", "51", "52", "53", "54"],
            "defend": ["01", "22", "23", "24", "25", "25", "24", "23", "22"],
            "death": ["01", "55", "56", "57", "58", "59", "60", "61"],
            "dead": ["61"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "41", "42", "43", "44", "45", "46", "47", "48"]
        }

        self.image = {"x_size": 288, "y_size": 288 / 1.125, "x_shift": -10, "y_shift": -10}

        self.init(i, j)

    # todo: Lightning Strike – 20% chance of lightning to strike. Damage = N * 10


class Roc(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'roc'
        self.ai = 1027

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 11, "damage": [11, 15],
                                                         "health": 60, "speed": 7},
                                "current_health": 60, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": True, "is_jumper": False
                                }

        self.animations = {
            "moving": ["12", "13", "14", "15", "14", "13"],
            "mouse_over": ["01", "05", "06", "07", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "49", "50", "51", "52", "53", "54"],
            "defend": ["01", "22", "23", "24", "25", "25", "24", "23", "22"],
            "death": ["01", "55", "56", "57", "58", "59", "60", "61"],
            "dead": ["61"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "41", "42", "43", "44", "45", "46", "47", "48"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 5, "y_shift": -10}

        self.init(i, j)


class Ogmag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ogmag'
        self.ai = 672

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 7, "damage": [6, 12],
                                                         "health": 60, "speed": 5},
                                "current_health": 60, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "22", "23", "24", "24", "25", "25", "23", "22"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": -10}

        self.init(i, j)

    # todo: three times can cast advanced level Bloodlust spell: +6 to the attack. Duration – 3 turns.


class Ogre(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'ogre'
        self.ai = 416

        self.characteristics = {"base_characteristics": {"attack": 13, "defense": 7, "damage": [6, 12],
                                                         "health": 40, "speed": 4},
                                "current_health": 40, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "22", "23", "24", "24", "25", "25", "23", "22"],
            "death": ["01", "50", "51", "52", "53", "54", "55", "56"],
            "dead": ["56"],
            "attack_up": ["01", "26", "27", "28", "29", "30", "31"],
            "attack_straight": ["01", "32", "33", "34", "35", "36", "37"],
            "attack_down": ["01", "38", "39", "40", "41", "42", "43"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -20, "y_shift": 0}

        self.init(i, j)


class Orcch(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'orcch'
        self.ai = 240

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 4, "damage": [2, 5],
                                                         "health": 20, "speed": 5},
                                "current_health": 20, "current_count": count, "current_arrows": 24,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["203", "204", "205", "206", "207", "208", "209", "210"],
            "mouse_over": ["227", "228", "229", "230", "230", "230", "230", "229", "228", "227"],
            "standing": ["268", "269", "270", "271", "270", "269", "268"],
            "getting_hit": ["220", "221", "222", "223", "224", "225", "226"],
            "defend": ["215", "216", "217", "218", "218", "218", "218", "217", "216", "215"],
            "death": ["259", "260", "261", "262", "263", "264"],
            "dead": ["264"],
            "attack_up": ["243", "244", "245", "246", "247", "248", "249"],
            "attack_straight": ["235", "236", "237", "238", "239", "240", "241"],
            "attack_down": ["251", "252", "253", "254", "255", "256", "257"],
            "shoot_up": ["283", "284", "285", "286", "287", "288", "289", "290", "291"],
            "shoot_straight": ["273", "274", "275", "276", "277", "278", "279", "280", "281"],
            "shoot_down": ["293", "294", "295", "296", "297", "298", "299", "300", "301"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Orc(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'orc'
        self.ai = 192

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 4, "damage": [2, 5],
                                                         "health": 15, "speed": 4},
                                "current_health": 15, "current_count": count, "current_arrows": 12,
                                "is_double": False, "is_shooter": True, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["003", "004", "005", "006", "007", "008", "009", "010"],
            "mouse_over": ["027", "028", "029", "030", "030", "030", "030", "029", "028", "027"],
            "standing": ["068", "069", "070", "071", "070", "069"],
            "getting_hit": ["020", "021", "022", "023", "024", "025", "026"],
            "defend": ["015", "016", "017", "018", "018", "018", "018", "017", "016", "015"],
            "death": ["059", "060", "061", "062", "063", "064"],
            "dead": ["064"],
            "attack_up": ["043", "044", "045", "046", "047", "048", "049"],
            "attack_straight": ["035", "036", "037", "038", "039", "040", "041"],
            "attack_down": ["051", "052", "053", "054", "055", "056", "057"],
            "shoot_up": ["083", "084", "085", "086", "087", "088", "089", "090", "091"],
            "shoot_straight": ["073", "074", "075", "076", "077", "078", "079", "080", "081"],
            "shoot_down": ["093", "094", "095", "096", "097", "098", "099", "100", "101"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -5}

        self.init(i, j)


class Uwlfr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'uwlfr'
        self.ai = 203

        self.characteristics = {"base_characteristics": {"attack": 8, "defense": 5, "damage": [3, 4],
                                                         "health": 10, "speed": 8},
                                "current_health": 10, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "19", "20", "21", "21", "22", "23", "24"],
            "death": ["01", "49", "50", "51", "52", "53", "54"],
            "dead": ["54"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -10}

        self.init(i, j)

    # todo: double attack


class Bwlfr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'bwlfr'
        self.ai = 130

        self.characteristics = {"base_characteristics": {"attack": 7, "defense": 5, "damage": [2, 4],
                                                         "health": 10, "speed": 6},
                                "current_health": 10, "current_count": count, "current_arrows": 0,
                                "is_double": True, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "04", "03", "02", "01"],
            "getting_hit": ["01", "43", "44", "45", "46", "47", "48"],
            "defend": ["01", "19", "20", "21", "21", "22", "23", "24"],
            "death": ["01", "49", "50", "51", "52", "53", "54"],
            "dead": ["54"],
            "attack_up": ["01", "25", "26", "27", "28", "29", "30"],
            "attack_straight": ["01", "31", "32", "33", "34", "35", "36"],
            "attack_down": ["01", "37", "38", "39", "40", "41", "42"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": 0, "y_shift": -15}

        self.init(i, j)


class Hgobl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'hgobl'
        self.ai = 78

        self.characteristics = {"base_characteristics": {"attack": 5, "defense": 3, "damage": [1, 2],
                                                         "health": 5, "speed": 7},
                                "current_health": 5, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "03", "02", "01"],
            "getting_hit": ["01", "46", "47", "48", "49", "50", "51"],
            "defend": ["01", "22", "23", "24", "24", "25", "26", "27", "28"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "34", "35", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "34", "35", "41", "42", "43", "44", "45"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)


class Gobli(Units):

    def __init__(self, i, j, count, team):
        super().__init__(team)

        self.name = 'gobli'
        self.ai = 60

        self.characteristics = {"base_characteristics": {"attack": 4, "defense": 2, "damage": [1, 2],
                                                         "health": 5, "speed": 5},
                                "current_health": 5, "current_count": count, "current_arrows": 0,
                                "is_double": False, "is_shooter": False, "is_flyer": False, "is_jumper": False
                                }

        self.animations = {
            "moving": ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
            "mouse_over": ["01", "05", "06", "07", "08", "08", "07", "06", "05"],
            "standing": ["01", "02", "03", "04", "03", "02", "01"],
            "getting_hit": ["01", "44", "45", "46", "47", "48", "49"],
            "defend": ["01", "22", "23", "24", "24", "25", "26", "27", "28"],
            "death": ["01", "52", "53", "54", "55", "56", "57", "58", "59"],
            "dead": ["59"],
            "attack_up": ["01", "34", "35", "29", "30", "31", "32", "33"],
            "attack_straight": ["01", "34", "35", "36", "37", "38", "39", "40"],
            "attack_down": ["01", "34", "35", "41", "42", "43", "44", "45"]
        }

        self.image = {"x_size": 216, "y_size": 216 / 1.125, "x_shift": -25, "y_shift": -10}

        self.init(i, j)
