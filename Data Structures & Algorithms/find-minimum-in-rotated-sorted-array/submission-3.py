class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        smallest = nums[0]
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < smallest:
                smallest = nums[mid]

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end] and nums[mid] > nums[start]:
                end = mid - 1
            else:
                if nums[start] > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1

        return smallest
            