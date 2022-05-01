from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.
    """
    return sorted(map(lambda num: num**2, nums))


def test_sorted_squares():
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
