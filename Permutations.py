class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        numset = set(num)
        lst = []
        res = []
        self.rec(numset,lst,res)
        return res
    def rec(self,numset,lst,res):
        if not numset:
            l = lst[:]
            res.append(l)
            return
        numbers = list(numset)
        for number in numbers:
            numset.remove(number)
            lst.append(number)
            self.rec(numset,lst,res)
            numset.add(number)
            lst.pop()
            
        