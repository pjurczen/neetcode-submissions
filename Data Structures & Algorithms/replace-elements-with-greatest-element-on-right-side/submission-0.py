class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx: int = len(arr) - 1
        greatestElem = arr[idx]
        arr[idx] = -1
        idx -= 1
        while idx >= 0:
            currentElem = arr[idx]
            arr[idx] = greatestElem
            greatestElem = max(currentElem, greatestElem)
            idx -= 1
        return arr