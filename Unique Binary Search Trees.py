class Solution:
    # @return an integer
    def numTrees(self, n):
        lst = [0]*(n+1)
        lst[0]=lst[1]=1
        for i in range(2,len(lst)):
            sum = 0
            for j in range(0,i):
                sum+=lst[j]*lst[i-j-1]
            lst[i] = sum
        return lst[n]
        