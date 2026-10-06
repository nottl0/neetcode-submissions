class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""

        def dfs(i, open_in_curr, closed_in_curr):
            nonlocal curr
            if i >= 2*n:
                res.append(curr)
                return res
            if open_in_curr < n:
                curr += "("
                dfs(i+1, open_in_curr+1, closed_in_curr)
                curr = curr[:-1]
            if open_in_curr > closed_in_curr:
                curr += ")"
                dfs(i+1, open_in_curr, closed_in_curr+1)
                curr = curr[:-1]

        dfs(0, 0, 0)
        return res
