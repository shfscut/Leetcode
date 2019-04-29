# @Time: 2019-04-26 19:05
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, i in enumerate(s):
            if i in s[:index] or i in s[index+1:]:
                continue
            return index
        return -1