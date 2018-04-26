#! /usr/bin/env python3
# coding: utf-8

"""Test the generator file."""

import inspect

from my_scripts.basic_coords_generator.generator import relative_coords


def create_generator():
    """Create a generator from relative_coords."""
    return next(relative_coords())


def test_is_a_generator():
    """Test if relative_coords is a generator."""
    assert inspect.isgeneratorfunction(relative_coords)


def test_return_a_list():
    """Test if relative_coords return a list."""
    assert isinstance(create_generator(), list)


def test_list_contains_tuples():
    """Test if the returned list contains tuple."""
    generator = create_generator()

    assert generator != []
    for value in generator:
        assert isinstance(value, tuple)


def test_tuples_contains_two_numbers():
    """Test if tuples contains two int numbers."""
    generator = create_generator()

    for value in [item for item in generator]:
        assert isinstance(value, int)
