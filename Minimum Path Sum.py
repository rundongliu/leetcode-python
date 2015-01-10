class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid:
            return 0
        lst = [0]*len(grid[0])
        lst[0] = grid[0][0]
        for i in range(1,len(grid[0])):
            lst[i] = lst[i-1]+grid[0][i]
        for i in range(1,len(grid)):
            for j in range(0,len(grid[0])):
                if j == 0:
                    lst[j] = lst[j]+grid[i][j]
                else:
                    lst[j] = min(lst[j],lst[j-1])+grid[i][j]
        return lst[-1]