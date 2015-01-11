# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
        dq = collections.deque()
        dq.append(root)
        dq.append(None)
        count = 1
        while dq:
            node = dq[0]
            dq.popleft()
            if node==None:
                count += 1
                if dq:
                    dq.append(None)
            elif node.left==None and node.right==None:
                return count
            else:
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)