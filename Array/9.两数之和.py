# coding: utf-8
# @Time: 2019-04-24 20:36
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            right=target - val
            if not right in nums:
                continue
            target_index = nums.index(right)
            if index == target_index:
                continue
            return [index, target_index]