# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []
        if root==None:
            return res
        lst = [root]
        index = 0
        while lst:
            temp = []
            next_list = []
            for node in  lst:
                temp.append(node.val)
                if node.left!=None:
                    next_list.append(node.left)
                if node.right!=None:
                    next_list.append(node.right)
            if index%2==1:
                temp.reverse()
            res.append(temp)
            lst = next_list
            index += 1
        return res