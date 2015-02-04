class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s:
            return True
        lst = [False]*len(s)
        for i in range(0,len(s)):
            if s[:i+1] in dict:
                lst[i] = True
                continue
            for j in range(i):
                if lst[j]==True and s[j+1:i+1] in dict:
                    lst[i] = True
                    break
        return lst[-1]