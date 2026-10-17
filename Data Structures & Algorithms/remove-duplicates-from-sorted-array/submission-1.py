class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 1, len(nums) - 1

        while L <= R:
            if nums[L - 1] == nums[L]:
                for i in range(L, R):
                    nums[i] = nums[i+1]
                R -= 1
            else:
                L += 1
        return R+1
