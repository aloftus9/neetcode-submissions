# k most frequent
# Top # of anything is good to be a heap

# First, we need to get the counts of everythign o(n)
# Still have to loop through the heap so instead of sorting nlogn it's nlogk

import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}
        heap = []

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        
        for num, count in count_dict.items():

            heapq.heappush(heap,(count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for c, num in heap:
            result.append(num)

        return result

        