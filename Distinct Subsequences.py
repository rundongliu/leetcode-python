class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S)==0 or len(T)==0:
            return 0
        mat = [[0 for j in range(len(S))] for i in range(len(T))]
        if S[0]==T[0]:
            mat[0][0]=1
        for i in range(1,len(S)):
            if T[0]==S[i]:
                mat[0][i] = mat[0][i-1]+1
            else:
                mat[0][i] = mat[0][i-1]
        for i in range(1,len(T)):
            for j in range(1,len(S)):
                if T[i]!=S[j]:
                    mat[i][j] = mat[i][j-1]
                else:
                    mat[i][j] = mat[i-1][j-1]+mat[i][j-1]
        return mat[-1][-1]