from typing import Iterable, TypeVar

from pyeo.scalar.base import Scalar

N = TypeVar('N', int, float)


class SumOf(Scalar[N]):
    def __init__(self, iterable: Iterable[N]):
        self.iterable = iterable

    def value(self) -> N:
        return sum(self.iterable)


class MinOf(Scalar[N]):
    def __init__(self, iterable: Iterable[N]):
        self.iterable = iterable

    def value(self) -> N:
        return min(self.iterable)


class MaxOf(Scalar[N]):
    def __init__(self, iterable: Iterable[N]):
        self.iterable = iterable

    def value(self) -> N:
        return max(self.iterable)


class AvgOf(Scalar[N]):
    def __init__(self, iterable: Iterable[N]):
        self.iterable = iterable

    def value(self) -> N:
        return DivisionOf(
            SumOf(self.iterable),
            LenOf(self.iterable)
        ).value(),


class DivisionOf(Scalar[N]):
    def __init__(self, first: Scalar[N], second: Scalar[N]):
        self.first = first
        self.second = second

    def value(self) -> N:
        return self.first.value() / self.second.value()


class LenOf(Scalar[N]):
    def __init__(self, iterable: Iterable[N]):
        self.iterable = iterable

    def value(self) -> int:
        return len(self.iterable)
