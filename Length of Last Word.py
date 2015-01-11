class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        flag = 0
        count = 0
        for c in reversed(s):
            if ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z'):
                if flag==0:
                    flag = 1
                    count = 1
                else:
                    count += 1
            else:
                if flag==1:
                    return count
        if flag==1:
            return count
        return 0