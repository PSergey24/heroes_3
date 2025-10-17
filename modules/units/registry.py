import inspect
import re

from . import castle, rampart, tower, inferno, necropolis, stronghold, fortress, conflux, dungeon, berth, neutral


_NAME_ASSIGNMENT_RE = re.compile(r"self\s*\.\s*name\s*=\s*['\"]([a-z0-9_]+)['\"]", re.IGNORECASE)


def _extract_unit_code_name(cls):
    try:
        src = inspect.getsource(cls)
    except OSError:
        return None
    m = _NAME_ASSIGNMENT_RE.search(src)
    if m:
        return m.group(1).lower()
    return None


def _collect_unit_classes():
    modules = [castle, rampart, tower, inferno, necropolis, stronghold, fortress, conflux, dungeon, berth, neutral]
    name_to_class = {}
    for mod in modules:
        for _, cls in inspect.getmembers(mod, inspect.isclass):
            code_name = _extract_unit_code_name(cls)
            if code_name:
                name_to_class.setdefault(code_name, cls)
            # also register by lowercased class name as a fallback alias
            name_to_class.setdefault(cls.__name__.lower(), cls)
    return name_to_class


_UNIT_CLASSES = _collect_unit_classes()


def get_unit_class(name: str):
    key = name.lower()
    if key in _UNIT_CLASSES:
        return _UNIT_CLASSES[key]
    raise KeyError(f"Unknown unit name: {name}")


def unit(name: str, i: int, j: int, count: int, team: int):
    return get_unit_class(name)(i, j, count, team)


