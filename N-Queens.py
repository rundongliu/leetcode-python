class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        self.rec([0]*n,0,n,res)
        return res
    def rec(self,lst,step,n,res):
        if step==n:
            res.append(self.gen(lst,n))
            return
        for i in range(n):
            if self.ok(lst,step,i):
                lst[step] = i
                self.rec(lst,step+1,n,res)
    def ok(self,lst,step,x):
        for i in range(step):
            if i+lst[i]==x+step or i-lst[i]==step-x or x==lst[i]:
                return False
        return True
    def gen(self,lst,n):
        matrix = []
        for num in lst:
            matrix.append('.'*num+'Q'+'.'*(n-num-1))
        return matrix