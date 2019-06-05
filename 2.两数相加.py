# @Time: 2019-05-14 09:44
# @Author: 'haifeng.shi@klook.com'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #         if l1 or l2:
        #             head = None
        #             return head

        #         node = self.addTwoNumbers(l1.next, l2.next)
        #         new_val = l1.val+l2.val
        #         ten_place=new_val//10
        #         one_place=new_val%10
        #         new_node=Node(one_place)
        #         node.next=new_node
        #         return node
        dummy_head = ListNode(None)
        cur = dummy_head
        ten = 0

        # 考虑l1和l2不一致问题
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = l1_val + l2_val + ten

            ten = new_val // 10
            one = new_val % 10

            new_node = ListNode(one)
            cur.next = new_node
            cur = cur.next
            l1, l2 = l1.next if l1 else None, l2.next if l1 else None
        if ten:
            cur.next=ListNode(ten)
        return dummy_head.next


def create_list_node(l):
    dummy_head = ListNode(None)
    cur = dummy_head
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy_head.next


def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return '-->'.join(result)


if __name__ == '__main__':
    l = [1, 3, 5, 7]
    head = create_list_node(l)
    print(print_linked_list(head))
