# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        st = []
        last = float('-inf')
        while True:
            if not root:
                if not st:
                    break
                if st[-1].val<=last:
                    return False
                last = st[-1].val
                root = st[-1].right
                st.pop()
            else:
                st.append(root)
                root = root.left
        return True
                