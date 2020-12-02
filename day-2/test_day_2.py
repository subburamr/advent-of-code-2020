"""Test cases for day 2."""
from day_2 import calculate_invalid_passwords, calculate_invalid_position


def test_calculate_invalid_passwords():
    assert calculate_invalid_passwords("test_data_input.txt") == 2


def test_calculate_invalid_passwords_position():
    assert calculate_invalid_position("test_data_input.txt") == 1
