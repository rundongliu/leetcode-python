class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        index = 0
        flag = 0
        while True:
            if index >= len(strs[0]):
                break
            c = strs[0][index]
            for i in range(1,len(strs)):
                if index >= len(strs[i]) or strs[i][index]!=c:
                    flag = 1
                    break
            if flag:
                break
            index += 1
        return strs[0][0:index]