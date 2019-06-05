# @Time: 2019-04-26 15:27
# @Author: 'haifeng.shi@klook.com'
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=len(s)
        i=0
        while i<length//2:
            j=length-1-i
            s[i],s[j]=s[j],s[i]
            i+=1

# NOTE 对撞指针
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    s=["h","e","l","l","o"]
    Solution2().reverseString(s)
    print(s)