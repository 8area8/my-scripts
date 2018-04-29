#! /usr/bin/env python3
# coding: utf-8

"""Used to moove an object in a 2D Cases-Map."""


def possible_coordinates():
    """Return lists of coordinates, correspond to a moove distance."""
    MAX_ITERATION = 100  # secure the generator
    max_moove = 0

    for _ in range(MAX_ITERATION):
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
