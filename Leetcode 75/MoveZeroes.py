class Solution(object):
  def moveZeroes(self, nums):
      zeroes = 0
      i = 0

      while i<len(nums):
          if nums[i] == 0:
              nums.pop(i)
              zeroes += 1
          else:
              i += 1

      nums.extend([0] * zeroes) 
