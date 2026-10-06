class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        
        # i -> current pointer (what nums are still availible)
        # curr -> elements in the current set
        # total -> sum of current elements
        def dfs(i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy()) # we only have 1 curr var, and it will change
                return 
            if i >= len(nums) or total > target:
                return 
            
            # 2 decisions at each node: 
            # 1) include cadnidate 
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            # remove inclusion of candidate
            curr.pop()
            # 2) not using candidate
            dfs(i+1, curr, total)
        dfs(0, curr, 0)
        return res