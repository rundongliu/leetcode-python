class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num)==1:
            return 0
        elif num[1]<num[0]:
            return 0
        elif num[-2]<num[-1]:
            return len(num)-1
        start = 1
        end = len(num)-2
        while start<=end:
            mid = (start+end)/2
            if num[mid]<=num[mid-1]:
                end = mid-1
            elif num[mid]<=num[mid+1]:
                start = mid+1
            else:
                return mid
        