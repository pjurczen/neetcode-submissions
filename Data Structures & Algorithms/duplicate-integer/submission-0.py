class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
            else:
                return True
        return False