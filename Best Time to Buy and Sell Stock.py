class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        low = prices[0]
        prof = 0
        for price in prices:
            low = min(low,price)
            prof = max(prof,price-low)
        return prof