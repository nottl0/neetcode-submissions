class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                        
                elif sums < 0:
                    j += 1
                else:
                    k -= 1
        return ans
        
            