class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        minel = nums[0]
        while l < r:
            mid = (r + l) // 2
            if nums[l] >= nums[mid] and nums[r] >= nums[mid]:
                # if this is true theres definitely a shift
                # bcs left coulndt have been bigger than mid
                # and if shift happened, el-s on the left can't 
                # be smaller than on the right 
                #if nums[l] > nums[r]:
                if nums[mid] < minel:
                    minel = nums[mid]
                r = mid - 1
            # nums[l] > nums[mid] and nums[r] < nums[mid]
            # is impossible bcs if nums[l] > nums[mid] there was
            # a shift so it cant be that nums[r] < nums[mid] < nums[l]
            
            elif nums[l] <= nums[mid] and nums[r] >= nums[mid]:
                # only possible with correct sorting bcs otherwise
                # nums[l] > nums[r] after rot-n
                return nums[l]
            
            elif nums[l] <= nums[mid] and nums[r] <= nums[mid]:
                if nums[r] < minel:
                    minel = nums[r]
                l = mid + 1

            else:
                print(nums[l:r+1])
                print('unexpected')
                return 0

        return minel

            


                
