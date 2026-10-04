class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # -4, -1, -1, 0, 1, 2
        # -4, -3, -1, 5, 7
        result = []
        nums.sort()
        lastVal1 = None
        for i in range(len(nums) - 2):
            val1 = nums[i]
            if val1 == lastVal1:
                continue
            lastVal1 = val1

            lastLeftVal = None
            lastRightVal = None

            left: int = i + 1
            right: int = len(nums) - 1
            while left < right:
                leftVal = nums[left]
                rightVal = nums[right]
                sum = val1 + leftVal + rightVal
                if sum == 0:
                    if leftVal != lastLeftVal or rightVal != lastRightVal:
                        result.append([val1, leftVal, rightVal])
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                lastLeftVal = leftVal
                lastRightVal = rightVal

        return list(result)
