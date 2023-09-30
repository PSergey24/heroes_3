from .castle import Rangl, Angel, Champ, Cavlr, Monkk, RGrif, Griff, Crusd, Sword, Hcbow, Halbd, Pkman
from .rampart import Ddrag, Gdrag, Wunic, Unico, Btree, Tree, Apegs, Pegas, Grelf, Elf, Bdwar, Dwarf, Ecent, Centr
from .tower import Gtita, Ltita, Nagag, Naga, Genie, Mage, Igole, Ogarg, Gargo, GremM, Grema
from .inferno import Adevl, Devil, Efree, Pfoe, Pfien, Thdem, Ohdem, Cerbu, Gog, Famil
from .necropolis import Ndrgn, Blord, Bknig, PLich, Lich, Nosfe, Vamp, Wrait, Wight, Zombi, Wskel, Skele
from .stronghold import Abehe, Ybehe, Cyclr, Cyclp, Tbird, Roc, Ogmag, Orc, Uwlfr, Hgobl, Gobli
from .fortress import Chydr, Hydra, Wyvmn, Wyver, Cgorg, Basil, Drfly, Aliza, Pliza, Gnolm, Gnoll
from .conflux import Phx, Fbird, Magel, Psyel, Eelem, Ston, Nrg, Icee, Storm, Sprit
from .dungeon import BDragon, Rdrgn, Cmcor, Minok, Meduq, Medus, Eveye, Harph, Harpy, Itrog
from .berth import Haspid, Serpent, Nixwarr, Nix, Sorcss, Priest, Assidup, Assid, Pr3up, Corsair, Pirate, Swash, Seadog, Oceanid, Nimph


def unit(name, i, j, count, team):
    # castle
    if name == 'rangl':
        return Rangl(i, j, count, team)
    if name == 'angel':
        return Angel(i, j, count, team)
    if name == 'champ':
        return Champ(i, j, count, team)
    if name == 'cavlr':
        return Cavlr(i, j, count, team)
    if name == "monkk":
        return Monkk(i, j, count, team)
    if name == "crusd":
        return Crusd(i, j, count, team)
    if name == "sword":
        return Sword(i, j, count, team)
    if name == 'rgrif':
        return RGrif(i, j, count, team)
    if name == 'griff':
        return Griff(i, j, count, team)
    if name == 'hcbow':
        return Hcbow(i, j, count, team)
    if name == 'halbd':
        return Halbd(i, j, count, team)
    if name == 'pkman':
        return Pkman(i, j, count, team)

    # rampart
    if name == 'ddrag':
        return Ddrag(i, j, count, team)
    if name == 'gdrag':
        return Gdrag(i, j, count, team)
    if name == 'wunic':
        return Wunic(i, j, count, team)
    if name == 'unico':
        return Unico(i, j, count, team)
    if name == 'btree':
        return Btree(i, j, count, team)
    if name == 'tree':
        return Tree(i, j, count, team)
    if name == 'apegs':
        return Apegs(i, j, count, team)
    if name == 'pegas':
        return Pegas(i, j, count, team)
    if name == 'grelf':
        return Grelf(i, j, count, team)
    if name == 'elf':
        return Elf(i, j, count, team)
    if name == 'bdwar':
        return Bdwar(i, j, count, team)
    if name == 'dwarf':
        return Dwarf(i, j, count, team)
    if name == 'ecent':
        return Ecent(i, j, count, team)
    if name == 'centr':
        return Centr(i, j, count, team)

    # tower
    if name == 'gtita':
        return Gtita(i, j, count, team)
    if name == 'ltita':
        return Ltita(i, j, count, team)
    if name == 'nagag':
        return Nagag(i, j, count, team)
    if name == 'naga':
        return Naga(i, j, count, team)
    if name == 'genie':
        return Genie(i, j, count, team)
    if name == 'mage':
        return Mage(i, j, count, team)
    if name == 'igole':
        return Igole(i, j, count, team)
    if name == 'ogarg':
        return Ogarg(i, j, count, team)
    if name == 'gargo':
        return Gargo(i, j, count, team)
    if name == 'gremm':
        return GremM(i, j, count, team)
    if name == 'grema':
        return Grema(i, j, count, team)

    # inferno
    if name == 'adevl':
        return Adevl(i, j, count, team)
    if name == 'devil':
        return Devil(i, j, count, team)
    if name == 'efree':
        return Efree(i, j, count, team)
    if name == 'pfoe':
        return Pfoe(i, j, count, team)
    if name == 'pfien':
        return Pfien(i, j, count, team)
    if name == 'thdem':
        return Thdem(i, j, count, team)
    if name == 'ohdem':
        return Ohdem(i, j, count, team)
    if name == 'cerbu':
        return Cerbu(i, j, count, team)
    if name == 'gog':
        return Gog(i, j, count, team)
    if name == 'famil':
        return Famil(i, j, count, team)

    # necropolis
    if name == 'ndrgn':
        return Ndrgn(i, j, count, team)
    if name == 'blord':
        return Blord(i, j, count, team)
    if name == 'bknig':
        return Bknig(i, j, count, team)
    if name == 'plich':
        return PLich(i, j, count, team)
    if name == 'lich':
        return Lich(i, j, count, team)
    if name == 'nosfe':
        return Nosfe(i, j, count, team)
    if name == 'vamp':
        return Vamp(i, j, count, team)
    if name == 'wrait':
        return Wrait(i, j, count, team)
    if name == 'wight':
        return Wight(i, j, count, team)
    if name == 'zombi':
        return Zombi(i, j, count, team)
    if name == 'wskel':
        return Wskel(i, j, count, team)
    if name == 'skele':
        return Skele(i, j, count, team)

    # stronghold
    if name == 'abehe':
        return Abehe(i, j, count, team)
    if name == 'ybehe':
        return Ybehe(i, j, count, team)
    if name == 'cyclr':
        return Cyclr(i, j, count, team)
    if name == 'cyclp':
        return Cyclp(i, j, count, team)
    if name == 'tbird':
        return Tbird(i, j, count, team)
    if name == 'roc':
        return Roc(i, j, count, team)
    if name == 'ogmag':
        return Ogmag(i, j, count, team)
    if name == 'orc':
        return Orc(i, j, count, team)
    if name == 'uwlfr':
        return Uwlfr(i, j, count, team)
    if name == 'hgobl':
        return Hgobl(i, j, count, team)
    if name == 'gobli':
        return Gobli(i, j, count, team)

    # fortress
    if name == 'chydr':
        return Chydr(i, j, count, team)
    if name == 'hydra':
        return Hydra(i, j, count, team)
    if name == 'wyvmn':
        return Wyvmn(i, j, count, team)
    if name == 'wyver':
        return Wyver(i, j, count, team)
    if name == 'cgorg':
        return Cgorg(i, j, count, team)
    if name == 'basil':
        return Basil(i, j, count, team)
    if name == 'drfly':
        return Drfly(i, j, count, team)
    if name == 'aliza':
        return Aliza(i, j, count, team)
    if name == 'pliza':
        return Pliza(i, j, count, team)
    if name == 'gnolm':
        return Gnolm(i, j, count, team)
    if name == 'gnoll':
        return Gnoll(i, j, count, team)

    # conflux
    if name == 'phx':
        return Phx(i, j, count, team)
    if name == 'fbird':
        return Fbird(i, j, count, team)
    if name == 'magel':
        return Magel(i, j, count, team)
    if name == 'psyel':
        return Psyel(i, j, count, team)
    if name == 'eelem':
        return Eelem(i, j, count, team)
    if name == 'ston':
        return Ston(i, j, count, team)
    if name == 'nrg':
        return Nrg(i, j, count, team)
    if name == 'icee':
        return Icee(i, j, count, team)
    if name == 'storm':
        return Storm(i, j, count, team)
    if name == 'sprit':
        return Sprit(i, j, count, team)

    # dungeon
    if name == 'bdrgn':
        return BDragon(i, j, count, team)
    if name == 'rdrgn':
        return Rdrgn(i, j, count, team)
    if name == 'cmcor':
        return Cmcor(i, j, count, team)
    if name == 'minok':
        return Minok(i, j, count, team)
    if name == 'meduq':
        return Meduq(i, j, count, team)
    if name == 'medus':
        return Medus(i, j, count, team)
    if name == 'eveye':
        return Eveye(i, j, count, team)
    if name == 'harph':
        return Harph(i, j, count, team)
    if name == 'harpy':
        return Harpy(i, j, count, team)
    if name == 'itrog':
        return Itrog(i, j, count, team)

    # berth
    if name == 'haspid':
        return Haspid(i, j, count, team)
    if name == 'serpent':
        return Serpent(i, j, count, team)
    if name == 'nixwarr':
        return Nixwarr(i, j, count, team)
    if name == 'nix':
        return Nix(i, j, count, team)
    if name == 'sorcss':
        return Sorcss(i, j, count, team)
    if name == 'priest':
        return Priest(i, j, count, team)
    if name == 'assidup':
        return Assidup(i, j, count, team)
    if name == 'assid':
        return Assid(i, j, count, team)
    if name == 'pr3up':
        return Pr3up(i, j, count, team)
    if name == 'corsair':
        return Corsair(i, j, count, team)
    if name == 'pirate':
        return Pirate(i, j, count, team)
    if name == 'swash':
        return Swash(i, j, count, team)
    if name == 'seadog':
        return Seadog(i, j, count, team)
    if name == 'oceanid':
        return Oceanid(i, j, count, team)
    if name == 'nimph':
        return Nimph(i, j, count, team)
