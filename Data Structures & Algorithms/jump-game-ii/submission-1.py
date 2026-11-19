class Solution:
    def jump(self, nums: List[int]) -> int:
        s = len(nums)
        steps = [float('inf')] * s
        steps[-1] = 0

        for i in range(s - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < s:
                    steps[i] = min(steps[i], steps[i+j] + 1)

        return steps[0]