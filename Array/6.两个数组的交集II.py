# coding: utf-8
# @Time: 2019-04-24 19:52
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums1, nums2=nums2, nums1
        result =[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                result.append(i)
        return result