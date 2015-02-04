class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dic = {}
        for s in strs:
            ts = str(sorted(s))
            if dic.has_key(ts):
                dic[ts].append(s)
            else:
                dic[ts] = [s]
        res = []
        for key in dic.keys():
            if len(dic[key])>=2:
                res += dic[key]
        return res