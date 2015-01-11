# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        return self.rec(root,0,sum)
        
    def rec(self,node,num,sum):
        num = num + node.val
        if node.left==None and node.right==None:
            if num==sum:
                return True
            else:
                return False
        if node.left!=None:
            if self.rec(node.left,num,sum):
                return True
        if node.right!=None:
            if self.rec(node.right,num,sum):
                return True
        return False
        