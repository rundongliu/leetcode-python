# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = (len(num)-1)/2
        left = num[:mid]
        right = num[mid+1:]
        mid_node = TreeNode(num[mid])
        mid_node.left = self.sortedArrayToBST(left)
        mid_node.right = self.sortedArrayToBST(right)
        return mid_node
        