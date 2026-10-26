from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for i in range(len(nums)):
            if len(window) > 0 and window[0][1] <= i - k:
                window.popleft()
            
            while len(window) > 0 and nums[i] > window[-1][0]:
                window.pop()
            window.append((nums[i], i))

            if i + 1 >= k:
                result.append(window[0][0])

        return result