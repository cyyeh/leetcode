from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    """Given an array of integers arr, return true if and only if it is a valid mountain array.
    https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
    """
    if len(arr) < 3:
        return False

    last_num = arr[0]
    has_topped = False
    for i, num in enumerate(arr[1:]):
        if last_num == num:
            return False

        if has_topped:
            if last_num < num:
                return False
        else:
            if last_num > num:
                if i == 0:
                    return False
                else:
                    has_topped = True

        last_num = num

    return has_topped


def test_valid_mountain_array():
    assert not valid_mountain_array([2, 1])
    assert not valid_mountain_array([3, 5, 5])
    assert valid_mountain_array([0, 3, 2, 1])
