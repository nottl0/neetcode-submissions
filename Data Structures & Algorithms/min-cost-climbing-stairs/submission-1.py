class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        # l[i] - minimum cost to reach i 
        l = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            l[i] = min(l[i-1] + cost[i-1], l[i-2] + cost[i-2])
        return l[-1]