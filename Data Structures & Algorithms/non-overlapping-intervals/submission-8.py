class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        elemsToDelAsc = set()

        intervals.sort()

        left = 0
        right = 1
        while right <= len(intervals) - 1 and left < len(intervals) - 1:
            if left in elemsToDelAsc:
                left += 1
                continue
            if right in elemsToDelAsc or left == right:
                right += 1
                continue
            if intervals[right][0] < intervals[left][1]:
                if intervals[right][1] > intervals[left][1]:
                    elemsToDelAsc.add(right)
                    right += 1
                else:
                    elemsToDelAsc.add(left)
                    left += 1
            else:
                left += 1
                right += 1

        return len(elemsToDelAsc)

