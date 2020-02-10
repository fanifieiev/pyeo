from numbers import Number
from typing import Iterable

from pyeo.scalar.base import Scalar


class SumOf(Scalar[Number]):
    def __init__(self, iterable: Iterable[Number]):
        self.iterable = iterable

    def value(self) -> Number:
        return sum(self.iterable)


class MinOf(Scalar[Number]):
    def __init__(self, iterable: Iterable[Number]):
        self.iterable = iterable

    def value(self) -> Number:
        return min(self.iterable)


class MaxOf(Scalar[Number]):
    def __init__(self, iterable: Iterable[Number]):
        self.iterable = iterable

    def value(self) -> Number:
        return max(self.iterable)


class AvgOf(Scalar[Number]):
    def __init__(self, iterable: Iterable[Number]):
        self.iterable = iterable

    def value(self) -> Number:
        return DivisionOf(
            SumOf(self.iterable),
            LenOf(self.iterable)
        ).value(),


class DivisionOf(Scalar[Number]):
    def __init__(self, first: Scalar[Number], second: Scalar[Number]):
        self.first = first
        self.second = second

    def value(self) -> Number:
        return self.first.value() / self.second.value()


class LenOf(Scalar[int]):
    def __init__(self, iterable: Iterable[Number]):
        self.iterable = iterable

    def value(self) -> int:
        return len(self.iterable)
