# @Time: 2019-05-27 11:59
# @Author: 'haifeng.shi@klook.com'

# binary search


# []

def binary_search(arr, target):
    l, r = 0, len(arr) - 1  # 在[l...r]范围内查找
    return search_recursion(arr, l, r, target)


def search(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1


def search_recursion(arr, l, r, target):
    while l > r:
        return None

    mid = (l + r) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return search_recursion(arr, l, mid - 1, target)
    else:
        return search_recursion(arr, mid + 1, r, target)


# 递归解法


if __name__ == '__main__':
    print(binary_search([1, 3, 5, 7, 9, 10], 9))
