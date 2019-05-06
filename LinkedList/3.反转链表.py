# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        last = None  # 指向上一个节点
        while head:
            # 先保存当前node指向的下一个节点
            temp = head.next

            # 指向上一个节点
            head.next = last
            #
            # 节点移动，
            last = head
            head = temp
        return last