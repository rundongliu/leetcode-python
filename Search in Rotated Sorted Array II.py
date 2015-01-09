class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        start = 0
        end = len(A)-1
        while start<end and A[start]>=A[end]:
            mid = (start+end)/2
            if A[mid]>A[start]:
                start = mid
            elif A[mid]<A[start]:
                end = mid
            else:
                start += 1
        pivot = start
        if A[-1]>=target:
            return self.bsearch(A,target,pivot,len(A)-1)
        else:
            return self.bsearch(A,target,0,pivot-1)
    def bsearch(self,A,target,start,end):
        while start<=end:
            mid = (start+end)/2
            if A[mid]==target:
                return True
            elif A[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return False
        