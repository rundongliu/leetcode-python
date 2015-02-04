class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        isp = [[False]*len(s) for i in range(len(s))]
        mincut = [len(s)]*len(s)
        for i in range(len(s)):
            m = len(s)
            for j in range(i+1):
                if s[i]==s[j]:
                    if i-1>=j+1 and isp[j+1][i-1]:
                        isp[j][i] = True
                    elif j+1>=i:
                        isp[j][i] = True
                    else:
                        continue
                    if j==0:
                        m = 0
                    else:
                        m = min(m,mincut[j-1]+1)
            mincut[i]  = m
        return mincut[-1]