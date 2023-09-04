from .castle import Angel, RGrif, Crusd, Hcbow
from .rampart import Elf
from .tower import Genie, Mage, GremM
from .inferno import Adevl, Efree
from .necropolis import PLich, Lich, Skele
from .stronghold import Cyclp
from .fortress import Hydra
from .conflux import Psyel, Nrg, Storm
from .dungeon import BDragon, Cmcor, Minok, Harph, Harpy


def unit(name, i, j, count, team):
    # castle
    if name == 'angel':
        return Angel(i, j, count, team)
    if name == "crusd":
        return Crusd(i, j, count, team)
    if name == 'rgrif':
        return RGrif(i, j, count, team)
    if name == 'hcbow':
        return Hcbow(i, j, count, team)

    # rampart
    if name == 'elf':
        return Elf(i, j, count, team)

    # tower
    if name == 'genie':
        return Genie(i, j, count, team)
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
    if name == 'plich':
        return PLich(i, j, count, team)
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
    if name == 'psyel':
        return Psyel(i, j, count, team)
    if name == 'nrg':
        return Nrg(i, j, count, team)
    if name == 'storm':
        return Storm(i, j, count, team)

    # dungeon
    if name == 'bdrgn':
        return BDragon(i, j, count, team)
    if name == 'cmcor':
        return Cmcor(i, j, count, team)
    if name == 'minok':
        return Minok(i, j, count, team)
    if name == 'harph':
        return Harph(i, j, count, team)
    if name == 'harpy':
        return Harpy(i, j, count, team)
