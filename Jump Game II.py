class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        step = [0]*len(A)
        far = 0
        if len(A)==1:
            return 0
        for i in range(0,len(A)):
            if i+A[i]>=len(A)-1:
                return step[i]+1
            if i+A[i]>far:
                for j in range(far+1,i+A[i]+1):
                    step[j]=step[i]+1
                far = i+A[i]
            
        return -1