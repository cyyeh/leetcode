from typing import List


def pivot_index(nums: List[int]) -> int:
    """Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly
    to the left of the index is equal to the sum of all the numbers strictly
    to the index's right.
    https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
    """
    if not nums:
        return -1
    elif len(nums) == 1:
        return 0 if nums[0] == 0 else -1
    else:
        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(len(nums)):
            if left_sum == right_sum:
                return i
            elif i + 1 < len(nums):
                left_sum += nums[i]
                right_sum -= nums[i + 1]

        return -1


def test_pivot_index():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
