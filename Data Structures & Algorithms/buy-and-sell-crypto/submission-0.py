class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)): 
            for j in range(len(prices)): 
                if i >= j or prices[i] > prices[j]: 
                    continue
                else: 
                    if (prices[j] - prices[i]) > max_profit: 
                        max_profit = prices[j] - prices[i]

        return max_profit