# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Input: s = "hello"
# Output: "holle"

class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1 # Two-pointer Technique: Initialize two pointers, left and right, pointing to the beginning and end of the list, respectively.

        while left < right:
            if s[left] not in vowels:
                left += 1 # Move the left pointer to the right until it points to a vowel.
            elif s[right] not in vowels:
                right -= 1 # Move the right pointer to the left until it points to a vowel.

            else:
                s[left], s[right] = s[right], s[left] # Swap the vowels pointed to by left and right.

                left += 1
                right -= 1
            # Move both pointers towards the center and repeat the process until they cross each other.

        return ''.join(s)