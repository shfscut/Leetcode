# @Time: 2019-06-16 18:45
# @Author: 'haifeng.shi@klook.com'

class Node:
    def __init__(self, e):
        self.e=e
        self.left=None
        self.right=None


class BST:
    def __init__(self, root):
        self.root = root

    def add(self, e):
        if self.root is None:
            self.root = Node(e)
        else:
            self._add(self.root, e)


    def _add(self, node, e):

        if node.e==e:
            return

        if node.e < e and node.left is None:
            node.left=Node(e)
            return
        elif node.e > e and node.right is None:
            node.right = Node(e)
            return


        if node.e < e:
            self._add(node.left, e)
        else:
            self._add(node.right, e)


class BST1:
    def __init__(self, root):
        self.root = root

    def add(self, e):

        self.root = self._add(self.root, e)

    def _add(self, node, e):
        if node is None:
            return Node(e)

        if e < node.e:
            node.left = self._add(node.left, e)
        elif e > node.e:
            node.right = self._add(node.right, e)
