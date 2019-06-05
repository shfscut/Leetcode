# @Time: 2019-05-12 16:34
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 创建dummyhead
        dummyhead = ListNode(None)
        dummyhead.next = head
        prev = dummyhead
        while prev.next is not None:
            if prev.next.val == val:
                cur = prev.next
                prev.next = prev.next.next
                cur.next = None
            else:
                prev = prev.next

        return dummyhead.next
