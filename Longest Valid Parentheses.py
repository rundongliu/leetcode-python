class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        st = []
        max_num = 0
        for i,x in enumerate(s):
            if x=='(':
                st.append((x,i))
            else:
                if st and st[-1][0]=='(':
                    st.pop()
                    if st:
                        max_num = max(max_num,i-st[-1][1])
                    else:
                        max_num = max(max_num,i+1)
                else:
                    st.append((x,i))
                    
        return max_num
        