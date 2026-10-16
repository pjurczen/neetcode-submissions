class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result: int = 0
        elemCount: int = k - 1
        sum: int = 0
        for i in range(k - 1):
            sum += arr[i]

        for j in range(k - 1, len(arr)):
            if elemCount == k:
                sum -= arr[j - k]
                elemCount -= 1
            
            sum += arr[j]
            elemCount += 1
            avg: float = sum / k
            if avg >= threshold:
                result += 1
        
        return result
