class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==1:
            return A[0]
        current = A[0]
        maxnum = A[0]
        for i in range(1,len(A)):
            if current<0:
                current = A[i]
            else:
                current += A[i]
            maxnum = max(maxnum,current)
        return maxnum
        