class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        start = 0
        end = len(A)-1
        storage = 0
        left_height = A[start]
        right_height = A[end]
        while start<end:
            if A[start]>left_height:
                left_height = A[start]
            if A[end]>right_height:
                right_height = A[end]
            if left_height<right_height:
                storage += left_height - A[start]
                start+=1
            else:
                storage += right_height - A[end]
                end -= 1
        return storage
        