class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #        i  
        # [1, 2, 3, 4, 5]
        #        j  
        # [1, 2, 4, 5, 6, 7, 8]

        # [1, 1, 2, 2, 3, 4 | 4, 5, 5, 6, 7, 8]
        #        i
        # [1, 2, 3, 4, 5]
        #       
        # [1, 2, 4, 5, 6, 7]
        #                 |
        # [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7]

        # [3]    
        # [1, 2]
        A, B = nums1, nums2
        total = len(nums1) + len(nums2) # 12
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # 0
            j = total//2 - i - 2 # 1 - 0 - 2 = -1
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
