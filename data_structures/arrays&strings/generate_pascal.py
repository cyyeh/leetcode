from typing import List


def generate_pascal(num_rows: int) -> List[List[int]]:
    if num_rows == 1:
        return [[1]]
    elif num_rows == 2:
        return [[1], [1, 1]]
    else:
        results = [[1], [1, 1]]
        for nth in range(1, num_rows - 1):
            nthRow = [1]
            for i in range(len(results[nth])):
                if i + 1 < len(results[nth]):
                    nthRow.append(results[nth][i] + results[nth][i + 1])
                else:
                    nthRow.append(1)
            results.append(nthRow)

        return results


def test_generate_pascal():
    assert generate_pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate_pascal(1) == [[1]]
