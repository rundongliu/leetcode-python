class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        while num[start]>num[end]:
            mid = (start+end)/2
            if num[mid]>=num[start]:
                start = mid+1
            else:
                end = mid
        return num[start]
        