class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            elif not stack or c==')' and stack[-1]!='(' or c=='}' and stack[-1]!='{' or c==']' and stack[-1]!='[':
                    return False
            else:
                stack.pop()
        return not stack