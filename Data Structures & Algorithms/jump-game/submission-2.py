class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s = len(nums) - 1
        goal = s
        for i in range(s - 1, -2, -1):
            if goal == 0:
                return True
            if nums[i] == 0:
                continue
            if nums[i] + i >= goal:
                goal = i

        return False