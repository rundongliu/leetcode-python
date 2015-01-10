class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        lst = [1]*n
        for i in range(m-1):
            for j in range(1,n):
                lst[j]=lst[j-1]+lst[j]
        return lst[n-1]
        