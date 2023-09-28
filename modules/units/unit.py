from .castle import Rangl, Angel, RGrif, Crusd, Hcbow, Halbd
from .rampart import Btree, Tree, Apegs, Elf
from .tower import Ltita, Naga, Genie, Mage, Igole, GremM
from .inferno import Adevl, Efree, Cerbu, Famil
from .necropolis import Ndrgn, PLich, Lich, Nosfe, Wskel, Skele
from .stronghold import Cyclp, Roc, Ogmag, Gobli
from .fortress import Hydra, Basil, Gnolm
from .conflux import Fbird, Magel, Psyel, Eelem, Nrg, Storm, Sprit
from .dungeon import BDragon, Cmcor, Minok, Harph, Harpy
from .berth import Nixwarr, Nix


def unit(name, i, j, count, team):
    # castle
    if name == 'rangl':
        return Rangl(i, j, count, team)
    if name == 'angel':
        return Angel(i, j, count, team)
    if name == "crusd":
        return Crusd(i, j, count, team)
    if name == 'rgrif':
        return RGrif(i, j, count, team)
    if name == 'hcbow':
        return Hcbow(i, j, count, team)
    if name == 'halbd':
        return Halbd(i, j, count, team)

    # rampart
    if name == 'btree':
        return Btree(i, j, count, team)
    if name == 'tree':
        return Tree(i, j, count, team)
    if name == 'apegs':
        return Apegs(i, j, count, team)
    if name == 'elf':
        return Elf(i, j, count, team)

    # tower
    if name == 'ltita':
        return Ltita(i, j, count, team)
    if name == 'naga':
        return Naga(i, j, count, team)
    if name == 'genie':
        return Genie(i, j, count, team)
    if name == 'mage':
        return Mage(i, j, count, team)
    if name == 'igole':
        return Igole(i, j, count, team)
    if name == 'gremm':
        return GremM(i, j, count, team)

    # inferno
    if name == 'adevl':
        return Adevl(i, j, count, team)
    if name == 'efree':
        return Efree(i, j, count, team)
    if name == 'cerbu':
        return Cerbu(i, j, count, team)
    if name == 'famil':
        return Famil(i, j, count, team)

    # necropolis
    if name == 'ndrgn':
        return Ndrgn(i, j, count, team)
    if name == 'plich':
        return PLich(i, j, count, team)
    if name == 'lich':
        return Lich(i, j, count, team)
    if name == 'nosfe':
        return Nosfe(i, j, count, team)
    if name == 'wskel':
        return Wskel(i, j, count, team)
    if name == 'skele':
        return Skele(i, j, count, team)

    # stronghold
    if name == 'cyclp':
        return Cyclp(i, j, count, team)
    if name == 'roc':
        return Roc(i, j, count, team)
    if name == 'ogmag':
        return Ogmag(i, j, count, team)
    if name == 'gobli':
        return Gobli(i, j, count, team)

    # fortress
    if name == 'hydra':
        return Hydra(i, j, count, team)
    if name == 'basil':
        return Basil(i, j, count, team)
    if name == 'gnolm':
        return Gnolm(i, j, count, team)

    # conflux
    if name == 'fbird':
        return Fbird(i, j, count, team)
    if name == 'magel':
        return Magel(i, j, count, team)
    if name == 'psyel':
        return Psyel(i, j, count, team)
    if name == 'eelem':
        return Eelem(i, j, count, team)
    if name == 'nrg':
        return Nrg(i, j, count, team)
    if name == 'storm':
        return Storm(i, j, count, team)
    if name == 'sprit':
        return Sprit(i, j, count, team)

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
