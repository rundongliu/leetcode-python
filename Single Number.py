class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        num = 0
        for i in A:
            num = num^i
        return num
        