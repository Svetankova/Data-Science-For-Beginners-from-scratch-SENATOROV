"""Math and numpy modules."""

# +
import math
from math import cos, dist, sin
from sys import stdin

import numpy as np
from numpy.typing import NDArray  # type: ignore

# +
# 1
x_val = float(input())

# fmt: off
result = (
    math.log(math.pow(x_val, 3 / 16), 32) +  # noqa: W504
    math.pow(x_val, math.cos((math.pi * x_val) / (2 * math.e))) -  # noqa: W504
    math.pow(math.sin(x_val / math.pi), 2)
)
# fmt: on

print(result)

# +
# 2


for line in stdin:
    numbers = map(int, line.split())
    print(math.gcd(*numbers))

# +
# 3

N_val, M_val = map(int, input().split())
print(math.comb(N_val - 1, M_val - 1), math.comb(N_val, M_val))

# +
# 4


inputs_val = list(map(float, input().split()))

geometric_mean = math.pow(math.prod(inputs_val), 1 / len(inputs_val))
print(geometric_mean)

# +
# 5


deca_x, deca_y = map(float, input().split())
pola_r, pola_f = map(float, input().split())
pola_x = pola_r * cos(pola_f)
pola_y = pola_r * sin(pola_f)
print(dist((deca_x, deca_y), (pola_x, pola_y)))

# +
# 6


def multiplication_matrix(size: int) -> NDArray[np.int64]:
    """Create an n x n multiplication table matrix."""
    matrix = np.arange(1, size + 1)
    return matrix * matrix.reshape(-1, 1)


# +
# 7


def make_board(num: int) -> NDArray[np.int8]:
    """Create a chessboard pattern matrix of size n x n."""
    matrix = np.indices((num, num)).sum(axis=0) % 2
    return np.array(np.rot90(matrix), dtype="int8")


# +
# 8


def snake(width: int, height: int, direction: str = "H") -> NDArray[np.int16]:
    """Create a snake pattern matrix of size N x M."""
    matrix = np.zeros((height, width), dtype=np.int16)

    if direction == "H":
        for i in range(height):
            if i % 2 == 0:
                matrix[i] = np.arange(i * width + 1, (i + 1) * width + 1)
            else:
                matrix[i] = np.arange((i + 1) * width, i * width, -1)
    elif direction == "V":
        for j_w in range(width):
            if j_w % 2 == 0:
                array_val = np.arange(j_w * height + 1, (j_w + 1) * height + 1)
                matrix[:, j_w] = array_val
            else:
                array_val = np.arange((j_w + 1) * height, j_w * height, -1)
                matrix[:, j_w] = array_val

    return matrix


# +
# 9


def rotate(matrix: NDArray[np.int64], angle: int) -> NDArray[np.int64]:
    """Rotate a matrix by the angle in degrees (must be multiple of 90)."""
    return np.rot90(matrix, (360 - angle) // 90)


# +
# 10


def stairs(vector: NDArray[np.int64]) -> NDArray[np.int64]:
    """Create a matrix where row is the vector shifted right by row index."""
    size = len(vector)
    matrix = np.zeros((size, size), dtype=vector.dtype)

    for i_val in range(size):
        matrix[i_val] = np.roll(vector, i_val)

    return matrix
