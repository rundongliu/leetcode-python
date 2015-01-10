class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in range(32):
            num = 0
            for ele in A:
                num = num+((ele>>i)&1)
            num = num%3
            res = res|(num<<i)
        if res&0x80000000:
            return -(res ^ 0xFFFFFFFF ) -1
        return res
        