class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        res = []
        def dfs(i):
            if i == len(s):
                res.append(curr.copy())
                return 
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j + 1)
                    curr.pop()
        dfs(0)
        return res

def isPali(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True