# @Time: 2019-05-08 17:59
# @Author: 'haifeng.shi@klook.com'

'''
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL


输入: 2->1->3->5->6->4->7->NULL

2 3 1 5 6 4 7
2 3 6 5 1 4 7
2 3 6 7 5 4 1
2 3 6 7 1 5 4

输出: 2->3->6->7->1->5->4->NULL
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        q=head
        p=q.next

        1 3 5
        while q and q.next:
            q.next=q.next.next
            q = q.next
