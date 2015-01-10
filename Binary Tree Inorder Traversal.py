# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        stack = []
        if root==None:
            return res
        stack.append(root)
        while stack:
            if stack[-1].left!=None:
                stack.append(stack[-1].left)
                stack[-2].left=None
            elif stack[-1].right!=None:
                temp = stack[-1]
                res.append(temp.val)
                stack.pop()
                stack.append(temp.right)
            else:
                res.append(stack[-1].val)
                stack.pop()
        return res
        