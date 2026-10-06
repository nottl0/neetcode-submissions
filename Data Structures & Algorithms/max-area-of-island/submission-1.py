class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        total = 0
        curr = 0

        neighbour_shifts = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def dfs(i, j):
            nonlocal total, curr
            
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 
            grid[i][j] = 0
            curr += 1
            if curr > total:
                total = curr
            for x, y in neighbour_shifts:
                dfs(i+x, j+y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
                curr = 0
        return total 

        