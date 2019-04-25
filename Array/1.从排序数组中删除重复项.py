# coding: utf-8
# @Time: 2019-04-24 19:50
# @Author: 'haifeng.shi@klook.com'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        for index, val in enumerate(nums):
            if index-1>=0 and val==nums[index-1]:
                # nums.remove(val)
                pass
            else:
                nums[j]=val
                j+=1
        return j