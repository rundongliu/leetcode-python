class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num)<2:
            return 0
        min_num = num[0]
        max_num = num[0]
        for x in num:
            min_num = min(min_num,x)
            max_num = max(max_num,x)
        m = (max_num-min_num)/len(num)+1
        lst1 = [-1]*len(num)
        lst2 = [-1]*len(num)
        for x in num:
            index = (x-min_num)/m
            if lst1[index]==-1:
                lst1[index] = x
                lst2[index] = x
            else:
                lst1[index] = min(x,lst1[index])
                lst2[index] = max(x,lst2[index])
        res = 0
        start = 0
        for i in range(1,len(num)):
            if lst1[i]==-1:
                continue
            res = max(res,lst1[i]-lst2[start])
            start = i
        return res