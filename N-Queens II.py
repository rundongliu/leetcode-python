class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.count = 0
        list = [0]*n
        self.nq(0,n,list)
        return self.count
    def nq(self,x,n,list):
        if x==n:
            self.count += 1
            return
        for i in range(n):
            if self.isOK(x,i,list):
                list[x] = i
                self.nq(x+1,n,list)
    def isOK(self,x,y,list):
        for i in range(x):
            if list[i]-i==y-x or list[i]+i==y+x or list[i]==y:
                return False
        return True