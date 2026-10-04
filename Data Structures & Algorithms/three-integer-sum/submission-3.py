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
            sum = val_1
            path = [val_1]
            hashmap[val_1] -= 1
            for j in range(i+1, len(nums)):
                val_2 = nums[j]
                sum += val_2
                path.append(val_2)
                hashmap[val_2] -= 1
                missing_val = (-1 * sum)
                if missing_val in hashmap and hashmap[missing_val] >= 1:
                    path.append(missing_val)
                    copy = path.copy()
                    copy.sort()
                    result.add(tuple(copy))
                    path.pop()
                path.pop()
                hashmap[val_2] += 1
                sum -= val_2
            hashmap[val_1] += 1

        return list(result)
