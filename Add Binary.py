class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_index = len(a)-1
        b_index = len(b)-1
        carry = 0
        lst = []
        while a_index>=0 or b_index>=0:
            if a_index>=0:
                a_char = int(a[a_index])
            else:
                a_char = 0
            if b_index>=0:
                b_char = int(b[b_index])
            else:
                b_char = 0
            sum = a_char+b_char+carry
            lst.append(str(sum%2))
            carry = sum/2
            a_index -= 1
            b_index -= 1
        if carry>0:
            lst.append(str(carry))
        lst.reverse()
        return "".join(lst)
        