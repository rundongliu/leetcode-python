# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root==None:
            return root
        if root.left==None and root.right==None:
            return root
        left_last_node = self.flatten(root.left)
        right_last_node = self.flatten(root.right)
        last_node = root
        if left_last_node!=None:
            last_node = left_last_node
        if right_last_node!=None:
            last_node = right_last_node
        if left_last_node!=None:
            left_last_node.right = root.right
            root.right = root.left
        root.left = None
        return last_node
        