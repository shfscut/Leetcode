# @Time: 2019-05-19 23:55
# @Author: 'haifeng.shi@klook.com'
import queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = queue.Queue()
        q.put(root)
        result=[root, ]
        while not q.empty():
            level_res=[]

            for i in range(q.qsize()):
                cur=q.get()
                if cur.left:
                    level_res.append(cur.left)
                    q.put(cur.left)
                if cur.right:
                    level_res.append(cur.right)
                    q.put(cur.right)
                result.append(level_res)
