class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = []
        for i in range(n):
            matrix.append([0]*n)
        count = 1
        for i in range(0,n/2):
            for j in range(i,n-1-i):
                matrix[i][j]=count
                count += 1
            for j in range(i,n-1-i):
                matrix[j][n-1-i]=count
                count += 1
            for j in range(n-1-i,i,-1):
                matrix[n-i-1][j] = count
                count += 1
            for j in range(n-1-i,i,-1):
                matrix[j][i] = count
                count += 1
        if n%2==1:
            matrix[n/2][n/2]=count
        return matrix
            
        