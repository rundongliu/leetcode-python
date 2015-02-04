class Solution:
    # @return a string
    def getPermutation(self, n, k):
        fac = [1]*n
        for i in range(1,n):
            fac[i] = fac[i-1]*i
        fac.append
        lst = [str(i) for i in range(1,n+1)]
        res = []
        k = k-1
        while k>0:
            num = k/fac[n-1]
            res.append(lst[num])
            del lst[num]
            k -= num*fac[n-1]
            n -= 1
        return ''.join(res+lst)