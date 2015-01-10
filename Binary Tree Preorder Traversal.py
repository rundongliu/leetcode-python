# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        stack = []
        if root == None:
            return res
        stack.append(root)
        while stack:
            element = stack[-1]
            stack.pop()
            res.append(element.val)
            if element.right!=None:
                stack.append(element.right)
            if element.left!=None:
                stack.append(element.left)
        return res
        