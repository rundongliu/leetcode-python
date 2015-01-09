class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        while start<=end:
            if num[start]<num[end]:
                return num[start]
            mid = (start+end)/2
            if num[mid]>num[start]:
                start = mid
            elif num[mid]<num[start]:
                end = mid
            else:
                start += 1
        return num[end]
        