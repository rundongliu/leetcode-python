class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        far = A[0]
        for i,num in enumerate(A):
            if i>far:
                return False
            elif far>=len(A)-1:
                return True
            else:
                far = max(far,i+num)
        return False