# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        dq = collections.deque()
        dq.appendleft(root.left)
        dq.append(root.right)
        while dq:
            ln = dq[0]
            rn = dq[-1]
            dq.popleft()
            dq.pop()
            if ln==None and rn!=None or ln!=None and rn==None:
                return False
            elif ln==None and rn==None:
                continue
            elif ln.val!=rn.val:
                return False
            else:
                dq.appendleft(ln.right)
                dq.append(rn.left)
                dq.appendleft(ln.left)
                dq.append(rn.right)
        return True