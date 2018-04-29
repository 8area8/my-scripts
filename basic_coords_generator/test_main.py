#! /usr/bin/env python3
# coding: utf-8

"""Test in main file: relative_coords."""

import inspect

from my_scripts.basic_coords_generator.main import relative_coords


def return_first_yield():
    """Create a generator from relative_coords; return the first Next value."""
    return next(relative_coords())


def test_is_a_generator():
    """Test if relative_coords is a generator."""
    assert inspect.isgeneratorfunction(relative_coords)


def test_return_a_list():
    """Test if relative_coords return a list."""
    assert isinstance(return_first_yield(), list)


def test_list_contains_tuples():
    """Test if the returned list contains tuple."""
    first_yield = return_first_yield()

    assert first_yield != []
    for value in first_yield:
        assert isinstance(value, tuple)


def test_tuples_contains_two_numbers():
    """Test if tuples contains two int numbers."""
    first_yield = return_first_yield()

    for a_tuple in first_yield:
        assert len(a_tuple) == 2

        for number in a_tuple:
            assert isinstance(number, int)


def test_tuple_result_one():
    """Test if the tuples (coordinates) correspond to a moove by one case."""
    first_yield = return_first_yield()

    possible_mooves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for a, b in first_yield:
        assert (a, b) in possible_mooves


def test_others_tuple_results():
    """Test others results: display them."""
    coords_generator = relative_coords()
    max_moove = 10

    print('\n')
    for i, value in enumerate(coords_generator):
        if i == max_moove:
            break

        value.sort(key=lambda x: max(abs(x[0]), abs(x[1])))
        print(value)
