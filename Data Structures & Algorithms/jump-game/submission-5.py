class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        i = target - 1
        flag = True
        while i >= 0:
            if i + nums[i] >= target:
                target = i
                flag = True
            else:
                flag = False
            i -= 1 
        return flag