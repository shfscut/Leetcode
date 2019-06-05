# @Time: 2019-06-05 07:55
# @Author: 'haifeng.shi@klook.com'
from typing import List

def my_sum(l: List[int]) -> int:
    if len(l) <=1:
        return l[0]
    return l[0] + my_sum(l[1:])


if __name__ == '__main__':
    print(my_sum([1,2,3,4,5]))
