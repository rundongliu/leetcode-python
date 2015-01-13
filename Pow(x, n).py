class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        flag = 0
        if n<0:
            flag = 1
            n = -n
        if n==0:
            return 1
        if n%2==1:
            t = self.pow(x,(n-1)/2)
            res = t*t*x
        else:
            t = self.pow(x,n/2)
            res = t*t
        if flag:
            res = 1/res
        return res