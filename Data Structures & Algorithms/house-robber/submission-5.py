class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        maxRobbable = [0] * len(nums)
        maxRobbable[1] = nums[1]
        maxRobbable[0] = nums[0]
        for i in range(2, len(nums)):   
            maxRobbable[i] = max((nums[i] + max(maxRobbable[:i-1])), maxRobbable[i-1])
        print(maxRobbable)
        return max(maxRobbable[-1], maxRobbable[-2])