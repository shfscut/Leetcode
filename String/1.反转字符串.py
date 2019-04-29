# @Time: 2019-04-26 15:27
# @Author: 'haifeng.shi@klook.com'

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