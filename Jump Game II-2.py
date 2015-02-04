class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<=1:
            return 0
        now = 0
        maxdis = now+A[now]
        count = 0
        while now<len(A):
            count+=1
            if maxdis>=len(A)-1:
                return count
            temp = maxdis
            for i in range(now+1,maxdis+1):
                temp = max(temp,i+A[i])
            now = maxdis
            maxdis = temp
        retunr -1