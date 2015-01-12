class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        res = []
        S = sorted(S)
        self.rec([],0,S,res)
        return res
    def rec(self,lst,from_num,S,res):
        l = lst[:]
        res.append(l)
        for i in range(from_num,len(S)):
            lst.append(S[i])
            self.rec(lst,i+1,S,res)
            lst.pop()