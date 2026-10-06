class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = nums[-1]
        nums_l = len(nums)
        new_arr = [nums[0]]*nums_l
        for i in range(0, nums_l):
            new_arr[i] = left
            left *= nums[i]
        for j in range(nums_l-2, -1, -1):
            new_arr[j] *= right
            right *= nums[j]
        return new_arr

