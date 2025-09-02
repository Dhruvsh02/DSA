# problem number - 238 

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # Calculate prefix products from starting 
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and combine with prefix products from ending 
        suffix_product = 1
        for i in reversed(range(n)):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result