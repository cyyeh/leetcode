from typing import List


def reverse_string(s: List[str]) -> None:
    """The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
    https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
    """
    if not s:
        return

    left_pointer_idx = 0
    right_pointer_idx = len(s) - 1

    while left_pointer_idx < right_pointer_idx:
        s[left_pointer_idx], s[right_pointer_idx] = (
            s[right_pointer_idx],
            s[left_pointer_idx],
        )
        left_pointer_idx += 1
        right_pointer_idx -= 1


def test_reverse_string():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
