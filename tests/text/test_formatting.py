#!/usr/bin/env python

"""Tests for `pyeo` package."""
from pyeo.text.base import TextOf
from pyeo.text.fomat import Formatted


def test_formatting():
    text = Formatted(
        TextOf("Hello {}. {} Do you like {}?"),
        TextOf('PyEO'),
        TextOf('How are you?'),
        TextOf('Java')
    )
    assert text.asStr() == "Hello PyEO. How are you? Do you like Java?", "test failed"
