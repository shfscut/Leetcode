# @Time: 2019-04-27 09:17
# @Author: 'haifeng.shi@klook.com'

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

"""

# NOTE 解法1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        if s==s[::-1]:
            return True
        return False


# NOTE 使用对撞指针
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l,r=0, len(s)-1
        while l<=r:
            while l<=r:
                if s[l].isalpha() or s[l].isdigit() and s[r].isalpha() or s[r].isdigit():
                    if s[l].lower()!=s[r].lower():
                        return False
                if not s[l].isdigit() and not s[l].isalpha():
                    l+=1
                if not s[r].isdigit() and not s[r].isalpha():
                    r-=1

        return True

if __name__ == '__main__':
    print(Solution2().isPalindrome(" "))
