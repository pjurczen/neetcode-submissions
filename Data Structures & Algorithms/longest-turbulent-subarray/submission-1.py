class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result, prev = 1, ""
        L: int = 0
        R: int = 1

        while R < len(arr):
            if arr[R-1] < arr[R] and prev != "<":
                result = max(result, R - L + 1)
                prev = "<"
                R += 1
            elif arr[R-1] > arr[R] and prev != ">":
                result = max(result, R - L + 1)
                prev = ">"
                R += 1
            else:
                prev = ""
                L = R if arr[R-1] == arr[R] else R -1
                R = L + 1
        
        return result
                