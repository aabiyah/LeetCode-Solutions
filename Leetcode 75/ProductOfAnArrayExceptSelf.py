class Solution(object):
  def productExceptSelf(self, nums):
      n = len(nums)
      answer = [1] * n

      # Forward pass: compute prefix products
      prefix_product = 1
      for i in range(n):
          answer[i] = prefix_product
          prefix_product *= nums[i]

      # Backward pass: compute suffix products and final result
      suffix_product = 1
      for i in range(n - 1, -1, -1):
          answer[i] *= suffix_product
          suffix_product *= nums[i]

      return answer