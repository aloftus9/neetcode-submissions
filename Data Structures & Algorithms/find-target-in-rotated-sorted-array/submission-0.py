

# Binary search
# One side is always sorted
# If left side
# [3,4,5,6,1,2]
# left 3
# right 5
# mid 4
# target = 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            # Left side is sorted, so can check the left side for the target
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right side is sorted so can check right 
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1


            
            
