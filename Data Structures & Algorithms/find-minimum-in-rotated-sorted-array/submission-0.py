
# Use binary search to only go through the list log(n) times
# If there is a sorted side we know the non sorted side will have the min unless the nums[left] == min
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0

        right = len(nums) - 1
        minimum = float("inf")

        while left <= right:
            mid = (left + right) // 2
            
            # If mid is the lowest
            if nums[mid] < nums [mid - 1]:
                return nums[mid]
                
            # The left is sorted
            if nums[mid] > nums[right]:
                left = mid + 1
            # The right is sorted
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                # The list is fully sorted
                return min(nums[left], nums[right])
        
