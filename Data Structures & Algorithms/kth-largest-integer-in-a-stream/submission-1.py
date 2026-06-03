import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        
        self.heap = heap
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0]


        
