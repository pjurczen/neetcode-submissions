class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # maxVal = len(nums) - 1
        # [1, maxVal]
        # [1, 2, 3, 1, 4]
        # 1 -> 2 -> 3 -> 1
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

        # 1 -> 2 -> 3 -> 4 -> 4
            
        # [3, 1, 3, 4, 2]
        # 3 -> 4 -> 2 -> 3

        # 4 -> 3 -> 1 -> 4 -> 2
        # 1 -> 3 -> 4 -> 4 -> 2  
        # 1 -> 3 -> 4 -> 2 
        #           |<---|
