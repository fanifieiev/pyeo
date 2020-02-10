#!/usr/bin/env python

"""Tests for `pyeo` package."""

from pyeo.scalar.numeric import SumOf, LenOf


def test_sum_of_ints():
    sum = SumOf([1, 2, 3, 4, 0.14]).value()
    assert sum == 10.14, "test failed"


def test_len_of():
    assert LenOf([1, 2, 3, 4, 0.14]).value() == 5, "test failed"

# def test_avg_of_ints():
#     avg = AvgOf(
#         [1, 1, 1, 1]
#     ).value()
#     assert avg == 1.0, "test failed"
