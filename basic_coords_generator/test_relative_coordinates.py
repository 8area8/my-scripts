#! /usr/bin/env python3
# coding: utf-8

"""Test in main file: relative_coordinates."""

import pytest

from my_scripts.basic_coords_generator.main import relative_coordinates


@pytest.mark.parametrize("distance, expected", [
    (1, {(1, 0), (0, 1), (-1, 0), (0, -1)}),
    (2, {(2, 0), (0, 2), (-2, 0), (0, -2),
         (1, 1), (-1, 1), (1, -1), (-1, -1)}), ])
def test_realtives_coordinates(distance, expected):
    """Test relative_coordinates."""
    result = relative_coordinates(distance, distance)
    for value in result:
        print(value)
        assert value in expected
