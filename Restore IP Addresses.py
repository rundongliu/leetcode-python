class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        self.rec(0,'',s,0,res)
        return res
    def rec(self,count,current,s,index,res):
        if index==len(s):
            if count==4:
                res.append(current[1:])
            return
        if count>=4:
            return
        for i in range(index+1,min(index+4,len(s)+1)):
            if s[index:i]=='0' or s[index]!='0':
                if i==index+3:
                    if int(s[index:i])<=255:
                        self.rec(count+1,current+'.'+s[index:i],s,i,res)
                else:
                    self.rec(count+1,current+'.'+s[index:i],s,i,res)
            