from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[tuple[int, int]] = [] # list[tuple[index, height]]
        largestArea = 0

        for i, h in enumerate(heights):
            iN = None
            while stack and h <= stack[-1][1]:
                ir, hr = stack.pop()
                largestArea = max(largestArea, (i - ir) * hr)
                iN = ir
            if iN is not None:
                i = iN
            stack.append((i, h))

        while stack:
            i, h = stack.pop()
            largestArea = max(largestArea, (len(heights) - i) * h)

        return largestArea