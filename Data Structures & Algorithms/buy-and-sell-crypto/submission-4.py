class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxDiff = 0
        while sell < len(prices):
            diff = prices[sell] - prices[buy]
            if diff > maxDiff:
                maxDiff = diff
            elif diff < 0:
                buy = sell
            sell += 1
        return maxDiff

