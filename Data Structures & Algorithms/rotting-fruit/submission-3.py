class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # total = 0
        if sum([sum(x) for x in grid]) == 0:
            return 0
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        def addGrid(i, j):
            if i >= ROWS or j >= COLS or min(i, j) < 0 \
                or grid[i][j] == 0 or (i, j) in visited:
                return 
            visited.add((i, j))
            grid[i][j] = 2
            queue.append((i, j))

        counter = 0  
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for m, n in neighbours:
                    addGrid(x + m, y + n)
            counter += 1
    
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    return -1
        return counter - 1 

        