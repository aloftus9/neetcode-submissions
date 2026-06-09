
# Trying to do logn time means we have to do binary search
# 
# We know the min is in the unsorted side
# But need to check if sorted
class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Right side is not sorted
            if nums[mid] > nums[right]:
                left = mid + 1
            # left side is not sorted or mid is the min
            else:
                right = mid

        return nums[left]
        
        