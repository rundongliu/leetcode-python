class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        res = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i] = res[i-1]+1
        num = res[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and res[i]<=res[i+1]:
                res[i] = res[i+1]+1
            num+= res[i]
        return num
        