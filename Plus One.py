class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i] = digits[i]+1
                break
            else:
                digits[i] = 0
        if digits[i]==0:
            digits.insert(0,1)
        return digits
        