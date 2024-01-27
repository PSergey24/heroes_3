import math
import pygame

pygame.init()


class Settings:
    # window
    width: int = 1200
    height: int = 800
    FONT = pygame.font.Font('data/fonts/Times New Roman Bold.ttf', 12)

    # field
    field_position = [160, 70]
    n_columns: int = 15
    n_rows: int = 11

    # hexagon
    R: int = 35
    r: float = round(math.sqrt(3) / 2 * R)
    bold: int = 1
    COLOR_BORDER = (128, 140, 64)
    COLOR_HOVER = (40, 40, 20, 150)
    COLOR_ACTIVE = (200, 200, 32)
    COLOR_POSSIBLE = (40, 40, 20, 90)

    # info block
    info_block_margin = 126
    info_block_width = width - 2 * info_block_margin
    info_block_height = 90
    left_ib_width = 117
    right_ib_width = 117
    center_ib_width = width - (left_ib_width + right_ib_width) - 2 * info_block_margin

    button_width = 44
    button_height = 36
    avatar_width = 53
    avatar_height = 59

    # special units:
    mass_attack_around = ["chydr", "hydra"]
    mass_attack_3 = ["magel", "psyel", "cerbu"]
    mass_fired = ["bdrgn", "rdrgn", "ddrag", "gdrag", "phx", "fbird", "adrgn"]
    mass_arrows = ["plich", "magog"]
    double_punch = ["crusd", "uwlfr"]

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
