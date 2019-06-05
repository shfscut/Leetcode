# @Time: 2019-05-29 14:08
# @Author: 'haifeng.shi@klook.com'

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if len(nums) == 0 or s is None:
            return 0

        min_len = len(nums) + 1
        l = 0
        sum = 0
        for r, val in enumerate(nums):
            sum += val
            while sum >= s:
                min_len = min(min_len, r - l + 1)
                sum-=nums[l]
                l += 1
        if min_len != len(nums) + 1:
            return min_len
        else:
            return 0

if __name__ == '__main__':
    s = 4
    nums = [1,4,4]
    print(Solution().minSubArrayLen(s, nums))