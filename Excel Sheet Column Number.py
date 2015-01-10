class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in range(len(s)):
            num = ord(s[i])-ord('A')+1
            res = res*26+num
        return res