class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = 0
        lookup_hash = {}
        # Find the smallest number, see if there's another number that equals that

        # For number in nums
        # Get the taget minus num, lookup
        for num in nums:
            number_to_look_for = target - num
            if number_to_look_for in lookup_hash:
                return [lookup_hash[number_to_look_for], count]
            else:
                lookup_hash[num] = count
            
            count += 1