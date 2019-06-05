class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummyhead = Node()
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        cur = self.dummyhead
        for i in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        prev = self.dummyhead
        for i in range(index):
            prev = prev.next

        node = Node(val)
        node.next = prev.next
        prev.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        prev = self.dummyhead
        for i in range(index):
            prev = prev.next

        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None

        self.size -= 1

    def to_string(self):
        result=[]
        temp = self.dummyhead.next
        while (temp):
            result.append(str(temp.val)+'->')
            temp = temp.next
        result.append('NULL')
        return ' '.join(result)


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    # methods=["MyLinkedList", "addAtIndex", "get", "deleteAtIndex"]
    # params = [[], [0, 0], [0], [0]]
    # methods=["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    # params=[[], [1], [3], [1, 2], [1], [1], [1]]
    #
    # # 初始化一个链表
    # my_linked_list=MyLinkedList()
    # nodes=[]
    # for i in params[0]:
    #     nodes.append(Node(i))
    #
    # if nodes:
    #     for i in range(len(nodes)-1):
    #         nodes[i].next=nodes[i+1]
    #     nodes[len(nodes)-1].next=None
    #     my_linked_list.dummyhead.next=nodes[0]
    #
    # for method, param in zip(methods[1:], params[1:]):
    #     getattr(my_linked_list, method)(*param)
    #
    #     print(my_linked_list.to_string())

    # 创建链表
    nodes=[1,2,3,4,5,6]
    
    def temp(node):
        if node is None:
            return
        print(node.val)
        return temp(node.next)

    temp(nodes[0])


