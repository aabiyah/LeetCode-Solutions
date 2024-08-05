class Solution(object):
  def compress(self, chars):
      write = 0  # Pointer to write the compressed characters
      read = 0  # Pointer to read through the characters

      while read < len(chars):
          char = chars[read]
          start = read

          # Move read pointer to the end of the current group of characters
          while read < len(chars) and chars[read] == char:
              read += 1

          # Calculate the length of the group
          length = read - start

          # Write the character
          chars[write] = char
          write += 1

          # Write the length if it's greater than 1
          if length > 1:
              for digit in str(length):
                  chars[write] = digit
                  write += 1

      return write
