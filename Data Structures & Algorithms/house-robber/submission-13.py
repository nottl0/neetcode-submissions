class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) 
        maxRobbed = [-1] * len(nums) 
        maxRobbed[0], maxRobbed[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            maxRobbed[i] = max(max(maxRobbed[:i-1]) + nums[i], maxRobbed[i - 1])
        return maxRobbed[-1]