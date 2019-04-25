# coding: utf-8
# @Time: 2019-04-24 19:51
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res ^=i
        return res