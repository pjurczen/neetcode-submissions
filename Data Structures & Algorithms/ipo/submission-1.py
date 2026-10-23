import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []
        for i in range(len(profits)):
            if capital[i] - w <= 0:
                heapq.heappush_max(maxHeap, profits[i])
            else:
                heapq.heappush(minHeap, (capital[i], i))

        for j in range(k):
            if maxHeap:
                w += heapq.heappop_max(maxHeap)
                while minHeap and minHeap[0][0] - w <= 0:
                    _, i = heapq.heappop(minHeap)
                    heapq.heappush_max(maxHeap, profits[i])
        
        return w

            