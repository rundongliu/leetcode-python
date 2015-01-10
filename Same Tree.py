# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if q==None and p!=None or p==None and q!=None:
            return False
        return p.val==q.val and Solution().isSameTree(p.left,q.left) and Solution().isSameTree(p.right,q.right)
        
        