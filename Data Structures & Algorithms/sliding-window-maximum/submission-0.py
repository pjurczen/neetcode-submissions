import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k - 1):
            heapq.heappush_max(window, (nums[i], i))
        
        result = []
        l = 0
        for r in range(k - 1, len(nums)):

            heapq.heappush_max(window, (nums[r], r))

            while window[0][1] < l:
                heapq.heappop_max(window)

            result.append(window[0][0])

            l += 1

        return result
            
