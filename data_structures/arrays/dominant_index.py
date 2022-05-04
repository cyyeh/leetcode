from typing import List


def dominant_index(nums: List[int]) -> int:
    """You are given an integer array nums where the largest integer is unique.
    Determine whether the largest element in the array is at least twice
    as much as every other number in the array. If it is,
    return the index of the largest element, or return -1 otherwise.
    https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
    """
    max_num = max(nums)
    max_num_idx = -1
    for i, num in enumerate(nums):
        if num != max_num:
            if num * 2 > max_num:
                return -1
        else:
            max_num_idx = i

    return max_num_idx


def test_dominant_index():
    assert dominant_index([3, 6, 1, 0]) == 1
    assert dominant_index([1, 2, 3, 4]) == -1
    assert dominant_index([1]) == 0
