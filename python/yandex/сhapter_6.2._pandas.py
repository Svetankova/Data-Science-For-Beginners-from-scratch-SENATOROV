"""Pandas."""

# +
# fmt: off
from typing import Callable

import numpy as np

# 6
import pandas as pd

# fmt: on

# +
# 1


def length_stats(line: str) -> pd.Series:  # type: ignore
    """Calculate length statistics for unique words in a string."""
    line = "".join([char for char in line if char.isalpha() or char == " "])
    data = sorted(set(line.lower().split()))

    return pd.Series(data=list(map(len, data)), index=data)


# +
# 2


def length_stats_tuple(line: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Return tuple of Series with odd and even length words."""
    line = "".join([char for char in line if char.isalpha() or char == " "])
    data = sorted(set(line.lower().split()))
    series = pd.Series(data=list(map(len, data)), index=data)
    return series[series % 2 != 0], series[series % 2 == 0]


# +
# 3


def cheque(price_list: pd.Series, **kwargs: int) -> pd.DataFrame:  # type: ignore
    """Create a DataFrame with product details and calculate total cost."""
    my_products = sorted(kwargs)

    data = pd.DataFrame(
        {
            "product": my_products,
            "price": [price_list[p] for p in my_products],
            "number": [kwargs[p] for p in my_products],
        }
    )

    data["cost"] = data["price"] * data["number"]
    return data


# +
# 4


def discount(result: pd.DataFrame):  # type: ignore
    """Apply discount to products and return updated DataFrame."""
    copy = result.copy()
    copy.loc[result["number"] > 2, "cost"] = result["cost"] * 0.5
    return copy


# +
# 5


def get_long(data: pd.Series, min_length: int = 5):  # type: ignore
    """Return Series with values >= min_length."""
    return data[data >= min_length]


# +
# 6


def best(progress: pd.DataFrame):  # type: ignore
    """Return students with good grades in all subjects."""
    data = progress.copy()
    return data[
        (data["maths"] >= 4) & (data["physics"] >= 4) & (data["computer science"] >= 4)
    ]


# +
# 7


def need_to_work_better(progress: pd.DataFrame):  # type: ignore
    """Return students with good grades in all subjects."""
    data = progress.copy()
    return data[
        (data["maths"] < 3) | (data["physics"] < 3) | (data["computer  science"] < 3)
    ]


# +
# 8


def update(progress: pd.DataFrame):  # type: ignore
    """Return DataFrame with average grade sorted by average and name."""
    data = progress.copy()
    data["average"] = (data["physics"] + data["maths"] + data["computer science"]) / 3
    sorted_data = data.sort_values(["average", "name"], ascending=(False, True))
    return sorted_data


# +
# 9


# pylint: disable=all
# flake8: noqa
top_angle_x, top_angle_y = map(int, input().split())
bottom_angle_x, bottom_angle_y = map(int, input().split())
game_data = pd.read_csv("data.csv")
print(
    game_data[
        (top_angle_x <= game_data["x"])
        & (game_data["x"] <= bottom_angle_x)
        & (bottom_angle_y <= game_data["y"])
        & (game_data["y"] <= top_angle_y)
    ]
)
# pylint: enable=all
# flake8: enable

# +
# 10


def values(
    func: Callable[[float], float], start: float, end: float, step: float
) -> pd.Series:  # type: ignore
    """Create Series of function values with given range and step."""
    index = np.arange(start, end + step, step, dtype="float64")
    return pd.Series(list(map(func, index)), index=index, dtype="float64")


def min_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x coordinate of leftmost minimum."""
    return float(min(data[data == min(data)].index))


def max_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x coordinate of rightmost maximum."""
    return float(max(data[data == max(data)].index))
