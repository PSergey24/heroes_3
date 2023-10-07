from .units import Units


class Haspid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'haspid'
        self.attack = 29
        self.defense = 20
        self.damage = [30, 55]
        self.health = 300
        self.speed = 12
        self.ai = 7220

        self.cur_health = self.health

        self.moving = ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["57", "58", "59", "60", "61", "62", "63", "64"]
        self.standing = ["85", "86", "87", "88", "89", "90", "89", "88", "87", "86", "85"]
        self.getting_hit = ["33", "34", "35", "36", "37", "38", "39"]
        self.defend = ["41", "42", "43", "44", "44", "44", "44", "43", "42", "41"]
        self.death = ["49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["66", "67", "68", "69", "70", "72", "74"]
        self.attack_straight = ["23", "24", "25", "26", "27", "29", "31"]
        self.attack_down = ["76", "77", "78", "79", "80", "82", "84"]

        self.img_size_x = 288
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -25

        self.update_hex(i, j)
        self.create_animation('standing')


class Serpent(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'serpent'
        self.attack = 22
        self.defense = 13
        self.damage = [30, 55]
        self.health = 180
        self.speed = 9
        self.ai = 3953

        self.cur_health = self.health

        self.moving = ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]
        self.mouse_over = ["57", "58", "59", "60", "61", "62", "63", "64"]
        self.standing = ["85", "86", "87", "88", "89", "90", "89", "88", "87", "86", "85"]
        self.getting_hit = ["33", "34", "35", "36", "37", "38", "39"]
        self.defend = ["41", "42", "43", "44", "44", "44", "44", "43", "42", "41"]
        self.death = ["49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["66", "67", "68", "69", "70", "72", "74"]
        self.attack_straight = ["23", "24", "25", "26", "27", "29", "31"]
        self.attack_down = ["76", "77", "78", "79", "80", "82", "84"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -5
        self.img_shift_y = 10

        self.update_hex(i, j)
        self.create_animation('standing')


class Nixwarr(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nixwarr'
        self.attack = 14
        self.defense = 17
        self.damage = [18, 22]
        self.health = 100
        self.speed = 7
        self.ai = 2116

        self.cur_health = self.health

        self.moving = ["14", "15", "16", "17", "18", "19", "20", "21"]
        self.mouse_over = ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"]
        self.standing = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["25", "26", "27", "28", "29", "30", "31", "32"]
        self.defend = ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"]
        self.death = ["48", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["61", "62", "63", "64", "65", "66", "67", "68", "69"]
        self.attack_straight = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.attack_down = ["70", "71", "72", "73", "74", "75", "76", "77"]

        self.img_size_x = 196
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Nix(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nix'
        self.attack = 13
        self.defense = 16
        self.damage = [18, 20]
        self.health = 90
        self.speed = 6
        self.ai = 1415

        self.cur_health = self.health

        self.moving = ["14", "15", "16", "17", "18", "19", "20", "21"]
        self.mouse_over = ["79", "80", "81", "82", "82", "82", "82", "81", "80", "79"]
        self.standing = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["25", "26", "27", "28", "29", "30", "31", "32"]
        self.defend = ["34", "35", "36", "37", "37", "37", "37", "36", "35", "34"]
        self.death = ["48", "49", "50", "51", "52", "53", "54", "55", "56"]
        self.dead = "56"
        self.attack_up = ["61", "62", "63", "64", "65", "66", "67", "68", "69"]
        self.attack_straight = ["39", "40", "41", "42", "43", "44", "45", "46"]
        self.attack_down = ["70", "71", "72", "73", "74", "75", "76", "77"]

        self.img_size_x = 196
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Sorcss(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'sorcss'
        self.attack = 12
        self.defense = 9
        self.damage = [10, 16]
        self.health = 35
        self.speed = 7
        self.arrows = 12
        self.ai = 852

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["141", "142", "143", "144", "145", "146", "145", "144", "143", "142", "141"]
        self.standing = ["120", "121", "122", "123", "122", "121", "120"]
        self.getting_hit = ["047", "048", "049", "050", "051", "052"]
        self.defend = ["127", "128", "129", "130", "131", "132", "133", "133", "133", "132", "131", "130", "129", "128", "127"]
        self.death = ["113", "114", "115", "116", "117", "118", "119"]
        self.dead = "119"
        self.attack_up = ["055", "056", "057", "059", "060", "063", "064", "066", "067", "069"]
        self.attack_straight = ["074", "075", "076", "078", "079", "082", "083", "085", "086", "085"]
        self.attack_down = ["093", "094", "095", "097", "098", "101", "102", "104", "105", "107"]
        self.shoot_up = ["015", "016", "017", "018", "019", "020", "021", "022", "023"]
        self.shoot_straight = ["026", "027", "028", "029", "030", "031", "032", "033", "034"]
        self.shoot_down = ["037", "038", "039", "040", "041", "042", "043", "044", "045"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Priest(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'priest'
        self.attack = 12
        self.defense = 7
        self.damage = [10, 14]
        self.health = 35
        self.speed = 6
        self.arrows = 12
        self.ai = 790

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["141", "142", "143", "144", "145", "146", "145", "144", "143", "142", "141"]
        self.standing = ["120", "121", "122", "123", "122", "121", "120"]
        self.getting_hit = ["047", "048", "049", "050", "051", "052"]
        self.defend = ["127", "128", "129", "130", "131", "132", "133", "133", "133", "132", "131", "130", "129", "128", "127"]
        self.death = ["113", "114", "115", "116", "117", "118", "119"]
        self.dead = "119"
        self.attack_up = ["055", "056", "057", "059", "060", "063", "064", "066", "067", "069"]
        self.attack_straight = ["074", "075", "076", "078", "079", "082", "083", "085", "086", "085"]
        self.attack_down = ["093", "094", "095", "097", "098", "101", "102", "104", "105", "107"]
        self.shoot_up = ["015", "016", "017", "018", "019", "020", "021", "022", "023"]
        self.shoot_straight = ["026", "027", "028", "029", "030", "031", "032", "033", "034"]
        self.shoot_down = ["037", "038", "039", "040", "041", "042", "043", "044", "045"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Assidup(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'assidup'
        self.attack = 11
        self.defense = 8
        self.damage = [6, 10]
        self.health = 30
        self.speed = 11
        self.ai = 645

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
        self.mouse_over = ["56", "57", "58", "59", "59", "59", "59", "58", "57", "56"]
        self.standing = ["60", "61", "62", "63", "64", "63", "62", "61"]
        self.getting_hit = ["45", "46", "47", "48", "49", "50", "51"]
        self.defend = ["74", "75", "76", "77", "78", "78", "78", "78", "77", "76", "75", "74"]
        self.death = ["65", "66", "67", "68", "69", "70", "71", "72"]
        self.dead = "72"
        self.attack_up = ["27", "28", "29", "30", "31", "32", "33", "34"]
        self.attack_straight = ["18", "19", "20", "21", "22", "23", "24", "25"]
        self.attack_down = ["36", "37", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Assid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'assid'
        self.attack = 10
        self.defense = 8
        self.damage = [6, 9]
        self.health = 30
        self.speed = 9
        self.ai = 502

        self.cur_health = self.health
        self.is_flyer = True

        self.moving = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
        self.mouse_over = ["56", "57", "58", "59", "59", "59", "59", "58", "57", "56"]
        self.standing = ["60", "61", "62", "63", "64", "63", "62", "61"]
        self.getting_hit = ["45", "46", "47", "48", "49", "50", "51"]
        self.defend = ["74", "75", "76", "77", "78", "78", "78", "78", "77", "76", "75", "74"]
        self.death = ["65", "66", "67", "68", "69", "70", "71", "72"]
        self.dead = "72"
        self.attack_up = ["27", "28", "29", "30", "31", "32", "33", "34"]
        self.attack_straight = ["18", "19", "20", "21", "22", "23", "24", "25"]
        self.attack_down = ["36", "37", "38", "39", "40", "41", "42", "43"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = 0
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Pr3up(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pr3up'
        self.attack = 12
        self.defense = 11
        self.damage = [3, 7]
        self.health = 16
        self.speed = 8
        self.arrows = 12
        self.ai = 602

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["014", "015", "016", "017", "018", "019", "020", "021"]
        self.standing = ["022", "023", "024", "025", "026", "025", "024", "023"]
        self.getting_hit = ["031", "032", "033", "034", "035", "036"]
        self.defend = ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"]
        self.death = ["043", "044", "045", "046", "047", "048"]
        self.dead = "048"
        self.attack_up = ["053", "054", "055", "056", "057", "058", "059"]
        self.attack_straight = ["061", "062", "063", "064", "065", "066", "067"]
        self.attack_down = ["069", "070", "071", "072", "073", "074", "075"]
        self.shoot_up = ["077", "079", "081", "082", "086", "087", "088", "089", "090"]
        self.shoot_straight = ["092", "094", "096", "097", "101", "102", "103", "104", "105"]
        self.shoot_down = ["107", "109", "111", "113", "116", "117", "118", "119", "120"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Corsair(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'corsair'
        self.attack = 10
        self.defense = 8
        self.damage = [3, 7]
        self.health = 15
        self.speed = 7
        self.arrows = 4
        self.ai = 407

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["014", "015", "016", "017", "018", "019", "020", "021"]
        self.standing = ["022", "023", "024", "025", "026", "025", "024", "023"]
        self.getting_hit = ["031", "032", "033", "034", "035", "036"]
        self.defend = ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"]
        self.death = ["043", "044", "045", "046", "047", "048"]
        self.dead = "048"
        self.attack_up = ["053", "054", "055", "056", "057", "058", "059"]
        self.attack_straight = ["061", "062", "063", "064", "065", "066", "067"]
        self.attack_down = ["069", "070", "071", "072", "073", "074", "075"]
        self.shoot_up = ["077", "079", "081", "082", "086", "087", "088", "089", "090"]
        self.shoot_straight = ["092", "094", "096", "097", "101", "102", "103", "104", "105"]
        self.shoot_down = ["107", "109", "111", "113", "116", "117", "118", "119", "120"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Pirate(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'pirate'
        self.attack = 8
        self.defense = 6
        self.damage = [3, 7]
        self.health = 15
        self.speed = 6
        self.arrows = 4
        self.ai = 312

        self.cur_health = self.health
        self.is_shooter = True

        self.moving = ["003", "004", "005", "006", "007", "008", "009", "010"]
        self.mouse_over = ["014", "015", "016", "017", "018", "019", "020", "021"]
        self.standing = ["022", "023", "024", "025", "026", "025", "024", "023"]
        self.getting_hit = ["031", "032", "033", "034", "035", "036"]
        self.defend = ["038", "039", "040", "041", "041", "041", "041", "040", "039", "038"]
        self.death = ["043", "044", "045", "046", "047", "048"]
        self.dead = "048"
        self.attack_up = ["053", "054", "055", "056", "057", "058", "059"]
        self.attack_straight = ["061", "062", "063", "064", "065", "066", "067"]
        self.attack_down = ["069", "070", "071", "072", "073", "074", "075"]
        self.shoot_up = ["077", "079", "081", "082", "086", "087", "088", "089", "090"]
        self.shoot_straight = ["092", "094", "096", "097", "101", "102", "103", "104", "105"]
        self.shoot_down = ["107", "109", "111", "113", "116", "117", "118", "119", "120"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Swash(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'swash'
        self.attack = 8
        self.defense = 6
        self.damage = [3, 4]
        self.health = 15
        self.speed = 6
        self.ai = 174

        self.cur_health = self.health

        self.moving = ["03", "04", "05", "06", "07", "08", "09", "10"]
        self.mouse_over = ["26", "27", "28", "29", "30", "31", "32", "33", "34"]
        self.standing = ["00", "68", "69", "70", "71", "72", "71", "70", "69", "68"]
        self.getting_hit = ["20", "21", "22", "23", "24", "25", "26"]
        self.defend = ["15", "16", "17", "18", "18", "18", "18", "17", "16", "15"]
        self.death = ["59", "60", "61", "62", "63", "64"]
        self.dead = "64"
        self.attack_up = ["43", "44", "45", "46", "47", "48", "49"]
        self.attack_straight = ["35", "36", "37", "38", "39", "40", "41"]
        self.attack_down = ["51", "52", "53", "54", "55", "56", "57"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Seadog(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'seadog'
        self.attack = 7
        self.defense = 4
        self.damage = [2, 4]
        self.health = 15
        self.speed = 5
        self.ai = 155

        self.cur_health = self.health

        self.moving = ["03", "04", "05", "06", "07", "08", "09", "10"]
        self.mouse_over = ["26", "27", "28", "29", "30", "31", "32", "33", "34"]
        self.standing = ["00", "68", "69", "70", "71", "72", "71", "70", "69", "68"]
        self.getting_hit = ["20", "21", "22", "23", "24", "25", "26"]
        self.defend = ["15", "16", "17", "18", "18", "18", "18", "17", "16", "15"]
        self.death = ["59", "60", "61", "62", "63", "64"]
        self.dead = "64"
        self.attack_up = ["43", "44", "45", "46", "47", "48", "49"]
        self.attack_straight = ["35", "36", "37", "38", "39", "40", "41"]
        self.attack_down = ["51", "52", "53", "54", "55", "56", "57"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = -5

        self.update_hex(i, j)
        self.create_animation('standing')


class Oceanid(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'oceanid'
        self.attack = 6
        self.defense = 2
        self.damage = [1, 3]
        self.health = 4
        self.speed = 8
        self.ai = 75

        self.cur_health = self.health
        self.is_jumper = True

        self.moving = ["02"]
        self.mouse_over = ["71", "72", "73", "74", "75", "75", "75", "74", "73", "72", "71"]
        self.standing = ["02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["42", "43", "44", "45", "46", "47"]
        self.defend = ["38", "39", "40", "41", "41", "41", "41", "40", "39", "38"]
        self.death = ["62", "63", "64", "65", "66", "67", "68", "69", "70"]
        self.dead = "70"
        self.attack_up = ["20", "21", "22", "23", "24", "25", "26", "27"]
        self.attack_straight = ["11", "12", "13", "14", "15", "16", "17", "18"]
        self.attack_down = ["29", "30", "31", "32", "33", "34", "35", "36"]
        self.start_moving = ["49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61"]
        self.stop_moving = ["61", "60", "59", "58", "57", "56", "55", "54", "53", "52", "51", "50", "49"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')


class Nimph(Units):

    def __init__(self, i, j, count, team):
        super().__init__(count, team)

        self.character = 'nimph'
        self.attack = 5
        self.defense = 2
        self.damage = [1, 2]
        self.health = 4
        self.speed = 6
        self.ai = 57

        self.cur_health = self.health
        self.is_jumper = True

        self.moving = ["02"]
        self.mouse_over = ["71", "72", "73", "74", "75", "75", "75", "74", "73", "72", "71"]
        self.standing = ["02", "03", "04", "05", "06", "07", "08", "09"]
        self.getting_hit = ["42", "43", "44", "45", "46", "47"]
        self.defend = ["38", "39", "40", "41", "41", "41", "41", "40", "39", "38"]
        self.death = ["62", "63", "64", "65", "66", "67", "68", "69", "70"]
        self.dead = "70"
        self.attack_up = ["20", "21", "22", "23", "24", "25", "26", "27"]
        self.attack_straight = ["11", "12", "13", "14", "15", "16", "17", "18"]
        self.attack_down = ["29", "30", "31", "32", "33", "34", "35", "36"]
        self.start_moving = ["49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61"]
        self.stop_moving = ["61", "60", "59", "58", "57", "56", "55", "54", "53", "52", "51", "50", "49"]

        self.img_size_x = 216
        self.img_size_y = self.img_size_x / 1.125
        self.img_shift_x = -25
        self.img_shift_y = 0

        self.update_hex(i, j)
        self.create_animation('standing')

    def create_moving(self, goal_row, goal_col):
        self.select_animation('start_moving')
        self.hex_worker.update_character_position(goal_row, goal_col)
        self.select_animation('stop_moving')
