class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end = len(A)-1
        while start<=end:
            mid = (start+end)/2
            if A[mid]==target:
                return mid
            if A[mid]>A[start]:
                if A[start]<=target and A[mid]>=target:
                    end = mid
                else:
                    start = mid+1
            elif A[mid]<A[start]:
                if A[end]>=target and target>=A[mid]:
                    start = mid
                else:
                    end = mid-1
            else:
                start+=1
        return -1