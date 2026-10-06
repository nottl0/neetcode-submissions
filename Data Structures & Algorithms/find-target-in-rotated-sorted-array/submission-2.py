class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        start = 0
        end = len(nums) - 1
        #prevmid = float('inf')
        while start <= end :
            print(start, end)
            mid = (start + end)//2
            # if mid == prevmid:
            #     break
            if nums[mid] == target:
                ans = mid
                return ans
            if nums[mid] >= nums[start]: 
                #sorted in ascending from start to mid 
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                #sorted in ascending from mid to end
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            print(start, end)
            # prevmid = mid
        return ans