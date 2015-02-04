class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.append(0)
        for num in A:
            n = num
            while n<len(A) and n>0 and A[n]!=n:
                    tmp = A[n]
                    A[n] = n
                    n = tmp
        for i in range(1,len(A)):
            if A[i]!=i:
                return i
        return len(A)