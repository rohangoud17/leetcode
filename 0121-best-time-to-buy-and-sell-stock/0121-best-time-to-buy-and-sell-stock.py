class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyStock = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):
            if (prices[i] < buyStock):
                buyStock = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - buyStock)
        
        return maxProfit
        