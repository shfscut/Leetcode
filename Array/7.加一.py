# coding: utf-8
# @Time: 2019-04-24 19:45
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        jw=1
        for i in digits[::-1]:
            if i+jw>=10:
                jw=(i+jw)//10
                result.append(i+jw-10)
            else:
                result.append(i+jw)
                jw=0
        if jw !=0:
            result.append(jw)
        print(result)
        return result[::-1]