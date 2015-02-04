class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle=='':
            return 0
        num = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+num]==needle:
                return i
        return -1