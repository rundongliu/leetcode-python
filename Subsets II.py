class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S=sorted(S)
    	res = []
    	self.rec([],S,0,res)
    	return res
    
    def rec(self,lst,S,index,res):
    	if index>=len(S):
    		l = lst[:]
    		res.append(l)
    		return
    	lst.append(S[index])
    	self.rec(lst,S,index+1,res)
    	lst.pop()
    	if not(lst and lst[-1]==S[index]):
    		self.rec(lst,S,index+1,res)
            
        