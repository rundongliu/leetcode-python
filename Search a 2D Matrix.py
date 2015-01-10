class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        rownum = self.findrow(matrix,target)
        if rownum==-1:
            return False
        colnum = self.findcol(matrix[rownum],target)
        if colnum==-1:
            return False
        return True
    
    def findrow(self,matrix,target):
        if target<matrix[0][0]:
            return -1
        elif target>matrix[-1][-1]:
            return -1
        start = 0
        end = len(matrix)-1
        while start<=end:
            mid = (start+end)/2
            if matrix[mid][0]==target:
                return mid
            elif matrix[mid][0]<target:
                start = mid+1
            else:
                end = mid-1
        return end
    def findcol(self,lst,target):
        start = 0
        end = len(lst)-1
        while start<=end:
            mid = (start+end)/2
            if lst[mid]==target:
                return mid
            elif lst[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return -1
        