class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0 : 1}
        total = 0
        result = 0
        for n in nums:
            total += n
            if (total - k) in counts:
                result += counts[total - k]
            counts[total] = 1 + counts.get(total, 0)
        return result
