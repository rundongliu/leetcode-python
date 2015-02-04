class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        words = {}
        for x in num:
            if words.has_key(x):
                words[x] += 1
            else:
                words[x] = 1
        res = []
        self.rec([],words,res)
        return res
    def rec(self,current_lst,words,res):
        if not words:
            res.append(current_lst[:])
            return
        for key in words.keys():
            current_lst.append(key)
            if words[key]==1:
                del words[key]
            else:
                words[key] -= 1
            self.rec(current_lst,words,res)
            current_lst.pop()
            if words.has_key(key):
                words[key] += 1
            else:
                words[key] = 1