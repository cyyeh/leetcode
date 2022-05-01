from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    """Given a binary array nums, return the maximum number of consecutive 1's in the array."""
    max_consecutive_ones = current_consecutive_ones = 0

    for num in nums:
        if num == 1:
            current_consecutive_ones += 1
        else:
            if current_consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = current_consecutive_ones

            current_consecutive_ones = 0

    return (
        current_consecutive_ones
        if current_consecutive_ones > max_consecutive_ones
        else max_consecutive_ones
    )


def test_find_max_consecutive_ones():
    assert find_max_consecutive_ones([]) == 0
    assert find_max_consecutive_ones([1, 1]) == 2
    assert find_max_consecutive_ones([0]) == 0
    assert find_max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert find_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1]) == 3
