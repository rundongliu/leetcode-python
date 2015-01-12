class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        lst = [0]*len(obstacleGrid[0])
        for i in range(len(lst)):
            if obstacleGrid[0][i]==0:
                lst[i]=1
            else:break
        for i in range(1,len(obstacleGrid)):
            for j in range(len(lst)):
                if obstacleGrid[i][j]==1:
                    lst[j] = 0
                elif j!=0:
                    lst[j] = lst[j]+lst[j-1]
        return lst[-1]