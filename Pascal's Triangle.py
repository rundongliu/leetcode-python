class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        if numRows==0:
            return result
        result.append([1])
        for i in range(2,numRows+1):
            lst = [1]
            for j in range(1,i-1):
                lst.append(result[-1][j-1]+result[-1][j])
            lst.append(1)
            result.append(lst)
        return result