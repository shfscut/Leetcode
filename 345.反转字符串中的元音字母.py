# @Time: 2019-05-28 00:21
# @Author: 'haifeng.shi@klook.com'

# 对撞指针解法


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vowel:
                l += 1
            while l < r and s[r] not in vowel:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
