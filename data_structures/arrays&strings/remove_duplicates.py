from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
    """
    if not nums:
        return 0

    first_idx = 0
    second_idx = 1

    while nums[first_idx] is not None and second_idx < len(nums):
        if nums[first_idx] == nums[second_idx]:
            second_idx += 1
        else:
            nums[first_idx + 1] = nums[second_idx]
            first_idx += 1
            second_idx += 1

    return first_idx + 1


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
