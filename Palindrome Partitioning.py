class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.res = []
        self.rec(0,[],s)
        return self.res
    def rec(self,index,now_lst,s):
        if index==len(s):
            self.res.append(now_lst[:])
            return
        for i in range(index+1,len(s)+1):
            string = s[index:i]
            if self.isp(string):
                now_lst.append(string)
                self.rec(i,now_lst,s)
                now_lst.pop()
        
    def isp(self,string):
        for i in range(len(string)/2):
            if string[i]!=string[len(string)-i-1]:
                return False
        return True
        