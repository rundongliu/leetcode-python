# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        res = self.rec(1,n)
        return res
        
    def rec(self,start,end):
        if start>end:
            return [None]
        lst = []
        for num in range(start,end+1):
            left_list = self.rec(start,num-1)
            right_list = self.rec(num+1,end)
            for left in left_list:
                for right in right_list:
                    node = TreeNode(num)
                    node.left = left
                    node.right = right
                    '''
                    node.left = self.copytree(left)
                    node.right = self.copytree(right)
                    '''
                    lst.append(node)
        return lst
    '''        
    def copytree(self,root):
        if root==None:
            return None
        node = TreeNode(root.val)
        node.left = self.copytree(root.left)
        node.right = self.copytree(root.right)
        return node
        '''