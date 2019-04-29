# @Time: 2019-04-28 22:43
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
