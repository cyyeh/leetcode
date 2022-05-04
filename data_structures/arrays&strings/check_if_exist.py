from typing import List


def check_if_exist(arr: List[int]) -> bool:
    """
    Given an array arr of integers, check if there exists two integers N and M
    such that N is the double of M ( i.e. N = 2 * M).
    https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
    """
    check_set = set()
    for num in arr:
        if num not in check_set:
            check_set.add(num * 2)
            if num % 2 == 0:
                check_set.add(num / 2)
        else:
            return True

    return False


def test_check_if_exist():
    assert check_if_exist([10, 2, 5, 3])
    assert check_if_exist([7, 1, 14, 11])
    assert not check_if_exist([3, 1, 7, 11])
