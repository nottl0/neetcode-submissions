class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        scandidates = sorted(candidates)
   
        def dfs(i, curr, total):
            if total == target and curr not in res:
                res.append(curr.copy())
            if i >= len(scandidates):
                return
            if total > target:
                return 
            curr.append(scandidates[i])
            print(i, curr)
            dfs(i+1, curr, total + scandidates[i])
            curr.pop()
            print(i, curr)
            dfs(i+1, curr, total)

        dfs(0, curr, 0)
        return res