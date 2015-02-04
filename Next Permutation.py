class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        index = -1
        for i in range(len(num)-2,-1,-1):
            if num[i]<num[i+1]:
                index = i
                break
        if index==-1:
            return list(reversed(num))
        last = -1
        for i in range(len(num)-1,-1,-1):
            if num[i]>num[index]:
                last = i
                break
        num[index],num[last] = num[last],num[index]
        return num[:index+1]+list(reversed(num[index+1:]))