class Solution(object):
  def increasingTriplet(self, nums):
      first = float('inf')
      second = float('inf')

      for num in nums:
          if num <= first:
              first = num  # Update first if num is smaller than or equal to first
          elif num <= second:
              second = num  # Update second if num is smaller than or equal to second but greater than first
          else:
              return True  # Return true if you find a number greater than both first and second

      return False