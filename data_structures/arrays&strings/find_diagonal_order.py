from typing import List


def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    """Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
    https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
    """
    if not mat:
        return []

    m = len(mat)
    n = len(mat[0])
    i = j = 0
    top_to_down = True
    pivot = True

    results = [mat[i][j]]
    while len(results) < m * n:
        if top_to_down:
            if pivot:
                if j + 1 < n:
                    j += 1
                else:
                    i += 1

                results.append(mat[i][j])
                pivot = False
            else:
                if i + 1 < m and j - 1 >= 0:
                    i += 1
                    j -= 1
                    results.append(mat[i][j])
                else:
                    pivot = True
                    top_to_down = False
        else:
            if pivot:
                if i + 1 < m:
                    i += 1
                else:
                    j += 1

                results.append(mat[i][j])
                pivot = False
            else:
                if i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                    results.append(mat[i][j])
                else:
                    pivot = True
                    top_to_down = True

    return results


def test_find_diagonal_order():
    assert find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        4,
        7,
        5,
        3,
        6,
        8,
        9,
    ]
    assert find_diagonal_order([[1, 2], [3, 4]]) == [1, 2, 3, 4]
