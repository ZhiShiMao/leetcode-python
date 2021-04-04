class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        array, i = [], 0
        while i < len(s):
            row = ["" for _ in range(numRows)]
            for j in range(numRows):
                if i < len(s):
                    row[j] = s[i]
                    i += 1
            array.append(row)
            for j in range(numRows - 2, 0, -1):
                row = ["" for _ in range(numRows)]
                if i < len(s):
                    row[j] = s[i]
                    i += 1
                    array.append(row)
        ret = ""
        for i in range(numRows):
            for j in range(len(array)):
                ret += array[j][i]
        return ret


import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        base = numRows * 2 - 2
        for i in range(numRows):
            pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "params": {"s": "PAYPALISHIRING", "numRows": 3},
            "results": "PAHNAPLSIIGYIR",
        },
        {
            "params": {"s": "PAYPALISHIRING", "numRows": 4},
            "results": "PINALSIGYAHRPI",
        },
        {
            "params": {"s": "A", "numRows": 1},
            "results": "A",
        },
    ]

    for test_case in test_cases:
        results = solution.convert(**test_case["params"])
        except_results = test_case["results"]
        print(results, except_results, results == except_results)