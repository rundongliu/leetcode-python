class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_num = 0
        dic = {}
        for i,num in enumerate(s):
            if num in dic:
                tmp = dic[num]
                for j in range(start,tmp+1):
                    del dic[s[j]]
                start = tmp+1
                dic[num] = i
                
            else:
                max_num = max(i-start+1,max_num)
                dic[num] = i
        return max_num