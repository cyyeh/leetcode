from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """Find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
    """
    result = ""
    for pairs in zip(*strs):
        if len(set(pairs)) == 1:
            result += pairs[0]
        else:
            return result

    return result


def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
