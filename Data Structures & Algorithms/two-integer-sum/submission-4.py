class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            if n not in hashmap:
                hashmap[n] = [i]
            else:
                hashmap[n].append(i)
        for key, value in hashmap.items():
            diff = target - key
            if diff == key and len(hashmap[diff]) >= 2:
                return [hashmap[diff][0], hashmap[diff][1]]
            elif diff != key and diff in hashmap:
                return [value[0], hashmap[diff][0]] if value[0] < hashmap[diff][0] else [hashmap[diff][0], value[0]]
        return []
