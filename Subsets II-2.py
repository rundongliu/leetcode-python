class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        if not S:
            return res
        S = sorted(S)
        S.append(S[-1]+1)
        count = 1
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                count += 1
            else:
                num = S[i-1]
                last_len = len(res)
                for j in range(1,count+1):
                    change_lst = j*[num]
                    for k in range(last_len):
                        lst = res[k]
                        lst = lst+change_lst
                        res.append(lst)
                count = 1
        return res