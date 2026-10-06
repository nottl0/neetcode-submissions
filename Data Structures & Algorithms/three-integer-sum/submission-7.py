class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums = sorted(nums)
        prevMid = None
        for start in range(len(nums)):
            # we dont skip for starts if we break with mids
            # if start >= 1 and nums[start] == nums[start-1]:
            #     mid = start + 1
            #     continue
            # else:
            mid = start + 1
            prevMid = None
            end = len(nums) - 1
            while mid < end:

                if prevMid and nums[mid] == prevMid:
                    mid += 1
                    continue

                num_sum = nums[start] + nums[mid] + nums[end]

                if num_sum == 0:
                    s.add((nums[start], nums[mid], nums[end]))
                    end -= 1
                    mid = start + 1
                    prevMid = None

                elif num_sum > 0:
                    end -= 1
                    mid = start + 1
                    prevMid = None

                else:
                    mid += 1
                    prevMid = mid
        return [list(subset) for subset in list(s)]
                    
                    

            
            