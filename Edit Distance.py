class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        mat = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for i in range(len(mat[0])):
            mat[0][i] = i
        for i in range(len(mat)):
            mat[i][0] = i
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                if word1[j-1]==word2[i-1]:
                    mat[i][j] = min(mat[i-1][j-1],mat[i][j-1]+1,mat[i-1][j]+1)
                else:
                    mat[i][j] = min(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+1
        return mat[-1][-1]