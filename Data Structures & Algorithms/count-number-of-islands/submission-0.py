class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbor_shift = [
        (x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)
        ]

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for x, y in neighbor_shift:
                dfs(i + x, j + y)

        total = 0 
        neighbor_shift = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total += 1
        return total