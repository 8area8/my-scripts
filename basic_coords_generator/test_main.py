#! /usr/bin/env python3
# coding: utf-8

"""Test in main file: relative_coordinates."""

from collections.abc import Collection
import pytest

from my_scripts.basic_coords_generator.main import relative_coordinates


def test_relative_coordinates_returns_collection():
    """Test if the value is a 'sized iterable container class'."""
    assert isinstance([relative_coordinates(2, 2)], Collection)


@pytest.mark.parametrize("distance, expected", [
    (1, {(1, 0), (-1, 0), (0, 1), (0, -1)}),
    (2, {(1, 0), (-1, 0), (0, 1), (0, -1),
         (2, 0), (1, 1), (0, 2), (-1, 1),
         (-2, 0), (-1, -1), (0, -2), (1, -1)}), ])
def test_relative_coords_distance_1(distance, expected):
    """Test if results correspond to the expected values."""
    result = relative_coordinates(distance, distance)
    for value in result:
        assert value in expected


def test_and_display_results():
    """Display the results."""
    generator = relative_coordinates(end=10)

    print('\n')
    for value in generator:
        print(sorted(value,
                     key=lambda x: max(abs(x[0]), abs(x[1])),
                     reverse=True))
