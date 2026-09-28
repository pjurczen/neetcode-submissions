import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq._heapify_max(heap)

        while len(heap) > 1:
            largest_stone = heap[0]
            second_largest_stone = max(heap[1], heap[2]) if len(heap) > 2 else heap[1]
            diff = largest_stone - second_largest_stone
            if diff == 0:
                heapq._heappop_max(heap)
                heapq._heappop_max(heap)
            else:
                heapq._heappop_max(heap)
                heapq._heappop_max(heap)
                heapq._heappush_max(heap, diff)

        return heap[0] if heap else 0