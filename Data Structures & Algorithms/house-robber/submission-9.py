class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums)
        maxMoney = nums.copy()
        for i in range(2, len(nums)):
            maxMoney[i] = max(max(maxMoney[:i-1]) + nums[i], maxMoney[i-1])
        return maxMoney[-1]

# [5, 1, 5, ]