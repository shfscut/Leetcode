# @Time: 2019-04-28 00:04
# @Author: 'haifeng.shi@klook.com'
class Solution:
    def myAtoi(self, str: str) -> int:
        MAX=2**31-1
        MIN=-2**31
        str_ = str.lstrip()
        symbol=0
        if str_[0] in ['-','+']:
            symbol=str_[0]
            str_=str_[1:]
        target=0
        if str_[0].isdigit():
            for index, i in enumerate(str_):
                if not i.isdigit():
                    break
                target += 1
            if symbol == '-':
                return max(int(str_[:target])*-1, MIN)
            else:
                return min(int(str_[:target]), MAX)
        else:
            return 0


print(Solution().myAtoi("-91283472332"))