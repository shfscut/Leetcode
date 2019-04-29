# @Time: 2019-04-26 19:04
# @Author: 'haifeng.shi@klook.com'
class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1 if x >= 0 else -1

        x = str(abs(x))
        result = [i for i in x[::-1]]
        result = int(''.join(result)) * symbol
        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0
        return result

