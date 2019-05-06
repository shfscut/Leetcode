# @Time: 2019-05-06 21:00
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = []

        while l1 and l2:
            temp = None
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            result.append(temp)

        if l1:
            while l1:
                result.append(l1)
                l1 = l1.next
        if l2:
            while l2:
                result.append(l2)
                l2 = l2.next

        # 构建链表
        if not result:
            return result
        i = 1
        head = result[0]
        while i < len(result):
            result[i - 1].next = result[i]
            i += 1
        return head

