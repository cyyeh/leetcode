from typing import List


def find_numbers(nums: List[int]) -> int:
    """Given an array nums of integers, return how many of them contain an even number of digits.
    https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
    """
    result = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            result += 1
    return result


def test_find_numbers():
    assert find_numbers([12, 345, 2, 6, 7896]) == 2
