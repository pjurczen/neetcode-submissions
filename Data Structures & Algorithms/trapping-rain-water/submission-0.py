class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxL, maxR = 0, 0
        volume = 0

        while L <= R:
            maxH = min(maxL, maxR)
            if maxL <= maxR:
                if height[L] < maxH:
                    volume += maxH - height[L]
                maxL = max(maxL, height[L])
                L += 1
            else:
                if height[R] < maxH:
                    volume += maxH - height[R]
                maxR = max(maxR, height[R])
                R -= 1

        return volume
