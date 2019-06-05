# @Time: 2019-05-14 18:57
# @Author: 'haifeng.shi@klook.com'

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while headA:
            # print(headA.val)
            while headB:
                print(headA.val, headB.val)
                if headA == headB:
                    print('sss')
                    return headA
                headB = headB.next
            headA = headA.next
