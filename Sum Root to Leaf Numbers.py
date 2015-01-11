# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.sum = 0
        if root==None:
            return self.sum
        self.rec(root,0)
        return self.sum
    def rec(self,node,num):
        num = num*10+node.val
        if node.left==None and node.right==None:
            self.sum += num
            return
        else:
            if node.left!=None:
                self.rec(node.left,num)
            if node.right!=None:
                self.rec(node.right,num)