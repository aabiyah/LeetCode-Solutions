class Solution(object):
  def reverseWords(self, s):
      # Split the string into words
      words = s.split()
      # Reverse the list of words
      reversed_words = words[::-1] # creates a new list with the elements of words in reverse order
      # Join the reversed list into a single string with a single space
      result = ' '.join(reversed_words)
      return result