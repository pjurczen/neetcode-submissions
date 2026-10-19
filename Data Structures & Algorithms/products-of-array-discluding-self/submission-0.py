class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        postfixProduct = [0 for _ in range(len(nums))]

        product = 1
        for L in range(len(nums)):
            product *= nums[L]
            prefixProduct.append(product)
            
        product = 1
        for R in range(len(nums) - 1, -1, -1):
            product *= nums[R]
            postfixProduct[R] = product
        
        result = []
        for i in range(len(nums)):
            left = prefixProduct[i - 1] if i > 0 else 1
            right = postfixProduct[i + 1] if i < len(nums) - 1 else 1
            result.append(left * right)
        
        return result

