from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """Increment the large integer by one and return the resulting array of digits.
    https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
    """
    num = str(int("".join(map(str, digits))) + 1)
    return list(map(int, num))


def test_plus_one():
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9]) == [1, 0]
