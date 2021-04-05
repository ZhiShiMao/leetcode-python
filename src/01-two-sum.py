"""
题目: https://leetcode-cn.com/problems/two-sum/
知乎: 
作者: Andy
日期: 2021-04-03 01:54

本代码不受版权限制，欢迎随意转载和使用。
仅保留作者探索的最优解法，欢迎大家在知乎进一步讨论。
------------------------------

题解思路:

"""

from typing import List


class Solution:
    """TITLE: 两数之和

    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。

    示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

    示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]

    示例 3：
    输入：nums = [3,3], target = 6
    输出：[0,1]

    NOTE: 提示：
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]