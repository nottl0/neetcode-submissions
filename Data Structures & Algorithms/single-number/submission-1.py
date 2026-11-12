class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # choose 0 as initial value, so that when the single
        # number is xor-ed with 0 it produces the number itself
        # because 0 is all 0s in bits, and the 1s from the number
        # remain
        result = 0
        # number xor-ed by the same number twice produces the number back
        for v in nums:
            result ^= v
        return result
