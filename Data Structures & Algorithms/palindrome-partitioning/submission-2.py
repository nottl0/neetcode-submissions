class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return res
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j + 1)
                    curr.pop()

        dfs(0)
        return res

    def isPali(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start, end = start + 1, end - 1
        return True 