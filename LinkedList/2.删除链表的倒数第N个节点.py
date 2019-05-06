# @Time: 2019-05-06 10:03
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        result = []
        print(head, head.val)
        while head:
            result.append(head)
            if head.next is None:
                break
            else:
                head = head.next

        if len(result) == 1:
            return None
        elif len(result) == n:
            result.pop(0)
            return result[0]

        target = result[-n - 1]
        target.next = target.next.next
        result.pop(n)
        return result[0]
