# @Time: 2019-05-25 17:20
# @Author: 'haifeng.shi@klook.com'
from typing import List


# TODO 递归解法
# def binary_search(t: List[int], target: int) -> int:
#     l, r = 0, len(t) - 1
#     return search(t, l, r, target)
#
#
# def search(t, l, r, target):
#     mid = (l + r) // 2
#     print(mid)
#     if t[mid] == target:
#         print('mid')
#         return mid
#     if t[mid] > target:
#         search(t, l, mid, target)
#     else:
#         search(t, mid, r, target)


# TODO 非递归解法
def binary_search(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1  # [l....r]范围内

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == '__main__':
    source = [1, 3, 5, 7, 9, 12, 14, 16]
    print(binary_search(source, 14))
