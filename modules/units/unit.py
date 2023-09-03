from .castle import Angel, RGrif, Hcbow
from .rampart import Elf
from .tower import Mage, GremM
from .inferno import Adevl, Efree
from .necropolis import Lich, Skele
from .stronghold import Cyclp
from .fortress import Hydra
# from .conflux import
from .dungeon import BDragon, Cmcor


def unit(name, i, j, count, team):
    # castle
    if name == 'angel':
        return Angel(i, j, count, team)
    if name == 'rgrif':
        return RGrif(i, j, count, team)
    if name == 'hcbow':
        return Hcbow(i, j, count, team)

    # rampart
    if name == 'elf':
        return Elf(i, j, count, team)

    # tower
    if name == 'mage':
        return Mage(i, j, count, team)
    if name == 'gremm':
        return GremM(i, j, count, team)

    # inferno
    if name == 'adevl':
        return Adevl(i, j, count, team)
    if name == 'efree':
        return Efree(i, j, count, team)

    # necropolis
    if name == 'lich':
        return Lich(i, j, count, team)
    if name == 'skele':
        return Skele(i, j, count, team)

    # stronghold
    if name == 'cyclp':
        return Cyclp(i, j, count, team)

    # fortress
    if name == 'hydra':
        return Hydra(i, j, count, team)

    # conflux

    # dungeon
    if name == 'bdrgn':
        return BDragon(i, j, count, team)
    if name == 'cmcor':
        return Cmcor(i, j, count, team)
