class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) in [0,1]:
            return 0
        buy = 0
        sell = 1
        while sell < len(prices):
            newProfit = prices[sell] - prices[buy]
            maxProfit = newProfit if newProfit > maxProfit else maxProfit
            if newProfit < 0:
                buy = sell
                continue
            sell += 1
        return maxProfit

            
        