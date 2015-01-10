class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        lst = []
        if n <= 0:
            return lst
        lst.append('()')
        for i in range(n-1):
            l = len(lst)
            for j in range(l):
                lst.append(lst[j]+'()')
                lst[j] = '('+lst[j]+')'
        return lst
        