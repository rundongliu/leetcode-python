class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        start = 0
        for i in range(len(A)):
            if A[i]==0:
                A[start],A[i] = A[i],A[start]
                start += 1
        for i in range(start,len(A)):
            if A[i]==1:
                A[start],A[i] = A[i],A[start]
                start += 1
        