#!/usr/bin/env python

"""Tests for `pyeo` package."""

from pyeo.text.base import TextOf
from pyeo.text.join import Joined


def test_joined_ints():
    joined = Joined(',', [TextOf('Fevzi'), TextOf('Anifieiev')])
    assert joined.asStr() == "Fevzi,Anifieiev", "test failed"
