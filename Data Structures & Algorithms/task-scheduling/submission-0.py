from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        minHeap = []
        for task, count in counter.items():
            for t in range(count):
                minHeap.append(t*(n + 1))
        heapq.heapify(minHeap)
        time = 0
        while minHeap:
            if minHeap[0] <= time:
                heapq.heappop(minHeap)
            time += 1
        return time
