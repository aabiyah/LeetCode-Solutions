# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        length = min(len(word1), len(word2))

        for i in range(length):
            merged.append(word1[i])
            merged.append(word2[i])

        if len(word1) > len(word2):
            merged.extend(word1[length:])
        else:
            merged.extend(word2[length:])

        return ''.join(merged) # Convert the list merged back to a string using join.