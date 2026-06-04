
# k ...est whatever is always gonna be heap
# Closest we need a MAx-heap. But python only has min...
# so go negatives in the heap

# -6, -4
# -4
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = ((x - 0)**2 + (y - 0)**2)**0.5
            heapq.heappush(heap, (distance * -1, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for x, coord in heap:
            result.append(coord)
        return result