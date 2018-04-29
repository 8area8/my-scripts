#! /usr/bin/env python3
# coding: utf-8

"""Used to moove an object in a 2D Cases-Map."""


def relative_coords():
    """Return lists of coordinates, correspond to a moove distance."""
    max_moove = 0

    while True:
        max_moove += 1
        middle_mooves = (range(max_moove))
        coordinates_group = set()

        for x in middle_mooves:
            y = max_moove - x

            possible_mooves = {
                (x, y), (y, x), (-x, y), (-y, x),
                (x, -y), (y, -x), (-x, -y), (-y, -x)}  # TRICK: this is a Set

            coordinates_group.update(possible_mooves)

        yield list(coordinates_group)
