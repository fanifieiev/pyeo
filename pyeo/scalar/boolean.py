from pyeo.scalar.base import Scalar


class Not(Scalar[bool]):
    def __init__(self, scalar: Scalar[bool]):
        self.scalar = scalar

    def value(self) -> bool:
        return not self.scalar.value()
