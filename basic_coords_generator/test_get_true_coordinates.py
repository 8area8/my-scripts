#! /usr/bin/env python3
# coding: utf-8

"""Test in main file: get_true_coordinates."""

import pytest

from my_scripts.basic_coords_generator.main import relative_coordinates
from my_scripts.basic_coords_generator.main import get_true_coordinates


@pytest.mark.parametrize("position, distance, expected", [
    ((10, -6), 1, {(11, -6), (9, -6), (10, -5), (10, -7)}),
    ((1, 35), 2, {(2, 36), (1, 37), (1, 36), (1, 34),
                  (3, 35), (2, 36), (0, 37), (0, 36),
                  (-1, 35), (0, 34), (1, 33), (2, 34)}), ])
def test_relative_coords_distance_1(position, distance, expected):
    """Test if the relatives coords has changed to true coordinates."""
    coords = relative_coordinates(distance, distance)
    true_coords = get_true_coordinates(coords, position)
    for value in true_coords:
        assert value in expected
