# @Time: 2019-04-28 22:43
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def getNextValue(self, val: str) -> str:
        lg = len(val)
        i, j = 0, 0
        result = []
        while j < lg:
            if val[i] != val[j]:
                lg_i = j - i
                result.append((lg_i, val[i]))
                i = j
            j += 1
        lg_i = j - i
        result.append((lg_i, val[i]))
        return ''.join(['{x}{y}'.format(x=x, y=y) for x, y in result])

    def countAndSay(self, n: int) -> str:
        """
            1.     1
            2.     11
            3.     21
            4.     1211
            5.     111221
            6.     312211
            7.     13112221
        """
        start_val = '1'
        while n > 1:
            start_val = self.getNextValue(start_val)
            n -= 1
        return start_val