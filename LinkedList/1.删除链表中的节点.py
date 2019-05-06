# @Time: 2019-05-06 10:02
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next == None:
            node = None
        node.val = node.next.val
        node.next = node.next.next
