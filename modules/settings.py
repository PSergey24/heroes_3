import math
import pygame

pygame.init()


class Settings:
    width: int = 1200
    height: int = 800
    start_battle_filed = [160, 70]
    n_columns: int = 15
    n_rows: int = 11
    R: int = 35
    r: float = round(math.sqrt(3) / 2 * R)
    bold: int = 1
    COLOR_BORDER = (128, 140, 64)
    COLOR_HOVER = (40, 40, 40, 120)
    COLOR_ACTIVE = (255, 215, 0)
    COLOR_POSSIBLE = (0, 0, 140, 60)
    FONT = pygame.font.Font('data/fonts/Times New Roman Bold.ttf', 12)

    info_block_margin = 126
    info_block_width = width - 2 * info_block_margin
    info_block_height = 90
    left_ib_width = 115
    right_ib_width = 115
    center_ib_width = width - (left_ib_width + right_ib_width) - 2 * info_block_margin

    button_width = 44
    button_height = 36
    avatar_width = 58
    avatar_height = 64

    # special units
    double_hex_units = ["bdrgn", "rdrgn", "chydr", "hydra", "rgrif", "griff", "cmcor", "mcore", "tbird", "roc",
                        "hdrgn", "ndrgn", "gbasi", "basil", "cerbu", "hhoun", "apegs", "pegas", "phx", "fbird",
                        "nagag", "naga", "meduq", "medus", "ddrag", "gdrag", "wunic", "unico", "ecent", "centr",
                        "cavlr", "champ", "abehe", "ybehe", "bgorg", "cgorg", "wyvmn", "wyver", "assidup", "assid",
                        "blord", "bknig", "icee", "welem", "uwlfr", "bwlfr", "haspid", "serpent", "adrgn"]
    without_answer = ["chydr", "hydra", "corsair"]
    factions = {"Dungeon": ["bdrgn", "rdrgn", "cmcor", "mcore", "minok", "minot", "meduq", "medus", "eveye", "behol", "harph", "harpy", "itrog", "trogl"],
                "Conflux": ["phx", "fbird", "magel", "psyel", "eelem", "ston", "nrg", "felem", "icee", "welem", "storm", "aelem", "sprit", "pixie"],
                "Fortress": ["chydr", "hydra", "wyvmn", "wyver", "bgorg", "cgorg", "gbasi", "basil", "drfir", "drfly", "aliza", "pliza", "gnolm", "gnoll"],
                "Stronghold": ["abehe", "ybehe", "cyclr", "cyclp", "tbird", "roc", "ogmag", "ogre", "orcch", "orc", "uwlfr", "bwlfr", "hgobl", "gobli"],
                "Necropolis": ["hdrgn", "ndrgn", "blord", "bknig", "plich", "lich", "nosfe", "vamp", "wrait", "wight", "zomlo", "zombi", "wskel", "skele"],
                "Inferno": ["adevl", "devil", "efres", "efree", "pfoe", "pfien", "thdem", "ohdem", "cerbu", "hhoun", "magog", "gog", "famil", "imp"],
                "Tower": ["gtita", "ltita", "nagag", "naga", "sulta", "genie", "amage", "mage", "igole", "sgole", "ogarg", "gargo", "gremm", "grema"],
                "Rampart": ["ddrag", "gdrag", "wunic", "unico", "btree", "tree", "apegs", "pegas", "grelf", "elf", "bdwar", "dwarf", "ecent", "centr"],
                "Castle": ["rangl", "angel", "champ", "cavlr", "zealt", "monkk", "crusd", "sword", "rgrif", "griff", "hcbow", "lcbow", "halbd", "pkman"],
                "Berth": ["haspid", "serpent", "nixwarr", "nix", "sorcss", "priest", "assidup", "assid", "pr3up", "corsair", "pirate", "swash", "seadog", "oceanid", "nimph"],
                "Neutral": ["adrgn"]}


class States:
    # game info:
    step = 0
    round = 1
    is_animate = False
    hexagons = []

    # all units info:
    queue = None
    animations = []

    # active unit info:
    unit_active = None
    active_is_double = None
    speed_active = None
    reachable_points = None
    reachable_left_points = None
    reachable_right_points = None
    double_reachable_points = None
    whom_attack = None
    point_attack = None
    direction_attack = None

    # shooter btn info:
    btn_shooter = False
    penalty_shooter = 1

    # mouse cursor info:
    cursor = None
    cursor_direction = None
    point_over = None
    point_x = None
    point_y = None
    point_z = None
    point_r = None
    point_c = None

    # block info:
    main = None
    left = None
    center = None
    right = None
    top_center = None
    bottom_center = None
