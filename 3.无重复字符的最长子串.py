# @Time: 2019-05-29 23:21
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        max_len = 0
        length = len(s)
        l, r = 0, -1
        while r < length:
            if r < length and s[r] in s[l:r]:
                max_len = max(r - l, max_len)
                l += 1
            else:
                r += 1
        return max_len

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('au'))