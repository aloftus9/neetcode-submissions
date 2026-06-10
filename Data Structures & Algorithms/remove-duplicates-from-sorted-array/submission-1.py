class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # don't need to check the first
        left = 1
        

        for right in range(1, len(nums)):

            # Check if right is equal to the previous
            if nums[right] != nums[right - 1]:
                # left marks where the next unique number should be written
                nums[left] = nums[right]
                left += 1


        return left