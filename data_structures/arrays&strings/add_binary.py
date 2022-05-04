def add_binary(a: str, b: str) -> str:
    """Given two binary strings a and b, return their sum as a binary string.
    https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
    """
    return "{0:b}".format(int(a, 2) + int(b, 2))


def test_add_binary():
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
