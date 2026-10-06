class Solution:
    def rob(self, nums: List[int]) -> int:
        l = [0]*len(nums)
        l[0] = nums[0]
        if len(nums) <= 2:
            return max(nums)
        else:
            l[0], l[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            l[i] = max(l[i-1], max(l[:i-1])+nums[i])
        return l[-1]