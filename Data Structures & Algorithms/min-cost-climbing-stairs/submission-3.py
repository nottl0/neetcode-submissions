class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumul = [-1] * len(cost)
        def dfs(i):
            if i >= len(cost) or i < 0:
                return 0
            if cumul[i] != -1:
                return cumul[i]
            cumul[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            print(cumul)
            return cumul[i]

        return min(dfs(0), dfs(1))