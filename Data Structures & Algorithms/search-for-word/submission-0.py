class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set() 

        def dfs(i, j, z):
            if z == len(word):
                return True
            if i >= rows or i < 0 or \
                j >= cols or j < 0 or word[z] != board[i][j] or \
                (i, j) in path:
                return False
            path.add((i, j))
            res = dfs(i+1, j, z+1) or \
                dfs(i-1, j, z+1) or \
                dfs(i, j-1, z+1) or \
                dfs(i, j+1, z+1)
            path.remove((i, j))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
            
        

            
