from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        longest = 1
        for n in s:
            if n - 1 not in s:
                l = 1
                while n + l in s:
                    l += 1
                longest = max(l, longest)
        return longest