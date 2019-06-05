# @Time: 2019-06-02 10:54
# @Author: 'haifeng.shi@klook.com'


"""

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = len(s)+1, None, None
        matched = 0

        dict_t=Counter(t)
        dict_between = {}

        l, r=0,0
        while r<len(s):

            char = s[r]
            dict_between[char] = dict_between.get(char, 0) + 1

            if char in dict_t and dict_between[char] == dict_t[char]:
                # 统计匹配计数
                matched += 1

            while l<=r and matched==len(dict_t):
                # 匹配之后，移动l，找到最小的子串
                if r-l+1<res[0]:
                    res = r-l+1, l, r

                # 移动l
                char = s[l]
                dict_between[char] -=1
                if dict_between[char] < dict_t[char]:
                    matched -=1
                l+=1

            r += 1

        return "" if res[0] == len(s)+1 else s[res[1]: res[2] + 1]


class Solution1:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and co***act the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

                # Keep expanding the window once we are done co***acting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    res = Solution().minWindow(S, T)
    print(res)