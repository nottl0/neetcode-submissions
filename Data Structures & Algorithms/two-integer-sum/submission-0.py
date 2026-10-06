class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                if d[target - n] < i:
                    return [d[target - n], i]
                else:
                    return [i, d[target - n]]
            else:
                d[n] = i