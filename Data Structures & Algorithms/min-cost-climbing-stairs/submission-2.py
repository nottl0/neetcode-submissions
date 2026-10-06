class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        cumCost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            cumCost[i] = min((cost[i-2] + cumCost[i-2]), (cost[i-1] + cumCost[i-1]))
        return cumCost[-1]