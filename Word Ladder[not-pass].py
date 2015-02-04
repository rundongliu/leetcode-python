class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dic = {}
        dq = collections.deque()
        dq.append(start)
        dq.append(None)
        st = set()
        count = 1
        while dq:
            word = dq.popleft()
            if not word:
                if not dq:
                    break
                count+=1
                dq.append(None)
            else:
                if word==end:
                    return count
                st.add(word)
                for x in dict:
                    if x not in st and self.trans(x,word):
                            dq.append(x)
        return 0
    def trans(self,word1,word2):
        flag = 0
        for x,y in zip(word1,word2):
            if x!=y:
                if flag==0:
                    flag=1
                else:
                    return False
        return True