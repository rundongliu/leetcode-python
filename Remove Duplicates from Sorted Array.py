class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        start = 1
        for i in range(1,len(A)):
            if A[i]!=A[start-1]:
                A[start]=A[i]
                start += 1
        return start
        