from typing import List

import pytest


def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
    """
    raise NotImplementedError


@pytest.mark.skip(reason="not implemented yet")
def test_merge_sorted_array():
    nums1 = [1, 2, 3, 0, 0, 0]
    merge_sorted_array(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge_sorted_array(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    merge_sorted_array(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [1, 0]
    merge_sorted_array(nums1, 1, [2], 1)
    assert nums1 == [1, 2]

    nums1 = [4, 0, 0, 0, 0, 0]
    merge_sorted_array(nums1, 1, [1, 2, 3, 5, 6], 5)
    assert nums1 == [1, 2, 3, 4, 5, 6]
