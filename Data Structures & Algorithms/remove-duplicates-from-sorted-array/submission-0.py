
# Sorted array can do binary search so that the tiem complexity is just O(logn)

# want to remove from current array 
# We can't binary search because we can't know where the duplicates are. Which side
# we can do sliding window for O(n) and space complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        left = 0
        # Start at one because we don't want same index
        right = 1
        while right < len(nums):
            if (nums[right] == nums[left]) and (left != right):
                nums.pop(right)
            else:
                left += 1
                right += 1
        
        return len(nums)
