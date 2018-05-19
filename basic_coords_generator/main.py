#! /usr/bin/env python3
# coding: utf-8

"""Used to moove an object in a 2D Cases-Map."""

from itertools import product


def relative_coordinates(start=1, end=100):
    """Return the relative coordinates of a distance from (0, 0).

    Capture coordinates from 'start' to 'end' include.
    Note: We use manhattan distance.
    (thanks to Dan737)
    """
    for distance in range(start, end + 1):

        for x in range(distance + 1):
            y = distance - x

            for coordinates in set(product((x, -x), (y, -y))):
                yield coordinates


def get_true_coordinates(coordinates, true_position):
    """Get true coordinates from a position."""
    a, b = true_position
    return ((x + a, y + b) for (x, y) in coordinates)
