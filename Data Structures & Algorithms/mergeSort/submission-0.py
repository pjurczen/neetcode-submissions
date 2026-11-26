# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def _mergeSort(s: int, e: int):
            if e - s + 1 <= 1:
                return

            m = (e + s) // 2
            _mergeSort(s, m)
            _mergeSort(m + 1, e)

            _merge(s, m, e)
        

        def _merge(s: int, m: int, e: int):
            left = pairs[s:m + 1]
            right = pairs[m + 1:e + 1]
            i = j = 0
            k = s
            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    pairs[k] = left[i]
                    i += 1
                else:
                    pairs[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                pairs[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                pairs[k] = right[j]
                j += 1
                k += 1
        
        _mergeSort(0, len(pairs) - 1)
        return pairs