import pytest

def add_numbers(a, b):#simple program that adds 2 numbers
    return a + b


def test_add_numbers_positive():#1 case test
    result = add_numbers(3, 5)
    assert result == 8

def test_add_numbers_negative():#2 case test
    result = add_numbers(-2, 7)
    assert result == 5