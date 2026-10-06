class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        infVal = pow(2, 31) - 1

        def addNeighbor(x, y, cnt):
            if min(x, y) < 0 or x >= rows or y >= cols or \
                grid[x][y] == -1 or grid[x][y] != infVal:
                return 
            else:
                grid[x][y] = cnt
                q.append((x, y))
                return

        counter = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i, j in neighbors:
                    addNeighbor(x + i, y + j, counter)
            counter += 1
        return 
                

