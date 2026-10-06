class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftOfNum = [1] * len(nums)
        rightOfNum = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            leftOfNum[i] = nums[i-1] * leftOfNum[i-1]
        for i in range(len(nums)):
            if i == 0:
                continue
            j = len(nums) - 1 - i
            rightOfNum[j] = nums[j+1] * rightOfNum[j+1]
        
        return [l*r for l, r in zip(leftOfNum, rightOfNum)]