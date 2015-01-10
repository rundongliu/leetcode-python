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
        if root==None:
            return
        dq = collections.deque()
        dq.append(root)
        dq.append(None)
        front = TreeNode(0)
        p = front
        while dq:
            node = dq[0]
            dq.popleft()
            if node!=None:
                p.next = node
                p = node
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            elif dq:
                p.next = None
                dq.append(None)
                p = front
        