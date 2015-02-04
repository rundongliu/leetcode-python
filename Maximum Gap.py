class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num)<2:
            return 0
        for i in range(32):
            first = []
            second = []
            for x in num:
                if ((x>>i)&1)==0:
                    first.append(x)
                else:
                    second.append(x)
            num = first+second
        res = 0
        for i in range(0,len(num)-1):
            res = max(num[i+1]-num[i],res)
        return res
        