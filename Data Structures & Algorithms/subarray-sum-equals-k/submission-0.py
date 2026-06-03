class Solution:

    # Classic prefix sum
    # will want a dictionary/hash map to track number of subarrays that add up to k
    # [1,2,3,4, -1]
    # k = 3
    # [1,2] [4,-1]
    # [1, 3, 6, 10, 9]
    # (current_index_val - k)
    # 
    #
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        prefix_dict= {0:1}
        count = 0
        for num in nums:
            prefix += num
            if (prefix - k) in prefix_dict:
                count += prefix_dict[prefix - k]
                
            prefix_dict[prefix] = prefix_dict.get(prefix, 0) + 1
        
        return count


        