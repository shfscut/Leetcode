# @Time: 2019-05-09 00:14
# @Author: 'haifeng.shi@klook.com'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self.size += 1
        else:
            self.add_node(self.root, val)

    def add_node(self, node, val):
        if node is None:
            node = TreeNode(val)

        if val < node.val and node.left is None:
            node.left = TreeNode(val)
            self.size += 1
            return
        elif val > node.val and node.right is None:
            node.right = TreeNode(val)
            self.size += 1
            return

        if val < node.val:
            self.add_node(node.left, val)
        else:
            self.add_node(node.right, val)

    def preOrder(self):
        self.pre_order(self.root)

    def pre_order(self, node):
        if node is None:
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def middleOrder(self):
        # handle left --> root --> right
        self.middle_order(self.root)

    def middle_order(self, node):

        self.middle_order(node.left)
        print(node.val)
        self.middle_order(node.right)


if __name__ == '__main__':
    solution=Solution()

    nums=[5,3,6,8,4,2]
    for num in nums:
        solution.add(num)

    solution.preOrder()
