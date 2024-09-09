class Solution(object):
  def isSubsequence(self, s, t):
      i, j = 0, 0  # Initialize i and j to 0

      while i < len(s) and j < len(t):
          if s[i] == t[j]: 
              i += 1  # Move the pointer for s when characters match
          j += 1  # Always move the pointer for t

      return i == len(s)  # True if all characters of s are found in t in order