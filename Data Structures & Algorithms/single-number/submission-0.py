class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for v in nums:
            if v not in s:
                s.add(v)
            else:
                s.remove(v)
        return list(s)[0]