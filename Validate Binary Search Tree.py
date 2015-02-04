# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.vali(root,float('-inf'),float('inf'))
    
    def vali(self,node,left,right):
        if not node:
            return True
        return left<node.val and node.val<right and self.vali(node.left,left,node.val) and self.vali(node.right,node.val,right)
        