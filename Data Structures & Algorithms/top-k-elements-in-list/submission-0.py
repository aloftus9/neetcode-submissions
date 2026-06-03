import heapq
class Solution:
    # We use dictionary to count the unique elements
    # use min-heap to (faster than sorting) get the largest
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,5,4,3,3,4,2,1,1,1,3]
        # k = 2
        count_dict = {}
        heap = []
        result = []
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        

        for num, count in count_dict.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        for h, num in heap:
            result.append(num)
        
        return result

        