class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        oldp = prices[0]
        sum = 0
        for currentp in prices:
            if currentp > oldp:
                sum += currentp - oldp
            oldp = currentp
        return sum
        