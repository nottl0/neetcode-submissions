class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 0
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[minn]
            print(minn, diff)
            if diff > profit:
                profit = diff
            if diff < 0:
                minn = i
        return profit
