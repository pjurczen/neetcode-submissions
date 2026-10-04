class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hashmap: dict[int, int] = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        result = set()

        path = []
        for i in range(len(nums) - 2):
            val_1 = nums[i]
            hashmap[val_1] -= 1
            for j in range(i+1, len(nums)):
                val_2 = nums[j]
                hashmap[val_2] -= 1
                missing_val = -(val_1 + val_2)
                if missing_val in hashmap and hashmap[missing_val] >= 1:
                    path = [val_1, val_2, missing_val]
                    path.sort()
                    result.add(tuple(path))
                hashmap[val_2] += 1
            hashmap[val_1] += 1

        return list(result)
