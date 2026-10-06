class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        l = [0] * (len(nums)-1)
        m = [0] * (len(nums)-1)
        l[0], m[0] = nums[0], nums[1]
        l[1], m[1] = nums[1], nums[2]
        for i in range(2, len(nums) - 1):
            print(i, max(l[:i-1]) + nums[i])
            l[i] = max(l[i-1], max(l[:i-1]) + nums[i])
        for i in range(3, len(nums)):
            m[i-1] = max(m[i-2], max(m[:i-2]) + nums[i])
        print(l)
        print(m)
        return max(l[-1], m[-1])