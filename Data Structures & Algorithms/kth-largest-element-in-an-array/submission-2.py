import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for n in nums[k:]:
            if n >= heap[0]:
                heapq.heappushpop(heap, n)
        return heap[0]