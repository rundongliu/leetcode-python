class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        t = x
        reverse = 0
        while t:
            reverse = reverse*10+(t%10)
            t = t/10
        return reverse == x