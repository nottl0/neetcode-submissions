class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        curr = 0
        sell = 1
        profit = 0

        while sell < len(prices) and sell > buy:
            if prices[curr] < prices[buy]:
                buy = curr
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
            curr += 1
            sell += 1
        return profit
            