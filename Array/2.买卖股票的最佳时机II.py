# coding: utf-8
# @Time: 2019-04-22 21:24
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        i=0
        result=[]
        while i<len(p)-1:
            start = i
            while i< len(p)-1 and p[i+1]>p[i]:
                i+=1
            end = i
            result.append((start, end))
            i += 1
        print(result)
        sum=0
        for m, n in result:
            if n>m:
                sum +=p[n]-p[m]
        return sum
