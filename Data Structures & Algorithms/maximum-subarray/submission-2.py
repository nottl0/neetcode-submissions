class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in nums[1:]:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
            