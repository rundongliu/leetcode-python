class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.rec([],0,candidates,target,res)
        return res
    
    def rec(self,lst,index,numbers,target,res):
        if target==0:
            res.append(lst)
            return
        if index>=len(numbers) or numbers[index]>target:
            return
        for i in range(0,target/numbers[index]+1):
            if not(lst and lst[-1]==numbers[index]):
                l = lst+[numbers[index]]*i
                self.rec(l,index+1,numbers,target-i*numbers[index],res)