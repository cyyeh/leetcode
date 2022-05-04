from enum import Enum
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Given an m x n matrix, return all elements of the matrix in spiral order.
    https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
    """
    if not matrix:
        return []

    class Direction(Enum):
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        UP = 4

    direction = Direction.RIGHT
    m = len(matrix)
    n = len(matrix[0])
    i = j = 0
    right_max = n
    down_max = m
    left_min = 0
    up_min = 1
    results = [matrix[i][j]]

    while len(results) < m * n:
        if direction is Direction.RIGHT:
            if j + 1 < right_max:
                j += 1
                results.append(matrix[i][j])
            else:
                direction = Direction.DOWN
                right_max -= 1
        elif direction is Direction.DOWN:
            if i + 1 < down_max:
                i += 1
                results.append(matrix[i][j])
            else:
                direction = Direction.LEFT
                down_max -= 1
        elif direction is Direction.LEFT:
            if j - 1 >= left_min:
                j -= 1
                results.append(matrix[i][j])
            else:
                direction = Direction.UP
                left_min += 1
        else:
            if i - 1 >= up_min:
                i -= 1
                results.append(matrix[i][j])
            else:
                direction = Direction.RIGHT
                up_min += 1

    return results


def test_spiral_order():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]
