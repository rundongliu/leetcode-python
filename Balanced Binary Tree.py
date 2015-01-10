# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if left==-1 or right==-1:
            return False
        elif abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    
    
    def height(self,root):
        if root==None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if(abs(left-right)>1):
            return -1
        else:
            return 1+max(left,right)
        