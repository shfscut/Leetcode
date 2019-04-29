# @Time: 2019-04-27 09:17
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        if s==s[::-1]:
            return True
        return False