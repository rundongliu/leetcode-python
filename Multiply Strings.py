class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res = '0'
        for i,c in enumerate(reversed(num2)):
            num = self.mul(num1,c)
            if num!='0':
                res = self.add(res,num+'0'*i)
        return res
    def mul(self,num,c):
        x = int(c)
        if x==0:
            return '0'
        res = ''
        carry = 0
        for i in reversed(num):
            s = int(i)*x+carry
            res = str(s%10)+res
            carry = s/10
        if carry:
            res = str(carry)+res
        return res
    def add(self,num1,num2):
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        if len(num1)<len(num2):
            num1,num2 = num2,num1
        carry = 0
        res = ''
        for i in range(len(num2)):
            s = int(num1[i])+int(num2[i])+carry
            res = str(s%10)+res
            carry = s/10
        for i in range(len(num2),len(num1)):
            s = int(num1[i])+carry
            res = str(s%10)+res
            carry = s/10
        if carry:
            res = str(carry)+res
        return res
            
            