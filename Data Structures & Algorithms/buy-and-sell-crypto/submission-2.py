class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxProfit = 0
        while s < len(prices):
            diff = prices[s] - prices[b]
            if diff < 0:
                b = s
                s += 1
                continue
            if diff > maxProfit:
                maxProfit = diff
            s += 1

        return maxProfit
            
            
                
            
            


