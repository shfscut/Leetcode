# coding: utf-8
# @Time: 2019-04-24 19:51
# @Author: 'haifeng.shi@klook.com'
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
