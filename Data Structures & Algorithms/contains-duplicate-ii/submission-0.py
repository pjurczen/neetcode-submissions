class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                hashset.remove(nums[L])
                L += 1
            
            if nums[R] in hashset:
                return True

            hashset.add(nums[R])
        
        return False
