class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        start = 0
        end = x
        while start<=end:
            mid = (start+end)/2
            if mid*mid>x:
                end = mid-1
            elif mid*mid<x:
                start = mid+1
            else:
                return mid
        return end