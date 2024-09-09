class Solution(object):
  def maxOperations(self, nums, k):
      count = {}  # Dictionary to track the frequency of numbers
      operations = 0  # To store the number of operations

      for num in nums:
          complement = k - num  # Find the complement that would sum with num to give k

          if count.get(complement, 0) > 0:  # If the complement is found
              operations += 1  # We found a valid pair
              count[complement] -= 1  # Decrease the complement's frequency
          else:
              # Otherwise, add num to the hashmap
              count[num] = count.get(num, 0) + 1

      return operations