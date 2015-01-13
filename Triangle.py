class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        lst = triangle[0]
        for i in range(1,len(triangle)):
            lst.append(lst[-1]+triangle[i][-1])
            for j in range(len(lst)-2,0,-1):
                lst[j] = triangle[i][j]+min(lst[j-1],lst[j])
            lst[0] = lst[0]+triangle[i][0]
        return min(lst)