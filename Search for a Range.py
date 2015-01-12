class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        index = self.bsearch(A,target,0,len(A)-1)
        if index==-1:
            return [-1,-1]
        left = index
        t = self.bsearch(A,target,0,left-1)
        while t!=-1:
            left = t
            t = self.bsearch(A,target,0,left-1)
        right = index
        t = self.bsearch(A,target,right+1,len(A)-1)
        while t!=-1:
            right = t
            t = self.bsearch(A,target,right+1,len(A)-1)
        return [left,right]
            
    def bsearch(self,A,target,start,end):
        if start<0 or start>=len(A):
            return -1
        while start<=end:
            mid = (start+end)/2
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return -1