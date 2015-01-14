class Solution:
    # @return a string
    def countAndSay(self, n):
        if n<=0:
            return ''
        res = '1'
        for i in range(n-1):
            res = self.read(res)
        return res
    def read(self,string):
        lst = []
        count = 0
        current_char = string[0]
        for c in string:
            if c==current_char:
                count += 1
            else:
                lst.append(str(count))
                lst.append(current_char)
                count = 1
                current_char = c
        lst.append(str(count))
        lst.append(current_char)
        return ''.join(lst)
        