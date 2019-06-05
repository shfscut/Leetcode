# @Time: 2019-05-07 20:05
# @Author: 'haifeng.shi@klook.com'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = q = head
        result = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                result = slow.next
                break
        if result:
            pos = 0
            while q:
                if q.val == result.val:
                    return pos
                q = q.next
                pos += 1
        return -1

t=[3,2,0,-4]
pos=1

#
node0=ListNode(3)
node1=ListNode(2)
node2=ListNode(0)
node3=ListNode(-4)

node0.next=node1
node1.next=node2
node2.next=node3
node3.next=node1

head=node0

t=Solution().detectCycle(head)
print(t)