class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            
            if (sell > buy):
                profit = sell - buy 
                maxProfit = max(profit, maxProfit)
            else:
                l = r

            r += 1

        return maxProfit