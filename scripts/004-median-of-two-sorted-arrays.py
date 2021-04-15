from typing import List


class Solution:
    """TITLE: 寻找两个正序数组的中位数
    给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出并返回这两个正序数组的 中位数 。
    NOTE: 示例
    示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2
    示例 2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
    示例 3：
    输入：nums1 = [0,0], nums2 = [0,0]
    输出：0.00000
    示例 4：
    输入：nums1 = [], nums2 = [1]
    输出：1.00000
    示例 5：
    输入：nums1 = [2], nums2 = []
    输出：2.00000
    示例 6:
    输入：nums1 = [0,0,0,0,0], nums2 = [-1,0,0,0,0,0,1]
    输出：0
    示例 7:
    输入：nums1 = [1,3], nums2 = [2,7]
    输出：2.5
    示例 8:
    输入：nums1 = [1,2,2], nums2 = [1,2,3]
    输出：2
    示例 9:
    输入：nums1 = [2], nums2 = [1,3,4]
    输出：2.5
    示例 10:
    输入：nums1 = [1,2,4], nums2 = [2]
    输出：2.5
    NOTE: 提示：
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
    NOTE: 进阶：
    你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getMedianInList(a: List):
            """获取一个列表的中位数"""
            if len(a) % 2 == 0:
                return (a[int(len(a) / 2)] + a[int(len(a) / 2) - 1]) / 2
            return a[int(len(a) / 2)]

        # 如果 nums1 和 nums2 为空, 则返回 0
        if not nums1 and not nums2:
            return 0

        # 如果 nums1 不为空, nums2 为空, 则返回 nums1 的中位数
        if nums1 and not nums2:
            return getMedianInList(nums1)

        # 如果 nums1 为空, nums2 不为空, 则返回 nums2 的中位数
        if not nums1 and nums2:
            return getMedianInList(nums2)

        # 如果 nums2 全部小于 nums1, 则可以看成一个列表
        if nums1[0] >= nums2[-1]:
            return getMedianInList(nums2 + nums1)

        # 如果 nums1 全部小于 nums2, 则可以看成一个列表
        if nums2[0] >= nums1[-1]:
            return getMedianInList(nums1 + nums2)

        # 两个列表联合起来进行分割查找中位数
        m, n = len(nums1), len(nums2)
        i = m / 2
        j = 0

        i, j = int(i), int(j)
        while True:
            if i + 1 >= m - 1 and i - 1 <= 0:
                break
            if j + 1 >= n - 1 and j - 1 <= 0:
                break
            if nums1[i] >= nums2[j + 1]:
                i += 1
                j -= 1
            if nums1[i + 1] <= nums2[j]:
                i -= 1
                j += 1
            if nums1[i] <= nums2[j + 1] and nums1[i + 1] >= nums2[j]:
                break
        if (m + n) % 2 == 0:
            a = max(nums1[i], nums2[j])
            b1 = 200 if i + 1 >= m else nums1[i + 1]
            b2 = 200 if j + 1 >= n else nums2[j + 1]
            b = min(b1, b2)
            return (a + b) / 2
        else:
            return max(nums1[i], nums2[j])


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """暴力法"""
        new_list = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        if i < len(nums1):
            new_list += nums1[i:]
        if j < len(nums2):
            new_list += nums2[j:]

        if len(new_list) == 0:
            return 0

        if len(new_list) % 2 == 0:
            return (
                new_list[int(len(new_list) / 2)] + new_list[int(len(new_list) / 2) - 1]
            ) / 2
        return new_list[int(len(new_list) / 2)]
