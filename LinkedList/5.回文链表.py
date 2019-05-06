# @Time: 2019-05-06 21:01
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val

        fast = slow = q = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 获取反转链表
        reverse = self.reverseList(slow.next)
        while reverse.next:
            # print('shf')
            if q.val != reverse.val:
                return False
            q = q.next
            reverse = reverse.next
        return q.val == reverse.val

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

