class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        s = len(word)
        # global
        path = set() 

        def dfs(i, j, m):
            if m == s:
                return True
            if min(i, j) < 0 or i >= rows or j >= cols or board[i][j] != word[m] or (i, j) in path:
                return False
            path.add((i, j))
            res = dfs(i - 1, j, m + 1) or \
                    dfs(i + 1, j, m + 1) or \
                    dfs(i, j - 1, m + 1) or \
                    dfs(i, j + 1, m + 1)
            path.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
            
        