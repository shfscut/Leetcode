# coding: utf-8
# @Time: 2019-04-23 14:51
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
