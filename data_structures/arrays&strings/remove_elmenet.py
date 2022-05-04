from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
    The relative order of the elements may be changed.
    Return k after placing the final result in the first k slots of nums.
    https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
    """
    left_idx = 0
    right_idx = len(nums) - 1
    result = 0

    while left_idx <= right_idx:
        if nums[left_idx] == val:
            if nums[right_idx] == val:
                right_idx -= 1
            else:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1
                right_idx -= 1
        else:
            left_idx += 1

    for num in nums:
        if num != val:
            result += 1
        else:
            break

    return result


def test_remove_element():
    assert remove_element([3, 2, 2, 3], 3) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
