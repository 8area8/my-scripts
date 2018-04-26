#! /usr/bin/env python3
# coding: utf-8

"""The source file."""


def relative_coords(max=10):
    """Return a list of coordinates.

    Used to moove an object in a 2D Cases_Map.
    """
    for _ in range(max):
        coords = []

        yield coords  # toutes les coords d'un cran


def get_relatives_moove_coords(relatives_coords=[], moove=8):
    """Return a list who contains the possibilities of movements.

    for each moove point, the list get a list of relatives coordinates.


    TIP: the 'relative_coords' parameter is created only ONE time,
    at the first function's call. As it is a mutable object,
    if we manipulate the parameter, it will save the changes.
    """
    relatives_coords.append([])

    for i in range(1, moove + 1):

        actual_list = relatives_coords[-1]
        a = moove - i
        b = i

        actual_list.append((a, b))
        actual_list.append((b, a))

        if a != 0:
            actual_list.append((-a, b))
            actual_list.append((b, -a))
        if b != 0:
            actual_list.append((a, -b))
            actual_list.append((-b, a))
        if a != 0 and b != 0:
            actual_list.append((-a, -b))
            actual_list.append((-b, -a))

    relatives_coords[-1] = list(set(actual_list))  # remove duplicates.
    relatives_coords[-1].sort(key=lambda x: max(abs(x[0]), abs(x[1])))
    """Wtf sorting. Not usefull but funny."""

    if moove > 1:
        get_relatives_moove_coords(moove=moove - 1)

    return relatives_coords


RELATIVES_COORDS = get_relatives_moove_coords()
RELATIVES_COORDS.sort(key=lambda x: [len(y) for y in x])
