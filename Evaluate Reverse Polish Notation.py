class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        st = []
        for token in tokens:
            if token=='+' or token=='-' or token=='/' or token=='*':
                y = st.pop()
                x = st.pop()
                if token =='+':
                    st.append(x+y)
                elif token=='-':
                    st.append(x-y)
                elif token=='*':
                    st.append(x*y)
                else:
                    if x*y>=0:
                        st.append(x/y)
                    else:
                        st.append(-(abs(x)/abs(y)))
            else:
                st.append(int(token))
        return st.pop()
        