class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        lst = [0]*(n+1)
        lst[0]=lst[1]=1
        for i in range(2,n+1):
            lst[i]=lst[i-1]+lst[i-2]
        return lst[n]