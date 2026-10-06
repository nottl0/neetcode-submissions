class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        indeces = []

        def dfs(i, indeces):
            if i >= len(nums):
                res.append(curr.copy())
                return
            for ind in indeces:
                curr.append(nums[ind])
                dfs(i+1, [x for x in indeces if x != ind])
                curr.pop()
        dfs(0, list(range(len(nums))))
        return res