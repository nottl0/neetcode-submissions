class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = set()
        curr = []
        def dfs(i):
            if i == len(nums) or sum(curr) > target:
                return 
            if sum(curr) == target:
                if tuple(curr) not in final:
                    final.add(tuple(curr.copy()))
                return 
            curr.append(nums[i])
            dfs(i)
            dfs(i + 1)
            curr.pop()
            dfs(i + 1)

        dfs(0)
        return [list(f) for f in list(final)]
