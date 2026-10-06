class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        scandidates = sorted(candidates)
   
        def dfs(i):
            if sum(curr) == target and curr not in res:
                res.append(curr.copy())
            if i >= len(scandidates):
                return
            if sum(curr) > target:
                return 
            curr.append(scandidates[i])
            print(i, curr)
            dfs(i+1)
            curr.pop()
            print(i)
            dfs(i+1)

        dfs(0)
        return res