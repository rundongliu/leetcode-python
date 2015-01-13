# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        if root==None:
            return res
        self.find(root,[],sum,res)
        return res
    
    def find(self,node,current_list,rest,res):
        current_list.append(node.val)
        rest -= node.val
        if node.left==None and node.right==None:
            if rest==0:
                res.append(current_list[:])
            current_list.pop()
            return
        if node.left!=None:
            self.find(node.left,current_list,rest,res)
        if node.right!=None:
            self.find(node.right,current_list,rest,res)
        current_list.pop()
        