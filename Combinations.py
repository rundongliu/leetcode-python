class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        lst = []
        self.rec(lst,1,n,k,res)
        return res
        
    def rec(self,lst,from_num,n,num_left,res):
        if num_left==0:
            lst = lst[:]
            res.append(lst)
            return
        for i in range(from_num,n-num_left+2):
            lst.append(i)
            self.rec(lst,i+1,n,num_left-1,res)
            lst.pop()
            