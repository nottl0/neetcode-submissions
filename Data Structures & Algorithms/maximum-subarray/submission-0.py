class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        interval_sum = 0

        for num in nums:
            interval_sum += num
            largest_sum = max(largest_sum, interval_sum)
            if interval_sum < 0:
                interval_sum = 0

        return largest_sum