class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts: list[int] = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i: int = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1
