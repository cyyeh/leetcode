def str_str(haystack: str, needle: str) -> int:
    """Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
    """
    if not needle:
        return 0
    elif len(needle) > len(haystack):
        return -1

    try:
        return haystack.index(needle)
    except ValueError:
        return -1


def test_str_str():
    assert str_str("hello", "ll") == 2
    assert str_str("aaaaa", "bba") == -1
    assert str_str("mississippi", "issip") == 4
