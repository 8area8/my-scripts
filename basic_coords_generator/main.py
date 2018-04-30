#! /usr/bin/env python3
# coding: utf-8

"""Used to moove an object in a 2D Cases-Map."""

from itertools import product


def relative_coordinates(start=1, end=100):
    """Return relative coordinates from 'start' to 'end'.

    We use manhattan distance.
    (thanks to Dan737)
    """
    for distance in range(start, end):
        coordinates = set()

        for x in range(distance + 1):
            y = distance - x

            coordinates.update(set(product((x, -x), (y, -y))))

        yield coordinates
