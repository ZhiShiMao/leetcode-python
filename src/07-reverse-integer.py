class Solution:
    """
    示例 1：
    输入：x = 123
    输出：321
    示例 2：
    输入：x = -123
    输出：-321
    示例 3：
    输入：x = 120
    输出：21
    示例 4：
    输入：x = 0
    输出：0
    示例5：
    输入：x = 1534236469
    输出：0
    """

    def reverse(self, x: int) -> int:
        if -(2 ** 31) <= x <= 2 ** 31 - 1:
            s = str(abs(x))
            if x >= 0:
                ret = int(s[::-1])
            else:
                ret = int("-" + s[::-1])
            if -(2 ** 31) <= ret <= 2 ** 31 - 1:
                return ret
            else:
                return 0
        else:
            return 0
