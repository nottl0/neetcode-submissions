class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = set()
        n = len(nums)

        for left in range(n):
            mid = left + 1
            right = n - 1

            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    sols.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1
                elif total < 0:
                    mid += 1
                else:
                    right -= 1

        return [list(t) for t in sols]
