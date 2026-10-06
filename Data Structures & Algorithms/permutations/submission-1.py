class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        indeces =[]

        def dfs(i, indeces):
            print(i, curr)
            if i >= len(nums) or len(indeces) == 0:
                #print(res)
                res.append(curr.copy())
                return 
            for idx in indeces:
                curr.append(nums[idx])
                dfs(idx, [x for x in indeces if x != idx])
                curr.pop()
            
        
        dfs(0, list(range(len(nums))))
        return res
        