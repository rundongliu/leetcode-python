class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        count = 1
        start = 0
        for i in range(1,len(A)):
            if A[i]==A[start]:
                count += 1
            else:
                count = 1
            if count<=2:
                start += 1
                A[start] = A[i]
        return start+1