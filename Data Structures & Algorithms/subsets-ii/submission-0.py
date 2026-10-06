class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        snums = sorted(nums)
    
        def dfs(i, curr):
            if i >= len(snums):
                res.append(curr.copy())
                return
            curr.append(snums[i])
            dfs(i+1, curr)
            curr.pop()
            while i + 1 < len(snums) and snums[i] == snums[i + 1]:
                i += 1 
            dfs(i+1, curr)
        
        dfs(0, [])
        return res