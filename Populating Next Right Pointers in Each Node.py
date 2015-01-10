# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        line = []
        line.append(root)
        while line:
            templist = []
            for elem in line:
                if elem.left:
                    templist.append(elem.left)
                if  elem.right:
                    templist.append(elem.right)
            line = templist
            if len(line)>1:
                for i in range(len(line)-1):
                    line[i].next = line[i+1]
        