class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_num = 0
        dic = {}
        for i,num in enumerate(s):
            if num in dic:
                start = max(start,dic[num]+1)
                dic[num] = i
                max_num = max(i-start+1,max_num)
            else:
                max_num = max(i-start+1,max_num)
                dic[num] = i
        return max_num