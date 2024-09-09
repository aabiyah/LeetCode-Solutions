class Solution(object):
  def maxArea(self, height):
      i, j = 0, len(height) - 1  # Two pointers: start and end of the array
      max_area = 0  # Initialize max_area

      # While the two pointers don't cross
      while i < j:
          # Calculate the current area
          width = j - i
          h = min(height[i], height[j])
          current_area = width * h

          # Update max_area if the current area is larger
          max_area = max(max_area, current_area)

          # Move the pointer pointing to the shorter line
          if height[i] < height[j]:
              i += 1  # Move left pointer to the right
          else:
              j -= 1  # Move right pointer to the left

      return max_area
