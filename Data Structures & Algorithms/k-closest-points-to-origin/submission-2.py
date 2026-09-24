from math import sqrt
from typing import List
#              |
# [5, 6, 1, 2, 3]

#  |
# [5, 6, 1, 2, 3]
#        |

#     |
# [1, 6, 5, 2, 3]
#           |

#      . |
# [1, 2, 5, 6, 3]
#              |


class Solution:
    # we can try doing a quicksort like procedure on this:
    # - we select our pivot, initialized as median or average
    # - after every decision, only one of the two branches is valid to contain our k-point by definition of quicksort algorithm
    # - we continue going down the branch that is on the k-point side until we find a sub-array where all points are smaller or equal to the k-point, meaning an array of length k
    # - and thats our stopping condition, e - s + 1 == k


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickselect(points, k, 0, len(points) - 1)

    def quickselect(self, points: List[List[int]], k: int, s: int, e: int) -> List[List[int]]:
        if e - s + 1 == k:
            return points[s: e+1]

        m = (e+s) // 2
        entries: dict[int, float] = {s: self.distance(points[s]), e: self.distance(points[e]), m: self.distance(points[m])}
        average: float = sum([x for x in entries.values()]) / len(entries.values())
        pivotIdx = min(entries, key=lambda idx: abs(entries[idx] - average))
        pivot = points[pivotIdx]

        points[pivotIdx] = points[e]
        points[e] = pivot

        pivotIdx = e

        left = s
        for i in range(s, e):
            if self.distance(points[i]) < self.distance(pivot):
                tmp = points[i]
                points[i] = points[left]
                points[left] = tmp
                left += 1

        points[pivotIdx] = points[left]
        points[left] = pivot
        endPivotIdx = left

        # tmp = points[left]
        # if self.distance(pivot) < self.distance(tmp):
        #     points[left] = pivot
        #     points[pivotIdx] = tmp
        #
        #     endPivotIdx = left
        # else:
        #     endPivotIdx = pivotIdx

        leftSlice = endPivotIdx - s + 1
        if leftSlice == k:
            return points[s:endPivotIdx+1]
        elif leftSlice > k:
            return self.quickselect(points, k, s, endPivotIdx - 1)
        else:
            missingElem = k - (endPivotIdx - s + 1)
            return points[s:endPivotIdx+1] + self.quickselect(points, missingElem, endPivotIdx + 1, e)

    def distance(self, point: List[int]) -> float:
        return sqrt((point[0])**2 + (point[1])**2)

