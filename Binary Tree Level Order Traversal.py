# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if root==None:
            return res
        dq = collections.deque()
        dq.append(root)
        dq.append(None)
        lst = []
        while dq:
            node = dq[0]
            dq.popleft()
            if node==None:
                res.append(lst)
                lst = []
                if dq:
                    dq.append(None)
            else:
                lst.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res