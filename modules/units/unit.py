from .castle import Angel, RGrif, Crusd, Hcbow
from .rampart import Btree, Tree, Elf
from .tower import Genie, Mage, GremM
from .inferno import Adevl, Efree, Famil
from .necropolis import PLich, Lich, Wskel, Skele
from .stronghold import Cyclp, Ogmag
from .fortress import Hydra
from .conflux import Psyel, Nrg, Storm
from .dungeon import BDragon, Cmcor, Minok, Harph, Harpy
from .berth import Nixwarr, Nix


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
    if name == 'btree':
        return Btree(i, j, count, team)
    if name == 'tree':
        return Tree(i, j, count, team)
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
    if name == 'famil':
        return Famil(i, j, count, team)

    # necropolis
    if name == 'plich':
        return PLich(i, j, count, team)
    if name == 'lich':
        return Lich(i, j, count, team)
    if name == 'wskel':
        return Wskel(i, j, count, team)
    if name == 'skele':
        return Skele(i, j, count, team)

    # stronghold
    if name == 'cyclp':
        return Cyclp(i, j, count, team)
    if name == 'ogmag':
        return Ogmag(i, j, count, team)

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

    # berth
    if name == 'nixwarr':
        return Nixwarr(i, j, count, team)
    if name == 'nix':
        return Nix(i, j, count, team)
