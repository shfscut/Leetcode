# @Time: 2019-04-26 19:06
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=[i for i in s]
        t=[j for j in t]
        s.sort()
        t.sort()
        if s==t:
            return True
        return False