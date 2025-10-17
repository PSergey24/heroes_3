from modules.settings import Settings


def compute_reachable_points(unit_info, field, tools):
    speed = unit_info.characteristics.get("base_characteristics", {}).get("speed", 0)
    is_flyer = unit_info.characteristics.get("is_flyer", False)
    is_jumper = unit_info.characteristics.get("is_jumper", False)

    start_cube = tools.offset2cube(unit_info.hex[0][0], unit_info.hex[0][1])
    visited = set()
    visited.add(tools.cube2offset(start_cube[0], start_cube[1], start_cube[2]))

    level = 0
    queue = [(start_cube, level)]
    while queue:
        (x, y, z), level = queue.pop(0)
        level += 1
        for i in range(6):
            nb = tools.cube_neighbor((x, y, z), i)
            r, c = tools.cube2offset(nb[0], nb[1], nb[2])
            if 0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns:
                engaged = field.hexagons[r][c].engaged
                same = engaged is not None and id(engaged) == id(unit_info)
                free_or_allowed = engaged is None or same or is_flyer or is_jumper
                if (r, c) not in visited and free_or_allowed and level <= speed:
                    visited.add((r, c))
                    queue.append((nb, level))

    return visited


