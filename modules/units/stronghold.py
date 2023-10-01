from .units import Units


class Abehe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'abehe'
        self.attack = 19
        self.defense = 19
        self.damage = [30, 50]
        self.health = 300
        self.speed = 9
        self.ai = 6168

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "22", "23", "24", "24", "23", "22"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55"]
        self.dead = "55"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 10
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Ybehe(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ybehe'
        self.attack = 17
        self.defense = 17
        self.damage = [30, 50]
        self.health = 160
        self.speed = 6
        self.ai = 3162

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "22", "23", "24", "24", "23", "22"]
        self.death = ["01", "49", "50", "51", "52", "53", "54", "55"]
        self.dead = "55"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 10
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Cyclr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'cyclr'
        self.attack = 17
        self.defense = 13
        self.damage = [16, 20]
        self.health = 70
        self.speed = 8
        self.arrows = 0 #todo
        self.ai = 1443

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["45", "46", "47", "48", "49", "50", "51", "52"]
        self.mouse_over = ["39", "40", "41", "42", "41", "40", "39"]
        self.standing = ["01", "02", "03", "04", "05", "06"]
        self.getting_hit = ["31", "30", "29"]
        self.defend = ["38", "37", "36", "35"]
        self.death = ["31", "30", "32", "33", "34"]
        self.dead = "34"
        self.attack_up = ["74", "53", "19", "20", "21", "22", "23"]
        self.attack_straight = ["74", "53", "24", "25", "26", "27", "28"]
        self.attack_down = ["74", "53", "14", "15", "16", "17", "18"]
        self.shoot_up = ["74", "53", "59", "60", "61", "62", "63", "64", "65", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_straight = ["01", "01", "74", "53", "53", "54", "55", "56", "57", "58", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_down = ["01", "01", "01", "74", "53", "66", "67", "68", "69", "70", "09", "08", "07", "10", "11", "12", "13"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25

        self.update_hex(i, j)
        self.create_animation('standing')


class Cyclp(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'cyclp'
        self.attack = 15
        self.defense = 12
        self.damage = [16, 20]
        self.health = 70
        self.speed = 6
        self.arrows = 0  # todo
        self.ai = 1266

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["45", "46", "47", "48", "49", "50", "51", "52"]
        self.mouse_over = ["39", "40", "41", "42", "41", "40", "39"]
        self.standing = ["01", "02", "03", "04", "05", "06"]
        self.getting_hit = ["31", "30", "29"]
        self.defend = ["38", "37", "36", "35"]
        self.death = ["31", "30", "32", "33", "34"]
        self.dead = "34"
        self.attack_up = ["74", "53", "19", "20", "21", "22", "23"]
        self.attack_straight = ["74", "53", "24", "25", "26", "27", "28"]
        self.attack_down = ["74", "53", "14", "15", "16", "17", "18"]
        self.shoot_up = ["74", "53", "59", "60", "61", "62", "63", "64", "65", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_straight = ["01", "01", "74", "53", "53", "54", "55", "56", "57", "58", "09", "08", "07", "10", "11", "12", "13"]
        self.shoot_down = ["01", "01", "01", "74", "53", "66", "67", "68", "69", "70", "09", "08", "07", "10", "11", "12", "13"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25

        self.update_hex(i, j)
        self.create_animation('standing')


class Tbird(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'tbird'
        self.attack = 13
        self.defense = 11
        self.damage = [11, 15]
        self.health = 60
        self.speed = 11
        self.ai = 1106

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["12", "13", "14", "15", "14", "13"]
        self.mouse_over = ["01", "05", "06", "07", "07", "06", "05", "01"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "49", "50", "51", "52", "53", "54"]
        self.defend = ["01", "22", "23", "24", "25", "25", "24", "23", "22"]
        self.death = ["01", "55", "56", "57", "58", "59", "60", "61"]
        self.dead = "61"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "41", "42", "43", "44", "45", "46", "47", "48"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -10
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Roc(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'roc'
        self.attack = 13
        self.defense = 11
        self.damage = [11, 15]
        self.health = 60
        self.speed = 7
        self.ai = 1027

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["12", "13", "14", "15", "14", "13"]
        self.mouse_over = ["01", "05", "06", "07", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "49", "50", "51", "52", "53", "54"]
        self.defend = ["01", "22", "23", "24", "25", "25", "24", "23", "22"]
        self.death = ["01", "55", "56", "57", "58", "59", "60", "61"]
        self.dead = "61"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "41", "42", "43", "44", "45", "46", "47", "48"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 5
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Ogmag(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ogmag'
        self.attack = 13
        self.defense = 7
        self.damage = [6, 12]
        self.health = 60
        self.speed = 5
        self.ai = 672

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "24", "25", "25", "23", "22"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Ogre(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'ogre'
        self.attack = 13
        self.defense = 7
        self.damage = [6, 12]
        self.health = 40
        self.speed = 4
        self.ai = 416

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "24", "25", "25", "23", "22"]
        self.death = ["01", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["01", "26", "27", "28", "29", "30", "31"]
        self.attack_straight = ["01", "32", "33", "34", "35", "36", "37"]
        self.attack_down = ["01", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -20
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Orcch(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'orcch'
        self.attack = 8
        self.defense = 4
        self.damage = [2, 5]
        self.health = 20
        self.speed = 5
        self.arrows = 0 #todo
        self.ai = 240

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["203", "204", "205", "206", "207", "208", "209", "210"]
        self.mouse_over = ["227", "228", "229", "230", "230", "230", "230", "229", "228", "227"]
        self.standing = ["268", "269", "270", "271", "270", "269", "268"]
        self.getting_hit = ["220", "221", "222", "223", "224", "225", "226"]
        self.defend = ["215", "216", "217", "218", "218", "218", "218", "217", "216", "215"]
        self.death = ["259", "260", "261", "262", "263", "264"]
        self.dead = "264"
        self.attack_up = ["243", "244", "245", "246", "247", "248", "249"]
        self.attack_straight = ["235", "236", "237", "238", "239", "240", "241"]
        self.attack_down = ["251", "252", "253", "254", "255", "256", "257"]
        self.shoot_up = ["283", "284", "285", "286", "287", "288", "289", "290", "291"]
        self.shoot_straight = ["273", "274", "275", "276", "277", "278", "279", "280", "281"]
        self.shoot_down = ["293", "294", "295", "296", "297", "298", "299", "300", "301"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Orc(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'orc'
        self.attack = 8
        self.defense = 4
        self.damage = [2, 5]
        self.health = 15
        self.speed = 4
        self.arrows = 0 #todo
        self.ai = 192

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["027", "028", "029", "030", "030", "030", "030", "029", "028", "027"]
        self.standing = ["068", "069", "070", "071", "070", "069"]
        self.getting_hit = ["020", "021", "022", "023", "024", "025", "026"]
        self.defend = ["015", "016", "017", "018", "018", "018", "018", "017", "016", "015"]
        self.death = ["059", "060", "061", "062", "063", "064"]
        self.dead = "064"
        self.attack_up = ["043", "044", "045", "046", "047", "048", "049"]
        self.attack_straight = ["035", "036", "037", "038", "039", "040", "041"]
        self.attack_down = ["051", "052", "053", "054", "055", "056", "057"]
        self.shoot_up = ["083", "084", "085", "086", "087", "088", "089", "090", "091"]
        self.shoot_straight = ["073", "074", "075", "076", "077", "078", "079", "080", "081"]
        self.shoot_down = ["093", "094", "095", "096", "097", "098", "099", "100", "101"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Uwlfr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'uwlfr'
        self.attack = 8
        self.defense = 5
        self.damage = [3, 4]
        self.health = 10
        self.speed = 8
        self.ai = 203

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "19", "20", "21", "21", "22", "23", "24"]
        self.death = ["01", "49", "50", "51", "52", "53", "54"]
        self.dead = "54"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Bwlfr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'bwlfr'
        self.attack = 7
        self.defense = 5
        self.damage = [2, 4]
        self.health = 10
        self.speed = 6
        self.ai = 130

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "43", "44", "45", "46", "47", "48"]
        self.defend = ["01", "19", "20", "21", "21", "22", "23", "24"]
        self.death = ["01", "49", "50", "51", "52", "53", "54"]
        self.dead = "54"
        self.attack_up = ["01", "25", "26", "27", "28", "29", "30"]
        self.attack_straight = ["01", "31", "32", "33", "34", "35", "36"]
        self.attack_down = ["01", "37", "38", "39", "40", "41", "42"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Hgobl(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'hgobl'
        self.attack = 5
        self.defense = 3
        self.damage = [1, 2]
        self.health = 5
        self.speed = 7
        self.ai = 78

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "03", "02", "01"]
        self.getting_hit = ["01", "46", "47", "48", "49", "50", "51"]
        self.defend = ["01", "22", "23", "24", "24", "25", "26", "27", "28"]
        self.death = ["01", "52", "53", "54", "55", "56", "57", "58", "59"]
        self.dead = "59"
        self.attack_up = ["01", "34", "35", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "34", "35", "41", "42", "43", "44", "45"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')


class Gobli(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'gobli'
        self.attack = 4
        self.defense = 2
        self.damage = [1, 2]
        self.health = 5
        self.speed = 5
        self.ai = 60

        self.cur_health = self.health

        self.moving = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
        self.mouse_over = ["01", "05", "06", "07", "08", "08", "07", "06", "05"]
        self.standing = ["01", "02", "03", "04", "04", "03", "02", "01"]
        self.getting_hit = ["01", "44", "45", "46", "47", "48", "49"]
        self.defend = ["01", "22", "23", "24", "24", "25", "26", "27", "28"]
        self.death = ["01", "52", "53", "54", "55", "56", "57", "58", "59"]
        self.dead = "59"
        self.attack_up = ["01", "34", "35", "29", "30", "31", "32", "33"]
        self.attack_straight = ["01", "34", "35", "36", "37", "38", "39", "40"]
        self.attack_down = ["01", "34", "35", "41", "42", "43", "44", "45"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -10

        self.update_hex(i, j)
        self.create_animation('standing')
