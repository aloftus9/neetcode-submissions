class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(set(nums)) < len(nums):
            return True
        else:
            return False