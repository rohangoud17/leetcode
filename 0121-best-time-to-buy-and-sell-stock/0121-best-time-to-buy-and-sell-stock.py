class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if ((prices[i] - prev) > max_profit):
                    max_profit = prices[i] - prev
            if (prices[i] <  prev):
                prev = prices[i]
        
        return max_profit
            

            






        