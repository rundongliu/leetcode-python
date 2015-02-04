class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.rec([],candidates,0,target,res)
        return res
    def rec(self,lst,candidates,index,target,res):
        if target==0:
            res.append(lst[:])
            return
        if target<0:
            return
        for i in range(index,len(candidates)):
            if i==index or candidates[i]!=candidates[i-1]:
                lst.append(candidates[i])
                self.rec(lst,candidates,i+1,target-candidates[i],res)
                lst.pop()