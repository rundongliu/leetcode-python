class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['u','t','v'],'9':['w','x','y','z']}
        lst = ['']
        for c in digits:
            lst = [x+y for x in lst for y in dic[c]]
        return lst