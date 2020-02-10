#!/usr/bin/env python
from pyeo.scalar.base import Scalar
from pyeo.scalar.mapping import Mapped
from pyeo.scalar.numeric import SumOf


def test_mapping_with_lambda():
    scalar: Scalar[str] = Mapped[int, str](
        lambda num: str(num),
        SumOf([1, 2, 3, 4, 5])
    )
    assert scalar.value() == "15", "test failed"


def test_mapping_with_func_method():
    def convert(num: int) -> str:
        return str(num)

    scalar: Scalar[str] = Mapped[int, str](
        convert,
        SumOf([1, 2, 3, 4, 5])
    )
    assert scalar.value() == "15", "test failed"
