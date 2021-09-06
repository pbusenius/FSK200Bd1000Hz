import numpy as np

index_ecc_lut = [
    [0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 0, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 1], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1],
]


class ECC:
    def __init__(self):
        pass

    @staticmethod
    def check(index, index_ecc):
        return np.array_equal(index, index_ecc_lut[index_ecc])