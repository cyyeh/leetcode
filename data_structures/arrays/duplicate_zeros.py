from typing import List


def duplicate_zeros(arr: List[int]) -> None:
    """Given a fixed-length integer array arr, duplicate each occurrence of zero,
    shifting the remaining elements to the right.
    https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
    """
    i = 0
    size = len(arr)
    while i < size:
        if arr[i] == 0:
            arr.insert(i, 0)
            i += 2
        else:
            i += 1

    del arr[size:]


def test_duplicate_zeros():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]

    arr = [1, 2, 3]
    duplicate_zeros(arr)
    assert arr == [1, 2, 3]
