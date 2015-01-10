class Solution:
    # @return an integer
    def reverse(self, x):
        flag = 0
        if x & 0x80000000:
            flag = 1
            x = -x
        res = 0
        while x > 0:
            num = x %10
            res = res *10 +num
            x = x/10
        if res>0x7fffffff:
            return 0
        if flag == 1:
            res = -res
        return res
        
        